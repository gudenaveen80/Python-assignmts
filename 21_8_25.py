# Built-in Functions: Working with list methods (append, remove)

# Initial list
list1 = [4, 5, 4, 5, 72, 78, 8]

# 1. Using index() function to find the index of an element in the specified range
print(list1.index(72, 0, 5))  # Expected output: 4

# 2. Using extend() to add multiple elements to the list
list1.extend([[6, 7, 8], 22])
print(list1)  # Expected output: [4, 5, 4, 5, 72, 78, 8, [6, 7, 8], 22]

# 3. Adding more elements using extend()
list1.extend([23, 67, 5])
print(list1)  # Expected output: [4, 5, 4, 5, 72, 78, 8, [6, 7, 8], 22, 23, 67, 5]

# 4. Using insert() to add an element at a specific index
list1.insert(5, 7)
print(list1)  # Expected output: [4, 5, 4, 5, 72, 7, 78, 8, [6, 7, 8], 22, 23, 67, 5]

# 5. Inserting 5 at the second-to-last position (-1)
list1.insert(-1, 5)
print(list1)  # Expected output: [4, 5, 4, 5, 72, 7, 78, 8, [6, 7, 8], 22, 23, 67, 5, 5]

# 6. Inserting 8 at the second-to-last position (-1)
list1.insert(-1, 8)
print(list1)  # Expected output: [4, 5, 4, 5, 72, 7, 78, 8, [6, 7, 8], 22, 23, 67, 5, 8, 5]

# 7. Using insert() to add multiple values in one go (will give an error)
# list1.insert(1, 4, 5)  # This will raise a TypeError because insert can only take 2 arguments.


# 8. Using append() to add an element to the end of the list
list1.append(100)
print(list1)  # Expected output: [4, 5, 4, 5, 72, 7, 78, 8, [6, 7, 8], 22, 23, 67, 5, 8, 5, 100]

# 9. Using remove() to remove the first occurrence of a value
list1.remove(5)
print(list1)  # Expected output: [4, 5, 4, 72, 7, 78, 8, [6, 7, 8], 22, 23, 67, 5, 8, 100]

# 10. Using remove() to remove a value that doesn't exist (will raise ValueError)


# Edge Cases for append() and remove()

# Case 1: Appending None to the list (adds None as a valid element)
list1.append(None)
print( list1)  # Expected output: list with None at the end

# Case 2: Appending an empty list to the list (adds a list as an element)
list1.append([])
print(list1)  # Expected output: list with an empty list at the end

# Case 3: Removing an element when the list is empty (will raise ValueError)
empty_list = []
print(empty_list.remove(1))
# ValueError: list.remove(x): x not in list

# Case 4: Remove all occurrences of the same value
# Removing all occurrences of 5 from the list (by using a loop)
while 5 in list1:
    list1.remove(5)
print(list1)  # Expected output: list without any 5's

# Case 5: Removing the last element of the list
list1.remove(100)  # Remove the last added element (100)
print(list1)  # Expected output: list without 100

# Initial list
list1 = [4, 5, 4, 5, 72, 78, 8]

# 11. Using pop() to remove and return an element at a specific index
# Popping the last element of the list (default behavior)
res = list1.pop()
print(res)  # Expected output: 8 (the last element)
print(list1)  # Expected output: list without the last element

# 12. Popping an element at a specific index (popping the element at index 0)
res_2 = list1.pop(0)
print(res_2)  # Expected output: 4 (the first element)
print(list1)#prints remaining elements except 4

list1.clear()
print(list1)#Expected output:Empty list[]

empty_list.reverse()
print(empty_list)# Expected output: empty_list

