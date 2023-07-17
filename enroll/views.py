from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from.forms import studentRegistraion
from .models import User
from django.contrib import messages




# Create your views here.
def add_show(request):
  if request.method == 'POST':
     fm=studentRegistraion(request.POST)
     if fm.is_valid():
      nm=fm.cleaned_data['name']
      em=fm.cleaned_data['email']
      pw=fm.cleaned_data['password']
      reg=User(name=nm,email=em)
      reg.save()
      fm=studentRegistraion()
  else:
   fm= studentRegistraion()
  Stud= User.objects.all()
  return render(request,'addandshow.html',{'form':fm, 
 'Stu':Stud})

def delete_data(request,id):
  if request.method=='POST':
   pi=User.objects.get(pk=id)
   pi.delete()
   return HttpResponseRedirect('/add_show/')
  
def update_data(request,id):
   if request.method=='POST':
     pi = User.objects.get(pk=id)
     fm=studentRegistraion(request.POST,instance=pi)
     if fm.is_valid():
        fm.save()
        fm=studentRegistraion()
        messages.success(request,"Updated Succesfully")
   else:
      pi=User.objects.get(pk=id)
      fm=studentRegistraion(instance=pi)
   return render(request,'updatestudent.html',{'form':fm})

