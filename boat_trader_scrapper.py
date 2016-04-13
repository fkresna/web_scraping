import requests
from bs4 import BeautifulSoup
import csv

#Create csv file and initialize column title
csvFile = 'dataBoatTrader.csv'
f = open(csvFile, 'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Boat Year', 'Boat Model','Boat Make', 'Seller Name', 'Postal Code', 'Boat Price') )
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
        result = requests.get(singleURL)
        resultText = result.text
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

        if boat_year != 0 and boat_model != 0 and boat_make != 0 and seller_name != 0 and postal_code != 0 and boat_price != 0:
            f = open(csvFile, 'a')
            try:
                writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow((boat_year,boat_model,boat_make,seller_name,postal_code,boat_price))
            finally:
                f.close()
            print "x written:"+str(x)
    print "Search Result: "+str(i)
print "Looping 10 done"
