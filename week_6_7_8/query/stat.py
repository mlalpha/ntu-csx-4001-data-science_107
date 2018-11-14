from pprint import pprint
import csv



def top20List():
    with open('collgraph.edgelist') as csvfile:
        lineReader = csv.reader(csvfile, delimiter='\n')
        collaborationList = [item[0].split(',') for item in list(lineReader)]

    collaborativeRank = {}
    for item in collaborationList:

        test = ["", ""]
        result = item
        test[0] = item[0].lower()
        test[1] = item[1].lower()

        if test[0][0] > test[1][0]:
            tmp = [item[1], item[0], item[2]]
        else:
            tmp = [item[0], item[1], item[2]]

        if collaborativeRank.get(int(item[2]), False) != False:
            collaborativeRank[int(item[2])].append(result)
        else:
            collaborativeRank[int(item[2])] = []
            collaborativeRank[int(item[2])].append(result)

    rank = list(collaborativeRank.keys())

    rank.sort(reverse=True)

    ranking = []
    numberOfRank = 0
    top20List = []


    def constructRow(a, b, c): return a + ',' + b + ',' + str(c) + '\n'


    i = 0
    for item in rank:
        if i == 20 or (len(top20List) >= 20):
            break
        collaborativeRank[item].sort(key=lambda x: (len(x[0])+len(x[1])))
        for item in collaborativeRank[item]:
            top20List.append(constructRow(item[0], item[1], item[2]))
            i = i + 1
            if i == 20:
                break

    return top20List

def rating_voting_correlation():
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