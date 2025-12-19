menu={
    'chai':10,
    'biskit':2,
    'samosha':5,
    'kachori':15,
    'litti':12
}
print("welcome to coder Restaurant")
print("chai:Rs10\nbiskit:Rs2\nsamosha:Rs5\nkachori:Rs15\nlitti:Rs12")
order=0
item1=input("enter the name of item you want to order=")
if item1 in menu:
    order=order+menu[item1]
    print(f"ordered item {item1} has been added avaialable yet!")
else:
    print(f"ordered item {item1} is not available")
anothterOrder=input("do you want to add another item?(yes/No)")
if anothterOrder == "yes":
    item2=input("enter tne name of second item=")
    if item2 in menu:
        order=order+menu[item2]
        print(f"Item {item2} has been added to order")
    else:
        print("Ordered item {item2} is not available!")
print(f"The total amount of items to pay is{order}")