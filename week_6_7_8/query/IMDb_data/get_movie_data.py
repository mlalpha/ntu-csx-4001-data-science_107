#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import json


def IMDb_query_url(id):
    # the returned query url for id='tt0407887' should be 'http://www.omdbapi.com/?i=tt0407887&plot=short&r=json'
    query_url = "http://www.omdbapi.com/?i=" + id + "&plot=short&r=json"

    return query_url


def get_movie_ids(input_file):
    id_list = []
    with open(input_file, 'r') as f:
        for line in f:
            id_list.append(line.replace('\n', ''))
        f.close()
    print "finished read id"

    return id_list


def get_all_data(in_file, out_file):
    movie_data_dict = {}
    movie_ids = get_movie_ids(in_file)

    id_counter = 0
    session = requests.Session()

    for id in movie_ids:
        url = IMDb_query_url(id)

        # start writing your code here
        # get movie data using the session.get(url).json()

        tmp = session.get(url)
        movie_data = tmp.text

        # you may need to handle some exceptions here
        try:
            movie_data = tmp.json()

        except:
            print ("Error found for request:" + url)
            print tmp.text
            print 20*"-"
            continue

        if movie_data["Response"]!= "False":
            movie_data_dict[movie_data["imdbID"]] = movie_data
            id_counter += 1


    # don't change any code below this line
    print "finished read json"
    with open(out_file, 'w+') as f:
        json.dump(movie_data_dict, f)

    print "finished write file"

if __name__ == '__main__':
    # don't change any code below this line
    movie_id_file = '..\IMDbIDCrawler\movie_ids06-15'
    movie_data_file = 'IMDb2006-2015.json'
    get_all_data(movie_id_file, movie_data_file)
