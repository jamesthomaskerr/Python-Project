from p_airportatlas import *


class LoadCurrencys:

    #arranging relevant information from CSV
    def __init__(self, country, currencycode):#
        self.country=country
        self.currencycode=currencycode

    #print string in this format once init is called
    def __str__(self):
        return "Country:{}, Currency:{}".format(self.country,self.currencycode)



class Currency:
    filename = "countrycurrency(1).csv"

    #automatically load csv file using "filename"
    def __init__(self, csvFile=filename):
        self.currency = self.loadData(csvFile)

    def loadData(self, csvFile):
        countrycurD={}

        with open(os.path.join(csvFile),"rt",encoding="utf8")as f:
            line = csv.reader(f)
            for row in line:
                try:
                    countrycurD[row[0]] = LoadCurrencys(row[0], row[14])
                except KeyError:
                   continue

        return countrycurD


    def getcurrency(self, country):

        try :
            return self.currency[country]
        except KeyError:
            return None


    def mapcode(self, airportcode):
        a=Airportatlas()
        map2=a.getAirport(airportcode)
        return self.getcurrency(map2.Country)




def main():
    currencys=Currency()
    print(currencys.mapcode("DUB"))
    print(currencys.getcurrency("United Kingdom"))
#main()