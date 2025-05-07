# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive

for i in range(0,21):
    print(i)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

for i in range(0,100000):
    print(i)


# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

x = list(range(0,100001))
print(x)
print(min(x))
print(max(x))
print(sum(x))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.

for x in range(0,21):
    if x % 2 == 1:
        print(x)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

for x in range(0,31):
    if x % 3 == 0:
        print(x)

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.


numbers = list(range(0,11))
for number in numbers:
    print(number ** 3)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.

cubes = [number ** 3 for number in range(0,11)]
print(cubes)