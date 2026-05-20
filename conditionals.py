# Basic Conditionals in Python

# if-else statement
# x = 10
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is not greater than 5")

# if-elif-else statement
# y = 15
# if y < 10:
#     print("y is less than 10")
# elif y == 15:
#     print("y is equal to 15")
# else:
#     print("y is neither less than 10 nor equal to 15")


'''1. Check whether a character is a vowel or consonant.'''

# char = input("Enter a character: ").lower()
# if char in 'aeiou':
#     print(char, "is a vowel.")
# elif char.isalpha():
#     print(char, "is a consonant.")
# else:
#     print("Invalid input. Please enter a single alphabetic character.")        

'''2. Check whether a number is divisible by 5 and 11.'''

# num = int(input("Enter a number: "))
# if num % 5 == 0 and num % 11 == 0:
#     print(num, "is divisible by both 5 and 11.")
# else:
#     print(num, "is not divisible by both 5 and 11.")    


# List

'''1. Create a list of 5 fruits and print them.'''

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# print("Fruits:", fruits)

'''2. Add a new fruit to the list and print the updated list.'''

# new_fruit = "mango"
# fruits.append(new_fruit)
# print("Updated fruits:", fruits)

'''3. Remove a fruit from the list and print the updated list.'''

# fruit_to_remove = "banana"
# if fruit_to_remove in fruits:
#     fruits.remove(fruit_to_remove)
#     print("Updated fruits after removal:", fruits)


'''4. Print the first and last element.'''    

# print("First fruit:", fruits[0])
# print("Last fruit:", fruits[-1])


'''5. Reverse a list.'''

# fruits.reverse()
# print("Reversed fruits:", fruits)


'''6. Sort a list of numbers in ascending order.'''

# numbers = [5, 2, 9, 1, 5]
# numbers.sort()
# print("Sorted numbers:", numbers)


'''7. Sort a list of numbers in descending order.'''

# numbers.sort(reverse=True)
# print("Sorted numbers in descending order:", numbers)

'''8. Find the maximum and minimum element.'''

# max_num = max(numbers)
# min_num = min(numbers)
# print("Maximum number:", max_num)
# print("Minimum number:", min_num)


'''9. Count how many times an item appears.'''

# item_to_count = 5
# count = numbers.count(item_to_count)
# print(item_to_count, "appears", count, "times in the list.")


'''10. Merge two lists.'''

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# merged_list = list1 + list2
# print("Merged list:", merged_list)


# Tuple

'''1. Create a tuple of 5 colors and print them.'''

# colors = ("red", "green", "blue", "yellow", "purple")
# print("Colors:", colors)

'''2. Count occurrences of an element.'''

# color_to_count = "blue"
# count = colors.count(color_to_count)
# print(color_to_count, "appears", count, "times in the tuple.")


'''3. Find the index of an element.'''

# color_to_find = "yellow"
# if color_to_find in colors:
#     index = colors.index(color_to_find)
#     print(color_to_find, "is at index", index, "in the tuple.")


'''4. Convert tuple to list.'''

# colors_list = list(colors)
# print("Colors as a list:", colors_list)


# Set
'''1. Create a set of 5 unique numbers and print them.'''

# num = {1, 2, 3, 4, 5}
# print("Set:", num)

'''2. Remove an element from the set and print the updated set.'''

# num = {1, 2, 3, 4, 5}
# num.remove(3)
# print("Updated set after removal:", num)


'''3. Find union of two sets.'''

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1.union(set2)
# print("Union of set1 and set2:", union_set)


'''4. Find intersection of two sets.'''

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# intersection_set = set1.intersection(set2)
# print("Intersection of set1 and set2:", intersection_set)


'''5. Find difference of two sets.'''

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# diff_set = set1.difference(set2)
# print("Difference of set1 and set2:", diff_set)


'''6. Check if an item exists in a set.'''

# item_check = 2
# num_set = {1, 2, 3, 4, 5}
# if item_check in num_set:
#     print(item_check, "exists in the set.")
# else:
#     print(item_check, "does not exist in the set.")    


# Dictionary

'''1. Create a dictionary with 5 key-value pairs and print it.'''

student = {
    "name": "Karthik",
    "age": 20,
    "major": "Computer Science",
    "GPA": 9.8,
    "is_student": True
}
print("Student Details:", student)


'''2. Access a value using its key.'''

print("Name:", student["name"])
print("Age:", student["age"])


'''3. Add a new key-value pair.'''

student["university"] = "XYZ University"
print("Updated Student Details:", student)


'''4. update the value of an existing key.'''

student["GPA"] = 9.9
print("Updated Student Details with new GPA:", student)


'''5. Remove a key-value pair.'''

del student["is_student"]
print("Updated Student Details after removal:", student)


'''6. Print all keys.'''

print("Keys in the student dictionary:", student.keys())


'''7. Print all values.'''

print("Values in the student dictionary:", student.values())


'''8. Iterate through dictionary items.'''

for key, value in student.items():
    print(key + ":", value)


'''9. Check if a key exists in the dictionary.'''    

key_to_check = "major"
if key_to_check in student:
    print(key_to_check, "exists in the student dictionary.")
else:
    print(key_to_check, "does not exist in the student dictionary.")    


