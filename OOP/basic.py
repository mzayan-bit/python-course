class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0 
        for val in self.marks:
            sum+=val
        print("Hello , ",self.name," your Avg Score is :",sum/3)
    
s1=Student("Zayan",[80,75,95])
s1.average()