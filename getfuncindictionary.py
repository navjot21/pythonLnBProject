#proram to use GEt() function in dictionary
"""
count=dict()
names=["navjot","jiten","kamal","akshaya","priya","kamal","jiten"]
for name in names:
    count[name]=count.get(name,0) + 1
print(count)
****************************
#take items from dictionary
n={"jyoti":5,"love":9,"nav":10}
print(list(n))

print(n.keys())
print(n.values())
print(n.items())

for aa,bb in n.items():

    print(aa,bb)
    """
count=dict()
n=input("enter the text:")
d=n.split()
print(d)

print("Count")
for name in d:
    count[name]=count.get(name,0) + 1
print(count)


