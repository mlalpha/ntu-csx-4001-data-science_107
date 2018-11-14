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

movie = movies['tt0117743']
