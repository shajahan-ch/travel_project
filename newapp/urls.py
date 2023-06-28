

from django.urls import path

from newapp import views

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition')
]