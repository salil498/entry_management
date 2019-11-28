from django.db import models

# Create your models here.
class HostDetails(models.Model):
    host_name=models.CharField(max_length=500,null=True)
    host_phone=models.BigIntegerField()
    host_email=models.CharField(max_length=500,null=True)
class Checkin(models.Model):
    visitor_name=models.CharField(max_length=500,null=True)
    visitor_phone=models.BigIntegerField()
    visitor_email=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=10,default='CHECKED_IN')
    checkin_time=models.DateTimeField(auto_now=True)
    checkout_time=models.DateTimeField(auto_now=True)
    host_id=models.ForeignKey(HostDetails,null=True,on_delete=models.SET_NULL)
