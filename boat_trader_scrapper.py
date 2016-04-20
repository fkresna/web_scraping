import requests
from bs4 import BeautifulSoup
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Create csv file and initialize column title
csvFile = 'dataBoatTraderNoPrice3.csv'
f = open(csvFile, 'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Boat Year', 'Boat Model','Boat Make', 'Seller Name', 'Postal Code', 'Boat Price', 'Boat Class','Boat Category','Boat Length','Propolsion Type','Hull Material','Fuel Type') )
finally:
    f.close()

for i in range(1,5789):
    initialUrl = "http://www.boattrader.com/search-results/NewOrUsed-any/Type-any/Category-all/Zip-33647/Radius-4000/Sort-Length:DESC/Page-"+str(i)+",28?"

    initialResult = requests.get(initialUrl)
    rawHtmlInitialRequest = initialResult.text
    boat = BeautifulSoup(rawHtmlInitialRequest,'html.parser')
    info = boat.find_all('a',{'class':'contact-seller-link'}) 
    for x in range(0,len(info)):
        singleURL = 'http:' + info[x]['href']
        print singleURL
        result = requests.get(singleURL)
        resultText = result.text
        resultText.encode('ascii','ignore')
        singleBS = BeautifulSoup(resultText,'html.parser')

        #year
        year = singleBS.find_all('span',{'class':'bd-year'})
        try:
            boat_year = year[0].text
        except IndexError as e:
            boat_year = 0;
        #print boat_year

        #make
        make = singleBS.find_all('span',{'class':'bd-make'})
        try:
            boat_make = make[0].text
        except IndexError as e:
            boat_make = 0;
        #print boat_make

        #model
        model = singleBS.find_all('span',{'class':'bd-model'})
        try:
            boat_model = model[0].text
        except IndexError as e:
            boat_model = 0;
        #print boat_model

        #postal Code
        postal = singleBS.find_all('span',{'class':'postal-code'})
        try:
            postal_code = postal[0].text
        except IndexError as e:
            postal_code = 0;
        #print postal_code

        #price
        price =  singleBS.find_all('span',{'class':'bd-price'})
        try:
            boat_price = price[0].text
            boat_price = boat_price.strip()
        except IndexError as e:
            boat_price = 0;
        if boat_price == "Request a Price":
            boat_price = 0;
        #print boat_price

        #seller
        seller = singleBS.find_all('span',{'id':'seller-name'})
        try:
            seller_name = seller[0].text
        except IndexError as e:
            seller_name = 0;
        #print seller_name

        #tableDetail
        tableDetail = singleBS.find('div',{'class':'collapsible open'})
        if tableDetail != None:
            rows = tableDetail.findAll('tr')
            #Boat Class
            col = rows[0].findAll('td')
            try:
                boatClass = col[0].text
            except IndexError as e:
                boatClass = 0;
            #print "Boat Class " + boatClass

            #Boat Category
            col = rows[1].findAll('td')
            try:
                boatCategory = col[0].text
            except IndexError as e:
                boatCategory = 0
            #print "Boat Category " + boatCategory

            #Boat Length
            col = rows[4].findAll('td')
            try:
                boatLength = col[0].text
            except IndexError as e:
                boatLength = 0
            #print "Boat Length " + boatLength

            #Boat Propulsion Type
            col = rows[5].findAll('td')
            try:
                propolsionType = col[0].text
            except IndexError as e:
                propolsionType = 0
            #print "Propolsion " + propolsionType

            #Hull Material
            col = rows[6].findAll('td')
            try:
                hullMaterial = col[0].text
            except IndexError as e:
                hullMaterial = 0
           #print "Hull Material " + hullMaterial

            #Fuel Type
            col = rows[7].findAll('td')
            try:
                fuelType = col[0].text
            except IndexError as e:
                fuelType = 0
            #print "Fuel Type " + fuelType
        else:
            boatClass = 0
            boatCategory = 0;
            boatLength = 0;
            propolsionType = 0
            hullMaterial = 0
            fuelType = 0

        #if boat_year != 0 or boat_model != 0 or boat_make != 0 and seller_name != 0 and postal_code != 0:
        f = open(csvFile, 'a')
        try:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow((boat_year,boat_model,boat_make,seller_name,postal_code,boat_price,boatClass,boatCategory,boatLength,propolsionType,hullMaterial,fuelType))
        finally:
            f.close()
    print "Search Result: "+str(i)
print "Looping done"
