Menu={'Rice':100,'Burger':60,'Dosa':120,'Roti':15,'Cheese Chili':150,'Egg':30}
total=0
for x in Menu.values():
    total=total+x
print('Bill Slip')
for a,b in Menu.items():
    print(a,':',b)
print('Total Bill=',total)
