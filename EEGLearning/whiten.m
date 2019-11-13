function [xcv, Ww]=whiten(xcv)
% whiten - Perform whitening
%
%Synopsis:
% [xw, Ww]= whiten(xcv)
%

[T,C,n]= size(xcv);

if T==1
  C= sqrt(C);
  xcv= reshape(xcv, [C,C,n]);
end

Sigma = mean(xcv,3);
[EV, ED]=eig(Sigma);
Ww = EV*diag(1./(sqrt(diag(ED))))*EV';

xcv = matmultcv(xcv, Ww);