import pandas as pd
import json
import matplotlib.pyplot as plt
import csv


# JSON


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
#plt.title('Orbital Period Distribution of Near-Earth Objects Discovered By NEOWISE')
plt.xlabel('Oribital Period Around Sun (years)')
plt.ylabel('Number of Near-Earth Objects')
#plt.show()


# CSV


df = pd.read_csv(r'adultarrests.csv', encoding="latin-1")

drug = list(df.groupby('Year')['Drug Felony'].sum())
violent = list(df.groupby('Year')['Violent Felony'].sum())
years = [1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

plt.plot(years, drug)
plt.plot(years, violent)
plt.xlabel('Year')
ax.set_xlim([1970, 2021])
plt.ylabel('Number of Felonies')
plt.legend(['Drug', 'Violent'])
plt.show()