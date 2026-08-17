from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class users(models.Model):
    photo = models.ImageField(upload_to='users/')
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    place=models.CharField(max_length=100)
    vehicle_number=models.CharField(max_length=50)
    vehicle_name=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class worker(models.Model):
    photo = models.ImageField(upload_to='workers/')
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)  
    specialization = models.CharField(max_length=100,default='General')
    experience = models.IntegerField(default=0)
    ID_proof=models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class EV_station(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    photo= models.ImageField(upload_to='stations/')
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)  
    latitude=models.FloatField()
    longitude=models.FloatField()


class Slot(models.Model):
    station = models.ForeignKey(EV_station, on_delete=models.CASCADE)
    charger_type = models.CharField(max_length=100)
    kw = models.FloatField()
    slot_number = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    

    def __str__(self):
        return f"{self.station.name} - Slot {self.slot_number}"

    
class Booking(models.Model):
    ev_users = models.ForeignKey(users, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    duration = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return self.ev_users.name
    


