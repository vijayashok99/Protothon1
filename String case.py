s="a big brown fox ran across the river.fox name is tiger"
#s=input("Enter the sentence")
print(s.upper())
print(s.lower())
print(s.title())
s=s.split(".")
for i in range(len(s)):
    print("\n",s[i].replace(s[i][0],s[i][0].upper(),1))
