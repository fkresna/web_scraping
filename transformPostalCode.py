import csv
import zipcode
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
    count2 = 0
    for row in reader:
    	f = open(cleanCSVFile, 'a')
        if row['Postal Code'] != '0':
            try:
                if len(row['Postal Code']) > 5:
                    temp = row['Postal Code']
                    temp = temp[:5]
                    myzip = zipcode.isequal(temp)
                else:
                    myzip = zipcode.isequal(row['Postal Code'])
                if myzip != None:
                    try:
                        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
                        writer.writerow((row['Boat Year'],row['Boat Model'],row['Boat Make'],row['Seller Name'],row['Postal Code'],row['Boat Price'],row['Boat Class'],row['Boat Category'],row['Boat Length'],row['Propolsion Type'],row['Hull Material'],row['Fuel Type'],myzip.city,myzip.state))
                        count2 = count2 + 1
                    finally:
                        f.close()
            except:
                print row['Postal Code']
    print count2
