import requests
from bs4 import BeautifulSoup

initialUrl = "http://www.boattrader.com/search-results/NewOrUsed-any/Type-any/Category-all/Zip-33684/Radius-4000/Sort-Length:DESC/Page-1,10?"

initialResult = requests.get(initialUrl)
rawHtmlInitialRequest = initialResult.text
boat = BeautifulSoup(rawHtmlInitialRequest,'html.parser')
info = boat.find_all('a',{'class':'contact-seller-link'}) 

for x in range(0,9):
	print x
	print info[x]['href'];
