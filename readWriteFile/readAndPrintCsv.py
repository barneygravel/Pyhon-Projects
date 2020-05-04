import csv

# open file in read mode
with open('inputValues.csv') as csvfile:
	# pass the file object to reader() to get the reader object
    readCSV = csv.reader(csvfile, delimiter=',')
	# Iterate over each row in the csv using reader object
    for row in readCSV:
		# row variable is a list that represents a row in csv
        print(row)
        print(row[0],row[1])