import os
import csv
csvpoll = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("election_results")

#Declare all variables
total_votes = 0
num_votes = 0
winner = str ()
name = ["","",""]
k_vote = 0
c_vote = 0
l_vote = 0
o_vote = 0
k_per = 0
c_per = 0
l_per = 0
o_per = 0

#Read and open the cvs file
#Calculate number of votes
with open(csvpoll) as csvfile:
    reader = csv.reader(csvfile)  

    for row in (reader):
        total_votes = total_votes + 1
#Print list of candidates
        # if row[2] == "Khan":
        #     name = row[2]
        # if row[2] != "Khan":
        #     name =  row[2]
        #     else 
        #         pass
#Show the number of votes for each candidate
        if row[2] == "Khan":
            k_vote = k_vote + 1 
        if row[2] == "Correy":
            c_vote = c_vote + 1
        if row[2] == "Li":
            l_vote = l_vote + 1
        if row[2] == "O'Tooley":
            o_vote = o_vote + 1

#Show the percentage of votes for each candidate 
        k_per = (k_vote + c_vote + l_vote + o_vote) / .100
        c_per = (k_vote + c_vote + l_vote + o_vote) / .100
        l_per = (k_vote + c_vote + l_vote + o_vote) / .100
        o_per = (k_vote + c_vote + l_vote + o_vote) / .100
#Show the winner of the election by popular vote 

#open & write the text file for the Election Results
with open(outputfile, "w") as file:
    file.write("election_results")
    file.write("------------------")
    file.write("Khan: "+ str(k_per) + "%" + str())
    file.write("Correy: "+ str(c_per) + "%" + str())
    file.write("Li: "+ str(l_per) + "%" + str())
    file.write("O'Tooley: " + str(o_per) + "%" + str())
    file.write("------------------")
    file.write("Winner: " + str())
#Print Totals
print(total_votes)
print(k_vote)
print(c_vote)
print(l_vote)
print(o_vote)
print(k_per) 