
from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.index, name='index'),
    # path('details/', views.details, name='details'),
    path('contact', views.contact_view, name='contact'),

]