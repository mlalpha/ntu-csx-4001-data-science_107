import json
import matplotlib.pyplot as plt
from pprint import pprint
import re

try:
    with open('IMDb_data/IMDb2006-2015.json') as data_file:
        data = json.load(data_file)
except:
    print("No such file or directory: 'IMDb_data\\IMDb2006-2015.json'")
    exit()


def getData():
    return data


movies = getData()



keys = list(movies.keys())
sortingRule = lambda a: -1 if movies[a]["imdbVotes"] == "N/A" else int(movies[a]["imdbVotes"].replace(",", ""))

keys.sort(key=sortingRule, reverse=True)

rankingOfVoter = []
numberOfVoter = 0
top30VoterList = []

for key in keys:
    if movies[key]["imdbVotes"] != "N\A":
        voters = int(movies[key]["imdbVotes"].replace(",", ""))
    else:
        voters = -1

    if voters not in rankingOfVoter:
        if numberOfVoter is 30 or len(top30VoterList)>=30:
            break
        numberOfVoter = numberOfVoter + 1
        rankingOfVoter.append(voters)
        top30VoterList.append(movies[key])
    else:
        top30VoterList.append(movies[key])

sortingRule = lambda a: -1 if movies[a]["imdbRating"] == "N/A" else float(movies[a]["imdbRating"])
keys.sort(key=sortingRule, reverse=True)

rankingOfRating = []
numberOfRating = 0
top30RatingList = []

for key in keys:
    if movies[key]["imdbRating"] != "N\A":
        rating = float(movies[key]["imdbRating"])
    else:
        rating = -1

    if rating not in rankingOfRating:
        if numberOfRating is 30 or len(top30RatingList)>=30:
            break
        numberOfRating = numberOfRating + 1
        rankingOfRating.append(rating)
        top30RatingList.append(movies[key])
    else:
        top30RatingList.append(movies[key])


commonInTop30 = [movie for movie in top30RatingList if movie in top30VoterList]

i = 1
init=0
f = open('top30rating', 'w')
for index in range(len(top30RatingList)):
    if init == 0:
        i
    elif top30RatingList[index]["imdbRating"]==top30RatingList[index-1]["imdbRating"]:
        i
    else:
        i = i + 1
    print(str(i)+"\t" + top30RatingList[index]["Title"]+"\t rating:"+top30RatingList[index]["imdbRating"])
    f.write((str(i)+"\t" + top30RatingList[index]["Title"]+"\t\t\t rating:"+top30RatingList[index]["imdbRating"]+"\n"))
    init=1

f.close()

print('-'*13+'separate'+'-'*13)

i = 1
init=0
f = open('top30votes', 'w')
for index in range(len(top30VoterList)):
    if init == 0:
        i
    elif top30VoterList[index]["imdbVotes"] == top30VoterList[index - 1]["imdbVotes"]:
        i
    else:
        i = i + 1
    print(str(i)+"\t" + top30VoterList[index]["Title"]+"\t voters:"+top30VoterList[index]["imdbVotes"])
    f.write((str(i)+"\t" + top30VoterList[index]["Title"]+"\t\t\t voters:"+top30VoterList[index]["imdbVotes"]+"\n"))
    init = 1

f.close()


f = open('commonInTop30','w')

if len(commonInTop30)==0:
    f.write('No common movie')
    print('No common movie')
else:
    for common in commonInTop30:
        f.write(common+'\n')
        print(common)

f.close()