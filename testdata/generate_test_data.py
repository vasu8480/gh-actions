# Example script to generate test data
import csv

data = [
    {"id": 3, "name": "Bob"},
    {"id": 4, "name": "Emma"}
]

with open("sample_data.csv", "a", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["id", "name"])
    for item in data:
        writer.writerow(item)

print("Test data generated successfully.")
