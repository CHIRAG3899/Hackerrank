#Context
#Given a 6X6 2D Array,A :

#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0
#We define an hourglass in A to be a subset of values with indices falling in
#this pattern in A's graphical representation:

#a b c
#  d
#e f g
#There are 16 hourglasses in A, and an hourglass sum is the sum of an
#hourglass' values.
#Task
#Calculate the hourglass sum for every hourglass in A, then print the maximum
#hourglass sum.
#Example
#In the array shown above, the maximum hourglass sum is 7 for the hourglass in
#the top left corner.
#Input Format
#There are 6 lines of input, where each line contains 6 space-separated
#integers that describe the 2D Array .
#Output Format
#Print the maximum hourglass sum in A.

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        res = []

    for x in range(0, 4):
        for y in range(0, 4):
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            res.append(s)
            
    print(max(res))
