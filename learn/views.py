from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,FileResponse,JsonResponse

# Create your views here.
# HttpResponseRedirect('/about')

def home(request):
 
    #response = FileResponse(open('media/banner-email-remind.jpg', 'rb'),content_type='image/jpeg')

    response = JsonResponse({'foo': 'bar'})

    return response

def about(request):
    return HttpResponse('About')