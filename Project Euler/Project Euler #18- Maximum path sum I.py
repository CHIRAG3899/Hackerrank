#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23. The path is denoted by numbers in bold.
#   3
#  7 4
# 2 4 6
#8 5 9 3
#
#That is, 3+4+7+9=23.
#Find the maximum total from top to bottom of the triangle given in input.
#
#Input Format
#First line contains , the number of testcases. For each testcase:
#First line contains , the number of rows in the triangle.
#For next  lines, 'th line contains  numbers.
#
#Output Format
#For each testcase, print the required answer in a newline.
#
#Sample Input
#1
#4
#3
#7 4
#2 4 6
#8 5 9 3
#Sample Output
#23

for _ in range(int(input())):
    n = int(input())
    s = []
    for i in range(n):
        s.append(list(map(int, input().split())))
    
    row = n-2
    while row >= 0:
        for i in range(len(s[row])):
            s[row][i] += max(s[row+1][i], s[row+1][i+1])
        row -= 1
    print(s[0][0])