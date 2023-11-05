i=int(input("Enter a number"))
original=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if original==sum:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
