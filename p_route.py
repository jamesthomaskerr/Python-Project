from itertools import permutations
from p_aircraft import *
from p_rates import *


class Intinerary:
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

    def getAirport(self, airportcode):
        try :
            return self.airports[airportcode.upper()]
        except KeyError:
            return None


    def minDistance(self,home,code1,code2,code3,code4):
        global value
        airport=[self.getAirport(code1),
                     self.getAirport(code2),
                     self.getAirport(code3),
                     self.getAirport(code4),
                     ]
        homeport=self.getAirport(home)
        permlist=[]
        dict_r={}
        for j in permutations(airport,4):
            total = 0
            permlist.append(list(j)) #adding each permutation line by line
            for x in range(3):
                d=(self.distance(j[x].latitude, j[x].longitude, j[x+1].latitude, j[x+1].longitude))
                #when calculating airport1 and airport2, add distance from home-airpor1
                if x == 0:
                   # homeport=self.getAirport(home)
                    dhome=self.distance(homeport.latitude, homeport.longitude, j[0].latitude, j[0].longitude)
                    total+=dhome
                #when calculating airport3 and airport4, add distance from airpor4-home
                elif (x+1) == 3:
                   # homeport=self.getAirport(home)
                    dhome=self.distance(j[3].latitude, j[3].longitude, homeport.latitude, homeport.longitude)
                    total+=dhome
                total+=d
            #creating a dictionary with the key being the route and the total distance=value of key
            dict_r[j]=total
        for key in (dict_r):
            value = dict_r[key]
        #return the smallest value
        mindist=min(dict_r, key=dict_r.get)
        return value




    def shortestRoute(self,home,code1,code2,code3,code4):
        airport=[self.getAirport(code1),
                     self.getAirport(code2),
                     self.getAirport(code3),
                     self.getAirport(code4),
                     ]
        homeport=self.getAirport(home)
        permlist=[]
        dict_r={}
        for j in permutations(airport,4):
            total = 0
            permlist.append(list(j)) #adding each permutation line by line
            for x in range(3):
                d=(self.distance(j[x].latitude, j[x].longitude, j[x+1].latitude, j[x+1].longitude))
                #when calculating airport1 and airport2, add distance from home-airport1
                if x == 0:
                   # homeport=self.getAirport(home)
                    dhome=self.distance(homeport.latitude, homeport.longitude, j[0].latitude, j[0].longitude)
                    total+=dhome
                #when calculating airport3 and airport4, add distance from airpor4-home
                elif (x+1) == 3:
                   # homeport=self.getAirport(home)
                    dhome=self.distance(j[3].latitude, j[3].longitude, homeport.latitude, homeport.longitude)
                    total+=dhome
                total+=d
            #creating a dictionary with the key being the route and the total distance=value of key
            dict_r[j]=total
        #return the key with the smallest value
        quickroute=min(dict_r, key=dict_r.get)
        return quickroute

    #gethome() will add the home oject to the permutation with the shortest distance
    def gethome(self,home,code1,code2,code3,code4):
        costlist=[]
        base=self.getAirport(home)
        hiho=self.shortestRoute(home,code1,code2,code3,code4)
        costlist.append(base)
        for i in hiho:
            costlist.append(i)
        costlist.append(base)
        return costlist



# routeCheck() will see if the Aircrafts range, can make each leg of the journey
    def routeCheck(self,home,code1, code2,code3,code4):
        global acode
        check=1
        while check>=1:
            rout=self.gethome(home,code1,code2,code3,code4)
            ac=Aircraft()
            try:
                acode=input("What Aircraft type will you be flying today? Enter code (i.e A320) : ")
            except KeyError:
                continue
            ranges=float(ac.getrange(acode.upper()))
            check=1
            for i in range(0,5):
                d=(self.distance(rout[i].latitude, rout[i].longitude, rout[i+1].latitude, rout[i+1].longitude))
                if d>ranges:
                    print("Range Error:",rout[i].airportcode,"to",rout[i+1].airportcode)
                    check+=1
            if check==1:
                check=0
                print("==============================================================")
                print("Aircraft capable of completing journey")
        return acode.upper()


    def getcost(self,home,code1, code2,code3,code4,acode):
        rout=self.gethome(home,code1,code2,code3,code4)
        ac=Aircraft()
        rangeleft=float(ac.getrange(acode.upper()))
        rangetotal=float(ac.getrange(acode.upper()))
        rate=Rates()
        totalcost=0
        fuelcost=0
        d=0
        for i in range(0,5):
            # rangeleft-=d
            d=(self.distance(rout[i].latitude, rout[i].longitude, rout[i+1].latitude, rout[i+1].longitude))
            if rangeleft<d:
                fillup=rangetotal-rangeleft
                rangeleft+=fillup
                fuelcost=rate.fromeuro(fillup,rout[i].airportcode)
                print("Refuel in: ", "Country:", rout[i].Country," Airport Code:", rout[i].airportcode)
            rangeleft-=d

        #if the plane makes journey without refulling, get cost of used fuel

        if fuelcost==0:
            used=rangetotal-rangeleft
            fuelcost+=rate.fromeuro(used,home)
        #if the plane refills, add the cost of a full tank to totalcost.
        #as when the plane started it filled up at home.(i.e get the cost of fulltank+cost of topup - fuel left over)
        else:
            homefill=rate.fromeuro(rangetotal,home)
            fuelcost=(fuelcost+homefill)-rangeleft
        totalcost=fuelcost

        return(totalcost)


def main():
    atlas=Intinerary()
    print(atlas.getcost("DUB","lhr","jfk","aal","ool","a330"))
    print(atlas.gethome("dub","lhr","jfk","aal","ool"))

#main()