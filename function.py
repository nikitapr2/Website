# What is the function in python 


# a=10
# b=15
# print(a+b)









# def add (a,b):
#     return a+b

# print(add(10,39))
# print(add(10,13))
# print(add(10,145))
# print(add(10,156))
# print(add(10,14))

# def total_bill(price,quantity):
#     total=price*quantity
#     return total


# price=int(input("Enter the price:"))
# quantity=int(input("Enter the quantity:"))


# print("Total bill:",total_bill(price, quantity))



# def multiply(x):
#     for i in range(1,11):
#         print(x,"x",i,"=",x*i)
# multiply(3)


# def add():
#     a=10
#     b=30
#     print(a+b)
# add()



# # Windsurf: Refactor | Explain | Generate Docstring | X
# def add(a,b):
#     return a+b
# # Windsurf: Refactor | Explain | Generate Docstring | X
# def sub(a,b):
#     return a-b
# # Windsurf: Refactor | Explain | Generate Docstring | X
# def multiply(a,b):
#     return a*b
# # Windsurf: Refactor | Explain | Generate Docstring | X
# def div(a,b):
#     if b == 0:
#         return "Cannot divide by zero"
#     return a/b

# print(multiply(12,10))


# print(sub(100,50))

# print(div(100,5))




# def calculate_total(marks):
#      return sum(marks)
# def calculate_average(marks):
#      return sum(marks)/len (marks)
# def result(average):
#      if average >=40:
#           return "pass"
#      else:
#          return "fail"
# student_name = input("enter student name:")

# marks = []

# for i in range(1,6):
#      mark = int(input("enter marks for subject " + str(i) + ":"))
#      marks.append(mark)
# total=calculate_total(marks)
# average=calculate_average(marks)
# result=result(average)

# print("student name:",student_name)
# print("total:",total)
# print("average:",average)
# print("result:",result)



# function in python of Questions 

# Greeting function

# def welcome_student(name):
#     print(f"Welcome, {name}! We are glad to have you here.")

# welcome_student("Anushka")

# Addition function

# def add_numbers(num1, num2):
#     return num1 + num2

# result = add_numbers(40,90)
# print(result)

# Even or odd
# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(check_even_odd(9))
# print(check_even_odd(8))
# print(check_even_odd(6))

# Factorial calculator
# def factorial(n):
#     result = 1

#     for i in range(1, n + 1):
#         result *= i

#     return result
# print(factorial(4))


# 5. Largest of three number

# def largest_of_three(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
        # return b/
    # else:
        # return c

# print(largest_of_three(10, 25, 15))


# Grade calculator


# def calculate_grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     elif marks >= 60:
#         return "D"
#     else:
#         return "F"
# print(calculate_grade(85))


# List statistics
# def calculate_total(numbers):
#     return sum(numbers)

# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)

# def find_minimum(numbers):
#     return min(numbers)

# def find_maximum(numbers):
#     return max(numbers)

# numbers = [10, 20, 30, 40, 50]

# print("Total:", calculate_total(numbers))
# print("Average:", calculate_average(numbers))
# print("Minimum:", find_minimum(numbers))
# print("Maximum:", find_maximum(numbers))

# Banking application

# Initial balance
# balance = 0

# def deposit(amount):
#     global balance
#     balance += amount
#     print(f"Deposited: {amount}")

# def withdraw(amount):
#     global balance
#     if amount <= balance:
#         balance -= amount
#         print(f"Withdrawn: {amount}")
#     else:
#         print("Insufficient balance!")

# def display_balance():
#     print(f"Current Balance: {balance}")

# # Menu loop
# while True:
#     print("\n--- Banking Application ---")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Display Balance")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         amount = float(input("Enter amount to deposit: "))
#         deposit(amount)

#     elif choice == 2:
#         amount = float(input("Enter amount to withdraw: "))
#         withdraw(amount)

#     elif choice == 3:
#         display_balance()

#     elif choice == 4:
#         print("Thank you for using the Banking Application!")
#         break

#     else:
#         print("Invalid choice. Please try again.")

# Grade calculator

# def calculate_grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     elif marks >= 60:
#         return "D"
#     else:
#         return "F"

# marks = int(input("Enter marks: "))
# print("Grade:", calculate_grade(marks))

# 
# 7. List statistics

# def calculate_total(numbers):
#     return sum(numbers)

# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)

# def calculate_minimum(numbers):
#     return min(numbers)

# def calculate_maximum(numbers):
#     return max(numbers)

# # Example usage
# numbers = [12, 45, 7, 23, 56, 18]

# print("Total:", calculate_total(numbers))
# print("Average:", calculate_average(numbers))
# print("Minimum:", calculate_minimum(numbers))
# print("Maximum:", calculate_maximum(numbers))


# Student record processor
def calculate_average(marks):
    return sum(marks) / len(marks)

def get_passing_students(students, pass_mark=40):
    passing_students = []

    for student in students:
        average = calculate_average(student["marks"])
        if average >= pass_mark:
            passing_students.append(student["name"])

    return passing_students

# List of student dictionaries
students = [
    {"name": "Alice", "marks": [85, 90, 78]},
    {"name": "Bob", "marks": [35, 40, 38]},
    {"name": "Charlie", "marks": [60, 70, 65]},
    {"name": "David", "marks": [25, 30, 35]}
]

# Display average marks for each student
for student in students:
    avg = calculate_average(student["marks"])
    print(f"{student['name']} Average: {avg:.2f}")

# Display passing students
print("\nPassing Students:")
for name in get_passing_students(students):
    print(name)
