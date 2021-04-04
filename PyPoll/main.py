import os
import csv
import numpy as np
file = os.path.join("Resources","PyPoll_Resources_election_data.csv")
output=os.path.join("Analysis","Analysis.txt")

candidate=[]
total_vote=0
with open(file,'r',encoding="utf-8") as csvfile :
    reader=csv.reader(csvfile,delimiter=',')
    header=next(reader)
    print(header)

    for row in reader :
        total_vote += 1
        candidate.append(row[2])

    candi=np.array(candidate)
    can, count = np.unique(candi,return_counts=True)
    percent=count/total_vote *100
    percent=[round(x,3) for x in percent ]
    # cast to list
    lst=[can.tolist(),percent,count.tolist()]
    # transpose
    lst=list(map(list,zip(*lst)))
    # sort
    slst=sorted(lst,key=lambda x:x[1],reverse=True)
    print(f'Election Results\nTotal Votes: {total_vote}\n{slst}\nWinner: {slst[0][0]}')


with open(output,'w') as out :
    out.writelines(f"Election Results\n---------------\nTotal Votes: {total_vote}\n---------------\n{slst}\n---------------\nWinner: {slst[0][0]}\n---------------")