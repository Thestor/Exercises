# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:43:44 2019

@author: Matthew
"""

from datetime import datetime
#import pygal
import random
import csv

filename = r"CSV Files\activity2.csv"

dates, steps_data, intervals = [], [], []
missing_data_count = 0

def save_csv(steps_data, dates, intervals):
     with open(r"CSV Files\activity3.csv", "w", newline = '') as csvfile:
         data_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         
         data_writer.writerow(["steps", "'date'", "'interval', 'daykind'"])
         
         for i in range(len(steps_data)):
             daykind = dates[i].strftime("%A")
             if daykind in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                 daykind = "Weekday"
             else:
                 daykind = "Weekend"
                 
             data_writer.writerow([str(steps_data[i]), str(dates[i]), str(intervals[i]), str(daykind)])
             
         csvfile.close()
    
with open(filename) as file:
    
    thefile = csv.reader(file)
    headerRow = next(thefile)
    
    for row in thefile:
        try:
            steps_datum = eval(row[0])
        except:
            pass
        finally:
            current_date = datetime.strptime(row[1], "%Y-%m-%d").date()
            interval = eval(row[2])
            dates.append(current_date)
            steps_data.append(steps_datum)
            intervals.append(interval)
            
            
    file.close()
    
save_csv(steps_data, dates, intervals)