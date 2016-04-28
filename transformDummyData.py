import csv
import zipcode
from re import sub
from decimal import Decimal

cleanCSVFile = 'dummyData.csv'
f = open(cleanCSVFile,'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Price', 'C.Pwc','C.Power','C.Sails','C.Small'));

#,'P.Other','P.SingleIn','P.SingleOut','P.TripleOut','P.TwinIn','P.TwinOut','H.Aluminium','H.Composite','H.Ferro','H.Fiberglass','H.Hypalon','H.Other','H.Pvc','H.Roplene','H.Steel','H.Wood','F.Diesel','F.Electric','F.Gas','F.Other','F.Propane','State') )

finally:
    f.close()

with open('cleanData3.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    count2 = 0
    for row in reader:
    	f = open(cleanCSVFile, 'a')
        if row['Boat Class'] == 'PWC':
            pwc = 1;
            power = 0;
            sails = 0
            small = 0
        elif row['Boat Class'] == 'Power':
            pwc = 0;
            power = 1;
            sails = 0
            small = 0
        elif row['Boat Class'] == 'Sails':
            pwc = 0;
            power = 0;
            sails = 1
            small = 0
        elif row['Boat Class'] == 'Small Boats':
            pwc = 0;
            power = 0;
            sails = 0
            small = 1

        try:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow((row['Boat Price'],pwc,power,sails,small))
            count2 = count2 + 1
        finally:
            f.close()
    print count2
