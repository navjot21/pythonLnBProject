a=[1,8,5,9,2]
b=[2,7,4,3,9]
c=0
for i in a:
    for j in b:

         if i==j:
            print(i,j)
            c+=1
         else:
            continue
if c>0:
 print("True")
else:
    print("False")