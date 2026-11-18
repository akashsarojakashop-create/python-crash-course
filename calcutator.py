a = int(input("enter first number"))
b = int(input("enter second number"))

print("what to do  * + - /")
choice = input("enter:")

if choice == "*":
    print("answer",a*b)
elif choice == "-":
    print("answer",a+b)
elif choice == "-":
    print("answer",a-b)
elif choice == "/":
    print("answer",a/b)
else:
     print("wrong choice!")