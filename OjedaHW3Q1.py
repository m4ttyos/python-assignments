from statistics import *
#start by asking how many students will you be inputting grades for
noStdts = int(input("Enter number of students: "))

#Ask for input of hw1
hw1Grades=[]
for i in range (noStdts):
    hw1Input = float(input("Enter Grade for student no." +str(i)+ " for Hw 1 out of 20 (Enter -1 to stop): "))
    hw1Grades.append(hw1Input)
    if hw1Input<0:
        hw1Grades.pop(i)
        break
    elif hw1Input>20 or hw1Input==str:
        print("Invalid entry")

#ask for input of hw2
hw2Grades=[]
for i in range (noStdts):
    hw2Input = float(input("Enter Grade for student no." +str(i)+ " for Hw 2 out of 20 (Enter -1 to stop): "))
    hw2Grades.append(hw2Input)
    if hw2Input<0:
        hw2Grades.pop(i)
        break
    elif hw2Input>20 or hw2Input==str:
        print("Invalid entry")

#Ask for input of hw3
hw3Grades=[]
for i in range (noStdts):
    hw3Input = float(input("Enter Grade for student no." +str(i)+ " for Hw 3 out of 20 (Enter -1 to stop): "))
    hw3Grades.append(hw3Input)
    if hw3Input<0:
        hw3Grades.pop(i)
        break
    elif hw3Input>20 or hw3Input==str:
        print("Invalid entry")

#Ask for input of Midterm
midtermGrades=[]
for i in range (0, noStdts):
    midInput = float(input("Enter Grade for student no." +str(i)+ " for Midterm exam out of 20 (Enter -1 to stop): "))
    midtermGrades.append(midInput)
    if midInput<0:
        midtermGrades.pop(i)
        break
    elif midInput>20 or midInput==str:
        print("Invalid entry")

#Ask for input of final exam
finalGrades=[]
for i in range (0, noStdts):
    finalInput = float(input("Enter Grade for student no." +str(i)+ " for final exam out of 20 (Enter -1 to stop): "))
    finalGrades.append(finalInput)
    if finalInput<0:
        finalGrades.pop(i)
        break
    elif finalInput>20 or finalInput==str:
        print("Invalid entry")
#Create some space
print()
#Create a list within a list
workbook = [hw1Grades, hw2Grades, hw3Grades, midtermGrades, finalGrades]
#You can use the statistics library for these calculations
#Find mode with function
def mode(listTitle):
    listTitle.sort()
    counter=0
    modes=0
    for i in listTitle:
        if listTitle.count(i)>counter:
            counter=listTitle.count(i)
            modes=i
    return modes
#find average for hw1 
hw1Avg = mean(hw1Grades)
#find the min of hw1 
minHw1 = min(hw1Grades)
#max for hw1
maxHw1 = max(hw1Grades)
#find median for hw1, have to sort first
hw1Grades.sort()
medHw1 = median(hw1Grades)
#find mode for hw1
modeHw1 = mode(hw1Grades)
#find std dev from hw1
hw1Stdev = stdev(hw1Grades)

#find average for hw2 
hw2Avg = mean(hw2Grades)
#find the min of hw2 
minHw2 = min(hw2Grades)
#max for hw2
maxHw2 = max(hw2Grades)
#find median for hw2, have to sort first
hw2Grades.sort()
medHw2 = median(hw2Grades)
#find mode for hw2
modeHw2 = mode(hw2Grades)
#find std dev from hw2
hw2Stdev = stdev(hw2Grades)

#find average for hw3 
hw3Avg = mean(hw3Grades)
#find the min of hw3 
minHw3 = min(hw3Grades)
#max for hw3
maxHw3 = max(hw3Grades)
#find median for hw3, have to sort first
hw3Grades.sort()
medHw3 = median(hw3Grades)
#find mode for hw3
modeHw3 = mode(hw3Grades)
#find std dev from hw3
hw3Stdev = stdev(hw3Grades)

#find average for midterm 
midAvg = mean(midtermGrades)
#find the min of midterm 
minMid = min(midtermGrades)
#max for midterm
maxMid = max(midtermGrades)
#find median for midterm, have to sort first
midtermGrades.sort()
medMid = median(midtermGrades)
#find mode for midterm
modeMid = mode(midtermGrades)
#find std dev from midterm
midStdev = stdev(midtermGrades)

#find average for final 
finAvg = mean(finalGrades)
#find the min of midterm 
minFin = min(finalGrades)
#max for midterm
maxFin = max(finalGrades)
#find median for midterm, have to sort first
finalGrades.sort()
medFin = median(finalGrades)
#find mode for midterm
modeFin = mode(finalGrades)
#find std dev from midterm
finStdev = stdev(finalGrades)

#Organize the mean,median,mode,max,min, and std dev neatly to be displayed
print("%27s%10s%10s%12s%10s" %("Hw1", "Hw2", "Hw3", "Midterm", "Final"))
print("Average: ", end="")
print("%20.2f%10.2f%10.2f%10.2f%10.2f" %(hw1Avg, hw2Avg, hw3Avg, midAvg, finAvg))
print("Minimum: ", end="")
print("%20.2f%10.2f%10.2f%10.2f%10.2f" %(minHw1, minHw2, minHw3, minMid, minFin))
print("Maximum: ", end="")
print("%20.2f%10.2f%10.2f%10.2f%10.2f" %(maxHw1, maxHw2, maxHw3, maxMid, maxFin))
print("Median: ", end="")
print("%21.2f%10.2f%10.2f%10.2f%10.2f" %(medHw1, medHw2, medHw3, medMid, medFin))
print("Mode: ", end="")
print("%23.2f%10.2f%10.2f%10.2f%10.2f" %(modeHw1, modeHw2, modeHw3, modeMid, modeFin))
print("Std Dev: ", end="")
print("%20.2f%10.2f%10.2f%10.2f%10.2f" %(hw1Stdev, hw2Stdev, hw3Stdev, midStdev, finStdev))




