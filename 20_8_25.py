#armstrong numbers in a given range.
def armstrng_or_not(num1):
    count=0
    total_sum=0
    temp=num1
    while num1>0:
        count+=1
        num1=num1//10
    num1=temp
    while num1>0:
        rem=num1%10
        total_sum+=rem**count
        num1=num1//10
    print(total_sum)
    if temp==sum:
        return True
    return False
armstrong_numbers=[]
for num1 in range(1,1000):
    if armstrng_or_not(num1):
        armstrong_numbers.append(num1)
print(" armstrong numbers between 1 to 1000",armstrong_numbers)

#prime numbers in a given range
def Prime_range(a,b):
    
    for i in range(a,b+1):
        if i<2:
            continue
        count=0
        
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                count+=1
                break
        if count==0:
            print(i)
    print()
Prime_range(1,1000)
