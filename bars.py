import urllib.request
import zipfile
import json
from math import hypot


destination = 'bari.zip'
url = 'http://data.mos.ru/opendata/export/1796/json/2/1'
urllib.request.urlretrieve(url, destination)
z = zipfile.ZipFile('bari.zip', 'r')
z.extractall()
z.close()
print('Введите,пожалуйста,ваши координаты')
try:
    longitude = float(input('Долгота:'))
except ValueError:
    longitude = None
if longitude is None:
    print('Неверный формат')
try:
    latitude = float(input('Широта:'))
except ValueError:
    latitude = None
if latitude is None:
    print('Неверный формат')
with open('Бары.json',encoding='utf-8') as json_data:
    data=json.load(json_data)
    places = [dat["Cells"]["SeatsCount"] for dat in data]
    
def biggest_bar(data,places):
    max1 = max(places)
    big_bar = [dat["Cells"]["Name"] for dat in data if max1 is dat["Cells"]["SeatsCount"]]
    print ('Самый большой бар:',big_bar)
    
def smallest_bar(data,places):
    min1 = min(places)
    small_bar = [dat["Cells"]["Name"] for dat in data if min1 is dat["Cells"]["SeatsCount"]]
    print('Самый маленький бар:',small_bar[1])
    
def geo_bar(data,longitude,latitude):
    distance=[]
    for dat in data:
        longitude1 = dat["Cells"]["geoData"]["coordinates"][0]
        latitude1 = dat["Cells"]["geoData"]["coordinates"][1]
        distance.append(hypot(longitude1 - longitude, latitude1 - latitude))
    min2 = min(distance)
    for dat in data:
        longitude1 = dat["Cells"]["geoData"]["coordinates"][0]
        latitude1 = dat["Cells"]["geoData"]["coordinates"][1]
        rast = hypot(longitude1 - longitude, latitude1 - latitude)
        if min2 == rast :
            nearest_bar = dat["Cells"]["Name"] 
    print('Самый близкий бар относительно вашей геопозиции:',nearest_bar)
    
biggest_bar(data,places)
smallest_bar(data,places)
geo_bar(data,longitude,latitude)
