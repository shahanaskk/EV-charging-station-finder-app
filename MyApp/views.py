from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,Group
from MyApp.models import EV_station, Slot, users
from django.contrib.auth import authenticate,login,logout
from django.utils.crypto import get_random_string
# Create your views here.
def add_EV(request):
    if request.method == "POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        latitude=request.POST['latitude']
        longitude=request.POST['longitude']
        photo=request.FILES['photo']

        fs=FileSystemStorage()
        date=datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'

        fs.save(date,photo)
        path=fs.url(date)

        if User.objects.filter(username=email).exists():
            messages.error(request,"An EV station with this Email already exists")
            return redirect('/add_EV/')

        password = phone

        user = User.objects.create_user(
        username=email,
        email=email,
        password=password
        )

        user.groups.add(Group.objects.get(name='EV_charging_station'))

        obj=EV_station()
        obj.user=user
        obj.name=name
        obj.phone=phone
        obj.email=email
        obj.latitude=latitude
        obj.longitude=longitude
        obj.photo=path
        obj.save()

        messages.success(
        request,
        f"EV Station added successfully! Username: {email} | Temporary Password: {password}")

        return redirect('/admin_view_ev/')
    
    return render (request,'add_EVstation.html') 

def admin_view_ev(request):
    station=EV_station.objects.all()
    return render(request,'admin_view_ev.html',{'data':station})

def edit_ev_station(request,id):

    station=EV_station.objects.get(id=id)

    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        latitude=request.POST['latitude']
        longitude=request.POST['longitude']

        if 'photo' in request.FILES:
            photo=request.FILES['photo']

            fs=FileSystemStorage()
            date=datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'

            fs.save(date,photo)
            path=fs.url(date)
            station.photo=path
            station.save()

        station.name=name
        station.phone=phone
        station.email=email
        station.latitude=latitude
        station.longitude=longitude
        station.save()

        return redirect('/admin_view_ev/')
    
    return render(request,'edit_ev.html',{'data':station})

def delete_ev_station(request,id):
    EV_station.objects.get(id=id).delete()
    return redirect('/admin_view_ev/')

def log_in(request):
    return render(request,'login.html')


def log_inPost(request):
    email=request.POST['email']
    password=request.POST['password']
    user=authenticate(request,username=email,password=password)

    print("Authenticated user:", user)

    if user is not None:
        
        login(request,user)  

        if user.groups.filter(name='admin').exists():
            return redirect('/admin_home/')
        
        if user.groups.filter(name='users').exists():
            
            return redirect('/user_home/')
        
        if user.groups.filter(name='worker').exists():
            
            return redirect('/worker_home/')

        if user.groups.filter(name='EV_charging_station').exists():
                    
                    return redirect('/ev_station_home/')

        else:
             return redirect('/log_in/')
        
    else:
            return redirect('/log_in/')
        

def admin_home(request):
    return render(request,'admin_home.html')

def sign_up(request):
    return render(request,'signUp.html')

def sign_upPost(request):

    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    password=request.POST['password']
    photo=request.FILES['photo']
    vehicle_name=request.POST['vehicle_name']
    vehicle_number=request.POST['vehicle_number']
    place=request.POST['place']

    fs=FileSystemStorage()
    date=datetime.now().strftime('%Y%m%d%H%M%S')+'.jpg'
    fs.save(date,photo)
    path=fs.url(date)

    if User.objects.filter(username=email).exists():
        return render(request, 'signUp.html', {'message': "This Email is already registered!"})


    a=User.objects.create_user(username=email,password=password)
    a.groups.add(Group.objects.get(name='users'))

    obj=users()
    obj.name=name
    obj.phone=phone
    obj.email=email
    obj.photo=path
    obj.vehicle_name=vehicle_name
    obj.vehicle_number=vehicle_number
    obj.place=place
    obj.user=a
    obj.save()

    return redirect('/log_in/')

def user_home(request):
    return render(request,'user_home.html')

def worker_home(request):
    return render(request,'worker_home.html')

def manage_slots(request):
    station=EV_station.objects.get(user=request.user)
    slots = Slot.objects.filter(station=station)
    return render(request, 'manage_slots.html',{'data':station, 'slots':slots})

def add_slots(request):

    station=EV_station.objects.get(user=request.user)    

    if request.method=='POST':
        charger_type=request.POST['charger_type']
        kw=request.POST['kw']
        slot_number=request.POST['slot_number']
        price=request.POST['price']

        slot=Slot()
        slot.station=station
        slot.charger_type=charger_type
        slot.kw=kw
        slot.slot_number=slot_number
        slot.price=price
        slot.save()

        return redirect('/manage_slots/')

    return render(request, 'add_slots.html')

def ev_station_home(request):
    return render(request,'ev_station_home.html')

def edit_slots(request,id):

    station=EV_station.objects.get(user=request.user)    
    
    slot=Slot.objects.get(id=id, station=station)

    if request.method== 'POST':
    
        charger_type=request.POST['charger_type']
        kw=request.POST['kw']
        slot_number=request.POST['slot_number']
        price=request.POST['price']

        slot.charger_type=charger_type
        slot.kw=kw
        slot.slot_number=slot_number
        slot.price=price
        slot.save()

        return redirect('/manage_slots/')

    return render(request, 'edit_slot.html', {'data':slot})

def delete_slot(request,id):
    station=EV_station.objects.get(user=request.user)
    Slot.objects.get(id=id, station=station).delete()
    return redirect('/manage_slots/')