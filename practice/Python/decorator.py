import time
from functools import wraps

def metric(func):
    @wraps(func)
    def wrapper(*args, **kwargs): 
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        use_time = end - start
        print('%s executed in %s ms' % (func.__name__, use_time))
        return func(*args, **kwargs)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.05)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.5)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')


def logged(func):
    @wraps(func) # functools.wraps可以将原函数对象的指定属性复制给包装函数对象，默认有 __module__、__name__、__doc__,或者通过参数选择.
    def with_logging(*args, **kwargs):
        """wrapper function"""
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
 
@logged
def f(x):
   """does some math"""
   return x + x * x
 
# print(f.__name__)  # prints 'f'
# print(f.__doc__)  # prints 'does some math'
