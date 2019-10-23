# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:19:27 2019

@author: Matthew
"""
import numpy
from operator import itemgetter

def ShowFileData(file, staffsList = None):
    
    if staffsList == None:
        staffsList = GetStaffsList(file)
        staffsList = sorted(staffsList,key=itemgetter(1))
            
        for staff in staffsList:
            print("|" + staff[0], "|" + staff[1], "|" + staff[2], "|" + staff[3])
            
    else:
        staffsList = sorted(staffsList,key=itemgetter(1))
        for staff in staffsList:
            print("|" + staff[0], "|" + staff[1], "|" + staff[2], "|" + staff[3])

def WriteNewRecord(file, staffsList):
    
    with open(file, "w") as fileName:
        for staff in staffsList:
            fileName.write(str(staff[0]) + "#" + str(staff[1]) + "#" + str(staff[2]) + "#" + str(staff[3]) + "\n")
                           
        fileName.close()
    
def GetIDListInList(file, staffsList = None):
    
    IDList = list()
    
    if staffsList == None:
        with open(file) as filename:
            content = filename.readlines()
            for line in content:
                line = line.rstrip().split("#")
                IDList.append(line[0])
                
            filename.close()
    else:
        for staff in staffsList:
            IDList.append(staff[0])
    
    return IDList

def GetStaffsList(file):
    
    StaffsList = list()
    
    with open(file) as filename:
        content = filename.readlines()
        for line in content:
            line = line.rstrip().split("#")
            StaffsList.append([line[0], line[1], line[2], line[3]])
            
        filename.close()
            
    return StaffsList
    
def AddStaff(fileName, StaffsList):
    
    while True:
        staffId = input("Input Staff ID: ")
        if len(staffId) != 5:
            print("Staff IDs must contain only 5 characters.")
            continue
        if staffId.startswith("S") == False:
            print("Staff IDs must start with a capital \"S\"")
            continue
        if not staffId[1:].isdigit():
            print("The 2nd to 5th characters must be only numbers.")
            continue
        
        if staffId in GetIDListInList(fileName, staffsList):
            print("That staff ID is already occupied. Try again.")
            continue
        
        break #SUCCESS
            
    while True:
        staffName = input("Input Staff Name: ")
        if len(staffName) <= 20:
            break
        else:
            print("The name is too long. Try again!")
            
    while True:
        staffPosition = input("Input Staff Position: ").title()
        try:
            if ["Staff", "Officer", "Manager"].index(staffPosition) >= 0:
                break
        except ValueError:
            print("There is no such a position.")
            
    while True:
        staffSalary = eval(input("Input Staff Salary: "))
        if staffPosition == "Staff" and 3500000 <= staffSalary <= 7000000:
            print("Confirmed.")
            break
        elif staffPosition == "Officer" and 7000001 <= staffSalary <= 10000000:
            print("Confirmed.")
            break
        elif staffPosition == "Manager" and staffSalary > 10000000:
            print("Confirmed.")
            break
        else:
            print("Staffs' Salary must be from 3,500,000 to 7,000,000.\n"
                  "Officers' Salary must be from 7,000,001 to 10,000,000.\n"
                  "Managers' Salary must be higher than 10,000,000.")
    
    StaffsList.append([staffId, staffName, staffPosition, str(staffSalary)])
    
    return StaffsList
    
def DeleteStaff(fileName, StaffsList):
    
    staffId = input("Input the ID of the staff you want to delete: ")
    
    IDList = GetIDListInList(fileName, StaffsList)
    
    try:
        index = IDList.index(staffId)
    except ValueError:
        print("That Staff ID doesn't exist.")
    else:
        if index >= 0:
            StaffsList.pop(index)
    finally:
        return StaffsList
        
def ViewSummaryData(StaffsList):
    
    listOfStaffs = [eval(x[3]) for x in StaffsList if x[2] == "Staff"]
    listOfOfficers = [eval(x[3]) for x in StaffsList if x[2] == "Officer"]
    listOfManagers = [eval(x[3]) for x in StaffsList if x[2] == "Manager"]
    
    print ("\n1. Staff\n")
    print ("Minimum Salary:", min(listOfStaffs))
    print ("Maximum Salary:", max(listOfStaffs))
    print ("Average Salary:", int(numpy.average(listOfStaffs)))
    
    print ("\n2. Officer\n")
    print ("Minimum Salary:", min(listOfOfficers))
    print ("Maximum Salary:", max(listOfOfficers))
    print ("Average Salary:", int(numpy.average(listOfOfficers)))
    
    print ("\n3. Manager\n")
    print ("Minimum Salary:", min(listOfManagers))
    print ("Maximum Salary:", max(listOfManagers))
    print ("Average Salary:", int(numpy.average(listOfManagers)))
    
    print ("\n")
    
    return StaffsList
    
def ShowMenu():
    msgToShow = """
                1. New Staff
                2. Delete Staff
                3. View Summary Data
                4. Save and Exit
                """
    print ("\n".join(map(str, (a.strip() for a in msgToShow.splitlines()))))

#PROGRAM DRIVE
fileName = "Text Files\data.txt"
staffsList = GetStaffsList(fileName)

while True:
    print("\n")
    ShowFileData(fileName, staffsList)
    ShowMenu()
    
    userChoice = input("Which of the following menus do you want to access? ")
    
    if userChoice == "1":
        staffsList = AddStaff(fileName, staffsList)
    elif userChoice == "2":
        staffsList = DeleteStaff(fileName, staffsList)
    elif userChoice == "3":
        staffsList = ViewSummaryData(staffsList)
    elif userChoice == "4":
        WriteNewRecord(fileName, staffsList)
        break
    else:
        print ("Invalid input!")
        
        