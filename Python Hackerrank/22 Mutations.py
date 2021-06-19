#Task
#Read a given string, change the character at a given index and then print the
#modified string.
#Function Description
#Complete the mutate_string function in the editor below.
#mutate_string has the following parameters:
#string string: the string to change
#int position: the index to insert the character at
#string character: the character to insert0
#Returns
#string: the altered string
#Input Format
#The first line contains a string, string .
#The next line contains an integer position, the index location and a string
#character, separated by a space.
#Sample Input
#STDIN           Function
#-----           --------
#abracadabra     s = 'abracadabra'
#5 k             position = 5, character = 'k'
#Sample Output
#abrackdabra

def mutate_string(string, position, character):
    l = list(s)
    l[int(i)] = c 
    return "".join(l)
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
