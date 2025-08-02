def sum_2(num1,num2):
    sum=num1+num2
    print(sum)
sum_2(num1=50,num2=100)

def num_square(num1):
    num_square=num1**2
    print(num_square)
num_square(10)
num_square(20)
num_square(30)


def even_odd(n):
    n=int(input("enter number:"))
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")
even_odd(10)

def factorial(factorial):
   factorial=1
   n=int(input("enter a number:"))
   for i in range(1,n+1):
     factorial=factorial*i
     print(factorial)
factorial(5)

def max_three(num1,num2,num3):
    if num1>num2:
        print(num1,"is greatest")
    elif num2>num3:
        print(num2,"is greatest")
    else:
        print(num3,"is greatest")
max_three(10,30,40)
max_three(10,30,50)
max_three(10,20,30)

def vowels():
    str_input = input("Enter a string: ")
    count = 0
    str_input = str_input.lower()

    for i in str_input:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
            print(i)

    print("Vowels are:", count)

    if count == 0:
        print("No vowels in string")

vowels()

def list_sum():
    list1=[10,20,30,40]
    temp=0
    for i in list1:
        temp+=i
        print(temp)
list_sum()

def reverse():
   str1="naveen"
   reverse_str=str1[::-1]
   print(reverse_str)
reverse()

def palindrome():
    string_1=input("enter a string man:")
    reverse_string=0
    reverse_string=string_1[::-1]
    if string_1==reverse_string:
      print(string_1,"is palindrome")
    else:
      print(string_1,"is not palindrome")
palindrome()

def even_list():
  list_1=[1,2,3,4,5,6,7,8,9,10]
  for i in list_1:
    if i%2==0:
     print(i,end=" ")
even_list()

def circle_radius(pie,r):
    radius_circle=pie*r**2
    print(radius_circle)
circle_radius(3.14,5)

def string_len():
    str1=input("enter a string:")
    count=0
    for i in str1:
       count+=1
       print(i, end="")
    print("length is",count)
string_len()

def average(*numbers):
    avg=sum(numbers)/len(numbers)
    print(avg)
average(300,350,400)
average(100,200)
average(200,300)
average(214,546,757,234,356)