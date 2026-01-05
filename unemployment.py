
import requests
import json
import pandas as pd
import os 

url = "https://api.worldbank.org/v2/country/fr/indicator/SP.POP.TOTL?format=json"

response = requests.get(url)


print(response.status_code)   # 200 = OK
data = response.json()

with open("population.json", "w", encoding="utf-8") as file:
    json.dump(data, file, sort_keys=True, indent = 4 )

path = "population.json"

with open(path, "r") as file:
    data = json.load(file)


pop = []

for i in data[1]: 
    row = {
        "annee" : i["date"],
        "population" : i["value"]
    }
    pop.append(row)

pop = pop[::-1]

print(pop[:3])
