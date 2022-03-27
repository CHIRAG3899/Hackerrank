#Given an array of integers, find the sum of its elements
#Function Description
#Complete the simpleArraySum function in the editor below.
#It must return the sum of the array elements as an integer.
#simpleArraySum has the following parameter(s):
#ar: an array of integers
#Input Format
#The first line contains an integer, , denoting the size of the array.
#The second line contains  space-separated integers representing the array's elements.

import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    sum1 = 0
    for i in range(len(ar)):
        sum1 = sum1 + ar[i]
    return sum1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
