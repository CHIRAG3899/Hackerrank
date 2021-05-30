#Task
#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price 
#being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.
#Function Description Complete the solve function in the editor below.

#solve has the following parameters:
#int meal_cost: the cost of food before tip and tax
#int tip_percent: the tip percentage
#int tax_percent: the tax percentage
#Returns The function returns nothing. Print the calculated value,
#rounded to the nearest integer.
#Note: Be sure to use precise values for your calculations, or you may
#end up with an incorrectly rounded result.

import math
import os
import random
import re
import sys


def solve(meal_cost, tip_percent, tax_percent):
     return print(round(meal_cost+((meal_cost*tip_percent/100)+(tax_percent*meal_cost/100))))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
