#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

#Initialise total votes counter
total_votes = 0

# Declare new list for candiates names
candidate_options = []

# Declare new dictionary for candidates' votes
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

#To do: read and analyse the data here
    file_reader = csv.reader(election_data)    

    #Read and print the header row
    headers = next(file_reader)
    
    # Print total votes and name of candidates
    for row in file_reader:
        total_votes +=1
        candidate_name = row[2]
        # Check if candidate name is in candidate options. If it isn't add to the candidate options list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1 

    # Determine the percentage of votes for each candidate by looping through the counts
    #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes)*100
        #4. Print the candidate name and percentage of votes
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")

        #To do: print out each candidate's name, vote count, and percentage of votes to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine if the votes is greater than the winning count.
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #And, set the winning_candiate equal to the candidate's name
            winning_candidate = candidate_name

        #To do: print out the winning candidate, vote count and percentage to terminal
        winning_candiate_summary=(
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

        print(winning_candiate_summary)
        

