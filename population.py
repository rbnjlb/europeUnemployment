
import requests
import json
import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter



country = "fr"
url = f"https://api.worldbank.org/v2/country/{country}/indicator/SP.POP.TOTL?format=json"

response = requests.get(url)


print(response.status_code)   # 200 = OK
data = response.json()

with open("population.json", "w", encoding="utf-8") as file:
    json.dump(data, file, sort_keys=True, indent = 4 )

path = "population.json"

with open(path, "r") as file:
    data = json.load(file)

countryFullName = data[1][0]["country"]["value"]
print(countryFullName)

pop = []


for i in data[1]:
    currentYear = i["date"]
    currentPop = i["value"]

    if currentPop is None:
        row = {
            "Year" : currentYear,
            "Population" : np.nan
        }
        pop.append(row)
        print(currentPop)
    
    else:
        row = {
            "Year" : currentYear,
            "Population" : currentPop
        }
        pop.append(row)
         

    
df = pd.DataFrame(pop, columns=['Year','Population']).sort_values(by='Year', ascending=True)
df = df.reset_index(drop=True)
df["Population"] = df["Population"].astype("Float64")
df["Year"] = df["Year"].astype(int)

df["Population_interpolated"] = df["Population"].interpolate(method="linear")




plt.figure(figsize=(10, 6))
plt.plot(df["Year"],(df["Population_interpolated"]), linewidth = 2.5)
plt.xticks(df["Year"][::5])

plt.tick_params(axis="x", labelsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.title(label=f"Population de la {countryFullName} (1975–2024)")
plt.xlabel("Année")
plt.ylabel("Population (millions)")
plt.tight_layout()


plt.show()

