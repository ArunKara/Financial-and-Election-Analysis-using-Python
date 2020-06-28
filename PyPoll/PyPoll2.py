import os
import csv
election_data_csv = os.path.join("Resources","election_data.csv")
#tracking output
count = 0 #start your counter
unique_list = []
candidate_list = []
count_vote = []
percent_vote = []
with open(election_data_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    print(csv_header)
    #total votes
    for i in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidate_list.append(i[2])
        # Create a set from the candidatelist to get the unique candidate names
    for j in set(candidate_list):
        unique_list.append(j)
        #let find the total number of votes per candidate
        number = candidate_list.count(j)
        count_vote.append(number)
        #let find the percent of total votes
        percent = (number/count)*100
        percent_vote.append(percent)
    most_votes_winner = max(count_vote)
    winner = unique_list[count_vote.index(most_votes_winner)]
print(f"Total Votes: {count}\n")
for i in range(len(unique_list)):
            print(unique_list[i] + ": " + str(percent_vote[i]) +"% (" + str(count_vote[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)

output_file = os.path.join("Analysis","Vote_Analysis.txt")
with open(output_file,"w") as datafile:
    writer = csv.writer(datafile)
    datafile.write(f"Total Votes: {count}\n")

    for i in range(len(unique_list)):
        
        datafile.write(f"{unique_list[i]} : {str(percent_vote[i])} % {str(count_vote[i])}\n")

    datafile.write(f"-------------------------\n")
    datafile.write(f"The winner is: {winner}")
    