from p_currency import *
from p_airportatlas import *
#from p_ratestemp import *
#coding: utf-8
import unicodedata


class LoadRates:

    #arranging relevant information from CSV
    def __init__(self, currcencycode, to_euro, from_euro):#
        self.currencycode=currcencycode
        self.to_euro = to_euro
        self.from_euro=from_euro

    #print string in this format once init is called
    def __str__(self):
        return "Currency:{} To-euro:{} From-Euro:{}".format(self.currencycode, self.to_euro, self.from_euro)


class Rates:
    filename = "currencyrates(1).csv"

    #automatically load csv file using "filename"
    def __init__(self, csvFile=filename):
        self.rate = self.loadData(csvFile)

    def loadData(self, csvFile):
        rates={}

        with open(os.path.join(csvFile),"rt",encoding="utf8")as f:
            line = csv.reader(f)
            for row in line:
                try:
                    rates[row[1]] = LoadRates(row[0], row[2], row[3])
                except KeyError:
                   continue

        return rates


    def getrate(self, currencycode):

        try :
            return self.rate[currencycode]
        except KeyError:
            return None

    def maprate(self, airportcode):
        a=Airportatlas()
        b=Currency()
        map2=a.getAirport(airportcode)
        map3=b.getcurrency(map2.Country)
        return self.getrate(map3.currencycode)

    def fromeuro(self, cost, airportcode):
        a=Airportatlas()
        b=Currency()
        map2=a.getAirport(airportcode)
        map3=b.getcurrency(map2.Country)
        map4=self.getrate(map3.currencycode)
        if map3.currencycode=="EUR":
            rate=cost
        else:
            rate=cost*float(map4.from_euro)
        return (rate)



def main():
    exchange=Rates()
    #at=Airportatlas()
    #print(at.getAirport("DUB"))
    #print(exchange.getrate("British Pound"))
    print(exchange.maprate("aal"))
    print(exchange.fromeuro(11069, "aal"))


   # print(currencys.getcurrency("United Kingdom"))
#main()