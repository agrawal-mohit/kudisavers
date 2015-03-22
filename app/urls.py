from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^search/$', views.search),
    url(r'^form/$', views.form),
    url(r'^$', views.home),
    url(r'^section/$', views.section),
    url(r'^mobiles/$', views.mobiles),
    url(r'^computers/$', views.computers),
    url(r'^cameras/$', views.cameras),
    url(r'^electronics/$', views.electronics),
    url(r'^appliances/$', views.appliances),
    url(r'^care/$', views.care),
    url(r'^men/$', views.men),
    url(r'^women/$', views.women),
    url(r'^kids/$', views.kids),
    url(r'^homedecor/$', views.homedecor),

    url(r'^mobiles/(?P<category>[a-zA-Z-]+)/(?P<prodType>[a-zA-Z-]+)$', views.mobiles_item),
    url(r'^cameras/(?P<category>[a-zA-Z-]+)/(?P<prodType>[a-zA-Z-]+)$', views.cameras_item),

     url(r'^mobiles/(?P<category>[a-zA-Z-]+)/(?P<prodType>[a-zA-Z-]+)/(?P<prodName>.*)$', views.mobiles_item_pricelist),

)
