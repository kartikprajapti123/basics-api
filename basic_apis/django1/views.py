from django.shortcuts import render
from django.http import HttpResponse
from .models import address,Person

# Create your views here.
def index(request):
    try:
        
        product=Person.objects.filter(address1__id__gte=5)
        print(product)
        
    except Exception as e:
        print(e)
    
    return render(request,"index.html")
def address_create(request):
    address1=address.objects.create(address="i am staying at ahmedabad in gujarat")
    return render(request,"index.html")


# for updating objects in django

def update_objects(request):
    address1=address.objects.filter(id=6).update(address="ppppppppppppppppppppppp")
    return render(request,"index.html")


# for deleting objects from database or tabel

def update_objects(request):
    address1=address.objects.filter(id=6).delete()
    return render(request,"index.html")


# in orm their is row function whic is used for sending databse in html 

def row_query(request):
    address1=Person.objects.raw("SELECT * FROM address")
    print(address1)
    for i in address1:
        print(i)
    return render(request,"index.html")