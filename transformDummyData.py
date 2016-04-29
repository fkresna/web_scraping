import csv
import zipcode
from re import sub
from decimal import Decimal

cleanCSVFile = 'dummyData.csv'
f = open(cleanCSVFile,'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Price', 'C.Pwc','C.Power','C.Sails','C.Small','F.Diesel','F.Electric','F.Gas','F.Other','F.Propane'));

#,'P.Other','P.SingleIn','P.SingleOut','P.TripleOut','P.TwinIn','P.TwinOut','H.Aluminium','H.Composite','H.Ferro','H.Fiberglass','H.Hypalon','H.Other','H.Pvc','H.Roplene','H.Steel','H.Wood','State') )

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

        if row['Fuel Type'] == 'Diesel':
            diesel = 1
            electric = 0
            gas = 0
            other = 0
            propane = 0
        elif row['Fuel Type'] == 'Electric':
            diesel = 0
            electric = 1
            gas = 0
            other = 0
            propane = 0
        elif row['Fuel Type'] == 'Gas':
            diesel = 0
            electric = 0
            gas = 1
            other = 0
            propane = 0
        elif row['Fuel Type'] == 'Other':
            diesel = 0
            electric = 0
            gas = 0
            other = 1
            propane = 0
        elif row['Fuel Type'] == 'Propane':
            diesel = 0
            electric = 0
            gas = 0
            other = 0
            propane = 1

        try:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow((row['Boat Price'],pwc,power,sails,small,diesel,electric,gas,other,propane))
            count2 = count2 + 1
        finally:
            f.close()
    print count2
