import pandas as pd
'''
df = pd.read_csv(r'urbanpop.csv', encoding="latin-1")
print(df)
test1 = df.values()
test2 = df.keys()
'''
import json
import matplotlib.pyplot as plt

'''
with open('meteors.json', 'rb') as f:
    text = f.read()
    text = text.decode('utf-8')
    meteors = json.loads(text)
'''

json1_file = open('meteors.json', encoding="latin-1")
json1_str = json1_file.read()
meteors = json.loads(json1_str)
#print(meteors)
#meteors = json.loads(meteors.json)
#print("letter = ", meteors[0]['name'])

print(type(meteors[0]['name'][0]))

letters = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}

for letter in letters:
    for meteor in meteors:
        if meteors[0]['name'][0] == letter:
            letters[letter] += 1
print(letters)


'''
for key in dict:
        if key in tweet['text'].lower():
            dict[key] +=1
'''
#print(type(meteors))

#df = pd.read_json(meteors['mass'])
#print(df)
#print(meteors)

'''
num_tweets = 0
output_tweets = []
for tweet in tweets:
    if 'trump' in tweet['text'].lower() and 'chicago' in tweet['text'].lower():
        num_tweets += 1
        output_tweets.append(tweet)
print('num_tweets=',num_tweets)
print('len(tweets)=', len(tweets))

fig, ax = plt.subplots()
#ax.bar(test2, test1)
#plt.show()
'''