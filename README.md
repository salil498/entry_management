# entry_management
This is an entry management software that  manages the entry details of the visitors
The backend is done using django and frontend is done by simple javascript. As soon as the visitor enters the details a message and a mail is triggere to the corresponding host with the details of the user and once he checks out he gets a mail and message with the details of the visit.
Packages required --> yagmail. pip install yagmail . 
sms is sent through--> smsjust.com api
To send the mail replace with your email and password in the views.py file and to send the message create an account on smsjust.com and enter the corresponding details in the views.py file

Form at the frontend takes the details from the visitor , at the backend the data is stored and a mail and message to the host is triggered
using yagmail and smsjust api and the current time stamp is also stored. Once the user checks out the check out time is stored and the details of the visit are sent to the visitor using the same yagmail and smsjust api. 
Two separate models have been created one to store the details of visitor and other to store details of host. If the details of that host exist then same details are used instead to creating new entry every time to reduce data redundancy.
if the user who wants to checkin after he has already checked in then an alert is generated.
If the user wants to checkout then he/she has to enter the mobile number used at the time of checkin.

Backend has been separately tested using Postman and is completely functional
Frontend is made to receive the details and can be modified much more to make it more user friendly and needs improvement.
