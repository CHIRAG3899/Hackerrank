#Function Description
#Complete the factorial function in the editor below. Be sure to use recursion.
#factorial has the following paramter:
#int n: an integer
#Returns
#int: the factorial of n
#Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .
#Input Format
#A single integer,  (the argument to pass to factorial).

#!/bin/python3

import math
import os
import random
import re
import sys

def factorial(n):
    if n<=1:
        return 1
    else:
        return (n*factorial(n-1)) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
