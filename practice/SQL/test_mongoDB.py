from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId


class TestMongo(object):

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['blog']

    def get_one(self):
        '''查询一条数据'''
        return self.db.blog.post.find_one()

    def get_more(self):
        '''查询多条数据'''
        return self.db.blog.post.find()
    
    def get_one_from_oid(self):
        '''根据id查询数据'''
        return self.db.blog.post.find_one({'_id': ObjectId(oid)})
    
    def add_one(self):
        '''新增一条数据'''
        post = {
            'title': '标题',
            'content': '博客内容',
            'author': '佚名',
            'create_at': datetime.now()
        }
        return self.db.blog.post.insert_one(post)

    def update(self):
        '''修改一条数据'''
        return self.db.blog.post.update_one({'title': '标题'}, {'$inc': {'x': 1})
        print(matched_count)
        print(modified_count)
        '''修改多条数据'''
        return self.db.blog.post.update({'title': '标题':}, {'$inc': {'x': 1}})

    def delete(self):
        '''一条数据'''
        return self.db.blog.post.delete_one({'title': '标题'})
        print(deleted_count)
        '''多条数据'''
        return self.db.blog.post.delete_many({'title': '标题':})


def main():
    obj = TestMongo()
    res = obj.add_one()
    print(res.inserted_id)


if __name__ == '__main__':
    main()