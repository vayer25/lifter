import csv

# Open the CSV file
with open('example.csv', mode='r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)
    
    # Skip the header (optional)
    next(csv_reader)
    
    # Read and print each row
    for row in csv_reader:
        print(row)
