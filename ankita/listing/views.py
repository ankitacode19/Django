from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.img = 'img-1.jpg'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.img = 'img-2.jpg'
    dest2.price = 650

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.img = 'img-3.jpg'
    dest3.price = 750

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
