import requests
import csv
import json


outputFile = open("data.csv", 'w') #load csv file
output = csv.writer(outputFile) #create a csv.write    

def scrape():
    i = 0
    while i < 99999999:
        try:
            requestGet(i)
            i += 1
            print(i)
        except:
            print("problem" + str(i))
            i += 1


def requestGet(i):
    num = (int)(f'{i:08}')
    r = requests.get("https://www.bestbuy.ca/api/v2/json/product/" + num + "?currentRegion=BC&include=all&lang=en-CA")
    data = r.json()    
    output.writerow(data.values()) #values row

scrape()



