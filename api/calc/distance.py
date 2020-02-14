from numpy import pi, cos, sin, arctan2, sqrt

def distance(lat1, lat2, lon1, lon2):

    dLat = lat2 - lat1
    dLon = lon2 - lon1
    a = sin(toRadians(dLat/2))*sin(toRadians(dLat/2)) + cos(toRadians(lat1)) \
    * cos(toRadians(lat2)) * sin(toRadians(dLon/2))*sin(toRadians(dLon/2))
    c = 2 * arctan2(sqrt(a),sqrt(1-a))

    return str(round(c * 6371))

def toRadians(val):
    return val*pi/180
