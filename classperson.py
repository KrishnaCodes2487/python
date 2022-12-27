class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __str__(self):
        return f"{self.name}({self.age})"
    def __repr__(self):
        return f'Person(name={self.name},age={self.age})'
obj=Person("xyz",30)
print(obj.__str__())
print(obj.__repr__())

    
