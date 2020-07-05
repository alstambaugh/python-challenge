import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# variable for counting total votes
Total_votes = 0

# Dictionary for tracking candidates
Candidate_dict = {}

# Loop to get total votes and candidate votes
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # Count total votes
        Total_votes = Total_votes + 1

        name = row[2]

        if name not in Candidate_dict:
            # Add candidate to dictionary
            Candidate_dict[name] = 1
        else:
            # Increment vote count for candidate    
            Candidate_dict[name] = Candidate_dict[name] + 1    
        

           
file = open("analysis/Output.txt", "w")
    
print("Election Results")
file.write("Election Results" "\n")
print("-----------------------")
file.write("-----------------------" "\n")
print(f"Total Votes: {Total_votes}")
file.write(f"Total Votes: {Total_votes}" "\n")
print("-----------------------")
file.write("-----------------------" "\n")

# Loop through dictionary to get results
for candidate_name, vote_count in Candidate_dict.items():
    # Calculate vote percentage
    percentage = "{:.3%}".format(vote_count / Total_votes)
    
    # Print candidate results
    print(f"{candidate_name}:  {percentage} ({vote_count})")
    file.write(f"{candidate_name}:  {percentage} ({vote_count})" "\n")     
    
    # Find winner
    winner = max(Candidate_dict.values())    
    
    if winner == vote_count:
        winner_name = candidate_name 


print("-----------------------")
file.write("-----------------------" "\n")
print("Winner: " + str(winner_name))
file.write("Winner: " + str(winner_name) + " " "\n")
print("-----------------------")
file.write("-----------------------" "\n")
file.close()