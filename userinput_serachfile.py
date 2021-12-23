#extract the content of user choice from a file using split function
s=open("file.txt")
for i in s:
    i=i.rstrip()
    w=i.split()

    if len(w)<3 and w[0]!="From":
        continue
    print(w[2])