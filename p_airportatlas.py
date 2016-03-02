import os
import csv
from p_airport import *
from math import *

class Airportatlas:
    airport_fn = "airport(2).csv"

    def __init__(self, csvFile=airport_fn):
        self.airports = self.loadData(csvFile)

    def loadData(self, csvFile):
        airportD={}

        with open(os.path.join(csvFile),"rt",encoding="utf8")as f:
            line = csv.reader(f)
            for row in line:
                try:
                    airportD[row[4]] = Airport(row[1],row[2],row[3],row[4],row[6],row[7])
                except KeyError:
                   continue

        return airportD


    def distance(self, lat1,long1,lat2,long2):
        rads = 2*pi/360
        if lat1 > 0:
            lat1 = (90 - lat1)
        else:
            lat1 = (90 + lat1)

        if lat2 > 0:
            lat2 = (90 - lat2)
        else:
            lat2 = (90 + lat2)

        lat1= lat1*rads
        lat2=lat2*rads
        long1=long1*rads
        long2=long2*rads

        r=6371
        dist = acos(sin(lat1)*sin(lat2)*cos(long1-long2)+cos(lat1)*cos(lat2))*r
        return dist

    def getAirport(self, code):
        try :
            return self.airports[code.upper()]
        except KeyError:
            return None

    def distanceBetweenAirports(self, code1, code2):

        airport1=self.getAirport(code1)
        airport2=self.getAirport(code2)
        return self.distance(airport1.latitude, airport1.longitude, airport2.latitude, airport2.longitude)

def main():
    atlas=Airportatlas()
    print(atlas.getAirport("DUB"))
    print(atlas.getAirport("lhr"))
    print(atlas.distanceBetweenAirports("DUB","LHR"))


    #code1 = input("Enter Airport code1: ")
    #code2 = input("Enter Airport code2: ")
    #print("Distance from", airportcode1, "to", code2, "is", atlas.distanceBetweenAirports("dub", "lhr"))

    #print(atlas.distanceBetweenAirports("dub","lhr"))

#main()