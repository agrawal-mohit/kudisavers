from django.shortcuts import render
from .models import Product
from django.db.models import Q
import operator
from functools import reduce
from django.core.serializers import serialize
from django.utils.safestring import mark_safe
from django.template import Library
from django.http import HttpResponse
import re
register = Library()

# Create your views here.

def home(request):
    return render(request, 'home.html', {}) #Looks for html files inside app_kudisavers/templates

def awshome(request):
    return HttpResponse("Hello from django, try out <a href='/admin/'>/admin/</a>\n")

def section(request):
    return render(request, 'section.html', {})

def mobiles(request):
    mobilePhones = Product.objects.filter(section__icontains='Mobiles')
    #tablets = Product.objects.filter(prodTypeName__icontains='tablet').exclude(prodTypeName__icontains='accessories')
    #mobileAccessories = Product.objects.filter(prodTypeName__icontains='mobile').filter(prodTypeName__icontains='accessories').exclude(prodName__icontains='headphone').exclude(prodName__icontains='headset')
    #headphonesHeadsets = Product.objects.filter(prodTypeName__icontains='mobile').filter( Q(prodName__icontains='headphone') | Q(prodName__icontains='headset'))

    return render(request, 'mobiles.html')


def computers(request):
    return render(request, 'computers.html', {'page' : "computers"})

def cameras(request):
    return render(request, 'cameras.html', {'page' : "cameras"})

def electronics(request):
    return render(request, 'electronics.html', {})

def appliances(request):
    return render(request, 'appliances.html', {})

def care(request):
    return render(request, 'care.html', {})

def men(request):
    return render(request, 'men.html', {})

def women(request):
    return render(request, 'women.html', {})

def kids(request):
    return render(request, 'kids.html', {})

def homedecor(request):
    return render(request, 'homedecor.html', {})


def mobiles_item(request, category, prodType):
    #prodTypeKeys = prodType.lower().split('-')
    #prodDescKeys = prodDesc.lower().split('-')
    #prodTypeQuery = reduce(operator.or_, (Q(prodTypeName__icontains = x) for x   in prodTypeKeys))
    #prodDescQuery = reduce(operator.and_, (Q(prodDesc__icontains     = x) for x   in prodDescKeys))
    #products = Product.objects.filter(prodType__icontains= prodType)
    products = mark_safe(serialize('json', Product.objects.filter(prodType__icontains= prodType)))

    return render(request, 'products-list.html', {'products' : products })


def cameras_item(request, prodType, prodDesc):
    prodTypeKeys = prodType.lower().split('-')
    prodDescKeys = prodDesc.lower().split('-')
    prodTypeQuery = reduce(operator.or_, (Q(prodTypeName__icontains = x) for x   in prodTypeKeys))
    prodDescQuery = reduce(operator.and_, (Q(prodDesc__icontains     = x) for x   in prodDescKeys))
    products = Product.objects.filter(prodTypeQuery).filter(prodDescQuery)

    return render(request, 'products-list.html', {'products' : products })

def mobiles_item_pricelist(request, category, prodType, prodName):
    print(category)
    print(prodType)
    print(prodName)
    #print(re.sub("[!@#$%^&*()[]\{\};:,./<>?\|`~-=_+]", "", prodName))
    return render(request, 'price-list.html', {'productname' : prodName })