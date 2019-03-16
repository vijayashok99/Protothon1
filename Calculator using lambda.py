a=float(input("Enter the float"))
b=float(input("Enter the float"))
o=input("Enter the operation to be performed[+,-,*,/,^]")
dict={"+":(lambda a,b:a+b),"-":(lambda a,b:a-b),"*":(lambda a,b:a*b),"/":(lambda a,b:a/b),"+":(lambda a,b:a+b),"^":(lambda a,b:a**b),}
try:
    print(dict[o](a,b))
except ZeroDivisionError:
    print("Float not divisible by 0")
