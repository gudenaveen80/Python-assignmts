
# num1=int(input("enter a number:"))
# flag=0
# for i in range(2,num1):
#     if num1%i==0:
#         flag=1
#         break
# if flag==1:
#     print("num1 is not prime")
# else:
#     print(num1,"is prime")

# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

for num1 in range(2, 101):  # Loop from 2 to 100
    flag = 0
    for i in range(2, num1):
        if num1 % i == 0:
            flag = 1
            break
    if flag == 0:
        print(num1, end=' ')
        
# Palindrome Program in Python
num10=input("enter a String:")
reverse=str(num10)[::-1]
if reverse==num10:
    print(num10,"is a palindrome")
else:
    print(num10,"is not a palindrome")

# enter a number:1221
# 1221 it is palindrome   
    
num4=int(input("enter a number:"))
temp=num4
reverse=0
while temp>0:
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp//10
if reverse==num4:
    print(num4,"it is palindrome")
else:
    print(num4,"it is not palindrome")
    
#   Fibonacci Series: 0 1 1 2 3 5 8 13 21 34   
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()

# enter a number:1634
# 1634 it is armstrong number

num5=int(input("enter a number:"))
digits=len(str(num5))
temp=num5
result=0
while temp>0:
    digit=temp%10
    result+=digit**digits
    temp=temp//10
if result==num5:
    print(num5,"it is armstrong number")
else:
    print(num5,"it is not an armstrong number")