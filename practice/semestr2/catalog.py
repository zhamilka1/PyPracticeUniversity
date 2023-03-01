import urllib.request as getCatalog
import json
from datetime import datetime
import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://quke.ru/shop/smartfony/apple?page-size=72"
result = getCatalog.urlopen(url).read().decode()
pricePattern = r"^(?:<div class=.b-card2-v2__old-price.>)([^<]*)"
namePattern = r"^(?:<a class=.b-card2-v2__name. href=./shop/UID_116610_apple_iphone_14_pro_max_128gb_deep_purple.html. title=).([^d<]*)"
names = re.findall(namePattern, result)
prices = re.findall(pricePattern, result)

print(names, prices)
print(result)