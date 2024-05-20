from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Datas
# Create your views here.
def home(request):
    mydata=Datas.objects.all()
    if(mydata!=''):
        return render(request,'home.html', {'datas':mydata})
    else:
        return render(request,'home.html')

def addData(request): 
    if request.method=='POST':
        type=request.POST['type']
        length=request.POST['length']
        width=request.POST['width']
        height=request.POST['height']
        quantity=request.POST['quantity']
        pickup=request.POST['pickup']
        drop=request.POST['drop']

        obj=Datas()
        obj.Type=type
        obj.Length=length
        obj.Width=width
        obj.Height=height
        obj.Quantity=quantity
        obj.Pickup = pickup
        obj.Drop = drop
        obj.save()
        mydata = Datas.objects.all()
        return render(request,'home.html', {'datas':mydata})
    return render(request,'home.html')

def updateData(request, id):
    mydata=Datas.objects.get(id=id)
    return render(request, 'update.html', {'data':mydata})