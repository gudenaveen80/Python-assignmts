# # n=5 #square
#    *****
#    *****
#    *****
#    *****
#    *****
# # for i in range(0,n):
# #     for j in range(i+n-i):
# #       print("*",end='')
# #     print()
# #
# #rectangle
# enter number1:4
# enter number2:3
# ***
# ***
# ***
# ***
# # n=int(input("enter number1:"))
# # m=int(input("enter number2:"))
# # for i in range(1,n+1):
# #     for j in range(m):
# #        print("*",end='')
# #     print()

# right aligned traingle
#    *
#   **
#  ***
# ****
# n=4
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#      print()

# 12345
# 1234
# 123
# 12
# n=4 # inverse numbers triangle...
# for i in range(n+1,1,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# 54321 
# 4321
# 321
# 21 

# n=4
# for i in range(n+1,1,-1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print() 
   
#     *
#    ***
#   *****
#  *******
# ********* 

# n=4
# for i in range(0,n+1):
#         for j in range(n-i):
#             print(" ",end="")
#         for j in range(2*i+1):
#             print("*",end='')
#         print()
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

# n=5
# num=1
# for i in range(1,n+1):
#    for j in range(1,i+1):
#        print(num,end=" ")
#        num+=1
      
#    print()

# A
# AB
# ABC
# ABCD

# n=4
# for i in range(0,n):
#     for j in range(i+1):
#         print(chr(65+j),end='')
#     print()