import os
import csv
csvpoll = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("election_results")

#Declare all variables
total_votes = 0
candidate_name = 0
candidate_votes = {}
winner = ""
winner_count = 0


#Read and open the cvs file
#Calculate number of votes
with open(csvpoll) as csvfile:
    reader = csv.reader(csvfile)  
    header = next(reader)

    for row in (reader):
        total_votes = total_votes + 1

# And begin tracking that candidate’s voter count
       total_votes[candidate_name] = 0
       total_votes[candidate_name] = total_votes[candidate_name] + 1
        if 
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
        
        vote_percentage = float(k_votes) / float(total_votes) * 100
        vote_percentage = float(c_votes) / float(total_votes) * 100
        vote_percentage = float(l_votes) / float(total_votes) * 100
        vote_percentage = float(o_votes) / float(total_votes) * 100

        # k_per = (k_vote + c_vote + l_vote + o_vote) / .100
        # c_per = (k_vote + c_vote + l_vote + o_vote) / .100
        # l_per = (k_vote + c_vote + l_vote + o_vote) / .100
        # o_per = (k_vote + c_vote + l_vote + o_vote) / .100
#Show the winner of the election by popular vote 
    print(". ", end="")
#open & write the text file for the Election Results
with open(outputfile, "w") as file:
    output = f”{candidate}: {vote_percentage:.3f}% ({votes})\n”
        print(voter_output, end=“”)


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
print(c_per)
print(l_per)
print(o_per)