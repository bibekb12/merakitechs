from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('flightdetail/<int:id>/', views.detailairlines, name='airlinedetail'),
    path('bookedlist/<int:id>/', views.bookedlist, name='bookedlist'),
]
