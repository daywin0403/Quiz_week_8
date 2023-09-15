import matplotlib.pyplot as plt
import pandas as pd
import openpyxl as op
import csv

#Read excel --- why were we taught about openpyxl when it doesn't open csv?

#sheet = op.load_workbook(r'climate.csv')

years = []
co2 = []
temp = []

#open the csv file and read it, append result by line
with open('climate.csv') as csvdata:
    reader = csv.reader(csvdata, delimiter=',')
    for r in reader:
        years.append(r[0])
        co2.append(r[1])
        temp.append(r[2])


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 