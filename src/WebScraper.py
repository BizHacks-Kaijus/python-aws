import urllib.request
import json

prefix = "https://www.bestbuy.ca/api/v2/json/product/"
suffix = "?currentRegion=BC&include=all&lang=en-CA"

#start 10000000 end 99999999

for i in range(12785800, 12785910):
    print(prefix + str(i) + suffix)
    try:
        with urllib.request.urlopen(prefix + str(i) + suffix) as url:
            s = url.read()
            # I'm guessing this would output the html source code ?
            js = json.loads(s)
            print(js['name'])
    except:
        print("not found")
