import urllib.request
import json
import csv

prefix = "https://www.bestbuy.ca/api/v2/json/product/"
suffix = "?currentRegion=BC&include=all&lang=en-CA"

#start 10000000 end 99999999

outputFile = open("data.csv", 'w') #load csv file
output = csv.writer(outputFile) #create a csv.write  

for i in range(10000000, 99999999):
    print(prefix + str(i) + suffix)
    try:
        with urllib.request.urlopen(prefix + str(i) + suffix) as url:
            s = url.read()
            # I'm guessing this would output the html source code ?
            js = json.loads(s)
            print(js['name'])
            output.writerow(js.values()) #values row
    except:
        print("not found")
