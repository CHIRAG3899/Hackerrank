#Task
#Complete the Difference class by writing the following:
#A class constructor that takes an array of integers as a parameter and saves
#it to the _elements  instance variable.
#A computeDifference method that finds the maximum absolute difference between
#any 2 numbers in  and stores it in the maximumDifference instance variable.
#Input Format
#You are not responsible for reading any input from stdin. The locked Solution
#class in the editor reads in  lines of input. The first line contains N,
#the size of the elements array. The second line has N space-separated integers
#that describe the _elements  array.
#Output Format
#You are not responsible for printing any output; the Solution class will print
#the value of the maximunDifference instance variable.
#Sample Input
#STDIN   Function
#-----   --------
#3       __elements[] size N = 3
#1 2 5   __elements = [1, 2, 5]
#Sample Output
#4

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    def computeDifference(self):
        min_element = 101
        max_element = 0
        for element in self.__elements:
            if element < min_element:
                min_element = element
            if element > max_element:
                max_element = element
        
        self.maximumDifference = max_element - min_element

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
