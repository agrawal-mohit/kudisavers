from django.shortcuts import render
from .models import Product
from django.db.models import Q
import operator
from functools import reduce
from django.core.serializers import serialize
from django.utils.safestring import mark_safe
from django.template import Library
from django.http import HttpResponse
from operator import itemgetter
from django.db.models import Avg, Max, Min
from django.forms.models import model_to_dict
from django.core import serializers

import re, json
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

    sites = ['kara', 'kaymu', 'jumia', 'regalbuyer' ]
    print('Action - mobiles_item_pricelist:')
    section_Q = Q(section__icontains= 'mobiles')
    category_Q = Q(category__icontains= category)
    prodType_Q =  Q(prodType__icontains= prodType)

    type_products = Product.objects.filter(section_Q).filter(category_Q).filter(prodType_Q)

    translation_table = dict.fromkeys(map(ord, '|_-!@#$'), None)
    #WIN - words in name
    win_list = prodName.translate(translation_table).split( )

    win_data = []
    for word in win_list:
        #print('Word : ', word )
        win_data.append({'word' : word , 'matches': len(list(type_products.filter(prodName__icontains= word)))})
    sorted_win_data = sorted(win_data, key=operator.itemgetter('matches'), reverse=True)
    print(sorted_win_data)

    '''
    match_list = []
    for win in sorted_win_data:
        print(win.get('word'))
        match_list.append(win.get('word'))
        print(match_list)
        match_Q = reduce(operator.and_, (Q(prodName__icontains = x) for x in match_list))
        matched_products = type_products.filter(match_Q)
        print(match_list, len(list(matched_products)))
        all_present = 1;
        for site in sites:
            print(site , len(list(matched_products.filter(Q(site__icontains= site)))))
            all_present = all_present*(len(list(matched_products.filter(Q(site__icontains= site)))))
        if (all_present==0):
            match_list.pop()
            break
    '''

    site_best_products = []
    site_Queries = {}
    for site in sites:
        match_list = []
        for win in sorted_win_data:
            match_list.append(win.get('word'))
            #print(match_list)
            match_Q = reduce(operator.and_, (Q(prodName__icontains = x) for x in match_list))
            matched_products = type_products.filter(Q(site__icontains = site)).filter(match_Q)
            if(len(list(matched_products))== 0 or len(match_list)==len(sorted_win_data)):
                match_list.pop()
                match_Q = reduce(operator.and_, (Q(prodName__icontains = x) for x in match_list))
                site_best_match =  type_products.filter(Q(site__icontains = site)).filter(match_Q).order_by("-price")[0]
                print(site, ':', match_list, len(list(type_products.filter(Q(site__icontains = site)).filter(match_Q))), site_best_match)
                site_best_products.append(site_best_match)
                break

    print(site_best_products)

    return render(request, 'price-list.html', {'site_best_products' : mark_safe(serialize('json', site_best_products))})