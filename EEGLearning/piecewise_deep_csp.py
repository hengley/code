import numpy as np
import scipy as sp
from scipy.io import loadmat
import theano
import theano.tensor as T
from scipy import signal
from sklearn.linear_model import LogisticRegression as LR
from sklearn.lda import LDA
from logistic_sgd import LogisticRegression
import cPickle

# Load dataset
data = loadmat('EEG_train_ay.mat')
X_train = data['X_train']
data = loadmat('EEG_test_ay.mat')
X_test = data['X_test']
data = loadmat('label_train_ay.mat')
Y_train = np.array(data['Y_train'], dtype=int)
data = loadmat('label_test_ay.mat')
Y_test = np.array(data['Y_test'], dtype=int)

Y_train = (Y_train + 1) / 2
Y_test = (Y_test + 1) / 2

def csp(x_train, y_train):
    """Calculate Common Spatial Patterns Decompostion and Returns spatial filters W """

    # Calculate correlation matrices
    X0 = x_train[:, :, y_train[0,:] == 0]
    X1 = x_train[:, :, y_train[0,:] == 1]

    C0 = 0.
    for i in xrange(X0.shape[2]):
        C0 = C0 + np.dot(X0[:, :, i].transpose(), X0[:, :, i])
    C0 = C0 / X0.shape[2]

    C1 = 0.
    for i in xrange(X1.shape[2]):
        C1 = C1 + np.dot(X1[:, :, i].transpose(), X1[:, :, i])
    C1 = C1 / X1.shape[2]

    # Calculate CSP
    D, V = sp.linalg.eig(C1, C1+C0);
    ind = sorted(range(D.size), key = lambda k: D[k])
    V = V[:, ind];
    W = np.hstack([V[:,0:2], V[:,25:]]);

    return W

def classify_csp(W, V, x_train, y_train, x_test, y_test):
    """ Classify data using CSP filter W """
    
	# Project data
    proj_train = sp.tensordot(W.transpose(), x_train, axes=[1,1])
    proj_test  = sp.tensordot(W.transpose(), x_test, axes=[1,1])

    # Calculate features
    ftr = np.log(np.tensordot(proj_train**2, V, axes=[1,0]))[:,:,0]
    fte = np.log(np.tensordot(proj_test **2, V, axes=[1,0]))[:,:,0]

    # Classify 
    logistic = LR()
    logistic.fit(ftr.transpose(), y_train[0,:])
    sc = logistic.score(fte.transpose(), y_test[0,:])
    
    return sc

W = csp(X_train, Y_train)
V = np.ones((301,1))
sc = classify_csp(W, V, X_train, Y_train, X_test, Y_test) 

# Fine tune CSP pipeline
# Note input data dim: [batches, time, channel]
# Filter dim: [channel_in, channel_out]
X_train_T = theano.shared(X_train.transpose(2, 0, 1))
X_test_T  = theano.shared(X_test.transpose(2, 0, 1))
Y_train_T = T.cast(theano.shared(Y_train[0,:]), 'int32')
Y_test_T  = T.cast(theano.shared(Y_test[0,:]) , 'int32')

lr         = .01 # learning rate
batch_size = 28
epochs     = 1700
index      = T.lscalar('index')
y          = T.ivector('y')
X          = T.tensor3('X')
csp_w      = theano.shared(W)
avg_v      = theano.shared(V)
proj_csp   = T.tensordot(X, csp_w, axes=[2,0])
layer0_out = T.pow(proj_csp, 2)
variance   = T.tensordot(layer0_out, avg_v, axes=[1,0])
layer1_out = T.log((variance))[:,:,0] 
layer2     = LogisticRegression(input=layer1_out, n_in=26, n_out=2)
loss       = layer2.negative_log_likelihood(y) + .01 * T.sum(T.pow(avg_v, 2))

f = open('params_dnn_al.pkl')
params_model = cPickle.load(f)
csp_w.set_value(params_model[0].get_value())
avg_v.set_value(params_model[1].get_value())
layer2.W.set_value(params_model[2].get_value())
layer2.b.set_value(params_model[3].get_value())
params = [csp_w, avg_v] + layer2.params

grads = T.grad(loss, params)
updates = []
for param_i, grad_i in zip(params, grads):
    updates.append((param_i, param_i - lr * grad_i))

train_model = theano.function([index], loss, updates=updates,
      givens={
          X: X_train_T[index * batch_size: (index + 1) * batch_size],
          y: Y_train_T[index * batch_size: (index + 1) * batch_size]})

test_model = theano.function([], layer2.errors(y), givens = {
        X: X_test_T, y: Y_test_T})

for i in range(epochs):
    for j in range(28/batch_size):
		loss_ij = train_model(j)
    print 'Loss at epoch %i = %f' % (i, loss_ij)
    
    er = test_model()
    print 'Epoch = %i' % i
    print 'Loss = %f' % loss_ij
    print 'Test error = % f' % er

#f = open('params_dnn_al.pkl','wb')
#cPickle.dump(params, f)
#f.close()
