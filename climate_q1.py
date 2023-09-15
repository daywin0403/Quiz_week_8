import matplotlib.pyplot as plt
import sqlite3

#Connect to the database
connection = sqlite3.connect(r'climate.db')

#Create cursor object
cursor = connection.cursor()

#Execute select query
cursor.execute("SELECT * FROM ClimateData")   

#Fetch the results from cursor
list = cursor.fetchall()

years = []
co2 = []
temp = []

#Iterate through list and append appropriate result
for r in list:
    years.append(r[0])
    co2.append(r[1])
    temp.append(r[2])

#close connection
connection.close()

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
plt.savefig("co2_temp_1.png") 

