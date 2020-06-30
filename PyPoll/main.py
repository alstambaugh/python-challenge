import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# variable for counting total votes
Total_votes = 0

# List of unique candidates
candidates_list = []

# Loop to get total votes and candidate names
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # Count total votes
        Total_votes = Total_votes + 1

        # Add unique candidate to candidate list
        if row[2] not in candidates_list:
                candidates_list.append(row[2])

# Create dictionary with candidate names as key; value as 0
Candidate_dict = { i : 0 for i in candidates_list}

# Loop to get votes per candidate; add to dictionary value
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # Variable for candidate name
         name = row[2]
        
        # Iterate through dictionary; if key matches candidate name, add 1 to value
         for key, value in Candidate_dict.items():
           if key == name:
                Candidate_dict[name] = int(Candidate_dict[name]) + 1
            
file = open("analysis/Output.txt", "w")
    
print("Election Results")
file.write("Election Results" "\n")
print("-----------------------")
file.write("-----------------------" "\n")
print(f"Total Votes: {Total_votes}")
file.write(f"Total Votes: {Total_votes}" "\n")
print("-----------------------")
file.write("-----------------------" "\n")

# Determine percentage of votes and winner
winner_votes = 0

# Loop through candidate list
for name in candidates_list:
    # Loop through candidate dictionary; change value to list with 2 items - percent and total    
    for key, value in Candidate_dict.items():
        if key == name:
            Candidate_dict[name] = [round(int(Candidate_dict[name])/Total_votes * 100, 4), Candidate_dict[name]]

            # Look for candidate with largest number of votes
            if Candidate_dict[name][1] > winner_votes:  
                winner = key
                winner_votes = Candidate_dict[name][1]

            # Print individual candidate statistics
            print(name + ":  " + "%.3f"%(Candidate_dict[name][0]) + "%  (" + str(Candidate_dict[name][1]) + ")")

            file.write(name + ":  " + "%.3f"%(Candidate_dict[name][0]) + "%  (" + str(Candidate_dict[name][1]) + ")" "\n")

print("-----------------------")
file.write("-----------------------" "\n")
print("Winner: " + winner)
file.write("Winner: " + winner + " " "\n")
print("-----------------------")
file.write("-----------------------" "\n")
file.close()