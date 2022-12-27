class calculate:
    n=int(input('Enter your choice='))
    if n==1:
        x=int(input('Enter the side of square='))
        obj=calculate()
        obj.area(x)
    if n==2:
        x=int(input('Enter Length='))
        y=int(input('Enter Breadth='))
        obj=calculate()
        obj.area(x,y)
a=calculate()
