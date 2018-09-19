
import csv

# open file

devices = {}
with open('devices.csv', 'rb') as f:
    reader = csv.reader(f)

    # read file row by row
    for row in reader:
        device = row[0] + ':' + row[1]
        user
        devices{}

