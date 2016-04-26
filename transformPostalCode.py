import csv
from re import sub
from decimal import Decimal

cleanCSVFile = 'cleanData3.csv'
f = open(cleanCSVFile,'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Boat Year', 'Boat Model','Boat Make', 'Seller Name', 'Postal Code', 'Boat Price', 'Boat Class','Boat Category','Boat Length','Propolsion Type','Hull Material','Fuel Type','City','State') )
finally:
    f.close()

with open('cleanData2.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0
    count2 = 0
    for row in reader:
    	f = open(cleanCSVFile, 'a')
    	try:
		writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
	writer.writerow((row['Boat Year'],row['Boat Model'],row['Boat Make'],row['Seller Name'],row['Postal Code'],row['Boat Price'],row['Boat Class'],row['Boat Category'],row['Boat Length'],row['Propolsion Type'],row['Hull Material'],row['Fuel Type']))
	count2 = count2 + 1
            finally:
                f.close()
        count = 0
    print count2
