from django.shortcuts import render
from .models import Datas
import json
from django.http import JsonResponse
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

def login(request):
    if request.method == 'OPTIONS':
        return JsonResponse({'message': 'Login successful'}, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        #user = authenticate(username=username, password=password)
        print(username, password)
        return JsonResponse({'message': 'Login successful'}, status=200)
        """
        else:
            # Authentication failed
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
        """
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)