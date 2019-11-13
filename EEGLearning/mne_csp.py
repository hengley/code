import numpy as np
import matplotlib.pyplot as plt

from mne import Epochs, pick_types, find_events
from mne.channels import read_layout
from mne.io import concatenate_raws, read_raw_edf
from mne.datasets import eegbci
from mne.decoding import CSP

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from sklearn.cross_validation import ShuffleSplit, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
from sklearn import metrics

import pdb

print(__doc__)

# Set parameters and read data
# avoid classification of evoked responses by using epochs that start 1s after cue onset.
# tmin, tmax = -1., 4.
# # dictionary keys can later be used to access associated events
# event_id = dict(hands=2, feet=3)
# # select subject
# # subject = 2
# # motor imagery task: hands vs feet
# runs = [6, 10, 14]

# total_epochs = np.empty((0,64,801))
# total_epochs_train = np.empty((0,64,161))
# total_labels = np.empty((0,))
# for sub in range(1,88):
# 	# download edf files from website
# 	raw_fnames = eegbci.load_data(sub, runs)
# 	# read edf files and convert into fif files
# 	raw_files = [read_raw_edf(f, preload=True) for f in raw_fnames]
# 	# concatenate raw instances as if they were continuous
# 	raw = concatenate_raws(raw_files)
# 	# strip channel names of "." characters
# 	raw.rename_channels(lambda x: x.strip('.'))
# 	# apply band-pass filter
# 	raw.filter(7., 30., method='iir')

# 	# find events of the stim channel affected by the trigger
# 	events = find_events(raw, shortest_event=0, stim_channel='STI 014')
# 	# pick eeg channels
# 	picks = pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False, exclude='bads')

# 	# extract epochs from a raw instance
# 	epochs = Epochs(raw, events, event_id, tmin, tmax, picks=picks, baseline=None, preload=True, add_eeg_ref=False)
# 	# train will be done only between 1 and 2s
# 	epochs_train = epochs.copy().crop(tmin=1., tmax=2.)
# 	# change labels from 2 or 3 to 0 or 1
# 	labels = epochs.events[:, -1] - 2
	
# 	# get all epochs and training epochs as 3d arrays
# 	epochs_data = epochs.get_data()
# 	epochs_data_train = epochs_train.get_data()
	
# 	# concatenate all subjects' data 
# 	total_epochs = np.append(total_epochs, epochs_data, axis=0)
# 	total_epochs_train = np.append(total_epochs_train, epochs_data_train, axis=0)
# 	total_labels = np.append(total_labels, labels, axis=0)

# np.save('total_epochs.npy', total_epochs)
# np.save('total_epochs_train.npy', total_epochs_train)
# np.save('total_labels.npy', total_labels)

total_epochs = np.load('total_epochs.npy')
total_epochs_train = np.load('total_epochs_train.npy')
total_labels = np.load('total_labels.npy')

# Classification with linear discrimant analysis
# assemble a classifier
#svc = SVC(kernel="linear", C=0.1)
#svc = GaussianNB()
#svc = AdaBoostClassifier()
#svc = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=5)
#svc = MLPClassifier(alpha=1)
#svc = DecisionTreeClassifier(max_depth=5)
svc = KNeighborsClassifier(3)
#svc = QuadraticDiscriminantAnalysis()
csp = CSP(n_components=16, reg=None, log=True)

# define a monte-carlo cross-validation generator (reduce variance):
cv = ShuffleSplit(len(total_labels), 10, test_size=0.2, random_state=42)

# Use scikit-learn Pipeline with cross_val_score function
clf = Pipeline([('CSP', csp), ('SVC', svc)])
# use only training data to classify the events
scores = cross_val_score(clf, total_epochs_train, total_labels, cv=cv, n_jobs=1)
# evaluate the class balance level
class_balance = np.mean(total_labels == total_labels[0])
class_balance = max(class_balance, 1. - class_balance)
# Printing the results
print("Classification accuracy: %f / Chance level: %f" % (np.mean(scores), class_balance))

# fit and transform original data
csp.fit_transform(total_epochs, total_labels)
#evoked = epochs.average()
#evoked.data = csp.patterns_.T
#evoked.times = np.arange(evoked.data.shape[0])
#layout = read_layout('EEG1005')
# plot CSP patterns estimated on full data for visualization
#evoked.plot_topomap(times="auto", ch_type='eeg', layout=layout, scale_time=1, 
#					time_format='%i', scale=1, unit='Patterns (AU)', size=1.5)

sfreq = 100
#sfreq = raw.info['sfreq']
# running classifier: window length
# w_length = int(sfreq * 0.5)
w_length = total_epochs_train.shape[2]
# running classifier: window step size
w_step = int(sfreq * 0.1)
w_start = np.arange(0, total_epochs.shape[2] - w_length, w_step)

scores_windows = []

for train_idx, test_idx in cv:
	y_train, y_test = total_labels[train_idx], total_labels[test_idx]
	# features are obtained from csp transformation using training time only
	X_train = csp.fit_transform(total_epochs_train[train_idx], y_train)
	X_test = csp.transform(total_epochs_train[test_idx])

	# fit classifier using training time
	svc.fit(X_train, y_train)
	# test on training time
	print svc.score(X_test, y_test)

	score_this_window = []
	for n in w_start:
		# regenerate the test data on whole scale of time
		X_test = csp.transform(total_epochs[test_idx][:, :, n:(n + w_length)])
		# test the classifier on sliding window
		score_this_window.append(svc.score(X_test, y_test))
	scores_windows.append(score_this_window)

# pdb.set_trace()

# Plot scores over time
w_times = (w_start + w_length / 2.) / sfreq - 1
#w_times = (w_start + w_length / 2.) / sfreq + epochs.tmin
plt.figure()
plt.plot(w_times, np.mean(scores_windows, 0), label='Score')
plt.axvline(0, linestyle='--', color='k', label='Onset')
plt.axhline(0.5, linestyle='-', color='k', label='Chance')
plt.xlabel('time (s)')
plt.ylabel('classification accuracy')
plt.title('Classification score over time')
plt.legend(loc='lower right')
plt.show()
