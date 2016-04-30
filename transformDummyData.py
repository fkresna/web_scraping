import csv
import zipcode
from re import sub
from decimal import Decimal

cleanCSVFile = 'dummyData.csv'
f = open(cleanCSVFile,'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Price', 'C.Pwc','C.Power','C.Sails','C.Small','F.Diesel','F.Electric','F.Gas','F.Other','F.Propane','P.Other','P.SingleIn','P.SingleOut','P.TripleOut','P.TwinIn','P.TwinOut','H.Aluminium','H.Composite','H.Ferro','H.Fiberglass','H.Hypalon','H.Other','H.Pvc','H.Roplene','H.Steel','H.Wood', 'eastCoast','fl','Length'));


finally:
    f.close()

with open('cleanData3.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    count2 = 0
    for row in reader:
    	f = open(cleanCSVFile, 'a')
        
        fl = 0
        if row['State'] == 'FL':
            fl = 1

        eastCoast = 0
        if row['State'] == 'FL' or row['State'] == 'GA' or row['State'] == 'SC' or row['State'] == 'NC' or row['State'] == 'VA' or row['State'] == 'MD' or row['State'] == 'DE' or row['State'] == 'NJ' or row['State'] == 'NY' or row['State'] == 'CT' or row['State'] == 'RI' or row['State'] == 'MA' or row['State'] == 'NH' or row['State'] == 'ME':
            eastCoast = 1

        hAluminium = 0
        hComposite = 0
        hFerro = 0
        hFiberglass = 0
        hHypalon = 0
        hOther = 0
        hPvc = 0
        hRoplene = 0
        hSteel = 0
        hWood = 0
        if row['Hull Material'] == 'Aluminum':
            hAluminium = 1
        elif row['Hull Material'] == 'Composite':
            hComposite = 1
        elif row['Hull Material'] == 'Ferro cement':
            hFerro = 1
        elif row['Hull Material'] == 'Fiberglass':
            hFiberglass = 1
        elif row['Hull Material'] == 'Hypalon':
            hHypalon = 1
        elif row['Hull Material'] == 'Other':
            hOther = 1
        elif row['Hull Material'] == 'Pvc':
            hPvc = 1
        elif row['Hull Material'] == 'Roplene':
            hRoplene = 1
        elif row['Hull Material'] == 'Steel':
            hSteel = 1
        elif row['Hull Material'] == 'Wood':
            hWood = 1

        pOther = 0;
        pSingleIn = 0
        pSingleOut = 0
        pTripleOut = 0
        pTwinIn = 0
        pTwinOut = 0
        if row['Propolsion Type'] == 'Other':
            pOther = 1;
        elif row['Propolsion Type'] == 'Single Inboard':
            pSingleIn = 1
        elif row['Propolsion Type'] == 'Single Outboard':
            pSingleOut = 1
        elif row['Propolsion Type'] == 'Triple Outboard':
            pTripleOut = 1
        elif row['Propolsion Type'] == 'Twin Inboard':
            pTwinIn = 1         
        elif row['Propolsion Type'] == 'Twin Outboard':
            pTwinOut = 1

        pwc = 0;
        power = 0;
        sails = 0
        small = 0
        if row['Boat Class'] == 'PWC':
            pwc = 1;
        elif row['Boat Class'] == 'Power':
            power = 1;
        elif row['Boat Class'] == 'Sails':
            sails = 1
        elif row['Boat Class'] == 'Small Boats':
            small = 1

        diesel = 0
        electric = 0
        gas = 0
        other = 0
        propane = 0
        if row['Fuel Type'] == 'Diesel':
            diesel = 1
        elif row['Fuel Type'] == 'Electric':
            electric = 1
        elif row['Fuel Type'] == 'Gas':
            gas = 1
        elif row['Fuel Type'] == 'Other':
            other = 1
        elif row['Fuel Type'] == 'Propane':
            propane = 1

        try:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow((row['Boat Price'],pwc,power,sails,small,diesel,electric,gas,other,propane,pOther,pSingleIn,pSingleOut,pTripleOut,pTwinIn,pTwinOut,hAluminium, hComposite, hFerro, hFiberglass, hHypalon, hOther, hPvc, hRoplene, hSteel, hWood,eastCoast,fl,row['Boat Length'] ))
            count2 = count2 + 1
        finally:
            f.close()
    print count2
