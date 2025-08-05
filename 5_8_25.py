# i. Write a program to find the greatest of three numbers.
def greatest_of_three(num1,num2,num3):
  if num1>num2 and num1>num3:
    return num1
  elif num2>num3 and  num2>num1:
    return num2
  else:
    return num3
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number"))
result=greatest_of_three(num1,num2,num3)
print(result)



# ii. Check if a year is a leap year.



def leap_or_not(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100!= 0):
        return "leap_year"
    else:
        return "not leap_year"

year = int(input("Enter a year: "))  
print(leap_or_not(year))


def leap_or_not(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return "leap_year"
    else:
        return "not leap_year"

print(leap_or_not(1900))


# iii. Write a program to classify a character entered by the user
# as a vowel, consonant, or neither.

def vowel_consonant(char1):
 vowel="AEIOUaeiou"
 if char1.isalpha():
     if char1 in vowel:
        print("it is vowel")
     else:
        print("it is consonant")
 else:
    print("neithe vowel or consonant")

char1=input("enter a char:")
vowel_consonant(char1)

# iv. Calculate the grade of a student based on the marks they
# score:
# 1. 90-100: Grade A
# 2. 80-89: Grade B
# 3. 70-79: Grade C
# 4. <70: Fail.

def student_grade(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    else:
        return "Fail"
marks=int(input("enter a number:"))
print(student_grade(marks))



# v. Write a program to check if three sides length form a valid
# triangle


def valid_triangle(side_1, side_2, side_3):
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        print("Forms a triangle")
    else:
        print("measures not adequate to form triangle")

side_1 = int(input("Enter a side_1: "))
side_2 = int(input("Enter a side_2: "))
side_3 = int(input("Enter a side_3: "))

valid_triangle(side_1, side_2, side_3)
