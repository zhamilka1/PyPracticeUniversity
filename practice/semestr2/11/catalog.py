import urllib.request as getCatalog
import json
from datetime import datetime
import csv
import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://quke.ru/shop/smartfony/apple?page-size=72"
result = getCatalog.urlopen(url).read().decode()
pricePattern = r"(?:<div class=.b-card2-v2__old-price.>)([^<]*)"
namePattern = r"(?:title=\"([^<]*)\"\ data)"
names = re.findall(namePattern, result)
prices = re.findall(pricePattern, result)
colnames = ['Name', 'Price']

with open("iphones.csv", encoding='utf-8', mode='w') as w_file:

    file_writer = csv.DictWriter(w_file, delimiter = "|", lineterminator="\r", fieldnames=colnames)
    file_writer.writeheader()
    for name in names:
        for price in prices:
            file_writer.writerow({"Name": name, "Price": price})

