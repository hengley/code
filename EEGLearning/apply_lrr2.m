function out=apply_lrr2(X, cls)

[C1, C2, n] = size(X);

if C1==1
  C = sqrt(C2);
  X = shiftdim(X);
elseif C1~=C2
  error('Input is not square.');
else
  C = C1;
  X = reshape(X, [C^2, n]);
end

W=cls.Ww*cls.W;

out = reshape(-0.5*W(:,1)*W(:,1)'+0.5*W(:,2)*W(:,2)', [1, C^2])*X+cls.bias;

