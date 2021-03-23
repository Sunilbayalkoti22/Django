
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('price', price, name='price'),
    path('contact', contact, name='contact'),
    path('protfolio', protfolio, name='protfolio'),

]