#Consider a list (list = []). You can perform the following commands:
#insert i e: Insert integer  at position i.
#print: Print the list.
#remove e: Delete the first occurrence of integer e.
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of n followed by  lines of commands
#where each command will be of the 7 types listed above. Iterate through
#each command in order and perform the corresponding operation on your list.
#Input Format
#The first line contains an integer,n , denoting the number of commands.
#Each line i of the n subsequent lines contains one of the commands described
#above.
#Output Format
#For each command of type print, print the list on a new line.

if __name__ == '__main__':
    N = int(input())
    lis =[]
    for i in range(N) :
        strie = input()
        stri= strie.split() # for splitting string in list
        if stri[0] =='insert' :
            lis.insert(int(stri[1]),int(stri[2]))
        if stri[0] == 'print' :
            print(lis)
        if stri[0] == 'remove':
            lis.remove(int(stri[1]))
        if stri[0] == 'append':
            lis.append(int(stri[1]))
        if stri[0] == 'sort':
            lis.sort()
        if stri[0] == 'pop' :
            lis.pop()
        if stri[0] == 'reverse':
            lis.reverse()
