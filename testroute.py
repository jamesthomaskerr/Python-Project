import csv
import os
from p_aircraft import *

class Intinerary:

    csvFile="testroutes.csv"

    def __init__(self, route, planeType):
        self.route=route
        self.aircrafttype=Aircraft(planeType)

    def __str__(self):
        return "{} = {}".format(self.aircrafttype, self.route)


class Loadintinerary:
    dictroute={}
    def __init__(self,csvFile):
        self.loadData(csvFile)


    def loadData(self, csvFile):


        with open(os.path.join(csvFile),"rt",encoding="utf8")as f:
            line = csv.reader(f)
            for row in line:
                try:
                    self.dictroute[row[5]] = Intinerary([row[0], row[1], row[2], row[3], row[4]], row[5])
                except KeyError:
                    continue

    def printlist(self):

        listdict=list(self.dictroute.values())
        print(listdict)
        for row in listdict:
            # for i in reversed(self.dictroute.values()):
            #     print(i)
            print(row)

    def printRevlist(self):
        listRev=list(self.route)
        for i in self.route:
            # for i in reversed(self.dictroute.values()):
            #     print(i)
            print(i)

    # def depart(self, aircrafttype):
    #     try :
    #         return self.loaddata[self.route.upper()]
    #     except KeyError:
    #         return None

def main():
    home = Loadintinerary("testroutes.csv")
    home.printlist()
    #home.printRevlist()
main()