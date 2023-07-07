# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 02:18:12 2023

@author: Tommy Vo
"""
'variables I will use for storing data'
x=0
a=0
b=0
c=0 
i=0
j=0
k=0
'getting the information to sort'
import os
import csv
csvpath= os.path.join("..","Resources","election_data.csv")

with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    'skip header/first line'
    next (csvfile)

    for row in csvreader:
        'adding up total votes'
        x = x + 1
        'counting up the votes for each person'
        if row[2] == 'Charles Casper Stockham' :
            a = a + 1
        elif row[2] == 'Diana DeGette' :
            b = b + 1
        elif row[2] == 'Raymon Anthony Doane' :
            c = c + 1
'finding the percentage of votes and rounding them'           
i = round((a/x)*100,3)
j = round((b/x)*100,3)
k = round((c/x)*100,3)
'print out the values I need for outcomes'
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(x))
print('-------------------------')
print('Charles Casper Stockham: ' + str(i) + '% (' + str(a) + ")")
print('Diana DeGette: ' + str(j) + '% (' + str(b) + ')')
print('Raymon Anthony Doane: ' + str(k) + '% (' + str(c) + ')')
print('-------------------------')
'Deciding who is the winner'
if a > b and c :
    y = 'Winner: Charles Casper Stockham'
elif b > a and c :
    y = 'Winner: Diana DeGette'
elif c > b and a :
    y ='Winner: Raymon Anthony Doane'
print(y)
print('-------------------------')
'exporting the results into a seperate file'
output_file = os.path.join("../analysis/pypoll_final.csv")
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(['Election Results'])
    writer.writerow(['-------------------------'])
    writer.writerow(['Total Months: ' + str(x)])
    writer.writerow(['-------------------------'])
    writer.writerow(['Charles Casper Stockham: ' + str(i) + '% (' + str(a) + ")"])
    writer.writerow(['Diana DeGette: ' + str(j) + '% (' + str(b) + ')'])
    writer.writerow(['Raymon Anthony Doane: ' + str(k) + '% (' + str(c) + ')'])
    writer.writerow(['-------------------------'])
    writer.writerow([y])
    writer.writerow(['-------------------------'])
    

