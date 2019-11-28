from django.conf.urls import url
from . import views
from .views import checkin,checkout

urlpatterns=[
    url(r'^checkin/$',checkin) ,
    url(r'^checkout/$',checkout),
    
]