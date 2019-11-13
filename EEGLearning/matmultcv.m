function xcv = matmultcv(xcv, W)
% matmultcv - multiplies matrix to each covarianced trial.
%
% Syntax:
%  xcv = matmultcv(xcv, W)
[C1,C2,n] = size(xcv);

if C1~=C2
  error('Input is not square.');
end

for i= 1:n
  Vi= W'*xcv(:,:,i)*W;
  xcv(:,:,i)= (Vi+Vi')/2;
end
