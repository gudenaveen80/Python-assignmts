# Palindromic Bus Ticket
# In a small town, bus tickets have a unique pattern — if the ticket number reads the same forwards and backwards, it is considered a “lucky” ticket.
# Given a ticket number as a string, write a program to:
# - Reverse the number
# - Check if it is a palindrome
# If it is, print "Lucky Ticket", otherwise print "Not Lucky".
# Input Format
# A single line containing the ticket number as a string.
# Output Format
# Print "Lucky Ticket" if it is a palindrome, otherwise print "Not Lucky".
# Constraints
# 1 ≤ length of ticket number ≤ 10
# Sample Test Cases
# Input:
# 121
# Output:
# Lucky Ticket
# Input:
# 123
# Output:
# Not Lucky



ticket_num=int(input("enter a ticket number:"))
original=ticket_num
rem=0
reverse=0
while ticket_num>0:
    rem=ticket_num%10
    reverse=reverse*10+rem
    ticket_num//=10
if reverse==original:
    print("Lucky Ticket")
else:
    print("Not Lucky")
    
# Sum of Magic Squares
# A wizard is teaching you a math spell to calculate the *magic sum* of square numbers.
# Given a number n, you must find the sum of the squares of all numbers from 1 to n.
# For example, if n = 3, the result is 1² + 2² + 3² = 14.
# Input Format
# A single integer n.
# Output Format
# The sum of squares from 1 to n.
# Constraints
# 1 ≤ n ≤ 10^4
# Sample Test Cases
# Input:
# 3
# Output:
# 14
# Input:
# 5
# Output:
# 55


num=int(input("enter a number:"))
sum_of_squares=0
for i in range(1,num+1):
    sum_of_squares+=i**2
print(sum_of_squares)

# Treasure Hunt Guessing Game
# You are on a treasure island, and the treasure is buried at a specific location marked by a secret number between 1 and 100.
# Write a program that keeps asking the player to guess the number until they find it.
# After each wrong guess, display "Try Again!", and when they guess correctly, display "Treasure Found!".
# Input Format
# Multiple integer guesses entered one per line until the correct number is guessed.
# Output Format
# "Try Again!" for each wrong guess, and "Treasure Found!" when correct.
# Constraints
# Secret number is between 1 and 100.
# Sample Test Cases
# Input:
# 50
# 30
# 42
# Output:
# Try Again!
# Try Again!
# Treasure Found!

num=42
while True:
    guess=int(input("enter a number:"))
    if guess==num:
        print("Treasure Found")
        break
    else:
        print("Try Again!")
# In a city fair, there is a game where you win a prize if your chosen number is a *perfect square*.
# Write a program to display all perfect square numbers between 1 and 500 so players can see which numbers will win.
# Input Format
# No input required.
# Output Format
# All perfect squares between 1 and 500 separated by spaces.
# Constraints
# Numbers between 1 and 500.
# Sample Test Cases
# Output:
# 1 4 9 16 25 36 49 64 81 100 ... 484

limit=500
i=1
while i*i<=limit:
       print(i*i)
       i+=1
       
# Cube Challenge
# In a video game, your character collects cubes of different sizes.
# Given a number n, print the cube of every number from 1 to n so the player knows the sizes of cubes they can collect.
# Input Format
# A single integer n.
# Output Format
# The cubes of numbers from 1 to n, each on a new line.
# Constraints
# 1 ≤ n ≤ 1000
# Sample Test Cases
# Input:
# 3
# Output:
# 1
# 8
# 27
# Input:
# 5
# Output:
# 1
# 8
# 27
# 64
# 125

num1=int(input("enter a number:"))
for i in range(1,num1+1):
    cube=i**3
    print(cube)


