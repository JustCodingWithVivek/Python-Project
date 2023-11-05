print("Welcome To Driving School Online Portal")
name=input("Enter your name -to continue further: ")
print("Hello",name.capitalize())
a = int(input("Enter Your Age: "))

if a>=7 and a <= 100:
 if a > 18:
   print(name.capitalize(),",You Are Eligible to Drive")

 elif a==18:
    print(name.capitalize(),",It Can't be Decided. Please Come To The Office Physically")

 elif a<18:
    print(name.capitalize(),",You Are Not Eligible To Drive")

else:
    print(name.capitalize(),",You Do Not Enter Logical Age to Drive")

print("Thank You To Visit Our Portal",name.capitalize())
