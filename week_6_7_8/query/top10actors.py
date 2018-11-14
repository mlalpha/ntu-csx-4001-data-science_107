from pprint import pprint
import csv

collaborativeRank = {}

with open('collgraph.edgelist') as csvfile:
    lineReader = csv.reader(csvfile, delimiter='\n')
    csv_list = [item[0].split(',') for item in list(lineReader)]
    for row in csv_list:
        if collaborativeRank.get(row[0], False):
            collaborativeRank[row[0]] = collaborativeRank[row[0]]+int(row[2])
        else:
            collaborativeRank[row[0]] = int(row[2])

        if collaborativeRank.get(row[1], False):
            collaborativeRank[row[1]] = collaborativeRank[row[1]]+int(row[2])
        else:
            collaborativeRank[row[1]] = int(row[2])

rank = list(collaborativeRank.items())
rank.sort(key=lambda a:int(a[1]),reverse=True)

ranking=[]
numberOfRank=0
top10List=[]


for item in rank:
    if len(top10List)==10:
        break
    if item[1] not in ranking:
        if numberOfRank is 10 or len(top10List)>=10:
            break
        numberOfRank=numberOfRank+1
        ranking.append(item[1])
        top10List.append((item))
    else:
        top10List.append(item)


f = open('top10List', 'w')
for actor in top10List:
    f.write(actor[0]+","+str(actor[1])+"\n")
    print(actor[0]+", "+str(actor[1]))
f.close()