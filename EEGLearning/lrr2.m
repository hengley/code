function [W, bias, out] = lrr2(X, Y, C, varargin)
% lrr2 - logistic regression with rank=2 approximation for binary classification problem
% f(X) = 1/2(-w1'*X*w1+w2'*X*w2)+bias
%
% [W, bias, stat] = lrr2(X, Y, C, <opt>)
%
% Inputs:
%  X      : Input matrices.
%           [C,C,n] array: Each X(:,:,i) assumed to be symmetric.
%           [C^2,n] array: Each reshape(X(:,i), sqrt(size(X,1))) assumed to be symmetric.
%          WHITEN the data beforehand with whiten.m
%  Y      : Binary lables. +1 or -1. [1,n] matrix. n is the number of samples.
%  C      : Regularization constant.
%           choose from e.g., exp(linspace(log(0.01),log(100),20))
%
%  <opt>
%  .W0        : initial value for W=[w1, w2]. default: random unit-orthogonal bases.
%  .weight    : 1xnSamples vector. sample weighting coefficients. default ones(1,nSamples)/n
%  .checkgrad : check analytic gradient.
%  .visualize : visualize the loss function.
%  .MaxIter   : number of iterations. default 1000.
%  .MaxFunEvals : defualt 1000*nChannels.
%  .TolFun      : default 1e-9.
%  .TolX      :   default 1e-9.
%
%
% Outputs:
%  W=[w1, w2] : projection coefficients
%  bias       : the bias
%  stat       : output of fminunc
%
% Example:
% =Train=
%  [Xtr, Ww] = whiten(Xtr);
%  [W, bias, stat]  = lrr2(X, Y, 0.1);
%  cls=struct('W',W,'bias',bias,'Ww',Ww);
%
% =Test =
%  out=apply_lrr2(Xte, cls);
%  acc=mean(out.*Yte>=0);
%
% See also:
%  covariance.m, whiten.m, apply_lrr2.m
%
% 
% Copyright(C) 2006-2010 Ryota Tomioka (Fraunhofer FIRST.IDA)

[T,d,n] = size(X);

if size(Y,1)>size(Y,2)
  Y=Y';
end

%% Binary classification
ncls = 2;

%% index of valid samples
iValid=find(Y==1 | Y==-1);


opt=propertylist2struct(varargin{:});
opt=set_defaults(opt, 'MaxIter', 1000, ...
                      'MaxFunEvals', d*1000, ...
                      'TolFun', 1e-9, ...
                      'TolX', 1e-9, ...
                      'tolerance_f', 1e-12,...
                      'tolerance_grad', 1e-6,...
                      'display', 'on', ...
                      'W0', [], ...
                      'weight', ones(1,length(iValid))/length(iValid),...
                      'checkgrad', 0,...
                      'visualize', [],...
                      'solver','fminunc');



if T==1
  d=sqrt(d);
  X=reshape(X, [d, d, n]);
else
  if d~=T
    error('Input matrices must be square');
  end
end

%% check analytic gradient
if opt.checkgrad
  [r,x]=checkGrad(@objLRR2, 2*d+1, 10, 'symmetric', X(:,:,iValid), Y(iValid), C, opt.weight);
  figure, plot(1:2*d+1, r);
  keyboard;
end

