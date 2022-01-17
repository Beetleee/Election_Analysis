# Assign a variable for the file to load and the path.
##file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
##election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
##election_data.close()

# Open the election results and read the file
##with open(file_to_load) as election_data:

     # To do: perform analysis.
     ##print(election_data)

#Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
##open(file_to_save, "w")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here. 
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    



# Using the with statement open the file as a text file.
##with open(file_to_save, "w") as txt_file:

    # Write data to file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

    # Write data to file -each on a new line.
    ##txt_file.write("Counties in the Election\n_______________________________\nArapahoe\nDenver\nJefferson")


#In this project, our final Python script will need to be able to deliver the following information when the script is run: 

#Total number of votes cast

# A complete list of candidates who received votes

# Total number of votes each candidate received

# Percentage of votes each candidate won

# The winner of the election based on popular vote