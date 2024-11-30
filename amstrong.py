a = int(input("enter a number"))
sum = 0
c = a
while c!=0:
    digit = c%10
    sum = sum+digit**3
    c = c//10
print(sum)
if sum==a:
    print("its a armstrong number")
else:
    print("its not a armstrong number")