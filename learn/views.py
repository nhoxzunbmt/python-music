from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,FileResponse,JsonResponse
from learn.models import Bloger,Entry,Author
from datetime import date,datetime
from random import randint
import datetime
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

    # for  x in range(0,99):
    #     body = 'Entry ' + str(x)
    #     en =  Entry()
    #     en.bloger = bloger1;
    #     en.headline = body
    #     en.body_text = body
    #     en.pub_date = datetime.now(tz=None)
    #     en.mod_date = datetime.now(tz=None)
    #     en.n_comments = 1
    #     en.n_pingbacks = 1
    #     en.rating = 1
    #     en.save()

    # q1 = Entry.objects.filter(headline__startswith='a')
    

      
    # Entry.objects.order_by('headline')[0]

    # Entry.objects.filter(pub_date__lte='2018-05-14')

    # Entry.objects.filter(headline__exact="1")

    # Entry.objects.folter(name__contains='a')
    

    
    
    
    
    response = JsonResponse({'status' : 'success'})
  
    return response

def about(request, year=2005):
    response = JsonResponse({'status' : year})
    return response

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def upload_file(request):
    return '123'