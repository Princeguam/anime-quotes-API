#CODE TO CONVERT JSON TO CSV

# import json
# import csv

# # Define the input JSON file and output CSV file names
# input_file = 'dataset.json'
# output_file = 'dataset_output.csv'

# # Open and read the JSON file
# with open(input_file, 'r') as json_file:
#     data = json.load(json_file)

# # Ensure the JSON data is a list of dictionaries (rows)
# if isinstance(data, dict):
#     # If the JSON data is a dictionary, convert it to a list of dictionaries
#     data = [data]

# # Extract the field names (keys) for the CSV header
# fieldnames = set()
# for entry in data:
#     fieldnames.update(entry.keys())

# # Write data to a CSV file
# with open(output_file, 'w', newline='') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)

# print(f"JSON data has been converted to CSV and saved to {output_file}")


























#CODE TO CONVERT CSV TO JSON

import csv
import json

def csv_to_json(csv_path, json_path):
    """
    Convert CSV file to JSON file.
    
    Args:
        csv_file (str): Path to the input CSV file.
        json_file (str): Path to the output JSON file.
    """
    # Read CSV file and convert to list of dictionaries
    with open(csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    
    # Write JSON data to file
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



csv_path = r'dataset_output.csv'
json_path = r'dataset_output.json'

csv_to_json(csv_path, json_path)


















#CODE TO REMOVE PARENTHESIS FROM A FIELD IN A CSV FILE USING REGULAR EXPRESSION MODULE AND CSV MODULE

# import csv
# import re

# # Function to remove parentheses from a string
# def remove_parentheses(text):
#     return re.sub(r'[()]', '', text)

# # Specify the input and output file names
# input_file = 'quotes.csv'
# output_file = 'quotes_output.csv'

# # Open the input CSV file for reading
# with open(input_file, 'r', newline='') as infile:
#     reader = csv.DictReader(infile)
#     fieldnames = reader.fieldnames

#     # Open the output CSV file for writing
#     with open(output_file, 'w', newline='') as outfile:
#         writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#         writer.writeheader()

#         # Process each row
#         for row in reader:
#             # Modify the specific field
#             row['Anime'] = remove_parentheses(row['Anime'])
#             writer.writerow(row)

# print(f"Processed CSV saved to {output_file}")
