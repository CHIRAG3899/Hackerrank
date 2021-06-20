#In this challenge, the user enters a string and a substring. You have to print
#the number of times that the substring occurs in the given string. String
#traversal will take place from left to right, not from right to left.
#NOTE: String letters are case-sensitive.
#Input Format
#The first line of input contains the original string. The next line contains
#the substring.
#Each character in the string is an ascii character.
#Output Format
#Output the integer number indicating the total number of occurrences of the
#substring in the original string.
#Sample Input
#ABCDCDC
#CDC
#Sample Output
#2

def count_substring(string, sub_string):
    sum=0
    while sub_string in string:
        x = string.index(sub_string)
        sum+=1
        string= string[x+1:]
    return sum

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
