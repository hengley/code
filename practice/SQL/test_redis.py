# http://redis-py.readthedocs.io/en/latest/

import redis


class Base(object):
    def __init__(self):
        '''连接redis数据库'''
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)


'''
set -- 设置值
mset -- 设置多个键值对
mget -- 获取多个键值对
append -- 添加字符串
del -- 删除
incr/decr -- 增加/减少 1
'''
class TestString(Base):

    def test_set(self):
        '''set -- 设置值'''
        res = self.r.set('user2', 'Amy')
        print(res)
        return res

    def test_get(self):
        '''get -- 设置值'''
        res = self.r.get('user2')
        print(res)
        return res


    def test_mset(self):
        '''mset -- 多个键值对'''
        d = {
            'user3': 'Tony',
            'user4': 'Tom'
        }
        res = self.r.mset(d)
        print(res)
        return res

    def test_mget(self):
        '''mget -- 多个键值对'''
        l = ['user3', 'user4']
        res = self.r.mget(l)
        print(res)
        return res

    def test_del(self):
        '''del -- 删除'''
        res = self.r.delete('user3')
        print(res)
        return res


'''
lpush/rpush -- 从左/右插入数据
lrange -- 获取指定长度的数据
ltrim -- 获取一定长度的数据
lpop/rpop -- 移除最左/最右的数据并返回
lpushx/rpushx -- key存在的时候才插入数据，不存在不做任何处理
'''
class TestList(Base):

    def test_push(self):
        '''lpush/rpush -- 从左/右插入数据'''
        s = ['left', 'right']
        res = self.r.lpush('stdents', *s)
        print(res)
        res = self.r.lrange('stdents', -1, 0)
        print(res)
        return res

    def test_ltrim(self):
        '''ltrim -- 按一定长度修剪数据'''
        res = self.r.ltrim('stdents', -1, 0) 
        print(res)
        return res

    def test_pop(self):
        '''lpop/rpop -- 移除最左/最右的数据并返回'''
        res = self.r.lpop('stdents')
        print(res)
        res = self.r.lrange('stdents', -1, 0)
        print(res)
        return res

    def test_pushx(self):
        '''lpushx/rpushx -- key存在的时候才插入数据，不存在不做任何处理'''
        res = self.r.lpushx('user5', 'Amy')
        print(res)
        return res


'''
sadd/srem -- 添加/删除数据
sismember -- 判断是否set一个item
smenmbers -- 返回该集合所有的item
sdiff -- 返回一个集合与其它集合的差异
sinter -- 返回几个集合的并集
sunion -- 返回几个集合的交集
'''
class TestSet(Base):
    def test_sadd(self):
        'sadd/srem -- 添加/删除数据'
        l = ('lion', 'tiger')
        res = self.r.sadd('animal1', *l)
        print(res)
        res = self.r.smenmbers('animal1')
        print(res)
        return res

    def test_srem(self):
        '''sadd/srem -- 添加/删除数据'''
        res = self.r.srem('animal2', 'lion')
        print(res)
        res = self.r.smenmbers('animal2')
        print(res)
        return res
  
    def test_sinter(self):
        '''sinter -- 返回几个集合的并集'''
        res = self.r.sinter('animal1', 'animal2')
        print(res)
        return res

    def test_sunion(self):
        '''sinter -- 返回几个集合的交集'''
        res = self.r.sunion('animal1', 'animal2')
        print(res)
        return res
    

def main():
    str_obj = TestString()
    res = str_obj.test_set()
    # str_obj.test_get()
    # str_obj.test_mset()
    # str_obj.test_mget()
    # str_obj.test_del()
    print(res)


if __name__ == '__main__':
    main()
