# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:36:49 2019

@author: Matthew
"""

from datetime import datetime
import matplotlib.pyplot as plt
import csv

filename = r"CSV Files\activity3.csv"

intervaler, stepper = [], []
intervaler2, stepper2 = [], []
minuteintervaldata = {}
minuteintervaldata2 = {}
missing_data_count, no_of_days = 0, 0
no_of_days2 = 0 

with open(filename) as file:
    
    thefile = csv.reader(file)
    headerRow = next(thefile)
    hold_steps = 0
    prev_date = ""
    
    for row in thefile:
        if row[3] == "Weekday":
            try:
                current_date = datetime.strptime(row[1], "%Y-%m-%d").date()
                current_interval = eval(row[2])
                steps_datum = eval(row[0])
            except:
                missing_data_count += 1
            else:
                if prev_date != current_date:
                    prev_date = current_date
                    no_of_days += 1
                minuteintervaldata[current_interval] = minuteintervaldata.get(current_interval, 0) + steps_datum
                
        else:
            try:
                current_date = datetime.strptime(row[1], "%Y-%m-%d").date()
                current_interval = eval(row[2])
                steps_datum = eval(row[0])
            except:
                missing_data_count += 1
            else:
                if prev_date != current_date:
                    prev_date = current_date
                    no_of_days2 += 1
                minuteintervaldata2[current_interval] = minuteintervaldata2.get(current_interval, 0) + steps_datum
            
    file.close()
    
for interval, steps in minuteintervaldata.items():
    haha = steps / no_of_days
    intervaler.append(interval)
    stepper.append(haha)

fig = plt.figure(dpi=80, figsize=(12, 7))
plt.bar(intervaler, stepper, color='green')
plt.title("Steps Taken in 2 Months (5-Minute Interval, Weekdays Only)")
plt.xlabel("Time")
plt.ylabel("Average of the eNumber of Steps Taken")
fig.autofmt_xdate()

plt.show()
plt.clf()

for interval, steps in minuteintervaldata2.items():
    haha = steps / no_of_days2
    intervaler2.append(interval)
    stepper2.append(haha)

fig = plt.figure(dpi=80, figsize=(12, 7))
plt.bar(intervaler2, stepper2, color='green')
plt.title("Steps Taken in 2 Months (5-Minute Interval, Weekends Only)")
plt.xlabel("Time")
plt.ylabel("Average of the Number of Steps Taken")
fig.autofmt_xdate()

plt.show()
plt.clf()

print("The number of missing data:", missing_data_count)
