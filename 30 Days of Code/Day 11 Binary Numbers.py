#Task
#Given a base-10 integer, n, convert it to binary (base-2). Then find
#and print the base-10 integer denoting the maximum number of consecutive 1's
#in n's binary representation. When working with different bases, it is common
#to show the base as a subscript.

#Example
#n=125
#The binary representation of 125 is 1111101. In base 10 , there are 5 and 1
#consecutive ones in two groups. Print the maximum,5 .

#Input Format
#A single integer,n .
#Output Format
#Print a single base-10 integer that denotes the maximum number of
#consecutive 1's in the binary representation of n.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    count = 0
    seq = []
    while n>0:
        if not n%2 == 0:
            count += 1
            seq.append(count)
            n = int(n/2)
        else:
            n = int(n/2)
            count = 0
    print(max(seq))
