
s="Perfect-Plan-B:0.7541"
print(type(s))
pos=s.find(":")
t=s[pos+1:]
f=float(t)
print(type(f))

s=open("Webservice API learnings.txt")
r=s.read()
print(len(r))
print(r[:77])
for i in s:
    i=i.rstrip()
    if  i.startswith("From"):
        continue
    print(i)

if "me" in r:
    print("yes")
    pos=r.find("me")
    print(r[pos:pos+5])
else:
    print("no")
