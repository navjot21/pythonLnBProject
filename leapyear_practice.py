#to verify the year is leap or not

n=int(input("enter the year: "))
if n%400==0:
    if n%4==0:
        print(n,": is a leap year")

else:
    print(n , ": is not a leap year")
