# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:14:02 2020

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = "uXx7jA1DEz0Y8nUi12XRAMI1lY45SE5Q"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)