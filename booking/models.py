from django.db import models
from datetime import datetime

class Airlines(models.Model):
    airline_name=models.CharField(max_length=200)
    airline_model=models.CharField(max_length=50)
    flight_origin=models.CharField(max_length=100)
    flight_destination=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now())
    
class Booked_list(models.Model):
    book_date=models.DateTimeField(null=False)
    book_time=models.DateTimeField(default=datetime.now())
    Airlines=models.ForeignKey(Airlines,on_delete=models.CASCADE)