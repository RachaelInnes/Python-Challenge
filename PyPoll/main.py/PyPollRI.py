import os
import csv

# Path to the CSV file
election_data_csv = os.path.join("..", "Resources", "election_data.csv")

# Initialize the data and data structures to store the values
def voting_information(file_path):
    election_data = {
        'Total_Votes_Cast': 0,
        'Candidate_Names': set(),
        'Votes_Per_Candidate': {},
        'Winner_Election': None
    }

    # Read the CSV file, skip the header row as the file has a header
    with open(file_path, mode='r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)  

        # Loop through each row in the file to undertake each of the following functions
        for row in csvreader:
            ballot_id = row[0]
            county = row[1]
            candidate = row[2]

            # For each row add to the votes from the row before 
            election_data['Total_Votes_Cast'] += 1

            # Add candidate to the set of candidate names, add the candidate to the set of candidate names as per dictionary
            election_data['Candidate_Names'].add(candidate)

            # Count votes for each candidate by checking the candidate in each row, if the next row is the same then add to the value for that candidate, if not, add it to the matching candidate
            if candidate not in election_data['Votes_Per_Candidate']:
                election_data['Votes_Per_Candidate'][candidate] = 0
            election_data['Votes_Per_Candidate'][candidate] += 1

    # Calculate percentage votes for each candidate using a place to store this by checking the candidate votes in the votes per candidate and divide by total votes * 100 to get percentage value
    percentages = {}
    for candidate, votes in election_data['Votes_Per_Candidate'].items():
        percentages[candidate] = (votes / election_data['Total_Votes_Cast']) * 100

    # Determine the winner by going through the votes of each candidate in the election data and find the maximum value to find the winner
    if election_data['Votes_Per_Candidate']:
        winner = max(election_data['Votes_Per_Candidate'], key=election_data['Votes_Per_Candidate'].get)
        election_data['Winner_Election'] = winner

    # Print out the results
    print("Election Results")
    print("                            ")
    print("---------------------------")
    print("                            ")
    print(f"Total Votes: {election_data['Total_Votes_Cast']}")
    print("                            ")
    print("---------------------------")
    for candidate, votes in election_data['Votes_Per_Candidate'].items():
        print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
    print("                            ")
    print("---------------------------")
    print("                            ")
    print(f"Winner: {election_data['Winner_Election']}")
    print("                            ")
    print("---------------------------")

# Call the function with the CSV file path
voting_information(election_data_csv)

