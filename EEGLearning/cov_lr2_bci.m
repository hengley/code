clc
clear
close all
load '../bci_iii_data_iv/data_set_IVa_aw.mat'
load '../bci_iii_data_iv/true_labels_aw.mat'
          
%% Reduced set of 49 channels
opt.chanind = [14, 15, 16, 17, 18, 19, 20, 21, 22, 33, 34, 35, 36, 37, 38, ...
               39, 50, 51, 52, 53, 54, 55, 56, 57, 58, 68, 69, 70, 71, 72, ...
               73, 74, 75, 76, 87, 88, 89, 90, 91, 92, 93, 94, 95, 104, 106,...
              108, 112, 113, 114];
opt.ival = [500 3500];
opt.band = [7 30];
          
%% Select channels and covert cnt into double
cnt  = 0.1 * double(cnt(:, opt.chanind));
clab = nfo.clab(opt.chanind);
C = length(clab);

%% Apply a band-pass filter
[B,A] = butter(opt.band(1), opt.band / nfo.fs * 2);
cnt = filtfilt(B, A, double(cnt));

%% Cut EEG into tirals
xepo = cutoutTrials(cnt, mrk.pos, opt.ival, nfo.fs);
X = covariance(xepo);
Y = (mrk.y - 1.5) * 2;

%% Find indices of training and test set
train_idx = find(~isnan(Y));
% test_idx  = find(isnan(Y));

X_train = X(:, :, train_idx);
Y_train = Y(train_idx);
X_test = X(:, :, test_idx);
Y_test = (true_y(test_idx) - 1.5) * 2;

%% Train nums & test nums
num_train = size(train_idx, 2);
num_test = size(test_idx, 2);

%% Whiten training data
[X_train, Ww] = whiten(X_train);

%% Set regularization parameter
lambda = exp(linspace(log(0.01), log(100), 20));
memo = repmat(struct('lambda',[],'cls',[],'out',[],'loss',[]), [1,length(lambda)]);

for i = 1:length(lambda)
  fprintf('lambda = %g\n', lambda(i));
  [W, b, stat] = lrr2(X_train, Y_train, lambda(i));
  memo(i).lambda = lambda(i);
  memo(i).cls = struct('W',W,'bias',b,'Ww',Ww);
  memo(i).out = apply_lrr2(X_test, memo(i).cls);
  memo(i).loss = loss_0_1(Y_test, memo(i).out);
  fprintf('accuracy = %g\n', 1 - memo(i).loss);
end

loss = zeros(size(memo));
for i = 1:numel(memo)
  loss(i) = memo(i).loss;
end

figure, plot(log(lambda), 100*(1-loss)', 'linewidth',2)
set(gca,'fontsize',20)
set(gca,'xtick',log(0.01):log(10):log(100))
set(gca,'xticklabel', {'0.01', '0.1', '1.0', '10', '100'})
grid on;
hold on;
plot(log(lambda), 100*(1-mean(loss)), 'color',[.7 .7 .7], 'linewidth', 2);
xlabel('Regularization constant \lambda')
ylabel('Classification accuracy')
