from csv import *
from textblob import TextBlob
from statistics import *

#import csv file
infile = open('applebees.csv', 'r')
#to be able to read it, have a csv reader
csvReader = reader(infile, delimiter=',')

#have stars and text be able to be read from csv and be put into a list
stars=[]
text=[]

i=0
for row in csvReader:
    if i>0:
        star= float(row[6])
        stars.append(star)
        
#get the polarity from the text in each row
        textReview=(row[8])
        b=TextBlob(textReview)
        polarity=b.sentiment.polarity
        text.append(polarity)

#make sure the list will keep going till the end
    i = i + 1
#print to make the list for stars and the polarity for the text
print(stars)
print(text)

infile.close()
#make a function for finding average of stars
def avgStars (stars):
    starRating=0
    total=0
    for i in stars:
        starRating= starRating +i
        total=total + 1
    avg= starRating / total
    return avg
starsAvg=avgStars(stars)
print("The stars average is: ", "%.2f" %starsAvg)

#make a function for stars min
def starsMin (stars):
    min_value= None
    for i in stars:
        if not min_value:
            min_value = i
        elif i < min_value:
            min_value = i
    return min_value
minimumStars=starsMin(stars)
print("The minimum rating for stars is: ", minimumStars)
#Find the max rating of stars
def starsMax (stars):
    max_value= None
    for i in stars:
        if not max_value:
            max_value = i
        elif i > max_value:
            max_value = i
    return max_value
maximumStars=starsMax(stars)
print("The max rating of stars are: ", maximumStars)
#find the range between the highest and lowest rated star while using a function
def starsRange (stars):
    min_value= None
    for i in stars:
        if not min_value:
            min_value = i
        elif i < min_value:
            min_value = i
    max_value= None
    for i in stars:
        if not max_value:
            max_value = i
        elif i > max_value:
            max_value = i
    rangedValue = max_value - min_value
    return rangedValue
rangeStars = starsRange (stars)
print("The range of star rating is: ", rangeStars)
#find the standard deviation of the stars
starsStdev = stdev(stars)
print("The standard deviation for stars is: ", "%.2f" %starsStdev)

#make a function for finding the average polarity
def avgPolarity (text):
    total=0
    polNum=0
    for i in text:
        total=total+1
        polNum=polNum+i
    avg=polNum/total
    return avg
polarityAvg=avgPolarity(text)
print("The polarity average is: ", "%.2f" %polarityAvg)
#make function for polarity min
def polMin (text):
    min_value= None
    for i in text:
        if not min_value:
            min_value = i
        elif i < min_value:
            min_value = i
    return min_value
minimumPol = polMin(text)
print("The minimum rating for polarity is: ", "%.2f" %minimumPol)
#make a function to find max polarity rating
def polMax (text):
    max_value= None
    for i in text:
        if not max_value:
            max_value = i
        elif i > max_value:
            max_value = i
    return max_value
maximumPol = polMax(text)
print("The maximum rating for polarity is: ", "%.2f" %maximumPol)
#find the range between the highest and lowest rating polarity while using a function
def polRange (text):
    min_value= None
    for i in text:
        if not min_value:
            min_value = i
        elif i < min_value:
            min_value = i
    max_value= None
    for i in text:
        if not max_value:
            max_value = i
        elif i > max_value:
            max_value = i
    rangedValue = max_value - min_value
    return rangedValue
rangePol = polRange (text)
print("The range of polarity is: ", "%.2f" %rangePol)
#find the standard deviation of the polarity from the text
polStdev = stdev(text)
print("The standard deviation for polarity is: ", "%.2f" %polStdev)





    
    
