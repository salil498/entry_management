from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
import json
import requests
from .models import Checkin,HostDetails
import datetime
import yagmail
# Create your views here.
def checkin(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        print(data)
        already_checked_in = list(Checkin.objects.filter(visitor_name=data['visitor_name'], visitor_phone=data['visitor_phone'],status='CHECKED_IN').values('status'))
        if len(already_checked_in)>0:
            print("OOO")
            return JsonResponse({"message": "User with this name and mobile number already_checked_in"},status=200)
        else:
            check_host_exists = list(HostDetails.objects.filter(host_name=data['host_name'], host_phone=data['host_phone'],host_email=data['host_email']).values('id'))
            print(check_host_exists)
            if len(check_host_exists)>0:
                host_id = check_host_exists[0]['id']
            else:
                create_host_entry = HostDetails.objects.create(host_name=data['host_name'], host_phone=data['host_phone'],host_email=data['host_email'])
                host_id = create_host_entry.id
            query_check_in = Checkin.objects.create(host_id=HostDetails.objects.get(id=host_id),visitor_name=data['visitor_name'], visitor_phone=data['visitor_phone'],visitor_email=data['visitor_email'])
            if query_check_in:
                message="New check in!!! \nVisitor name:" +data['visitor_name']+ "\nemail:"+data['visitor_email']+"\nphone:"+str(data['visitor_phone'])

                data1 = {'username':"username of smsjust.com",'pass':"password here ",'senderid':'sender id here','dest_mobileno':str(data['host_phone']),'message':message}
                send_detail = requests.post('https://www.smsjust.com/blank/sms/user/urlsms.php',data=data1)
                yag = yagmail.SMTP({'email here': 'header here'}, '*email password here*')
                subject = "NEW Checkin!"
                contents = [message]
                yag.send(data['host_email'], subject, contents)

                return JsonResponse({"message": "Successfully Checked in"},status=200)
            else:
                print("noooo")
                return JsonResponse({"message": "Could not Check in. Please try again"},status=200)

    else:
        return JsonResponse({"message":"request method error"},status=502)

def checkout(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        print(data)
        already_checked_in = list(Checkin.objects.filter(visitor_phone=data['visitor_phone'],status='CHECKED_IN').values('visitor_email'))
        if len(already_checked_in)>0:
            time =datetime.datetime.now()
            query_check_out = Checkin.objects.filter(visitor_phone=data['visitor_phone'],status='CHECKED_IN').update(status='CHECK_OUT',checkout_time=time)
            query_check_out_details= list(Checkin.objects.filter(visitor_phone=data['visitor_phone'],status='CHECK_OUT').values('visitor_name','visitor_phone','checkin_time','checkout_time','host_id__host_name','host_id__host_phone'))
            message="You Successfully checked out!!! \nVisitor name:" +query_check_out_details[-1]['visitor_name']+"\nphone:"+str(data['visitor_phone'])+"\nCheckin Time: "+str(query_check_out_details[-1]['checkin_time'])+"\nCheckout Time: "+str(query_check_out_details[-1]['checkout_time'])+"\nHost: "+query_check_out_details[-1]['host_id__host_name']

            data1 = {'username':"kietgzb",'pass':"kiet@123",'senderid':'KIETGZ','dest_mobileno':str(query_check_out_details[-1]['host_id__host_phone']),'message':message}
            send_detail = requests.post('https://www.smsjust.com/blank/sms/user/urlsms.php',data=data1)
            yag = yagmail.SMTP({'email here': 'header here'}, 'password')
            subject = "Visit Details!"
            contents = [message]
            yag.send(already_checked_in[0]['visitor_email'], subject, contents)
            return JsonResponse({"message": "Successfully checked out!!!!"},status=200)
        else:
                return JsonResponse({"message": "No Check in entry found for that mobile number"},status=200)

    else:
        return JsonResponse({"message":"request method error"},status=502)
