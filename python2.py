a=int(input("Enter your age : "))
if a<18:
    print("You are a teenager")
elif a==18:
    print("You are a youngester")
elif a>=40:
    print("You are asad khan")

#nested if statement
b=int(input("Enter 1st number :"))
c=int(input("Enter 2nd number :"))
d=int(input("Enter 3rd number :"))
if b>c:
    if b>d:
        print(b,"b is greatest")
    else:
        print(d,"d is greatest")
elif c>d:
    print(c,"c is greatest")
else:
    print(d,"d is greatest")