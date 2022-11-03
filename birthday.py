from random import random
from random import randrange
import numpy
import math

#create a set for finding matching birthdays
birthdays = set()
#create a sum of #people needed for a match, to be averaged across trials later.
hits = 0
#greater N for higher accuracy
N = 50000
#for loop for trials outside of for loop for matching birthdays
for trials in range(N):
    #nn is just number of people in the trial
    for nn in range(0,100):
        birthday = randrange(0,365)
        if birthday in birthdays:
            #subtract 1 because we're calling the 1st person the 0th,
            #and I don't know how to fix this directly :)
            hitsnew = hits + nn - 1
            hits = hitsnew
        #when we get a match, add nn to tally and reset loop.
            birthdays = set()
            #clear birthday list so other trials are not screwed
            break
        else:
            #if no match, add it to the list of distinct birthdays
            birthdays.add(birthday)
#this is the average number of people needed in the room to get a match
#meaning it is the number of people that corresponds to .5 probability
avgpeople = hits/N
print('the calculated average comes to:')
print(avgpeople)
answer = round(avgpeople)
print('therefore, the number of people needed to take the probability of a birthday match to 50% is:')
print(answer)
