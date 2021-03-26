import csv

entry = "test.csv"

fields = []
rows = []
with open(entry, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

for row in rows[:4]:
    # parsing each column of a row
   
        print(row[0])
    