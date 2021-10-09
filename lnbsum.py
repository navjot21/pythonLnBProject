n = int(input("Enter any number of 5 digits= "))
s = 0
while n > 0:
    p = n % 10
    if p < 9:
        s += p
    else:
        print(0)
    n = n // 10
print(int(s))
