import urllib.request
import zipfile
import json
from math import hypot
import sys

def input1():
    try:
        longitude = float(input('Долгота:'))
        return (longitude)
    except ValueError:
        
        longitude = None
    if longitude is None:
        print('Неверный формат')
        sys.exit()

def input2():
    try:
        latitude = float(input('Широта:'))
        return (latitude)
    except ValueError:
        latitude = None
    if latitude is None:
        print('Неверный формат')
        sys.exit()

def open_json():
    with open('Бары.json',encoding='utf-8') as json_data:
        return (json.load(json_data))
    
def biggest_bar(data):
    return(max(data, key = lambda x: x["Cells"]["SeatsCount"]))
    
def smallest_bar(data):
    return (min(data, key = lambda x: x["Cells"]["SeatsCount"]))
    
def geo_bar(data,longitude,latitude):
    diction = [dat["Cells"]["geoData"]["coordinates"] for dat in data]
    geo = min(diction, key = lambda x: hypot(x[0]-longitude,x[1]-latitude))
    geo_name = [dat["Cells"]["Name"] for dat in data if geo is dat["Cells"]["geoData"]["coordinates"]]
    return (geo_name)


##    подскажите,какой вариант лучше для нахождения ближайшего бара(приоритетный вариант выше,т.к.
##    во втором варианте получиласьислишком длинная строка)
##    def geo_bar(data,longitude,latitude):
    ##    geo = min(data, key = lambda x: hypot(x["Cells"]["geoData"]["coordinates"][0]-longitude,x["Cells"]["geoData"]["coordinates"][1]-latitude))
    ##    return (geo)


if __name__ == '__main__':
    destination = 'bari.zip'
    url = 'http://data.mos.ru/opendata/export/1796/json/2/1'
    urllib.request.urlretrieve(url, destination)
    z = zipfile.ZipFile('bari.zip', 'r')
    z.extractall()
    z.close()
    print('Введите,пожалуйста,ваши координаты')
    longitude = input1()
    latitude = input2()
    data = open_json()
    big_bar = biggest_bar(data)
    print('Самый большой бар:',big_bar["Cells"]["Name"])
    small_bar = smallest_bar(data)
    print ('Самый маленький бар:',small_bar["Cells"]["Name"])
    geo = geo_bar(data,longitude,latitude)
    print ('Ближайший бар относительно вашей геопозиции:', geo)
##    для второго варианта:
##    print('Ближайший бар относительно вашей геопозиции:', geo["Cells"]["Name"])
