num1 = int(input("Enter a number: "))
original = num1
digits = len(str(num1))
total = 0

while num1 > 0:
    rem = num1 % 10
    total += rem ** digits
    num1 = num1 // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

    