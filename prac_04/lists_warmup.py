numbers = [3, 1, 4, 1, 5, 9, 2]

'''
What values do the following expressions have?
Without running the code, 
write down your answers to these questions (on paper, or in your Python file as a comment), 
then use Python to see if you were correct.
'''

'''
numbers[0]
3
numbers[-1]
2
numbers[3]
1
numbers[:-1]
[3,1,4,1,5,9]
numbers[3:4]
[1]
5 in numbers
True
7 in numbers
False
"3" in numbers
False
numbers + [6, 5, 3]
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
'''

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

'''
Write Python expressions (in the same Python file) to achieve the following:

'''

'''
Change the first element of numbers to "ten" (the string, not the number 10)
'''
numbers[0] = "ten"

'''
Change the last element of numbers to 1
'''
numbers[-1] = 1

'''
Get all the elements from numbers except the first two (slice)
'''
print(numbers[2:])

'''
Check if 9 is an element of numbers
'''
print(9 in numbers)