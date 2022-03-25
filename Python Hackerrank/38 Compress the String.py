#You are given a string S. Suppose a character 'c' occurs consecutively X times
#in the string. Replace these consecutive occurrences of the character 'c' with
#(X,c) in the string.
#For a better understanding of the problem, check the explanation.
#Input Format
#A single line of input consisting of the string S.
#Output Format
#A single line of output consisting of the modified string.
#Sample Input
#1222311
#Sample Output
#(1, 1) (3, 2) (1, 3) (2, 1)
#Explanation91,1)
#First, the character 1 occurs only once. It is replaced by (1,1). Then the
#character 2 occurs three times, and it is replaced by (3,2) and so on.

s = input() + '-'
counter = 0
current_dig = s[0]
for i in range(len(s)):
    if current_dig == s[i]:
        counter += 1
    else:
        print(f"({counter}, {current_dig})", end = ' ')
        counter = 1
        current_dig = s[i]
