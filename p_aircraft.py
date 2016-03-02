import os
import csv

class LoadAircraft:
    #arranging relevant information from CSV
     def __init__(self, aircraftcode, range):
        self.aircraftcode=aircraftcode
        self.range=range
    #print string in this format once init is called
     def __str__(self):
        return "Aircraft code:{}, Flying Range:{}".format(self.aircraftcode, self.range)
     def __repr__(self):
        return "{}".format(self.range)


class Aircraft:

    filename = "aircraft.csv"

    def __init__(self, csvFile=filename):
        self.aircrafts = self.loadData(csvFile)

    def loadData(self, csvFile):
        aircraftdict={}

        with open(os.path.join(csvFile),"rt",encoding="utf8")as f:
            line = csv.reader(f)
            for row in line:
                try:
                    aircraftdict[row[0]] = LoadAircraft(row[0], row[4])
                except KeyError:
                   continue

        return aircraftdict

    def getAircaft(self, aircraftcode):
        try :
            return self.aircrafts[aircraftcode]
        except KeyError:
            return None

    def printAircrafts(self,filename):
        getAL=self.loadData(filename)
        #after loading csv file in getAL(AircraftList), sorting it by the key of the loade dictionary
        #will display Acode and range at bottom of list, so reversed was used to get it to the top.
        sortbykey=reversed(sorted(getAL.items(),key=lambda t:t[0]))

        for key in sortbykey:
            print(key)
        return ""



    def getrange(self,aircraftcode):
        p1=self.getAircaft(aircraftcode)
        return p1.range

def main():
    plane=Aircraft()
    print(plane.getAircaft("A319"))
    print(plane.getrange("A319"))
    print(plane.printAircrafts("aircraft.csv"))
#main()