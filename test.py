from cgi import print_exception
from cmath import exp
from pickle import FALSE
from sre_parse import expand_template
from sys import flags


print("-----------------Shopping Basket------------------")

product={'books','medical','food','other'}
product={'books':'book', 'food':'chocolate bar','other':'chocolates', 'medical':'pills'}
shopping_items={}
shopping_itemsupdated=[]
stop= False
total=0
global price
price=0
#to get items and detail
while not stop:
    quantity=int(input("Enter the quantity\n"))
    name=input("Enter the item\n")
    cost=float(input("Enter the price\n"))
    shopping_items={'item_name':name, 'quantity':int(quantity), 'cost':float(cost)}
    shopping_itemsupdated.append(shopping_items)
    response=input("Anything more\n y or n \n")
    if response=='y':
        stop=False
    else:
        stop=True
    price+=cost

def tax_calcu():
    for item in shopping_itemsupdated:
        global cost
        global total
        global salestax
        global prices
        prices=0
        salestax=0
        if "imported" in item['item_name']:
            item['cost']+= item['cost']*.05
            if item['item_name'] not in product.values():
                    item['cost']+=item['cost']*.1   
        elif item['item_name'] not in product.values():
            item['cost']+=item['cost']*.1
        total+=item['cost']
        salestax=total-price
        print("%d %s : %.2f" %(item['quantity'],item['item_name'], round(item['cost'],2)))

for items in shopping_itemsupdated:
    print("%d %s at %.2f" %(items['quantity'],items['item_name'],items['cost']))

print("-----------------------------------------------------")
print("*Bill Summary*\n")
tax_calcu()
print("Salestax: %.2f" %(salestax))
print('Total:',round(total,2))
print("*******************Thank you*************************")
print("See you again!")


        


        
