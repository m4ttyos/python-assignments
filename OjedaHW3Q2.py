#set a constant for how many rows and columsn there will be(country=rows, medals=columns)
COUNTRIES = 5
MEDALS = 3
#create the list with the country names
countries = ["USA",
             "China",
             "Russia",
             "Spain",
             "UK"]
#create a list of the medal counts
counts = [
    [5, 6 ,3],
    [4, 7, 3],
    [3, 2, 1],
    [2, 1, 2],
    [1, 1, 1]
    ]
#make a seperate list for total rows
totalRow=[5,6,3,4,7,3,3,2,1,2,1,2,1,1,1]
#print the table header
print("%10s%8s%8s%8s%8s" %("Country", "Gold", "Silver", "Bronze", "Total"))
#now to print the countries, counts, and row totals
for i in range (COUNTRIES):
    print("%10s" %countries[i], end="")
    
    #print each row element and get the totals
    total = 0
    for j in range (MEDALS):
        print("%7d" %counts[i][j], end="")
        total= total + counts[i][j]
    #Show the row totals
    print("%10s" %total)
#Show column totals
print("%10s" %("Total"), end="")
for j in range (MEDALS):
    sumColumn = 0
    for i in range (COUNTRIES):
        sumColumn = sumColumn + counts[i][j]
    print("%7d" %sumColumn, end="")
addedQ = 0
addedQ = sum(totalRow)
print("%10d" %addedQ)

#print average
print("%10s" %("Average"), end="")
#create a function for finding average
def medalAvg(totalN, number):
    avg= float(totalN / number)
    return avg
addedAvg = float(medalAvg(addedQ, COUNTRIES))
for m in range (MEDALS):
    sumColumn=0
    for p in range (COUNTRIES):
        sumColumn = sumColumn + counts[p][m]
        average= float(medalAvg(sumColumn, COUNTRIES))
    print("%8.2f" %average, end="")
print("%7.2f" %addedAvg)
        




    
