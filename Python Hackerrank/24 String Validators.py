#Task
#You are given a string S.
#Your task is to find out if the string S contains: alphanumeric characters,
#alphabetical characters, digits, lowercase and uppercase characters.
#Input Format
#A single line containing a string S.
#Output Format
#In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
#In the second line, print True if S has any alphabetical characters. Otherwise, print False.
#In the third line, print True if S has any digits. Otherwise, print False.
#In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
#In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
#Sample Input
#qA2
#Sample Output
#True
#True
#True
#True
#True

if __name__ == '__main__':
    s = input()
    begin = [False for i in range(5)]
    for i in range(len(s)):
        if s[i].isalnum() == True:
            begin[0] = True
    for i in range(len(s)):
        if s[i].isalpha() == True:
            begin[1] = True
    for i in range(len(s)):
        if s[i].isdigit() == True:
            begin[2] = True
    for i in range(len(s)):
        if s[i].islower() == True:
            begin[3] = True
    for i in range(len(s)):
        if s[i].isupper() == True:
            begin[4] = True
            
    for _ in begin:
        print(_)
