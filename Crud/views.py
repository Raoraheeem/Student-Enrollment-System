from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime, timedelta


def home(request):
  return render(request,'base.html')

def setcookie(request):
   reponse= render(request,'setcookie.html')
   reponse.set_signed_cookie('name','rao', salt='nm',expires=datetime.utcnow()+timedelta(days=2))
   return reponse
def getcookie(request):
   
   #name=request.COOKIES['name']
   name=request.get_signed_cookie('name',default="Guest",salt='nm')
   return render(request,'getcookie.html',{'name':name})

def delcookie(request):
   reponse=render(request,'delcookie.html')
   reponse.delete_cookie('name')
   return reponse


   


