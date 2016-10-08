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
print('Введите,пожалуйста,ваши координаты(вначале долготу,потом широту')
x1 = float(input())
y1 = float(input())
with open('Бары.json',encoding='utf-8') as json_data:
    data=json.load(json_data)
    places = [dat["Cells"]["SeatsCount"] for dat in data]
    
def biggest_bar(data,places):
    max1 = max(places)
    big_bar = [dat["Cells"]["Name"] for dat in data if max1 == dat["Cells"]["SeatsCount"]]
    print (big_bar)
    
def smallest_bar(data,places):
    min1 = min(places)
    small_bar = [dat["Cells"]["Name"] for dat in data if min1 == dat["Cells"]["SeatsCount"]]
    print(small_bar[1])
    
def geo_bar(data,x1,y1):
    distance=[]
    for dat in data:
        x2 = dat["Cells"]["geoData"]["coordinates"][0]
        y2 = dat["Cells"]["geoData"]["coordinates"][1]
        distance.append(hypot(x2 - x1, y2 - y1))
    min2 = min(distance)
    for dat in data:
        x2 = dat["Cells"]["geoData"]["coordinates"][0]
        y2 = dat["Cells"]["geoData"]["coordinates"][1]
        rast = hypot(x2 - x1, y2 - y1)
        if min2 == rast :
            nearest_bar = dat["Cells"]["Name"] 
    print(nearest_bar)
    
biggest_bar(data,places)
smallest_bar(data,places)
geo_bar(data,x1,y1)
