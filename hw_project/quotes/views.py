from django.shortcuts import render
from django.core.paginator import Paginator

from.utils import get_db
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Tag, Quote

# Create your views here.
def main(request, page=1): 
   db = get_db()
   quotes = db.quotes.find()
   per_page = 10
   paginator = Paginator(list(quotes), per_page)
   quotes_on_page = paginator.page(page) 
   return render(request, 'quotes/index.html', context={"quotes":quotes_on_page})

def detail(request, author_fullname):
   author = get_object_or_404(Author, fullname=author_fullname)
   return render(request, 'quotes/author_detail.html', {"author": author})


def detail_tag(request, tag_name):
   tag = Tag.objects.filter(name=tag_name).first()
   quotes = Quote.objects.filter(tags=tag.id).all()
   return render(request, 'quotes/tag_detail.html', {"quotes": quotes})


# def detail(request, note_id):
#     note = get_object_or_404(Note, pk=note_id)
#     return render(request, 'hw_project/index.html', {"note": note})



#it was before changes 08/06/23 (Buttons) 

# from django.shortcuts import render
# from django.core.paginator import Paginator

# from.utils import get_db


# # Create your views here.
# def main(request, page=1): 
#    db = get_db()
#    quotes = db.quotes.find()
#    per_page = 10
#    paginator = Paginator(list(quotes), per_page)
#    quotes_on_page = paginator.page(page) 
#    return render(request, 'quotes/index.html', context={"quotes":quotes_on_page})






    
