# ===============================
#        PYTHON LOOPS NOTES
#        Author: Rohit Rana
# ===============================

print("\n----- 1. FOR LOOP -----")
for i in range(5):
    print("For loop iteration:", i)


print("\n----- 2. WHILE LOOP -----")
count = 0
while count < 5:
    print("While loop count:", count)
    count += 1


print("\n----- 3. LOOP WITH BREAK -----")
for i in range(10):
    if i == 5:
        break
    print("Breaking at:", i)


print("\n----- 4. LOOP WITH CONTINUE -----")
for i in range(5):
    if i == 2:
        continue
    print("Skipping 2:", i)


print("\n----- 5. FOR-ELSE LOOP -----")
for i in range(3):
    print("Loop:", i)
else:
    print("Else executes when loop completes fully")


print("\n----- 6. WHILE-ELSE LOOP -----")
x = 0
while x < 3:
    print("x:", x)
    x += 1
else:
    print("While loop else executed")


print("\n----- 7. RANGE FUNCTION -----")
print("range(5):", list(range(5)))
print("range(2, 10, 2):", list(range(2, 10, 2)))


print("\n----- 8. ENUMERATE (for index + value) -----")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


print("\n----- 9. ZIP LOOP (loop over two lists) -----")
names = ["Rohit", "Kirti", "Aman"]
ages = [21, 22, 20]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


print("\n----- 10. NESTED LOOPS -----")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


print("\n----- 11. LIST COMPREHENSION -----")
squares = [x * x for x in range(5)]
print("Squares:", squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)


print("\n----- 12. DICT COMPREHENSION -----")
numbers = {x: x*x for x in range(5)}
print("Dictionary:", numbers)


print("\n----- 13. SET COMPREHENSION -----")
unique_squares = {x * x for x in range(5)}
print("Unique squares set:", unique_squares)


print("\n----- 14. LOOPING THROUGH DICTIONARY -----")
student = {"name": "Rohit", "age": 21, "course": "Python"}

for key, value in student.items():
    print(key, ":", value)


print("\n----- 15. PATTERN PRINTING (STAR) -----")
for i in range(1, 6):
    print("*" * i)


print("\n----- 16. REVERSE LOOP -----")
for i in range(10, 0, -1):
    print(i, end=" ")


print("\n\n----- 17. FACTORIAL USING LOOP -----")
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of 5 =", fact)


print("\n----- 18. SUM OF LIST USING LOOP -----")
nums = [10, 20, 30, 40]
total = 0
for n in nums:
    total += n
print("Total:", total)


print("\n----- 19. LOOP OVER STRING -----")
for ch in "ROHIT":
    print(ch)


print("\n----- 20. INFINITE LOOP (use carefully) -----")
# Commented to avoid infinite run
# while True:
#     print("Press Ctrl + C to stop")
