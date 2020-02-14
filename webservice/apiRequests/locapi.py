import requests
import json

def getCountryList():
    response = requests.get('http://127.0.0.1:5002/getCountries')
    return response.json()['locations']

def getMyLanguageCode(country):
    response = requests.get('http://127.0.0.1:5002/getCode?country='+country)
    return response.json()['code']

def getMyCapital(country):
    response = requests.get('http://127.0.0.1:5002/getCapital?country='+country)
    return response.json()['capital']

def getMyDistance(capital1,capital2):
    response = requests.get('http://127.0.0.1:5002/getDistance?start='+capital1+'&end='+capital2)
    return response.json()['distance']
