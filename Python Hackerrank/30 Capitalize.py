#You are asked to ensure that the first and last names of people begin with
#a capital letter in their passports. For example, alison heck should be
#capitalised correctly as Alison Heck.
#Given a full name, your task is to capitalize the name appropriately.
#Input Format
#A single line of input containing the full name,S .
#Note: in a word only the first character is capitalized. Example 12abc
#when capitalized remains 12abc.
#Output Format
#Print the capitalized string, .
#Sample Input
#chris alan
#Sample Output
#Chris Alan

import math
import os
import random
import re
import sys

def solve(s):
    res = ""
    spaceFlag = True
    for ch in s:
        if ch == " ":
            spaceFlag = True
        elif spaceFlag == True:
            spaceFlag = False
            if ch>='a' and ch<='z':
                ch = chr(ord(ch)-32)
        res+=ch
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
