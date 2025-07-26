num,power=3,2
print(num**power)

# enter a number:10
# factorial of 10 3628800

num=int(input("enter a number:"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("factorial of", num,factorial)

# hcf of 60 and 36 are 12
num1=60
num2=36
hcf=1
for i in range(1,min(num1,num2)):
    if num1%i== 0 and num2%i== 0:
     hcf=i
print("hcf of",num1,"and",num2,"is",hcf)

# lcm of 20 and 30 is 60
num4=20
num5=30
for i in range(max(num4,num5),1+(num4*num5)):
    if i % num4==i% num5==0:
        lcm=i
        break
print("lcm of" ,num4, "and",num5,"is",lcm)


# Python Program for checking a character is a vowel or consonant
c = 'E'
if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
    print(c, "is a vowel") 
else:
    print(c, "is a consonant") 
  
# a is alphabet  
chr=" "
if 'a'<=chr<='z' or 'A'<=chr<='Z':
    print(chr,"is alphabet")
else:
    print(chr,"is not alphabet")
    
#ascii to character   
ord=97
charactr=chr(ord)
print(charactr)

#character to ascii value 
Char = 'z'
Ascii_val = ord(Char)
print('The ASCII value of', Char, 'is', Ascii_val)

#24 string length without using len() function.
str1="naveen gude was born on "
count=0
for i in str1:
    count+=1
print(count)

# toggle the string altenatively are: NAVEEN
str4="naveen"
print("toggle the string altenatively are:",str4.swapcase())

# Python Program to Remove Spaces from a String
str4="naveen_ gude is born on"
str4="".join(str4.split())
print(str4)

# enter a string1:heart
# enter a string2:earth
# given strings are anagrams

str1=input("enter a string1:")
str2=input("enter a string2:")
str1=sorted(str1.lower())
str2=sorted(str2.lower())
if str1==str2:
    print("given strings are anagrams")
else:
    print("given strings are not anagrams")
