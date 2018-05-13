from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,FileResponse,JsonResponse
from learn.models import Bloger,Entry,Author
from datetime import date,datetime
from random import randint
# Create your views here.
# HttpResponseRedirect('/about')

def home(request):

    # b = Bloger(name='Beatles Blog', tagline='All the latest Beatles news.')
    # b.save();

    # b = Bloger.objects.get(pk=1)

    # entry = Entry.objects.get(pk=1)

    # # joe = Author.objects.create(name="Joe")
    # paul = Author.objects.create(name="Paul")
    # joe = Author.objects.get(pk=5)
    # entry.authors.add(joe,paul)
    
    # bloger1 = Bloger.objects.get(pk=1)

    # en =  Entry()
    # en.bloger = bloger1;
    # en.headline = 'a'
    # en.body_text = 'Abc ' 
    # en.pub_date = datetime.now(tz=None)
    # en.mod_date = datetime.now(tz=None)
    # en.n_comments = 1
    # en.n_pingbacks = 1
    # en.rating = 1
    # en.save()

    q1 = Entry.objects.filter(headline__startswith='a')
    

    


    

    
    
    response = JsonResponse({'status' : 'success'})
  
    return response

def about(request):
    return HttpResponse('About')