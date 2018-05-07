from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,FileResponse,JsonResponse
from models import Group,Person,Membership
# Create your views here.
# HttpResponseRedirect('/about')

def home(request):
 
    #response = FileResponse(open('media/banner-email-remind.jpg', 'rb'),content_type='image/jpeg')

    response = JsonResponse({'foo': 'bar'})

    paul = Group.objects.filter(members__name__startswith='Paul')


    return response

def about(request):
    return HttpResponse('About')