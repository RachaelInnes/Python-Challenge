import os
import csv

#Open and read the CSV from the path
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")


 # Initialize variables and data structures
def calculate_financial_totals(file_path):
  
    financial_information = {
        'Total_Months': 0,
        'Total_Profit_Loss': 0,
        'Greatest_Increase_In_Profits': ('', float('-inf')),
        'Greatest_Decrease_In_Profits': ('', float('inf')),
        'Average_Change': 0
    }
    changes = []
    previous_profit_loss = None

    # Read the CSV file, file has a header, skip first row 
    with open(file_path, mode='r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader) 
    
    #set where each value is in the csv file
        for row in csvreader:
            date = row[0]
            current_profit_loss = int(row[1])

            # Update the total months and total profit/loss by looking at the months and then adding/subtracting amount of the previous value
            financial_information['Total_Months'] += 1
            financial_information['Total_Profit_Loss'] += current_profit_loss

            # Calculate the monthly change and track it
            if previous_profit_loss is not None:
                change = current_profit_loss - previous_profit_loss
                changes.append(change)

                # Formula to calcuate the greatest increase in profits, look the value in each row, if there is a change look to see if it is equal or greater than previous value
                if change > financial_information['Greatest_Increase_In_Profits'][1]:
                    financial_information['Greatest_Increase_In_Profits'] = (date, change)

                # Forumala to calculate the greatest decrease in profits,look at the value in each row, if there a change look to see if is is equal or less than the previous row
                if change < financial_information['Greatest_Decrease_In_Profits'][1]:
                    financial_information['Greatest_Decrease_In_Profits'] = (date, change)

            # Set the previous profit/loss for the next iteration
            previous_profit_loss = current_profit_loss

        # Formula to calculate the average change by looking at the CSV file, and then the results are equal to the sum/changes is the average
        if changes:
            financial_information['Average_Change'] = sum(changes) / len(changes)

    # Print out the results stored in the dictionary
    print(f"Financial Analysis")
    print(                               )
    print(f"----------------------------")
    print(                               )
    print(f"Total Months: {financial_information['Total_Months']}")
    print(                               )
    print(f"Total: ${financial_information['Total_Profit_Loss']:}")
    print(                               )
    print(f"Average Change: ${financial_information['Average_Change']:,.2f}")
    print(                               )
    print(f"Greatest Increase in Profits: {financial_information['Greatest_Increase_In_Profits'][0]} (${financial_information['Greatest_Increase_In_Profits'][1]})")
    print(                               )
    print(f"Greatest Decrease in Profits: {financial_information['Greatest_Decrease_In_Profits'][0]} (${financial_information['Greatest_Decrease_In_Profits'][1]})")

# Call the function with the CSV file path
calculate_financial_totals(budget_data_csv)


# Example data for testing
financial_information = {
    'Total_Months': 12,
    'Total_Profit_Loss': 1234567,
    'Average_Change': 12345.67,
    'Greatest_Increase_In_Profits': ('Aug-16', 1862002),
    'Greatest_Decrease_In_Profits': ('Feb-14', -1825558)
}

# Define the data to be written to the text file
data = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {financial_information['Total_Months']}",
    f"Total: ${financial_information['Total_Profit_Loss']:,.0f}",
    f"Average Change: ${financial_information['Average_Change']:,.2f}",
    f"Greatest Increase in Profits: {financial_information['Greatest_Increase_In_Profits'][0]} (${financial_information['Greatest_Increase_In_Profits'][1]})",
    f"Greatest Decrease in Profits: {financial_information['Greatest_Decrease_In_Profits'][0]} (${financial_information['Greatest_Decrease_In_Profits'][1]})"
]

# Specify the file name
txt_file = "test_financial_analysis.txt"

# Write data to text file
with open(txt_file, mode='w') as file:
    for line in data:
        file.write(line + "\n")

print(f"Test text file '{txt_file}' generated successfully.")
#export the results to a text file 
txt_file = "test_financial_analysis.txt"

