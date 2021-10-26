# to make a program for input number from user and show the factorial of number
n=int(input("Enter the number: "))
f=1
for i in range(1,n+1):
    f=f*i

print(f)

if f % 5 == 0:
    print("number is even")
else:
    print("number is odd")
