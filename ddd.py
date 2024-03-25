from tinydb import TinyDB, Query
db = TinyDB('db.json')
table = db.table('posts')

table.insert({'title': 'Rohlik', 'content': 'bezne pecivo'})
table.insert({'title': 'Houska', 'content': 'beznejsi pecivo'})
table.insert({'title': 'Chleba', 'content': 'nejbeznejsí pecivo'})
table.insert({'title': 'Dalamanek', 'content': 'nejmene bezny pecivo'})
table.insert({'title': 'Kaizerka', 'content': 'bezne pecivo'})

print(table.all())