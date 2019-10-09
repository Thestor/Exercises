# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:53:27 2019

@author: Matthew
"""

from datetime import datetime
#import pygal
import matplotlib.pyplot as plt
import statistics
import csv

filename = r"CSV Files\activity.csv"

dates, steps_data, missing_data = [], [], []
missing_data_count = 0

with open(filename) as file:
    
    thefile = csv.reader(file)
    headerRow = next(thefile)
    hold_steps = 0
    prev_date = ""
    
    for row in thefile:
        try:
            current_date = datetime.strptime(row[1], "%Y-%m-%d").date()
            steps_datum = eval(row[0])
        except:
            missing_data_count += 1
            missing_data.append(current_date)
            steps_datum = 0
            if current_date == prev_date:
                hold_steps += 0
            else:
                dates.append(current_date)
                steps_data.append(hold_steps)
                prev_date = current_date
                hold_steps = 0
                hold_steps += 0
        else:
            if current_date == prev_date:
                hold_steps += steps_datum
            else:
                dates.append(current_date)
                steps_data.append(hold_steps)
                prev_date = current_date
                hold_steps = 0
                hold_steps += steps_datum
            
    file.close()
    
#n, bins, patches = plt.hist(x = dates, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    
#initializing dates list
#mpl_data = mdates.epoch2num(dates)

fig = plt.figure(dpi=100, figsize=(12, 7))
#fig, ax = plt.subplots(1,1)
plt.bar(dates, steps_data, color='green')
plt.title("Steps Taken in 2 Months")
plt.xlabel("Dates")
plt.ylabel("Number of Steps Taken")
fig.autofmt_xdate()

plt.savefig(r"Figures\Steps Per Day Graph 1.png")

#ax.xaxis.set_major_locator(mdates.YearLocator())
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%y'))

plt.show()

#maxfreq = n.max()
# Set a clean upper y-axis limit.
# plt.ylim(ymax=n.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

print("The number of missing data:", missing_data_count)

for i in range(len(steps_data)-1):
    print("The total number of steps taken (Day %i):" %(i+1), steps_data[i+1])
    
print("Average:", statistics.mean(steps_data))
print("Median:", statistics.median(steps_data))

