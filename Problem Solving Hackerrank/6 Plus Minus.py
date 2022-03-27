#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
#Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.
#
#Example
#arr=[1,1,0,-1,-1]
#There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5=0.4,2/5=0.4  and 1/5=0.2. Results are printed as:
#0.400000
#0.400000
#0.200000
#
#Function Description
#Complete the plusMinus function in the editor below.
#plusMinus has the following parameter(s):
#int arr[n]: an array of integers
#
#Print
#Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.
#
#Input Format
#The first line contains an integer,n , the size of the array.
#The second line contains n space-separated integers that describe arr[n].
#
#Output Format
#Print the following 3 lines, each to 6 decimals:
#proportion of positive values
#proportion of negative values
#proportion of zeros
#
#Sample Input
#STDIN           Function
#-----           --------
#6               arr[] size n = 6
#-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
#
#Sample Output
#
#0.500000
#0.333333
#0.166667

n = int(input().strip())
arr = [1 if int(temp)>0 else -1 if int(temp)<0 else 0 for temp in input().strip().split(' ') ]
print("{0:.6f}".format(arr.count(1)/n))
print("{0:.6f}".format(arr.count(-1)/n))
print("{0:.6f}".format(arr.count(0)/n))
