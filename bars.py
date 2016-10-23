import urllib.request
import zipfile
import json
from math import hypot
import os

def input1():
    try:
        longitude = float(input('Долгота:'))
        return (longitude)
    except ValueError:
        longitude = None
    if longitude is None:
        print('Неверный формат')

def input2():
    try:
        latitude = float(input('Широта:'))
        return (latitude)
    except ValueError:
        latitude = None
    if latitude is None:
        print('Неверный формат')

def get_zip():
    destination = 'bari.zip'
    url = 'http://data.mos.ru/opendata/export/1796/json/2/1'
    urllib.request.urlretrieve(url, destination)
    return (destination)

def extract_zip(destination):
    if not os.path.exists(destination):
        print('Zip архив не скачался')
    else:
        z = zipfile.ZipFile(destination, 'r')
        z.extractall()
        z.close()
        
def open_json():
    try:
        with open('Бары.json',encoding='utf-8') as json_data:
            return (json.load(json_data))
    except OSError :
        dest = None
    if dest is None:
        print('Список баров отсутствует')
        
    
def biggest_bar(data):
    return(max(data, key = lambda x: x["Cells"]["SeatsCount"]))
    
def smallest_bar(data):
    return (min(data, key = lambda x: x["Cells"]["SeatsCount"]))
    

def geo_bar(data,longitude,latitude):
    bar_key = lambda x: hypot(x["Cells"]["geoData"]["coordinates"][0]-longitude,x["Cells"]["geoData"]["coordinates"][1]-latitude)
    geo = min(data, key = bar_key )
    return (geo)
    
def print_all(big_bar,small_bar,geo):
    try:
        print('Самый большой бар:',big_bar["Cells"]["Name"])
        print ('Самый маленький бар:',small_bar["Cells"]["Name"])
        print('Ближайший бар относительно вашей геопозиции:', geo["Cells"]["Name"])
    except TypeError :
        pass
    
if __name__ == '__main__':
    print('Введите,пожалуйста,ваши координаты')
    longitude = input1()
    latitude = input2()
    if longitude and latitude is not None:
        destination = get_zip()
        extract_zip(destination)
        data = open_json()
        if data is not None:
            big_bar = biggest_bar(data)
            small_bar = smallest_bar(data)
            geo = geo_bar(data,longitude,latitude)
            print_all(big_bar,small_bar,geo)

