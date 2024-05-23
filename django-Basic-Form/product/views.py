from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Customer, Shipper, Shipment
from django.views.decorators.csrf import csrf_exempt

def home(request):
    mydata=Shipment.objects.all()
    if(mydata!=''):
        return render(request,'home.html', {'datas':mydata})
    else:
        return render(request,'home.html')
@csrf_exempt
def sendListing(request):
    if request.method == 'GET':
        return JsonResponse({'shipmentID': "1",
                            'pickupLocation' : Shipment.objects.get(id=1).Pickup,
                            'deliveryLocation':Shipment.objects.get(id=1).Drop,
                            'shipmentWeight':str(Shipment.objects.get(id=1).Weight),
                            'itemName':Shipment.objects.get(id=1).Type}, status=200)

@csrf_exempt
def filterShipment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        pickup = data.get('pickup')
        delivery = data.get('delivery')

        shipments = Shipment.objects.filter(Pickup = pickup).filter(Drop = delivery)
        data = list(shipments.values())
        return JsonResponse({'data': data}, status=200)

@csrf_exempt
def addData(request): 
    if request.method == 'POST':
        data = json.loads(request.body)
        type=data.get('type')
        length=data.get('length')
        width=data.get('width')
        height=data.get('height')
        quantity=data.get('quantity')
        pickup=data.get('pickup')
        drop=data.get('drop')

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
        for sp in mydata:
            print(sp.Type, sp.Drop)
            
        return JsonResponse({}, status=201)
    else:
        return JsonResponse({'error':"Sucess"}, status=405)

def updateData(request, id):
    mydata=Shipment.objects.get(id=id)

    return render(request, 'update.html', {'data':mydata})

@csrf_exempt
def login(request):
    
    if request.method == 'POST':
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





def find_shipments():
    shipments = Shipment.objects.all()
  
    
        
    print("Query results:", list(shipments))

   
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