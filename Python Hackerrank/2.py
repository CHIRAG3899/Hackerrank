#Task
#Given an integer, , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of  2 to 5 , print Not Weird
#If n is even and in the inclusive range 6 of 20 to , print Weird
#If n is even and greater than 20 , print Not Weird

#Input Format
#A single line containing a positive integer, .

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 or 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird') 
