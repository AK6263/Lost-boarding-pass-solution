# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:23:26 2020

@author: Abhay Kshirsagar

On a sold-out flight, 100 people line up to board the plane. The first 
passenger in the line has lost his boarding pass but was allowed in, 
regardless. He takes a random seat. Each subsequent passenger takes his 
or her assigned seat if available, or a random unoccupied seat, otherwise.
What is the probability that the last passenger to board the plane finds 
his seat unoccupied?

"""
import random

def sim():
    prev = [i for i in range(1,101)] 
    random.shuffle(prev)# the previously alloted seats
    shits_seat = random.choice(prev) # shit is our guy who takes a random seat
    taken = [shits_seat]# the shit takes the seat( index is no of the guy) 
    untaken = [i for i in prev if i != shits_seat]
    passenger = 2# we will start alloting from 2nd passenger
    while passenger <= 100:
        # if the passenger still has his seat empty he will get his
        # if not then a random seat will be alloted from untaken list
        if prev[passenger-1] not in taken:
            taken.append(prev[passenger-1])
            untaken = [i for i in untaken if i != prev[passenger-1]]
        else:
            k = random.choice(untaken)
            taken.append(k)
            untaken = [i for i in untaken if i != k]
        passenger +=1
    if taken[-1] == prev[-1]:
        return 1
    else:
        return 0
trials = 20000
results = [sim() for i in range(trials)]
print(sum(results) / trials)
        
