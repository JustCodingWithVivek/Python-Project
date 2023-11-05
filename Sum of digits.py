i=int(input("Enter a number to find sum of digits: "))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("Sum of digits of the number", sum)
