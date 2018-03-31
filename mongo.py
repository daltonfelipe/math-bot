from pymongo import MongoClient

client = MongoClient("mongodb://dalton10:dalton10@ds131329.mlab.com:31329/math-bot")
db = client.get_default_database()
msg = db['messages']

def save(data):
    msg.insert_one({'user':data['from'].username,'user_id':data['from'].id,'chat_id':data.chat.id,'chat_type':data.chat.type,'content':data.text,'date':data.date})
