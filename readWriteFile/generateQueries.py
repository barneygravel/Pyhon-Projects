import csv

#CSV Delimiter
csvDelimiter =','

#Query constants
query1 = 'INSERT INTO student (id, name) VALUES ('
query2 = ', \''
query3 = '\');'

#Output File Object
f= open("queries.txt","w+")

#Open Input CSV file in read mode
with open('inputValues.csv', 'r') as csvfile:
	readCSV = csv.reader(csvfile, delimiter= csvDelimiter)
	for row in readCSV:
		output = query1 + row[0] + query2 + row[1] + query3
		#print(output)
		f.write(output)
		f.write('\n')
		
		
#Close the File Objects
f.close()
csvfile.close()