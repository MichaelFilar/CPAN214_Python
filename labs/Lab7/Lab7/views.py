import datetime
from django.http import HttpResponse
from django.shortcuts import render
import json
import random
import requests

def greeting(request):
    return(HttpResponse("<h1>Michael Filar. n:01499766</h1>"))

def now(request):
    currentdate = datetime.datetime.now()
    return(HttpResponse(f'<h1>{currentdate}</h1>'))

def qr(request):
    return
    
def get_xkcd(request):
    if request.method == "POST":
        print(request.POST)
        comic_id = request.POST.get("comic_id")

        if comic_id:
            comic_url = f'https://xkcd.com/{comic_id}/info.0.json'
        else:
            random_integer = random.randint(1, 1000)
            comic_url = f'https://xkcd.com/{random_integer}/info.0.json'

        print(comic_url)

        response = requests.get(comic_url)

        if response.status_code == 200:
            data = response.json()
            comic_img_url = data["img"]
        else:
            comic_img_url = ""

        print(comic_img_url)
        


        return (render(request, "get_xkcd.html",
        {"comic_img_url": comic_img_url}))
    else:
        random_integer = random.randint(1, 1000)
        comic_url = f'https://xkcd.com/{random_integer}/info.0.json'

        print(comic_url)

        response = requests.get(comic_url)

        if response.status_code == 200:
            data = response.json()
            comic_img_url = data["img"]
        else:
            comic_img_url = ""

        print(comic_img_url)
    return (render(request, "get_xkcd.html",
        {"comic_img_url": comic_img_url}))

def get_dog(request):
    if request.method == "POST":
        print(request.POST)
        dog_breed = request.POST.get("dog_breed")

        if dog_breed:
            dog_url = f'https://dog.ceo/api/breed/hound/{dog_breed}/images'
        else:
            dog_url = f'https://dog.ceo/api/breeds/image/random'

        print(dog_url)

        response = requests.get(dog_url)

        if response.status_code == 200:
            data = response.json()
            dog_img_url = data["message"]
            if hasattr(dog_img_url, "__len__"):
                dog_img_array = data["message"] 
        else:
            dog_img_url = ""

        print(dog_img_url)
        print(dog_img_array)
        


        return (render(request, "get_dog.html",
        {"dog_img_array": dog_img_array}))
    
    else:
        dog_url = f'https://dog.ceo/api/breeds/image/random'
        print(dog_url)

        response = requests.get(dog_url)

        if response.status_code == 200:
            data = response.json()
            dog_img_url = data["message"]
        else:
            dog_img_url = ""

        print(dog_img_url)
    return (render(request, "get_dog.html",
        {"dog_img_url": dog_img_url}))

def get_qr(request):
    qr_url = f'https://image-charts.com/chart?chs=200x200&cht=qr&chl=Hello%20World&choe=UTF-8'
    if request.method == "POST":
        print(request.POST)
        qr_value = request.POST.get("qr_value")
        width = request.POST.get("width")
        height = request.POST.get("height")

        if not width:
            width = 200
        
        if not height:
            height = 200

        if not qr_value:
            qr_value = "Hello World"
        qr_url = f'https://image-charts.com/chart?chs={height}x{width}&cht=qr&chl={qr_value}&choe=UTF-8'

    print(qr_url)
        


    return (render(request, "get_qr.html",
        {"qr_url": qr_url}))