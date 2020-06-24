from firebase import Firebase
import os

config = {"add your own firebase config here"}

firebase = Firebase(config)
auth = firebase.auth()
db = firebase.database()

def get_nearest_aed(lat,lng):
    aeds = db.get().val()
    minDist = 999999999999
    minLat = 0
    minLng = 0
    for i,j in aeds.items():
        if ((lat - float(j["lat"])) ** 2) + ((lng - float(j["lng"])) ** 2) < minDist:
            minDist = ((lat - float(j["lat"])) ** 2) + ((lng - float(j["lng"])) ** 2)
            minLat = float(j["lat"])
            minLng = float(j["lng"])
    return (minLat,minLng)