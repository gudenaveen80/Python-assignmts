num1=int(input("enter a num:"))
original=num1
digit=0
reverse=0
digit_sum=0
while num1>0:
  digit=num1%10
  reverse=reverse*10+digit
  digit_sum+=digit
  num1=num1//10
print(digit_sum)
print(reverse)
if reverse==original:
    print("it is palindrome")
else:
    print("it is not palindrome")

num1 = 1  

while num1 > 0:
    num1 = int(input("Enter a number: "))
    if num1 < 0:
        print("Finally, you have entered a negative number.")
        
num1=0
num2=1
total=int(input("enter a number:"))
for i in range(total):
    num3=num1+num2
    num1=num2
    num2=num3
    print("fibonnaci series",num1)
    
flag=0
num1=int(input("enter a number:"))
for i in range(1,num1):
    if num1%i==0:
        flag=1
        break
    if flag==1:2
    print("it is not prime")
else:
    print("it is prime")
    
num2=5
factorial=1
while num2>0:
    factorial=factorial*num2
    num2-=1
print(factorial)


while True:
    print("Menu:")
    print("1. Square of a number")
    print("2. Cube of a number")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print("Square is:", num ** 2)

    elif choice == 2:
        num = int(input("Enter a number: "))
        print("Cube is:", num ** 3)

    elif choice == 3:
        print("Exiting... Bye!")
        break

    else:
        print("Invalid choice. Try again.")
        
i=1
password="naveen"
while 4>i:
 num1=input("enter a password:")
 if password==num1:
     print("login successfull")
     break
 else:
     i+=1
if i==4:
     print("too many attempts,try after 24 hours")
     
     
flag=0
count=0
num1=int(input("enter a number:"))
for i in range(1,num1):
    if num1%i==0:
        flag+=1
        print(i)
if i==num1:
    print("it is perfect number")
else:
    print("it is not perfect number")
    
    
flag=0
count=0
num1=int(input("enter a number:"))
for i in range(1,num1):
    if num1%i==0:
        flag+=1
        print(i)
if i==num1:
    print("it is perfect number")
else:
    print("it is not perfect number")
        

