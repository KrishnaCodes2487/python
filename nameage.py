class Student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __str__(self):
        return f"{self.name}({self.age})"
obj=Student("abc",20)
print(obj)
        
