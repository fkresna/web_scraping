import csv
cleanCSVFile = 'cleanData.csv'
f = open(cleanCSVFile,'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Boat Year', 'Boat Model','Boat Make', 'Seller Name', 'Postal Code', 'Boat Price', 'Boat Class','Boat Category','Boat Length','Propolsion Type','Hull Material','Fuel Type') )
finally:
    f.close()

with open('dataTemp.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0
    count2 = 0
    for row in reader:
        if row['Boat Year'] == '0':
            count = count + 1
        if row['Boat Model'] == '0':
            count = count + 1
        if row['Boat Make'] == '0':
            count = count + 1
        if row['Seller Name'] == '0':
            count = count + 1
        if row['Postal Code'] == '0':
            count = count + 1
        if row['Boat Price'] == '0':
            count = count + 1
        if row['Boat Class'] == '0':
            count = count + 1
        if row['Boat Category'] == '0':
            count = count + 1
        if row['Boat Length'] == '0':
            count = count + 1
        if row['Propolsion Type'] == '0':
            count = count + 1
        if row['Hull Material'] == '0':
            count = count + 1
        if row['Fuel Type'] == '0':
            count = count + 1

        if count == 0:
            f = open(cleanCSVFile, 'a')
            try:
                writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow((row['Boat Year'],row['Boat Model'],row['Boat Make'],row['Seller Name'],row['Postal Code'],row['Boat Price'],row['Boat Class'],row['Boat Category'],row['Boat Length'],row['Propolsion Type'],row['Hull Material'],row['Fuel Type']))
                count2 = count2 + 1
            finally:
                f.close()
        count = 0
    print count2
