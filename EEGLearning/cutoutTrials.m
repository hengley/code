function xepo = cutoutTrilas(xcnt, pos, ival, fs)
% cutoutTrials - cuts out trials from continuous EEG recording
% xepo = cutoutTrials(xcnt, pos, ival, fs)
%  ival = [t1 t2] (ms)

[TT, d] = size(xcnt);
n = length(pos);

i1 = floor(ival(1)/1000*fs);
i2 = floor(ival(2)/1000*fs);

xepo = zeros(i2-i1+1, d, n);

for i=1:length(pos)
 xepo(:,:,i) = xcnt(pos(i)+i1:pos(i)+i2, :);
end
 