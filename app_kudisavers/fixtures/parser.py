# -*- coding: utf-8 -*-


import json

data = []
n = 0

with open('mobiles-data.json') as f:
	data_str = dict()
	for line in f:
		n = n + 1
		datum = json.loads(line)
		if(str(datum['category']) in data_str.keys()):
			data_str[str(datum['category'])][datum['prodType']] = 'http://c0028545.cdn1.cloudfiles.rackspacecloud.com/new3595-204-thumb.jpg'
		else:
			data_str[str(datum['category'])] = dict()
		if(type(datum['price'] is str)):
			datum['price'] =  float(str(datum['price']).replace(",", "")) or 0.00
			data.append({"model" : "app_kudisavers.product", "pk" : n ,"fields" : datum})
		

f.close()
#file = open('mobiles-fixture.json', 'wb')
#file.write(json.dumps(data, indent=4))
#file.close()


str_file = open('mobiles-str.json', 'wb')
str_file.write(json.dumps(data_str, indent=4))
str_file.close()