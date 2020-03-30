import os
import csv
csvdata = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("financial_analysis.txt")

#declare all variables
total_months = 0
net_total = 0
months_change = []
gincrease = ["",0]
gdecrease = ["",999999]
column_1 = []
change = 0
av_change = []

#dataset=["Total Months", "Total Amount",""]

with open(csvdata) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in (reader):
        print(row[0], row[1])

#calculate the total number of months 
#calculate the net total amount of "Profit/Losses"
#calculate the average of changes in "Profit/Losses"
#calculate the greatest increase
#calculate the greatest decrease
        total_months = total_months + 1  
        net_total = row[1]
        column_1.append(int(row[1]))
        if total_months != 1:
            av_change.append(int(row[1]) - change)
        
        if (int(row[1]) - change) < gdecrease[1]:
            gdecrease[1] = (int(row[1]) - change)
            gdecrease[0] = row[0]

        if (int(row[1]) - change) > gincrease[1]:
            gincrease[1] = (int(row[1]) - change)
            gincrease[0] = row[0]

        change = int(row[1]) 
    average_change = (sum(av_change)) / (total_months - 1)
    net_total = column_1[-1] - column_1[0]

#write the text file for the Financial Analysis
with open(outputfile, "w") as file:
    file.write("Financial Analysis")
    file.write("------------------")
    file.write("Total months: " + str(total_months))
    file.write("Total: " + "$" + str(net_total))
    file.write("Average Change: " + str(average_change))
    file.write("Greatest Increase in Profits: " + str(gincrease))
    file.write("Greatest Decrease in Profits: " + str(gdecrease))

#Print Totals
print(total_months)  
print(net_total)
print(average_change)
print(gdecrease)
print(gincrease)
print(outputfile)
