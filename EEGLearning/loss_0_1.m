function loss = loss_0_1(y, out)
% loss_0_1 - zero-one loss.
%
% Syntax:
%  loss = loss_0_1(y, out)
  
loss = mean((y.*out)<=0);