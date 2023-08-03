from pymongo import MongoClient



def get_db():

    client = MongoClient("mongodb+srv://NickoSuerte:Nick1987Burjuy@cluster0.tquscaz.mongodb.net/")
    db = client.hw_10

    return db