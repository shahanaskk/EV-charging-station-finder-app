from datetime import datetime

from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,Group
from MyApp.models import EV_station, users
from django.contrib.auth import authenticate,login,logout
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

        obj=EV_station()
        obj.name=name
        obj.phone=phone
        obj.email=email
        obj.latitude=latitude
        obj.longitude=longitude
        obj.photo=path
        obj.save()

        return redirect('/add_EV/')
    
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

