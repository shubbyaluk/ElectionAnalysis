#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

#Open the election results and read the file
with open(file_to_load) as election_data:

    #Create a filename variable to a direct or indirect path to the file
    file_to_save = os.path.join("Analysis","election_analysis.txt")

# Using the with statement open the file as a text file.
    with open (file_to_load) as election_data:
    
    #To do: read and analyse the data here
        file_reader = csv.reader(election_data)

    #Read and print the header row
        headers = next(file_reader)
        print (headers)


