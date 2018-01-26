# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:07:13 2018

@author: inedumaj
"""

import urllib.request, urllib.parse 
import json
import requests

api_suche = "http://api.chefkoch.de/api/1.0/api-recipe-search.php?"
api_rezept = "http://api.chefkoch.de/api/1.0/api-recipe.php?"
rezept_url = "http://www.chefkoch.de/rezepte/"

def get_list(search_text, limit=2):
    params = {}
    params["Suchbegriff"] = search_text.strip()
    params["limit"] = limit # you can pass the limit amount of results you like to receive

    response = requests.get(api_suche, params=params)
    
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
    
def get_details(id):
    params = {}
    params["ID"] = id
    
    response = requests.get(api_rezept, params=params)
    
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
    
Startinput=['Fisch','Fleisch','Burger','Pizza']

data=[]

for input in Startinput:
    list = get_list(input,2)
    for dic in list['result']:
        data.append(get_details(dic['RezeptShowID']))