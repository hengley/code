# http://docs.mongoengine.org/tutorial.html

from mongoengine import connect, Document, EmbeddedDocument, EmbeddedDocumentField,\
    StringField, FloatField, IntField, DateTimeField, ListField

connect('students')

class Grade(EmbeddedDocument):
    '''学生的成绩'''
    name = StringField(required=True)
    score = FloatField(required=True)


SEX_CHOIES = (
    ('female', '女'),
    ('male', '男')
)

class Student(Document):
    '''学生模型'''
    name = StringField(required=True, max_length=20)
    age = IntField(required=True)
    sex = StringField(required=True, choices=SEX_CHOIES)
    grade = FloatField()
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade))

    meta = {
        'collection': 'students',
        '_ordering_': ['-grade']
    }


class TestMongoengine(object):

    def add_one(self):
        '''新增数据'''
        English = Grade(
            name = '英语',
            score = 56
        )
        math = Grade(
            name = '数学',
            score = 100
        )
        Chinese = Grade(
            name = '语文',
            score = 89
        )
        stu_obj = Student(
            name = '张三',
            age = 12,
            sex = 'male',
            grades = [English, math, Chinese]
        )
        # stu_obj.remark = 'remark'
        stu_obj.save()
        return stu_obj

    def get_one(self):
        '''查询一条数据'''
        return Student.objects.first()

    def get_more(self):
        '''查询多条数据'''
        return Student.objects.all()

    def get_one_from_oid(self, oid):
        '''根据id查询数据'''
        return Student.objects.filter(pk=oid).first()

    def update(self):
        '''修改一条数据'''
        return Student.objects.filter(age=12).updata_one(inc__age=1)
        '''修改多条数据'''
        return Student.objects.filter(age=12).updata(inc__age=1)

    def delete(self):
        '''删除一条数据'''
        return Student.objects.filter(age__gt=12, sex='male').first().delete()
        '''删除多条数据'''
        return Student.objects.filter(age=12).delete()

def main():
    obj = TestMongoengine()
    res = obj.add_one()
    print(res.id)


if __name__ == '__main__':
    main()