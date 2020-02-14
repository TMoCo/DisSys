import requests
from PIL import Image
from io import BytesIO

def getMap(location1, location2):
    response = requests.get(
    'https://maps.googleapis.com/maps/api/staticmap?size=512x512&maptpe=roadmap&markers='
    +location1+'|'+location2+'&key=AIzaSyCDgKp6g0qfdNqSNJUPD-ffg9ldueoyFLo')
    # google maps api returns an image in jpeg, png or gif; an array of bytes
    path = './webservice/web/static/map.png'
    map = Image.open(BytesIO(response.content))
    map.save(path)
    return 'saved'
