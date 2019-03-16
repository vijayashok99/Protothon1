a=[]
s=0;i=0
a=input("Enter the numbers")
a=a.split(" ")
for i in range(len(a)):
    s=s+float(a[i])**2
print((s/len(a))**(0.5))
