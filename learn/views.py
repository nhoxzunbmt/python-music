from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,FileResponse,JsonResponse
from learn.models import Bloger
# Create your views here.
# HttpResponseRedirect('/about')

def home(request):

    b = Bloger(name='Beatles Blog', tagline='All the latest Beatles news.')
    b.save();

    b = Bloger.objects.get(pk=1)

    
    response = JsonResponse({'name' : b.name,'id' : b.id})
  
    return response

def about(request):
    return HttpResponse('About')