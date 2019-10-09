# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:36:49 2019

@author: Matthew
"""

from datetime import datetime
import matplotlib.pyplot as plt
import csv

filename = r"CSV Files\activity.csv"

intervaler, stepper = [], []
minuteintervaldata = {}
missing_data_count, no_of_days, max_steps = 0, 0, 0
intervalchosen = ""

with open(filename) as file:
    
    thefile = csv.reader(file)
    headerRow = next(thefile)
    hold_steps = 0
    prev_date = ""
    
    for row in thefile:
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
            
    file.close()
    
for interval, steps in minuteintervaldata.items():
    haha = steps / no_of_days
    if haha > max_steps:
        intervalchosen = interval
        max_steps = haha
    intervaler.append(interval)
    stepper.append(haha)

fig = plt.figure(dpi=80, figsize=(12, 7))
plt.bar(intervaler, stepper, color='green')
plt.title("Steps Taken in 2 Months (5-Minute Interval)")
plt.xlabel("Time")
plt.ylabel("Average of the Number of Steps Taken")
fig.autofmt_xdate()

plt.show()

print("The number of missing data:", missing_data_count)
print("Most steps are taken at %i." %intervalchosen)
