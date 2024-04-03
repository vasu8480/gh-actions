# Example script to generate test data
import csv

data = [
    {"id": 3, "name": "Bob"},
    {"id": 4, "name": "Emma"}
]

with open("sample_data.csv", "a", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["id", "name"])
    
    # Print field names
    print("Field names:", writer.fieldnames)
    
    writer.writeheader()  # Write header if file is empty
    for item in data:
        writer.writerow(item)

print("Test data generated successfully.")
