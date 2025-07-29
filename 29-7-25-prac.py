# 1      1
# 12    21
# 123  321
# 12344321
# n = 4
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print(" " * (2 * (n - i)), end="")
#     for j in range(i, 0, -1):
#         print(j, end="")

#     print()

# 0 
# 1 2 
# 3 4 5 
# 6 7 8 9 
# 10 11 12 13 14
# n=5
# count=0
# for i in range(1,n+1):
#     for j in range(i):
#       print(count,end=" ")
#       count+=1
#     print()

# AB
# ABC
# ABCD
# ABCDE
# n=4
# for i in range(1,n+1):
#     for j in range(0,i+1):
#         print(chr(ord('A')+j),end="")
#     print()

# ABCDE
# ABCD
# ABC
# AB
# A
# n=5
# for i in range(n+1,0,-1):
#     for j in range(0,i-1):
#       print(chr(ord("A")+j),end="")
#     print()

# A
# BB
# CCC
# DDDD
# EEEEE

# n=4
# for i in range(0,n+1):
#     for j in range(0,i+1):
#       print(chr(ord("A")+i),end="")
#     print()

#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#       print(" ",end="")
#     for j in range(0,i):
#       print(chr(ord('A')+j),end="")
    
#     for j in range(i-2,-1,-1):
#         print(chr(ord('A')+j),end="")
#     print()

# E 
# D E 
# C D E 
# B C D E 
# A B C D E 
# n=5
# for i in range(n-1,-1,-1):
#     for j in range(i,n):
#         print(chr(ord("A")+j),end=" ")
#     print()

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# n = 7
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     for j in range(2 * i):
#         print("",end=" ")
#     for j in range(n-i):
#         print("*",end="")
#     print()
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print(" "*(2 * (n - i)), end="")
#     for j in range(i, 0, -1):
#         print("*", end="")

#     print()

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# n=5
# for i in range(1,n+1):
#     print("*" * i + " " * (2 *(n-i)) + "*" * i)
# for i in range(n,0,-1):
#     print("*" * i + " " * (2 *(n-i)) + "*" * i)


# *****
# *   *
# *   *
# *   *
# *****

# n=5 
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end="")
#         else:
#           print(" ",end="")
#     print("")

# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4 

# n = 4
# size = 2 * n - 1

# for i in range(size):
#     for j in range(size):
#         value = n - min(min(i, j), min(size - 1 - i, size - 1 - j))
#         print(value, end=" ")
#     print()
