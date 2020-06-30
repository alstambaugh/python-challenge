import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# variables for counting
PL_change_start = 0

# Generate lists for each column and for profit/loss change
Month_list = []
PL_list = []
PL_change_list = []


#Add items to list; calculate profit/loss monthly change 
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        # Add month to list
        Month_list.append(row[0])
        
        # Add profit/loss to list
        PL_list.append(int(row[1]))

        # Calculate difference from previous month and add to list
        PL_change_list.append((int(row[1])) - PL_change_start)

        #Reset PL for next iteration
        PL_change_start = int(row[1])



#Find average change
PL_length = len(PL_list)
average_change = round((PL_list[PL_length - 1] - PL_list[0]) / (PL_length - 1),2)

#Find month of greatest increase/decrease
max_value = max(PL_change_list)
max_index = (PL_change_list.index(max_value))

min_value = min(PL_change_list)
min_index = (PL_change_list.index(min_value))




#Final Results
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {len(Month_list)}")
print(f"Total: ${sum(PL_list)}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {Month_list[max_index]}: (${max_value})")
print(f"Greatest Decrease in Profits: {Month_list[min_index]}: (${min_value})")

file = open("analysis/Output.txt", "w")
file.write("Financial Analysis" "\n") 
file.write("-------------------------------------" "\n")
file.write(f"Total Months: {len(Month_list)}" "\n")
file.write(f"Total: ${sum(PL_list)}" "\n")
file.write(f"Average Change: ${average_change}" "\n")
file.write(f"Greatest Increase in Profits: {Month_list[max_index]}: (${max_value})" "\n")
file.write(f"Greatest Decrease in Profits: {Month_list[min_index]}: (${min_value})" "\n")
file.close()