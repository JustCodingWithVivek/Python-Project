n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum1=1
for i in range(2,n+1):
    sum2=sum1+((x**i)/i)
print("The sum of series is",sum2)
