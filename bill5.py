Old_price={'milk':5,'Bread':3,'Butter':2,'Cheese':1}
d_r=80
new_price={key:value*d_r for key,value in Old_price.items()}
print(new_price)
