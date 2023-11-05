a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))
if a>b and a>c:
      print("1st number is larger and 2nd,3rd is smaller")
elif b>c and b>a:
      print("2nd number is greater and 1st,3rd are smaller")
else:
      print("3rd number is larger and 1st,2nd is smaller")
