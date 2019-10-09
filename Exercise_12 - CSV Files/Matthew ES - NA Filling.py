# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:01:01 2019

@author: Matthew
"""

from datetime import datetime
#import pygal
import random
import csv

filename = r"CSV Files\activity.csv"

dates, steps_data, intervals = [], [], []
missing_data_count = 0

def save_csv(steps_data, dates, intervals):
     with open(r"CSV Files\activity2.csv", "w", newline = '') as csvfile:
         data_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         
         data_writer.writerow(["steps", "'date'", "'interval'"])
         for i in range(len(steps_data)):
             data_writer.writerow([str(steps_data[i]), str(dates[i]), str(intervals[i])])
             
         csvfile.close()
    
with open(filename) as file:
    
    thefile = csv.reader(file)
    headerRow = next(thefile)
    
    for row in thefile:
        try:
            steps_datum = eval(row[0])
        except:
            missing_data_count += 1
            steps_datum = random.randint(0, 300)
        finally:
            current_date = datetime.strptime(row[1], "%Y-%m-%d").date()
            interval = eval(row[2])
            dates.append(current_date)
            steps_data.append(steps_datum)
            intervals.append(interval)
            
            
    file.close()
    
save_csv(steps_data, dates, intervals)

print("The number of missing data:", missing_data_count)
