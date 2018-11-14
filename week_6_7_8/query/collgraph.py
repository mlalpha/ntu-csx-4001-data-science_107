# from pprint import pprint
import networkx as nx
import json
import matplotlib.pyplot as plt

try:
    with open('IMDb_data/IMDb2006-2015.json') as data_file:
        data = json.load(data_file)
except:
    print("No such file or directory: 'IMDb_data\\IMDb2006-2015.json'")
    exit()


def getData():
    return data


movies = getData()
CollaborationGraph = nx.Graph()

numberOfFilm = 0
for key, movie in movies.items():
    # if numberOfFilm == 100:
    #     break
    # numberOfFilm += 1

    actors = movie["Actors"].split(', ')
    for actor in actors:
        if actor == "N/A":
            actors.remove(actor)
        elif CollaborationGraph.has_node(actor) is False:
            CollaborationGraph.add_node(actor)
    # print actors

    for i in range(len(actors)):
        for j in range(i + 1, len(actors)):
            if CollaborationGraph.has_edge(actors[i], actors[j]):
                # print CollaborationGraph[actors[i]][actors[j]]['weight']
                CollaborationGraph[actors[i]][actors[j]]['weight'] = \
                    CollaborationGraph[actors[i]][actors[j]]['weight'] + 1
            else:
                CollaborationGraph.add_edge(actors[i], actors[j], weight=1)


edges = sorted(CollaborationGraph.edges(),
               key=lambda tup: (len(tup[0])+len(tup[1])))


f = open('collgraph.edgelist', 'w')


def constructRow(a, b, c): return a+','+b+','+str(c)+'\n'


for edge in edges:
    if min([edge[0], edge[1]], key=str.lower) != edge[0]:
        edge = (edge[1], edge[0])

    f.write(constructRow(
        edge[0], edge[1], CollaborationGraph[edge[0]][edge[1]]['weight']))


f.close()
