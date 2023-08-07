import json
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb+srv://NickoSuerte:Nick1987Burjuy@cluster0.tquscaz.mongodb.net/")
db = client.hw_10

# with open('C:\Users\Mykola\Documents\GitHub\Web1.1.Home_work__10_3\hw_project\utils', 'r', encoding='utf-8') as fd:
#     quotes = json.load(fd)

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'full_name': quote['author']})
    
    if author:
        print(author)
        db.quotes.insert_one({
            'quote': quote["text"],
            'tags': quote['tags'],       
            'author': ObjectId(author['_id'])       
        })




