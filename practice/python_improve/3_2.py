#coding: utf8
#判断是否为素数
class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in xrange(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in xrange(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k

for x in PrimeNumbers(1, 100):
    print x