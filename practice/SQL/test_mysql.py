import MySQLdb


class MySQLsecrch(object):
    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='',
                db='flask_news',
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    def get_one(self):
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `news_type` = %s ORDER BY `created_at` DESC;' 
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql, ('体育', ))
        # 拿到结果
        res = cursor.fetchone()
        # 处理结果
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()

    def get_more(self):
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `news_type` = %s ORDER BY `created_at` DESC;' 
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql, ('体育', ))
        # 拿到结果
        res = [dict(zip([k[0] for k in cursor.description], row) for row in cursor.fetchall())]
        # 处理结果
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return res

    def get_more_by_page(self, page, pagesize):
        offset = (page - 1) * pagesize
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `news_type` = %s ORDER BY `created_at` DESC LIMIT %s, %s;' 
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql, ('体育', offset, pagesize))
        # 拿到结果
        res = [dict(zip([k[0] for k in cursor.description], row) for row in cursor.fetchall())]
        # 处理结果
        # 关闭cursor/连接
        cursor.close()
        self.close_conn()
        return res
    
    def add_one(self):
        try:
            # 准备SQL
            sql = 'INSERT INTO `news` (`title`, `content`, `news_type`, `img_url`) VALUE(%s, %s, %s, %s);' 
            # 找到cursor
            cursor = self.conn.cursor()
            # 执行sql
            cursor.execute(sql, ('标题', '内容', '类型', '/static/images/7'))
            # 执行事务
            self.conn.commit()
            # 关闭cursor/连接
            cursor.close()    
        except:
            print('Error!')
            self.conn.rollback()
        self.close_conn()

def main():
    obj = MySQLsecrch()
    obj.add_one()
    # res = obj.get_more()
    # res = obj.get_more_by_page(2, 3)
    # for r in res:
    #     print(res)


if __name__ == '__main__':
    main()