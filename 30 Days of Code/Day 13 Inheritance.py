#Task
#You are given two classes, Person and Student, where Person is the base
#class and Student is the derived class. Completed code for Person and a
#declaration for Student are provided for you in the editor. Observe that
#Student inherits all the properties of Person.
#Complete the Student class by writing the following:
#A Student class constructor, which has 4 parameters:
#A string,firstName .
#A string,lastName .
#An integer,idNumber .
#An integer array (or vector) of test scores,scores .
#A char calculate() method that calculates a Student object's average and
#returns the grade character representative of their calculated average:
#Input Format
#The locked stub code in the editor reads the input and calls the Student
#class constructor with the necessary arguments. It also calls the calculate
#method which takes no arguments.
#The first line contains firstName ,lastName , and idNumber , separated
#by a space. The second line contains the number of test scores. The third
#line of space-separated integers describes scores.


class Student(Person):
    def __init__(self, firstname, lastname, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        sum = 0
        for score in scores:
            sum += score
        average = sum/len(scores)
        if average < 40:
            return 'T'
        elif average < 55:
            return 'D'
        elif average < 70:
            return 'P'
        elif average < 80:
            return 'A'
        elif average < 90:
            return 'E'
        else:
            return 'O'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
