import requests
from bs4 import BeautifulSoup
import csv

#Create csv file and initialize column title
f = open('dataBoatTrader.csv', 'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Boat Year', 'Boat Model','Boat Make', 'Seller Name', 'Postal Code', 'Boat Price') )
finally:
    f.close()

initialUrl = "http://www.boattrader.com/search-results/NewOrUsed-any/Type-any/Category-all/Zip-33684/Radius-4000/Sort-Length:DESC/Page-1,10?"
initialUrl = "http://www.boattrader.com/search-results/NewOrUsed-any/Type-any/Category-all/Zip-33647/Radius-4000/Sort-Length:DESC/Page-2,28?"

initialResult = requests.get(initialUrl)
rawHtmlInitialRequest = initialResult.text
boat = BeautifulSoup(rawHtmlInitialRequest,'html.parser')
info = boat.find_all('a',{'class':'contact-seller-link'}) 
print info[0]['href']
singleURL = 'http:' + info[0]['href']
result = requests.get(singleURL)
resultText = result.text
singleBS = BeautifulSoup(resultText,'html.parser')

#year
year = singleBS.find_all('span',{'class':'bd-year'})
boat_year = year[0].text
print boat_year

#make
make = singleBS.find_all('span',{'class':'bd-make'})
boat_make = make[0].text
print boat_make

#model
model = singleBS.find_all('span',{'class':'bd-model'})
boat_model = model[0].text
print boat_model

#postal Code
postal = singleBS.find_all('span',{'class':'postal-code'})
postal_code = postal[0].text
print postal_code

#price
price =  singleBS.find_all('span',{'class':'bd-price'})
boat_price = price[0].text
boat_price = boat_price.strip()
if boat_price == "Request a Price":
    boat_price = 0;
print boat_price

#seller
seller = singleBS.find_all('span',{'id':'seller-name'})
seller_name = seller[0].text
print seller_name



#for x in range(0,len(info)):
#	print x
#	print info[x]['href'];

