function xcv = covariance(xepo);
% covariance - calculate the covariance between channels for each sample
%
% xcv = proc_covariance(xepo)
%

[T,C,n]=size(xepo);

xcv = zeros(C,C,n);
for i=1:n
  xcv(:,:,i) = cov(xepo(:,:,i));
end
