import requests

def getTranslation(langcode, text):
    response = requests.get('https://api.mymemory.translated.net/get?q=' + \
    text + '&langpair=en|' + langcode)

    return response.json()['matches'][1]["translation"]
