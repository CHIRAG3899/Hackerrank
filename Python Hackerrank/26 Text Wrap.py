#You are given a string S and width w.
#Your task is to wrap the string into a paragraph of width w.
#Function Description
#Complete the wrap function in the editor below.
#wrap has the following parameters:
#string string: a long string
#int max_width: the width to wrap to
#Returns
#string: a single string with newline characters ('\n') where the breaks should be
#Input Format
#The first line contains a string, string.
#The second line contains the width, maxwidth.
#Sample Input 0
#ABCDEFGHIJKLIMNOQRSTUVWXYZ
#4
#Sample Output 0
#ABCD
#EFGH
#IJKL
#IMNO
#QRST
#UVWX
#YZ

def wrap(string, max_width):
    newStr = ''
    n = len(string)
    i = 0
    while i < n:        
        split_str = string[i:i+max_width]
        newStr = newStr + '\n' + split_str
        i = i + max_width
    return newStr.lstrip('\n')

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
