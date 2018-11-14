from pprint import pprint
import csv

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


for item in top20List:
    print(item)

# f = open('top20List', 'w')
# for result in top20List:
#     f.write(result)
# f.close()

def top20List():
    return top20List