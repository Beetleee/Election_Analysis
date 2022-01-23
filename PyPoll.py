# # Assign a variable for the file to load and the path.
# ##file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# ##election_data = open(file_to_load, 'r')

# # To do: perform analysis.

# # Close the file.
# ##election_data.close()

# # Open the election results and read the file
# ##with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      ##print(election_data)

# #Add our dependencies
# #import csv
# #import os
# # Assign a variable for the file to load and the path.
# #file_to_load = os.path.join("Resources", "election_results.csv")
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Initialize a vote counter.
# total_votes = 0

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     #Print the file object.
#     #print(election_data)
# # Using the open() function with the "w" mode we will write data to the file.
# ##open(file_to_save, "w")

#     #To do: read and analyze the data here. 
#     #Read the file object with the reader function.
#     file_reader = csv.reader(election_data)

#     #Read header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         #2.Add to tht total vote count.
#         total_votes +=1

# #3. Print the total votes.
# print(total_votes)
  




# # Using the with statement open the file as a text file.
# ##with open(file_to_save, "w") as txt_file:

#     # Write data to file.
#     #txt_file.write("Arapahoe, ")
#     #txt_file.write("Denver, ")
#     #txt_file.write("Jefferson")

#     # Write data to file -each on a new line.
#     ##txt_file.write("Counties in the Election\n_______________________________\nArapahoe\nDenver\nJefferson")


# #In this project, our final Python script will need to be able to deliver the following information when the script is run: 

# ####1) Total number of votes cast
# #Add our dependencies
# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Initialize a vote counter.
# total_votes = 0

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     #Print the file object.
#     #print(election_data)
# # Using the open() function with the "w" mode we will write data to the file.
# ##open(file_to_save, "w")

#     #To do: read and analyze the data here. 
#     #Read the file object with the reader function.
#     file_reader = csv.reader(election_data)

#     #Read header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         #2.Add to tht total vote count.
#         total_votes +=1

# #3. Print the total votes.
# print(total_votes)

### 2)A complete list of candidates who received votes
#Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a vote counter.
total_votes = 0

#Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Print the file object.
    #print(election_data)
# Using the open() function with the "w" mode we will write data to the file.
##open(file_to_save, "w")
#To do: read and analyze the data here. 
#Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #2.Add to tht total vote count.
        total_votes +=1

#Print the candidatee name from each row.
candidate_name = row[2]

#use this if you want to report ALL names
#Add the candidate name to the candidate list.
#candidate_options.append(candidate_name)

#If the candidate doesn't match any existing candidate...
if candidate_name not in candidate_options:
    #Add it to the list of candidates
        candidate_options.append(candidate_name)

# Print the candidate list
print(candidate_options)

###3) Print the total votes.
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

# Print the candidate vote dictionary.
print(candidate_votes)
if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

            #2. Begin tracking that candidate's vote count.
        candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary.
        print(candidate_votes)

###4) Total number of votes each candidate received



###5) Percentage of votes each candidate won

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
#for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    #votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    #vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    
###6) The winner of the election based on popular vote