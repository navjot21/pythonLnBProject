#Take input from user in string form only and calculate the length of string
#IF length is greater than 7 then display only those character which are present in even index number
#If length is less than or equals to 7 then display only those character which are present in odd index number

n=input("Enter any string of your choice:")
print("length of string is:",+(len(n)))


if  len(n)<=7:
    print(n[1:len(n):2])
elif len(n)>7:
    print(n[0:len(n):2])







