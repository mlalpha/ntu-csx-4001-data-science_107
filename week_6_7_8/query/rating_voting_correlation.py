import numpy as np
import matplotlib.pyplot as plt
import json

try:
    with open('IMDb_data/IMDb2006-2015.json') as data_file:
        data = json.load(data_file)
except:
    print("No such file or directory: 'IMDb_data\\IMDb2006-2015.json'")
    exit()


def getData():
    return data


movies = getData()


N = len(movies)
x,y=[],[]
xMax=0
yMax=0

for key, movie in movies.iteritems():
    try:
        y1 = int(movie["imdbVotes"].replace(",",""))
        x1 = float(movie["imdbRating"])
        x.append(x1)
        y.append(y1)
        if x1>xMax:
            xMax = x1
        if y1>yMax:
            yMax = y1
    except:
        continue
        # print  "imdbVotes:"+movie["imdbVotes"]+",imdbRating:"+movie["imdbRating"]


plt.scatter(x,y, alpha=0.3)
plt.xlim(0,xMax+xMax*0.1)
plt.ylim(0,yMax+yMax*0.02)
plt.xlabel('Rating')
plt.ylabel('# of Voters')
plt.savefig('rating_voting_correlation.png')
plt.show()