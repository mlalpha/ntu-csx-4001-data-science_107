import numpy as np
import matplotlib.pyplot as plt
import json
import csv

try:
    with open('IMDb_data/IMDb2006-2015.json') as data_file:
        data = json.load(data_file)
    with open('bipartitegraph.json') as data_file:
        bipartgraph = json.load(data_file)
except:
    print("No such file or directory: 'IMDb_data\\IMDb2006-2015.json'")
    print("No such file or directory: 'bipartitegraph.json'")
    exit()


def getData():
    return data


def getBipartGraph():
    return bipartgraph


movies = getData()
# for key in movies.keys():
#     tmp_movie = movies.pop(key)
#     movies[tmp_movie['imdbID']] = tmp_movie

bipartgraph = getBipartGraph()


with open('top20List') as csvfile:
    lineReader = csv.reader(csvfile, delimiter='\n')
    top20CollActor = [item[0].split(',') for item in list(lineReader)]


popDirectorsList = []
for item in top20CollActor:
    actorA = item[0]
    actorB = item[1]
    try:
        actorAFilm = bipartgraph['actor_to_movies'][actorA]
        actorBFilm = bipartgraph['actor_to_movies'][actorB]
    except:
        continue
        # print "some encoding problem encounter with "+item[0]+","+item[0]

    commonFilm = [movieID for movieID in actorAFilm if movieID in actorBFilm]
    commonDirector = {}

    for movieID in commonFilm:
        director = movies[movieID]['Director']
        if director == 'N/A':
            continue
        if commonDirector.get(item[0]+','+item[1]+','+director, False) != False:
            commonDirector[item[0]+','+item[1]+',' +
                           director] = commonDirector[item[0]+','+item[1]+','+director] + 1
        else:
            commonDirector[item[0]+','+item[1]+','+director] = 1

    keys = commonDirector.keys()
    mostCollaborateTime = 0
    for director in keys:
        popDirectorsList.append(([director, commonDirector[director]]))
    commonDirector.clear()


popDirectorsList.sort(key=lambda x: (x[1], -len(x[0])), reverse=True)


f = open('popDirector', 'w')
i = 0
for popDirector in popDirectorsList:
    i = i+1
    f.write(popDirector[0]+'\n')
    print(popDirector[0], ',', popDirector[1])
    if i == 20:
        break

f.close()