%% visualization
if ~isempty(opt.visualize)
  W1=opt.visualize{1}.W;
  for i=1:length(opt.visualize)
    %% a small hack to get rid of the sign ambiguity
    Wtmp = opt.visualize{i}.W;
    Wtmp = Wtmp*diag(sign(diag(W1'*Wtmp)));
    xp(:,i)=[reshape(Wtmp, [2*d,1]); opt.visualize{i}.bias];
  end

  switch size(xp,2)
   case 2 % 1D visualization
    xl=-2:0.02:2;
    visualize1d(xl,X(:,:,iValid),Y(iValid),C,xp,opt);
    
   case 3 % 2D visualization
    xl=-2:0.2:2;
    visualize2d(xl,X(:,:,iValid),Y(iValid),C,xp,opt);
  end
end

if isempty(opt.W0)
  W0 = rand(d,2);
  [EV, ED]=eig(W0'*W0);
  W0=W0*EV*diag(1./sqrt(diag(ED)));
  opt.W0 = [W0(:,1); W0(:,2); 0];
elseif isequal(size(opt.W0), [d, 2])
  opt.W0 = [opt.W0(:,1); opt.W0(:,2); 0];
end  

switch(opt.solver)
 case 'fminunc'
  optfmu = optimset('GradObj','on',...
                    'Hessian','on',...
                    'display',opt.display,...
                    'MaxIter', opt.MaxIter, ...
                    'MaxFunEvals', opt.MaxFunEvals, ...
                    'TolFun', opt.TolFun,...
                    'TolX', opt.TolX);

  [W1, fval, exitflag, out] = fminunc(@objLRR2, opt.W0, optfmu, X(:,:,iValid), Y(iValid), C, opt.weight);
 case 'lbfgs'
  fun=@(x)objLRR2(x, X(:,:,iValid), Y(iValid), C, opt.weight);
  ll =-inf*ones(2*d+1,1);
  uu = inf*ones(2*d+1,1);
  [W1, stat] = lbfgs(fun, opt.W0, ll, uu, [], [],'maxiter', opt.MaxIter,'epsg',opt.tolerance_grad,'display',1);
  fval=stat.fval;
  exitflag = 1;
end


W = orthogonalize([W1(1:d), W1(d+1:2*d)]);
bias = W1(end);
x= [reshape(W,[2*d,1]); bias];
[f,g,H]=objLRR2(x,X(:,:,iValid),Y(iValid), C, opt.weight);

if f>fval+10*eps
  fprintf('orthogonalization icreases the loss...\n');
  W=[W1(1:d), W1(d+1:2*d)];
  out.fval = fval;
  [f,g,H]=objLRR2(W1,X(:,:,iValid),Y(iValid), C, opt.weight);
  out.g    = g;
  out.H    = H;
else
  out.fval = f;
  out.g    = g;
  out.H    = H;
end

out.exitflag = exitflag;

% V = reshape(V, [d*d,n]);
% fv.x = reshape(-0.5*W(:,1)*W(:,1)'+0.5*W(:,2)*W(:,2)', [1, d*d])*V+bias;


function W1 = orthogonalize(W)
% orthogonalization does not change the decision function
% but decreases the regulalization term
D=sqrtm(W'*W);
[EV, ED]=eig(D*diag([-1 1])*D');

W1 = W*inv(D)*EV*diag(sqrt(abs(diag(ED))));

% for debug
% W1'*W1
% rangeof(W*diag([-1 1])*W'-W1*diag([-1 1])*W1')

function [f, g, H] = objLRR2(x, X, Y, C, weight)
ncls = 2;
d = (size(x,1)-1)/ncls;
n = length(Y);

w1 = x(1:d);
w2 = x(d+1:2*d);
b  = x(end);

f = 0.5*C/n*x'*x;
g = C/n*x;


Hww1 = zeros(d,d);
Hww2 = zeros(d,d);
Hw1w2 = zeros(d,d);
Hw1b = zeros(d,1);
Hw2b = zeros(d,1);
Hbb  = 0;

for i=1:n
  expi = exp(-Y(i)*(-0.5*w1'*X(:,:,i)*w1+0.5*w2'*X(:,:,i)*w2+b));
  p = 1/(1+expi);
  
  Vw1 = X(:,:,i)*w1;
  Vw2 = X(:,:,i)*w2;
  
  
  f = f - log(p)*weight(i);
  gw1 =   Y(i)*Vw1*(1-p);
  gw2 = - Y(i)*Vw2*(1-p);
  gb  = - Y(i)*(1-p);
  g = g + [gw1; gw2; gb]*weight(i);
  
  Hww1  = Hww1  + (Vw1*Vw1'*p*(1-p) + Y(i)*X(:,:,i)*(1-p))*weight(i);
  Hww2  = Hww2  + (Vw2*Vw2'*p*(1-p) - Y(i)*X(:,:,i)*(1-p))*weight(i);
  Hw1w2 = Hw1w2  -Vw1*Vw2'*p*(1-p)*weight(i);
  Hw1b  = Hw1b   -Vw1*p*(1-p)*weight(i);
  Hw2b  = Hw2b  + Vw2*p*(1-p)*weight(i);
  Hbb   = Hbb   + p*(1-p)*weight(i);

end

H = C/n*eye(2*d+1) +...
    [Hww1,   Hw1w2, Hw1b;...
     Hw1w2', Hww2,  Hw2b;...
     Hw1b',  Hw2b', Hbb];


function visualize1d(X,V,Y,C,xp,opt)
d=size(V,1);
n=size(V,3);
F=zeros(size(X));
G=zeros(size(X));
loss=zeros(size(X));

dx = xp(:,2)-xp(:,1);

keyboard;
for i=1:length(X)
  x=xp(:,1)+dx*(X(i)+1)/2;
  [F(i),g]=objLRR2(x,V,Y, C, opt.weight);
  out = out1d(X(i),V,xp);
  % out = reshape(-0.5*x(1:d)*x(1:d)'+...
  %                0.5*x(d+1:2*d)*x(d+1:2*d)', [1, d*d])*...
  %        reshape(V,[d*d,n])+x(end);
  loss(i) = mean(out.*Y<0);
  G(i)=dx'*g;
end

figure, ax=plotyy(X, F, X, G);
ax(3)=axes('position',get(gca,'position'), 'YColor', [1 0 0], 'Color','none');
h=line(X, loss); set(h,'color',[1 0 0]);

axes(ax(1));
grid on;
hold on;
Ip=[find(X==-1), find(X==1)];
plot(X(Ip), F(Ip), 'ro', 'linewidth', 2);
set(ax(1),'Color','none')
for i=1:length(Ip)
  try
    text(X(Ip(i)), F(Ip(i)), opt.visualize{i}.desc, 'color', 'red');
  end
end

keyboard;

function visualize2d(X,V,Y,C,xp,opt)
d=size(V,1);
n=size(V,3);

[Xg,Yg]=meshgrid(X);
F=zeros(size(Xg));
G=zeros(size(Xg));
A=[1 -1 0; .5 .5 -1; 1 1 1]'; A=A*diag(1./sqrt(sum(A.^2)));
zp=A'*(eye(3)-ones(3)/3); zp=zp(1:2,:);
for i=1:size(zp,2)
  [Fp(i),g]=objLRR2(xp(:,i),V,Y, C, opt.weight);
  Gp(i)=norm(g);
end
for i=1:length(X)
  for j=1:length(X)
    x=xp*(ones(3,1)/3+A(:,1)*Xg(i,j)+A(:,2)*Yg(i,j));
    [F(i,j),g]=objLRR2(x,V,Y, C, opt.weight);
    G(i,j)=norm(g);
  end
end

figure, surf(Xg,Yg,F);
hold on;
plot3(zp(1,:), zp(2,:), Fp, 'ro', 'linewidth', 2);
for i=1:size(zp,2),
  try
    text(zp(1,i), zp(2,i), Fp(i)*1.1, opt.visualize{i}.desc, 'color', 'red');
  end
end

keyboard;

function cv=curv1d(V,xp)
d=size(V,1);
dx = xp(:,2)-xp(:,1);
cv=reshape(-.5*dx(1:d)*dx(1:d)'+...
           .5*dx(d+1:2*d)*dx(d+1:2*d)',[1,d*d])*...
   reshape(V,[d*d,size(V,3)]);

function out=out1d(X,V,xp)
d=size(V,1);
dx = xp(:,2)-xp(:,1);
for i=1:length(X)
  x=xp(:,1)+dx*(X(i)+1)/2;
  out(i,:)=reshape(-0.5*x(1:d)*x(1:d)'+...
                   0.5*x(d+1:2*d)*x(d+1:2*d)',[1,d*d])*...
           reshape(V,[d*d,size(V,3)])+x(end);
end


% This is a MATLAB implementation of the Limited-memory
% Broyden-Fletcher-Goldfarb-Shanno (L-BFGS) algorithm written
% by Jorge Nocedal
% http://www.eecs.northwestern.edu/~nocedal/lbfgs.html
% 
% References
% J. Nocedal. Updating Quasi-Newton Matrices with Limited Storage
% (1980), Mathematics of Computation 35, pp. 773-782.
% D.C. Liu and J. Nocedal. On the Limited Memory Method for Large Scale
% Optimization (1989), Mathematical Programming B, 45, 3, pp. 503-528.
  
function [xx, status] = lbfgs(fun, xx, ll, uu, Ac, bc, varargin)

opt=propertylist2struct(varargin{:});
opt=set_defaults(opt, 'm', 6,...
                      'ftol', 1e-5, ...
                      'maxiter', 0,...
                      'max_linesearch', 50,...
                      'display', 0,...
                      'epsg', 1e-5);


nn = size(xx,1);

t0 = cputime;

% Limited memory
lm = repmat(struct('s',zeros(nn,1),'y',zeros(nn,1),'ys',0,'alpha',0),[1, opt.m]);

[fval,gg,gloss]=fun(xx);


% The initial step is gradient
dd = -gg;

kk = 1;
stp = 1/norm(dd);

bResetLBFGS = 0;
ixend = 1;
bound = 0;
while 1
  fp = fval;
  xxp = xx;
  ggp = gg;

  % Perform line search
  [ret, xx,fval,gg,gloss,stp]=...
      linesearch_backtracking(fun, xx, ll, uu, Ac, bc, fval, gg, dd, stp, opt, varargin{:});
  
  if ret<0
    break;
  end

  % Progress report
  gnorm = norm(gg);
  if opt.display>1
    fprintf('[%d] xx=[%g %g...] fval=%g gnorm=%g step=%g\n',kk,xx(1),xx(2),fval,gnorm,stp);
  end

  if gnorm<opt.epsg
    if opt.display>0
      fprintf('Optimization success! gnorm=%g\n',gnorm);
    end
    ret=0;
    break;
  end
  
  if kk==opt.maxiter
    if opt.display>0
      fprintf('Maximum #iterations=%d reached.\n', kk);
    end
    ret = -3;
    break;
  end

  % L-BFGS update
  if opt.m>0
    lm(ixend).s = xx-xxp;
    lm(ixend).y = gg-ggp;
    ys = lm(ixend).y'*lm(ixend).s; yy = sum(lm(ixend).y.^2);
    lm(ixend).ys  = ys;
  else
    ys = 1; yy = 1;
  end
  
  bound = min(bound+1, opt.m);
  ixend = (opt.m>0)*(mod(ixend, opt.m)+1);

  % Initially set the negative gradient as descent direction
  dd = -gg;
  
  jj = ixend;
  for ii=1:bound
    jj = mod(jj + opt.m -2, opt.m)+1;
    lm(jj).alpha = lm(jj).s'*dd/lm(jj).ys;
    dd = dd -lm(jj).alpha*lm(jj).y;
  end

  dd = dd *(ys/yy);
  
  for ii=1:bound
    beta = lm(jj).y'*dd/lm(jj).ys;
    dd = dd + (lm(jj).alpha-beta)*lm(jj).s;
    jj = mod(jj,opt.m)+1;
  end

  stp = 1.0;
  
  kk = kk + 1;
end

status=struct('ret', ret,...
              'kk', kk,...
              'fval', fval,...
              'gg', gg,...
              'time', cputime-t0,...
              'opt', opt,...
              'gloss',gloss);


function [ret, xx, fval, gg, gloss, step]...
    =linesearch_backtracking(fun, xx, ll, uu, Ac, bc, fval, gg, dd, step, opt, varargin)

floss=0;
gloss=zeros(size(gg));

dginit=gg'*dd;

if dginit>=0
  if opt.display>0
    fprintf('dg=%g is not a descending direction!\n', dginit);
  end
  step = 0;
  ret = -1;
  return;
end

Ip=find(dd>0);
In=find(dd<0);
step=min([step, 0.999*min((xx(In)-ll(In))./(-dd(In))), 0.999*min((uu(Ip)-xx(Ip))./dd(Ip))]);


xx0 = xx;
f0  = fval;
gg0 = gg;
cc = 0;

if opt.display>2
  fprintf('finit=%.20f\n',f0);
end

while cc<opt.max_linesearch
  ftest = f0  + opt.ftol*step*dginit;
  xx    = xx0 + step*dd;

  if ~isempty(Ac)
    bineq = all(Ac*xx<=bc);
  else
    bineq = true;
  end

  if bineq && all(xx>=ll) && all(xx<=uu)
    [fval, gg, gloss]=fun(xx);
    
    if fval<=ftest
      break;
    end
  else
    fval = inf;
  end
  if opt.display>2
    fprintf('[%d] step=%g fval=%.20f > ftest=%.20f\n', cc, step, fval, ftest);
  end
  
  step = step/2;
  cc = cc+1;
end

if cc==opt.max_linesearch
  if opt.display>0
    fprintf('Maximum linesearch=%d reached\n', cc);
  end
  xx   = xx0;
  [fval, gg, gloss]=fun(xx);
  step = 0;
  ret = -2;
  return;
end


ret = 0;
