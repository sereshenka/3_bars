import urllib.request
import zipfile
import json
from math import hypot
import os
import tempfile

def input1():
    try:
        longitude = float(input('Долгота:'))
    except ValueError:
        longitude = None
    return longitude
        

def input2():
    try:
        latitude = float(input('Широта:'))
        return (latitude)
    except ValueError:
        latitude = None
    return latitude


def get_zip(tmpdirectory):
    destination = os.path.join(tmpdirectory,'bari.zip')
    url = 'http://data.mos.ru/opendata/export/1796/json/2/1'
    urllib.request.urlretrieve(url, destination)
    if not os.path.exists(destination):
        return None
    return destination


def extract_zip(destination):
    z = zipfile.ZipFile(destination, 'r')
    z.extractall()
    z.close()

        
def open_json():
    try:
        with open('Бары.json',encoding='utf-8') as json_data:
            return (json.load(json_data))
    except OSError :
        dest = None
        return dest
          
    
def biggest_bar(data):
    return max(data, key = lambda x: x["Cells"]["SeatsCount"])

    
def smallest_bar(data):
    return min(data, key = lambda x: x["Cells"]["SeatsCount"])


def geo_bar(data,longitude,latitude):
    bar_key = lambda x: hypot(x["Cells"]["geoData"]["coordinates"][0]-longitude,x["Cells"]["geoData"]["coordinates"][1]-latitude)
    geo = min(data, key = bar_key )
    return geo

    
def print_all(big_bar,small_bar,geo):
    print('Самый большой бар:',big_bar["Cells"]["Name"])
    print ('Самый маленький бар:',small_bar["Cells"]["Name"])
    print('Ближайший бар относительно вашей геопозиции:', geo["Cells"]["Name"])
    

    
if __name__ == '__main__':
    while True:
        with tempfile.TemporaryDirectory() as tmpdirectory:
            print(tmpdirectory)
            destination = get_zip(tmpdirectory)
            if destination is None:
                print('Zip архив не скачался')
                break
            zip_archive = extract_zip(destination)
            data = open_json()
            if data is None:
                print('Список баров отсутствует')
                break
        print('Введите,пожалуйста,ваши координаты')
        longitude = input1()
        latitude = input2()
        if longitude is None or latitude is None:
            print('Неверный формат')
            break
        big_bar = biggest_bar(data)
        small_bar = smallest_bar(data)
        geo = geo_bar(data,longitude,latitude)
        print_all(big_bar,small_bar,geo)
        break
