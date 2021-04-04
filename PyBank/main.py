import os 
import csv

file = os.path.join('Resources','budget_data.csv')
output=os.path.join('Analysis','Analysis.txt')

total_months=0
revenue=[]
month=[]
rev_change=[]

with open (file,"r",encoding="utf-8") as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    header=next(reader)
    print(header)
    

    for row in reader:
        total_months += 1
        month.append(row[0])
        revenue.append(int(row[1]))
    for r in range(len(revenue)-1):
        rev_change.append(revenue[r+1]-revenue[r])
        
    max_rc=max(rev_change)
    max_rc_month=month[rev_change.index(max_rc)+1]
    min_rc=min(rev_change)
    min_rc_month=month[rev_change.index(min_rc)+1]

    total=sum(revenue)
    avg_change=(revenue[-1]-revenue[0])/(total_months-1)
    Analysis=("Total Months: {}\nAverage Change: ${} \nTotal: ${} \nGreatest Increase in profit: ${}, {} \nGreatest Decrease in Profit: ${}, {}\n".format(
        total_months,avg_change,total,max_rc,max_rc_month,min_rc,min_rc_month))
    print(Analysis)


    
with open(output,"w") as o:
    o.writelines(["Financial Analysis \n","----------------------\n", Analysis])