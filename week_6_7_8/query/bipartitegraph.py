from pprint import pprint
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

BipartitieG = nx.Graph()

movie_id_list = []
actor_list = []

numberOfFilm = 0
for key, movie in movies.items():

    try:
        movie_id = movie["imdbID"]
    except:
        print(movie_id)

    BipartitieG.add_node(movie_id)
    movie_id_list.append(movie_id)

    actors = movie["Actors"].split(', ')
    for actor in actors:
        if actor == "N/A":
            actors.remove(actor)
        elif BipartitieG.has_node(actor) is False:
            BipartitieG.add_node(actor)
            actor_list.append(actor)

    edges = [(movie_id, actor) for actor in actors]
    BipartitieG.add_edges_from(edges)

# pprint(BipartitieG.adjacency_list())

f = open('bipartitegraph.json', 'w')


def constructRow(a, b):
    return "\""+a+"\":"+json.dumps(b)


f.write('{\"movie_to_actors\":{')

index = 0
for movie_id in movie_id_list:
    if index == 0:
        index = 1
    else:
        f.write(',')
    f.write(constructRow(movie_id, BipartitieG.neighbors(movie_id)))

f.write('},\"actor_to_movies\":{')

index = 0
for actor in actor_list:
    if index == 0:
        index = 1
    else:
        f.write(',')
    f.write(constructRow(actor, BipartitieG.neighbors(actor)))

f.write('}}')

f.close()


# nx.draw_networkx(BipartitieG)
# plt.show()
