# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root@localhost:3306/test_news?charset=utf8')
Base = declarative_base()


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    news_type = Column(String(20), nullable=False)
    img_url = Column(String(200))
    author = Column(String(20))
    view_count = Column(Integer)
    create_at = Column(TIMESTAMP, default=text('now()'))
    updated_at = Column(TIMESTAMP)
    is_vaild = Column(Boolean)


class ORMTest(object):
    def __init__(self):
        self.session = Session()

    def add_one(self):
        new_obj = News(
            title='标题',
            content='内容',
            news_type='体育',
        )
        self.session.add(new_obj)
        self.session.commit()

    def get_one(self):
        '''获取一条数据'''
        return self.session.query(News).get(1)

    def get_more(self):
        '''获取多条数据'''
        return self.session.query(News).filter_by(is_vaild=1)

    def update_data(self, pk):
        '''更新数据'''
        datas = self.session.query(News).filter_by(is_vaild=1)
        for data in datas:
        # data = self.session.query(News).get(pk)
            data.is_vaild = 0
            if data:
                self.session.add(data)
            else:
                return False
        self.session.commit()
        return True

    def delete_data(self):
        '''删除数据'''
        data = self.session.query(News).get(1)
        self.session.delete(data)
        self.session.commit()


def main():
    obj = ORMTest()
    obj.add_one()
        
if __name__ == '__main__':
    main( )
