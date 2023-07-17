from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from.models import Markssheet
from django.contrib import messages
from.forms import Uploadmarks



def Markssheet1(request,name):
 if request.method=='POST':
      fm=Uploadmarks(request.POST)
      if fm.is_valid():
       Mat=fm.cleaned_data['Maths']
       Phy=fm.cleaned_data['Physics']
       Chy=fm.cleaned_data['Chemistry']
       Bio=fm.cleaned_data['Biology']
       Eng=fm.cleaned_data['English']
       Tot=fm.cleaned_data['Total']
       Per=fm.cleaned_data['Percentage']
       Add=Markssheet(Maths=Mat,Physics=Phy,Chemistry=Chy,Biology=Bio,English=Eng,Total=Tot,Percentage=Per)
       Add.save()
       fm=Uploadmarks()
       messages.success(request,"Marks Uploaded Succesfully")
 else:
      fm=Uploadmarks()
 mar=Markssheet.objects.all()
 return render(request,'Markssheet.html',{'name':name,'form':fm,'marks':mar})

def delete_marks(request,name):
   if request.method=='POST':
      pi=Markssheet.objects.get(pk=name)
      pi.delete()
   return HttpResponseRedirect('/add_show/',)

def update_marks(request,id):
   if request.method=='POST':
     pi = Markssheet.objects.get(pk=id)
     fm=Uploadmarks(request.POST,instance=pi)
     if fm.is_valid():
        fm.save()
        fm=Uploadmarks()
        messages.success(request,"Updated Succesfully")
   else:
      pi=Markssheet.objects.get(pk=id)
      fm=Uploadmarks(instance=pi)
   return render(request,'updatemarks.html',{'form':fm})
   
    

# Create your views here.
