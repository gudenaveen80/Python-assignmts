str1="N"
if str1.isupper():
    print("uppercase")
else:
    print("lowercase")




str1=input("enter letter:")
if str1.isupper():
    res=chr(ord(str1)+32)
    print("lowercase",res)
else:
    print(str1)

num10=int(input("enter a number:"))
count=0
for i in range(1,num10+1):
    if num10%i==0:
        print(i)
        count+=1
print("count:",count)

n=10
i=2
while i<n+1:
    print(i)
    i+=2

sum=0
for i in range(1,6):
    sum+=i
print(sum)