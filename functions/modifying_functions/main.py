def apply_discount(price, discount=0.05):
    return price * (1 - discount)

def apply_tax(price, tax=0.07):
    return price * (1+tax)

def calculate_total(price, discount=.05, tax=.07):
    i=apply_discount(price, discount)
    i=apply_tax(i, tax)
    return i

'''
i=apply_discount(80)
print(i)

i=apply_tax(i)
print(i)
'''
c=calculate_total(120)
print("Total cost with default discount and tax: $", c)

c=calculate_total(price=100,discount=.10,tax=.08)
print("Total cost with custom discount and tax: $",c)
