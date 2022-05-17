from django.shortcuts import render

from eshopping.models import Destination

# Create your views here.
def index(request):

    #dest1 = Destination()
    #dest1.name = 'Incredible Gujarat'
    #dest1.desc = 'Renowned for beaches, temples and history'
    #dest1.img ='gujarat.jpg'

    #dest2 = Destination()
    #dest2.name = 'Essence of North'
    #dest2.desc = 'Encompassing majestic & mesmerizing'
    #dest2.img ='north.jpg'

    #dest3 = Destination()
    #dest3.name = 'Ladakh And Kashmir Tour'
    #dest3.desc = 'Known for their natural beauty'
    #dest3.img ='kashmir.jpg'

    #dest4 = Destination()
    #dest4.name = 'Rajasthan Heritage Tour'
    #dest4.desc = 'Feel like a royal by visiting ❤ Rajasthan'  
    #dest4.img ='rajastan.jpg'

    dests = Destination.objects.all()
    
    return render(request,'index.html', {'dests':dests})