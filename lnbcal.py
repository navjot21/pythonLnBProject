#Take 2 integer input from user and print their products(their multiplication)
#IF product is greater than 500 then return their sum
#If the product is smaller than 500 then return "Hello LNB code is running fine !!"
n=int(input("Please enter the first number= "))
m=int(input("Please enter the Second number= "))
mul=n*m
print("Product of two numbers is=",+ mul)
if mul>500:
    sum=m+n
    print()
    print("The product of numbers is greater than 500  so we showing the sum of numbers which is=" ,+ sum)
else:
    print()
    print("Hello LNB Code is running fine !!")
