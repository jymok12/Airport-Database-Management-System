class Dbquery():
    @staticmethod
    def updateRoutesQuery():
        return "Update routes r, country c, country d, airport a, airport b set r.touristdemand =  (" \
               "c.tourismExpend+d.tourismExpend)*1000/(c.population+d.population)*((" \
               "c.GDPpercapita*a.NearbyPopulation)/2000000000)+(b.NearbyPopulation*d.GDPpercapita)/2000000000 Where " \
               "r.codeDeparture = a.airportCode AND r.codeArrival = b.airportCode AND c.CountryKey = a.CountryID AND " \
               "d.CountryKey = b.CountryID;"
    @staticmethod
    def updateRoutesDomesticModifierTourism():
        return "Update routes r, country c, country d, airport a, airport b set r.touristdemand =  r.touristdemand* 9 Where r.codeDeparture = a.airportCode AND r.codeArrival = b.airportCode AND c.CountryKey = a.CountryID AND d.CountryKey =  b.CountryID AND c.countrykey = d.countrykey"
    @staticmethod
    def updateRoutesDomesticBusiness():
        return "Update routes r, country c, country d, airport a, airport b set r.buisnessdemand =  r.buisnessdemand* 5 Where r.codeDeparture = a.airportCode AND r.codeArrival = b.airportCode AND c.CountryKey = a.CountryID AND d.CountryKey =  b.CountryID AND c.countrykey = d.countrykey"
    @staticmethod
    def populateRoutesInnitial():
        return "insert ignore into routes SELECT DISTINCT a.AirportCode, b.AirportCode," \
                "(c.tourismExpend+d.tourismExpend)*1000/(c.population+d.population)*((" \
                "c.GDPpercapita*a.NearbyPopulation)/2000000000)+(b.NearbyPopulation*d.GDPpercapita)/2000000000, " \
                "(((c.GDPpercapita*d.GDPpercapita)/50000)^2)/1000*(a.NearbyPopulation+b.nearbyPopulation)/150000*(" \
                "c.GDPIndustrailRatio*d.GDPIndustrailRatio), null FROM testairports a, testairports b, country c, " \
                "country d wHERE a.AirportCode <> b.AirportCode AND c.CountryKey = a.CountryID AND d.CountryKey = " \
                "b.CountryID limit 200000; "

    @staticmethod
    def updateRoutesBuisnessQuery():
        return "Update routes r, country c, country d, airport a, airport b set r.buisnessdemand =  (((" \
               "c.GDPpercapita*d.GDPpercapita)/50000)^2)/1000*(a.NearbyPopulation+b.nearbyPopulation)/150000*(" \
               "c.GDPIndustrailRatio*d.GDPIndustrailRatio) Where r.codeDeparture = a.airportCode AND r.codeArrival = " \
               "b.airportCode AND c.CountryKey = a.CountryID AND d.CountryKey =  b.CountryID; "

    @staticmethod
    def updateTestAirports():
        return "insert ignore into testairports Select *from airport where NearbyPopulation> 1000000;"
    @staticmethod
    def createTestAirportsTable():
        qry = "CREATE TABLE IF NOT EXISTS testAirports(AirportCode CHAR(4), AirportName VARCHAR(64),CountryID CHAR(" \
        "2), NSCoordinates float,EWCoordinates float,NearbyPopulation INT, MaximumRunWayLength INT," \
        "PRIMARY KEY (AirportCode),FOREIGN KEY (CountryID) REFERENCES Country(CountryKey));"
        return qry
    @staticmethod
    def deleteTestAirportsTable():
        return "Drop table if exists testAirports;"
    @staticmethod
    def createTriggerQuery():
        return """Create trigger flightUpdater
after update
on routes
for each row
Update flight f, routes r, airplane a
set f.loadfactor = a.paxcap2/(r.touristdemand+r.buisnessdemand)*100
where f.airplaneModelType = a.modelname0 AND r.codearrival = f.codearrival AND f.codedeparture = r.codedeparture"""
