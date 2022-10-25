import pandas as pd
import json
import matplotlib.pyplot as plt

with open('asteroids.json', 'rb') as f:
    text = f.read()
    text = text.decode('utf-8')
    asteroids = json.loads(text)

periods = {"0-0.5":0,"0.5-1":0,"1-1.5":0,"1.5-2":0,"2-2.5":0,"2.5-3":0,"3-3.5":0,"3.5-4":0,"4-4.5":0,"4.5-5":0}

oribital_period = asteroids[0]['period_yr']
op = float(oribital_period)

for asteroid in asteroids:
    for value in periods:
        if op >= 0 and op <= 0.5:
            value += 1
print(periods)

'''
fig, ax = plt.subplots()
ax.bar(test2, test1)
plt.show()
'''