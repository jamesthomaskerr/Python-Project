class Airport:
    AirportID=0
    AirportName=""                              #Name of airport. May or may not contain the City name.
    CityName=""                                 #Main city served by airport. May be spelled differently from Name.
    Country=""                                  #Country or territory where airport is located.
    airportcode= ""                                     #3-letter IATA code
    ICAOcode=""       #<-12 positions            ICAO 4-letter ICAO code.
    latitude=0        #reading from csv          Latitude Decimal degrees, usually to six significant digits.
    longitude=0                                 #Longitude Decimal degrees, usually to six significant digits.
    TimeOffset=0                                #Timezone Hours offset from UTC.
    Fractional=""                               #hours are expressed as decimals, e.g. India is 5.5.
    DST=""                                      #Daylight savings time. One of
    Tz=""

    #arranging relevant information from CSV
    def __init__(self, AirportName, CityName, Country, airportcode, latitude, longitude):#
        self.AirportName=AirportName
        self.CityName=CityName
        self.Country=Country
        self.airportcode=airportcode
        self.latitude=float(latitude)
        self.longitude=float(longitude)

    def __str__(self):
        return "{} (Name:{},{},{} lat:{} long:{})".format(self.airportcode, self.AirportName, self.CityName, self.Country,self.latitude, self.longitude)

    def __repr__(self):
        return "{}".format(self.airportcode)