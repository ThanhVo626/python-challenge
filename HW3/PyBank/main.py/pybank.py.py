# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:23:47 2023

@author: Tommy Vo
"""
import os
import csv

csvpath= os.path.join("..","Resources","budget_data.csv")
'Variables to hold and store values to do calculations later on'
i=0
j=0
k=0
l=0
w=0
x=0
y=0
z=0
a=0
b=0
' Accessing the resouces files and splitting the months/year from the Profits with ,'
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    'skipping the header/title so it doesnt mess up our data collection'
    next (csvfile)
    
    'Going through each row of the csvfile and collecting the infromation we need for later calculations'
    for row in csvreader:
        'w adds profit for total'
        w = int(row[1]) + w
        'x is for total months'
        x = x + 1
        'y is for current profit'
        y = int(row[1])
        if z != 0:
            'i is for change in profit'
            i = y - z
        'j is for total change in profit in order to get average change'
        j = j + i
        'z is for previous profit to calculate average change'
        z = y
        'check for greatest increase profit'
        if i > k :
            k = i
            'store the month/year of gip'
            a = row[0]
        'check for great decrease profit'
        if i < l :
            l = i
            'store the month/year of gdp'
            b = row[0]

'round average change so its not 10 extra decimal points'
Rounded_Average= round(j/(x-1),2)
      
        
'Print all the Values we are looking for and converting them into strings'  

print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(x))
print('Total: $'+ str(w))
print("Average Change: $" + str(Rounded_Average))
print('Greatest Increase in Profits: ' + a + ' $' + str(k))
print('Greatest Decrease in Profits: ' + b + ' $' + str(l))
'exporting all the values into seperate file'
output_file = os.path.join("../analysis/pybank_final.csv")
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(['----------------------------'])
    writer.writerow(['Total Months: ' + str(x)])
    writer.writerow(['Total: $'+ str(w)])
    writer.writerow(["Average Change: $" + str(Rounded_Average)])
    writer.writerow(['Greatest Increase in Profits: ' + a + ' $' + str(k)])
    writer.writerow(['Greatest Decrease in Profits: ' + b + ' $' + str(l)])
                    
    

    
