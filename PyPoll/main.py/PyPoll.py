import os
import csv

# Path to the CSV file
election_data_csv = os.path.join("..", "Resources", "election_data.csv")

#define the data that is storing as the parameter
def calculate_votes_total(election_data):

    #declare where the variables will be stored
    total_votes = 0
    candidates_votes = {}
    unique_ballots = set()  
      
    # Open the CSV file and skip the header as there is a header in the csv file
    with open(election_data, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        header = next(csv_reader)

        # Go over the rows where variables are stored 
        for row in csv_reader:
            ballot_id = row[0]
            candidate = row[2]

        #Calculate the total votes 
            if ballot_id not in unique_ballots:
                unique_ballots.add(ballot_id)
                total_votes += 1
                if candidate in candidates_votes:
                    candidates_votes[candidate] += 1
                else:
                    candidates_votes[candidate] = 1
    
    #Find the percentage of the total votes that each candidate received


    # Find the candidate with the maximum votes
    winner = max(candidates_votes, key=candidates_votes.get)
    max_votes = candidates_votes[winner]

    # Print the results
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    for candidate, (votes) in candidates_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

# Call the function with the path to the CSV file
calculate_votes_total(election_data_csv)

