app = input("Application")
usrnm = input("Username")
pwd = input("Password")

from mongoengine import *
connect('mongoengine_test',host ='localhost',port=27017)

import datetime

class Post(Document):
    app = StringField(required=True, max_length=200)
    usrnm = StringField(required=True)
    pwd = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)

post_1 = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Scott'
)
post_1.save()       # This will perform an insert
print(post_1.title)
post_1.title = 'A Better Post Title'
post_1.save()       # This will perform an atomic edit on "title"
print(post_1.title)
print(post_1.content)
