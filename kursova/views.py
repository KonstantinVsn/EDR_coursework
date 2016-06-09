#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render
import requests
import re
from django.http import HttpResponseRedirect

from kursova_django.myforms import SearchForm


global n

def start(request):
    global n
    n = ""
    sec = 100
    page = request.get_full_path()
    return render(request, "base.html", {"sec": sec, "page":page})

def Search(request):
    mass = []
    valuesearch = ""
    tmp = ""
    page = request.get_full_path()
    if request.method == 'POST':
        valuesearch = request.POST['search']
        if (request.POST['sort'] == "person"):
            tmp = "{'mainPerson':{'contains':'" + request.POST['search'] + "'}}"
        elif (request.POST['sort'] == "address"):
            tmp = "{'address':{'contains':'" + request.POST['search'] + "'}}"
        elif (request.POST['sort'] == "occupation"):
            tmp = "{'occupation':{'contains':'" + request.POST['search'] + "'}}"
        info = AboutComp(tmp)
        for i in info:
            if (ValidAdress(i["address"]) != False):
                mass.append(ValidAdress(i["address"]))
    return render(request, "mapall.html", {"page": page, "valuesearch": valuesearch, "addresses": mass})


def map(request):
    valuesearch = "Enter query"
    page = request.get_full_path()
    return render(request, "mapall.html", {"page": page, "valuesearch": valuesearch})

def addtomap(request):
    global n
    mass = []
    print ("INFO", n)
    for i in AboutComp(n):
        if (ValidAdress(i["address"]) != False):
            mass.append(ValidAdress(i["address"]))
    print (mass)
    page = request.get_full_path()
    return render(request, "map.html", {"page": page, "addresses": mass})

def graph(request):
    global n
    page = request.get_full_path()
    print (n)
    if (n != ""):
        v = ValidName(n)
        info = AboutComp(n)
        mainPerson = v[0]
        comp = v[1:]
        return render(request, "graph.html", {"page": page, "companies": comp, "mainPerson": mainPerson, "info": info})
    else:
        return render(request, "graph.html", {"page": page})

def bubble(request):
    page = request.get_full_path()
    return render(request, "index.html", {"page": page})

def about(request):
    page = request.get_full_path()
    return render(request, "about.html", {"page": page})

def contact(request):
    page = request.get_full_path()
    return render(request, "contact.html", {"page": page})

def ValidName(name):
    _name = name
    print(name)
    adress = name.replace("'", '"')
    print("replaced", adress)
    url = 'http://edr.data-gov-ua.org/api/companies?where='+adress
    print("url", url)
    url = url.replace("%20", " ")
    return getcompany(url, _name)

def getcompany(name,_name):
    r = requests.get(name)
    print("r", r.json())
    r = r.json()
    companies = []
    adresses = []
    print("name", _name.split("'")[5])
    companies.append(_name.split("'")[5])
    for line in r:
        #print(line)
        print(line["name"])
        comp = line["name"]
        comp = comp.replace('"', "")
        comp = comp.replace("\'", "")
        companies.append(comp)
        adresses.append(line["address"])
    print(companies)
    return companies
   # print(adresses)

def getadress(address):
    mass = {}
    r = requests.get(address)
    try:
        r = r.json()
        mass.update({"l": r["results"][0]["geometry"]["location"]["lat"], "w": r["results"][0]["geometry"]["location"]["lng"]})
        print ("GFGGGGGG", mass)
        return mass
    except:
        return False

def ValidAdress(adress):
    print(adress)
    adress = adress.replace(", ", "+")
    print(adress)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+adress
    print("url", url)
    url = url.replace(" ", "%20")
    print(url)
    return getadress(url)
    #getinfo(url)

def search(request):
    global n
    if request.method == 'POST':
        print ("1 if")
        n = request.POST['search']
        n = "{'mainPerson':{'contains':'" + n + "'}}"
        return HttpResponseRedirect(reverse('graph'))
    else:
        return HttpResponseRedirect('Gavno')

def AboutComp(name):
    name1 = name.replace("'", '"')
    url = 'http://edr.data-gov-ua.org/api/companies?where='+name1
    r = requests.get(url)
    r = r.json()
    return r