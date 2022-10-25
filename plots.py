import pandas as pd
import json
import matplotlib.pyplot as plt
import csv

with open('asteroids.json', 'rb') as f:
    text = f.read()
    text = text.decode('utf-8')
    asteroids = json.loads(text)

periods = {"0.5-1":0,"1-1.5":0,"1.5-2":0,"2-2.5":0,"2.5-3":0,"3-3.5":0,"3.5-4":0,"4-4.5":0,"4.5-5":0,"5-10":0,"10+":0}

orbital_periods = [d["period_yr"] for d in asteroids if "period_yr" in d]
orbital_periods = list(map(float, orbital_periods))

for op in orbital_periods:
    if op >= 0.5 and op < 1.0:
        periods["0.5-1"] += 1
    if op >= 1.0 and op < 1.5:
        periods["1-1.5"] += 1
    if op >= 1.5 and op < 2.0:
        periods["1.5-2"] += 1
    if op >= 2.0 and op < 2.5:
        periods["2-2.5"] += 1
    if op >= 2.5 and op < 3.0:
        periods["2.5-3"] += 1
    if op >= 3.0 and op < 3.5:
        periods["3-3.5"] += 1
    if op >= 3.5 and op < 4.0:
        periods["3.5-4"] += 1
    if op >= 4.0 and op < 4.5:
        periods["4-4.5"] += 1
    if op >= 4.5 and op < 5.0:
        periods["4.5-5"] += 1
    if op >= 5.0 and op < 10.0:
        periods["5-10"] += 1
    if op >= 10.0:
        periods["10+"] += 1

buckets = list(periods.keys())
counts = list(periods.values())

fig, ax = plt.subplots()
ax.bar(buckets, counts)
plt.title('Orbital Period Distribution of Near-Earth Objects Discovered By NEOWISE')
plt.xlabel('Oribital Period Around Sun (years)')
plt.ylabel('Number of Near-Earth Objects')
#plt.show()



df = pd.read_csv(r'causedeathfr.csv', encoding="latin-1")
print(df)

dict = {}

columns = ['TIME', "ICD10", 'Value']

'''
df = pd.read_csv(r'causedeathfr.csv', usecols=columns)

# Plot the lines
df.plot()

plt.show()


#test1 = df.values()
#test2 = df.keys()
'''