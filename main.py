from pymongo import MongoClient


client = MongoClient('localhost',27017)

db = client['mybase']

cred = db.usrcredntl
rec = {
    'site': 'xyz',
    'usrnm': 'payload',
    'pwd': 'armgdn'
}

cred.insert_one(rec)