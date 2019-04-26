import csv

with open('subtlex-pl.csv', encoding='utf-8') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		print(row[0])

##
##import csv
##
##with open('subtlex-pl.csv', encoding='utf-8') as csvfile:
##    readCSV = csv.reader(csvfile, delimiter=',')
##
##    words = []
##    
##    for row in readCSV:
##        word = row[1]
##
##        words.append(word)
##
##    print(words)
