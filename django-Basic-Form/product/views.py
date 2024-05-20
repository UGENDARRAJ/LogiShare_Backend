from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Customer, Shipper, Shipment

def home(request):
    mydata=Shipment.objects.all()
    if(mydata!=''):
        return render(request,'home.html', {'datas':mydata})
    else:
        return render(request,'home.html')

def addData(request): 
    if request.method == 'POST':
        type=request.POST['type']
        length=request.POST['length']
        width=request.POST['width']
        height=request.POST['height']
        quantity=request.POST['quantity']
        pickup=request.POST['pickup']
        drop=request.POST['drop']

        obj=Shipment()
        obj.Type=type
        obj.Length=length
        obj.Width=width
        obj.Height=height
        obj.Quantity=quantity
        obj.Pickup = pickup
        obj.Drop = drop
        obj.save()
        mydata = Shipment.objects.all()
        return render(request,'home.html', {'datas':mydata})
    return render(request,'home.html')

def updateData(request, id):
    mydata=Shipment.objects.get(id=id)
    return render(request, 'update.html', {'data':mydata})


def login(request):
    if request.method == 'OPTIONS':
        return JsonResponse({'message': 'Login successful'}, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('phno')
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
def cust_register(request):
    if request.method == 'POST':
        #this wont work
        user = authenticate(phone=request.POST['phno'], password=request.POST['password'])   
        if user is None:
            Customer.objects.create(phno=request.POST['phno'], password_hash=request.POST['password'])
        else:
            return JsonResponse({'error': 'User already exists'}, status=400)
        return JsonResponse({'message': 'User created successfully'}, status=201)        
    
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def shipper_register(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])   
        if user is None:
            Shipper.objects.create(username=request.POST['username'], password_hash=request.POST['password'])
        else:
            return JsonResponse({'error': 'User already exists'}, status=400)
        return JsonResponse({'message': 'User created successfully'}, status=201)        
    
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)