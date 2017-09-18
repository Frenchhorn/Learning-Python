import os.path

import peewee

# 配置
DATABASE = 'peewee.db'

# 创建数据库
database = peewee.SqliteDatabase(DATABASE)

# 基础类
class BaseModel(peewee.Model):
    class Meta:
        database = database

# 用户表
class User(BaseModel):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    email = peewee.CharField()
    join_date = peewee.DateTimeField()
    
    class Meta:
        order_by = ('username',)

    # 返回关注的对象
    def following(self):
        return User.select().join(
            Relationship, on=Relationship.to_user,
        ).where(Relationship.from_user == self)

    # 返回关注我的对象
    def followers(self):
        return User.select().join(
            Relationship, on=Relationship.from_user,
        ).where(Relationship.to_user == self)

    # 判断是否关注某一用户
    def is_following(self, user):
        return Relationship.select().where(
            (Relationship.from_user == self) &
            (Relationship.to_user == user)
        ).count() > 0

    # 返回头像
    def gravatar_url(self, size=80):
        return 'http://lorempixel.com/'+str(size)+'/'+str(size)+'/?' + self.username

# 关系表
class Relationship(BaseModel):
    from_user = peewee.ForeignKeyField(User, related_name='relationships')
    to_user = peewee.ForeignKeyField(User, related_name='related_to')

    class Meta:
        indexes = (
            (('from_user', 'to_user'), True),
        )

# 消息表
class Message(BaseModel):
    user = peewee.ForeignKeyField(User)
    content = peewee.TextField()
    pub_date = peewee.DateTimeField()

    class Meta:
        order_by = ('-pub_date',)

# 数据库初始化，只有于创建数据库
def create_tables():
    database.connect()
    database.create_tables([User, Relationship, Message])
    database.close()

if __name__ == '__main__':
    if not os.path.isfile(DATABASE):
        create_tables()