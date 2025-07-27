# # print(bin(29))
# # dict1={"name":"Naveen","age":22,"class":56}
# # print(dict1.values())
# # print(dict1.keys())
# # for i in range(1,200):
# #     if i%7==0 and i%9==0:
# #         print(" common are:",i)
# str1="naveen"
# # print(str1[10])
# # print(str1[0:1000])
# # print(str1[::-1])
# # print(3 and 2)
# # print(3 or 2)
# # print(9 ^ 7)
# # print(9 & 7)
# # print(bin(9))
# # print(bin(7))
# # print(bin(1))
# # print(bin(14))
# # set1={10,20,30,frozenset({20,40,50})}
# # print(set1)
# # print(type(set1))
# # dict1={"name":"Naveen","age":22,"class":56,"vaysu":30}
# # print(dict1)
# # #keys are  unique in the dictionary but not the case with values are not same in the dictionary. because keys are like roll nos which are unique despite having same names.
# # #sets are not allowed the inside set ,fronzenset allowed in set
# # #dictionaries are ordered whereas sets are unordered...
# # even_odd=
# # if even_odd%2==0:
# #     print("even")
# # else:
# #     print("odd")
# # leap1=int(input("enter a year:"))
# # if leap1%4==0 and leap1%400==0:
# #     print("given year is leap:",leap1)
# # else:
# #     print("not a leap year")
# # num1=0
# # num2=1
# # if num1>num2:
# #     print("num1 is greatest:",num1)
# # else:
# #     print("num2 is greatest:",num2)
# # age=14
# # wait=18-age
# # if age>=18:
# #     print("you are eligible:",age)
# # else:
# #     print(f"{age} is minor")
# # marks=int(input("enter marks beta:"))
# # if marks>=90:
# #     print("Grade A")
# # elif marks>=75:
# #     print("Grade B")
# # elif marks>=60:
# #     print("Grade C")
# # elif marks>=40:
# #     print("Grade D")
# # else:
# #     print("Fail")
# # num4=-5
# # if num4>0:
# #     if(num4%2==0):
# #         print("it is even")
# #     else:
# #         print("it is odd")
# # if num4<0:
# #         print("it is negative")
    
# # else:
# #     print("zero")
# num6=int(input("enter a number1:"))
# num7=int(input("enter a number2:"))
# # add=num6+num7
# # sub=num6-num7
# # mul=num6*num7
# # div=num6/num7
# # print(add)
# # print(sub)
# # print(mul)
# # print(div)
# # if num6>num7 or num6<num7:
# #     print(num6+num7)
# # elif num6>num7 or num6<num7:
# #     print(num6-num7)
# # elif num6>num7 or num6<num7:
# #     print(num6*num7)
# # elif num6>num7 or num6<num7:
# #     print(num6/num7)
# # Get user input
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# # Perform calculation using if-else
# if operator == "+":
#     print("Result:", num1 + num2)
# elif operator == "-":
#     print("Result:", num1 - num2)
# elif operator == "*":
#     print("Result:", num1 * num2)
# elif operator == "/":
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operator.")# Get user input
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# # Perform calculation using if-else
# if operator == "+":
#     print("Result:", num1 + num2)
# elif operator == "-":
#     print("Result:", num1 - num2)
# elif operator == "*":
#     print("Result:", num1 * num2)
# elif operator == "/":
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operator.")
# If Else Questions:
# 1)a or b which is bigger
# 2) a or b or c which is bigger.
# 4)Wap to find a number is even or odd
# 3)Wap to find Leap Year
# 4) Write a program to check if a given number is positive, negative, or zero. 
# 5) Check if a person is eligible to vote (age >= 18). 
# 6) Print "Pass" if a student scores more than 40 marks; otherwise, print "Fail." 
# 7) Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).
# 8) Implement a simple calculator to perform addition, subtraction, multiplication, and division.
# 9) Write a program to classify a character entered by the user as a vowel, consonant, or neither. 
# 10) Calculate the grade of a student based on the marks they score: 1. 90-100: Grade A 2. 80-89: Grade B 3. 70-79: Grade C 4. <70: Fail. 
# 11) Write a program to check if three sides length form a valid triangle
# marks=70
# if marks>40:
#     print("pass")
# else:
#     print("fail")
# day=int(input("enter num:"))
# if day==1:
#     print("1 is monday")
# elif day==2:
#     print("2 is tuesday")
# elif day==3:
#     print("3 is wednesday")
# elif day==4:
#     print("4 is thursday")
# elif day==5:
#     print("5 is friday")
# elif day==6:
#     print("6 is saturday")
# elif day==7:
#     print("sunday")
# else:
#     print("hey man enter 1 to 7 only")
# char=input("enter a char:")
# vowel='a','e','i','o','u'
# if char in vowel:
#     print("it is vowel")
# elif char not in vowel:
#     print("it is consonant")
# else:
#     print("it is neither")
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
c=int(input("enter a number3:"))

if a+b>c and b+c>a and c+a>b:
  print("this is triangle")
else:
    print("this is not triangle")
