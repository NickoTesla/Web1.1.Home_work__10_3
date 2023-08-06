import os
import django

from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Quote, Tag, Author 

client = MongoClient("mongodb+srv://NickoSuerte:Nick1987Burjuy@cluster0.tquscaz.mongodb.net/")
db = client.hw_10

authors = db.authors.find() 

for author in authors:
    Author.objects.get_or_create(
        fullname=author['full_name'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['author_description'],
    )

