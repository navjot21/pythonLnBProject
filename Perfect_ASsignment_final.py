#to calculate Simple Intrest and Compound Intrest
p=int(input("Enter the principal amount: "))
r=float(input("Enter the rate: "))
t=int(input("Enter the time: "))
si=(p*r*t)/100
ci=p*(pow((1+r/100),t))
print(si)
print(ci)