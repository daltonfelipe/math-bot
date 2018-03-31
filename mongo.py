from pymongo import MongoClient
import os
URI = os.environ['MONGODB_URI']

client = MongoClient(URI)
db = client.get_default_database()
msg = db['messages']

def save(data):
    message = {'user':data['from_user'].username,'user_id':data['from_user'].id,'chat_id':data.chat.id,'chat_type':data.chat.type,'content':data.text,'date':data.date,'chat_title':data.chat.title}
    msg.insert_one(message)
