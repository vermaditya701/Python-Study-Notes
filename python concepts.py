# #todo: Input function
# name = input("Enter your name: ")
# print(name)
# #Input function for integer
# age = int(input("Enter your age: "))
# print(age)



 # #todo: Multiple I/p in one line
# a,b = input("Enter two numbers: ").split()
# a = int(a)
# b = int(b)
# print(a, b)


# #OR
# a,b = map(int, input("Enter two numbers: ").split())   
# print(a, b)


# a = int(a)
# b = int(b)
# print(a + b) 



# #todo: Swapping values
# c,d = 20,30
# print(c,d) #output: 20 30

# a = 10
# b = 20
# t = a
# a = b
# a,b = b,a #?swapping without temp variable
# print(a,b) = t
# print(a,b)   #output: 20 10

# #OR


# #Todo: Chained comparison operators
# print(10<30<20)     #10<30 and 30<20  #output: False
# print(10>30<20)     #10>30 and 30<20  #output: False
# print(10>30>20)     #10>30 and 30>20  #output: False

# print(bool(True))
# print(bool(" "))
# print(int(False))
# a=5
# b=2



# #todo: Float Division (/)
# ➤ What it does
# Divides two numbers
# Always returns a float, even if the result is a whole number

# a /b  float division
# print(a) #output: 5

# #todo: Floor Division (//)
# ➤ What it does
# Divides and removes the decimal part
# Returns the floor value (rounds down, not toward zero)

# a // b  #floor division
# print(a) #output: 5
# a % b   #modulus
# print(a) #output: 5

# print(2**2**2)  #output: 16
# print(True + True)  #output: 2
# print(True + False) #output: 1
# print(False + False) #output: 0



# #todo: if-else
# age  = int(input("ENTER YOO AGE : "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")


#     #todo: ternary operator
# result = "Adult" if age >= 18 else "Minor"  
# print(result)



# #todo: check if a number is even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# #OR by using:
# #ternary operator
# result = 'Even' if num%2==0 else'Odd'
# print(result)



# #todo: check if a number is positive, negative or zero 
# num = int(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is positive")
# elif num < 0:
#     print(f"{num} is negative")
# else:
#     print(f"{num} is zero")



# z,y = int(input("enter a number: ")).split()
#? print(z+y)           this is wrong :
#                               input() returns a string
#                               .split() works only on strings
#                               int() converts to an integer → integers don’t have .split()

# so corrected code is:

# data = input("Enter two numbers: ")  # "10 20"
# parts = data.split()                # ["10", "20"]
# z = int(parts[0])
# y = int(parts[1])
# print(z + y)
# #or
# z, y = map(int, input("Enter two numbers: ").split())
# print(z + y)


# #todo: switch case statement
# day = int(input("Enter day number (1-7): "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day number")



#todo: for loop
# for i in range(1, 6):
#     print(i)

# for i in range(10,1,-2):
#      print(i)






# #Todo: make a right angle triangle using for-loop  
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")



#  #todo: while loop
# count = 1
# while count <= 5:
#     print(count)
#     count += 1
# print("Done")



# #Todo: reverse the digits
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# print("Reversed Number:", rev)


# #todo: 5check the number is prime or not
# num = int(input("Enter a number: "))
# is_prime = True
# if num <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")


# # #todo: check palindrome
# num = int(input("Enter a number: "))
# original_num = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# if original_num == rev:
#     print(f"{original_num} is a palindrome")
# else:
#     print(f"{original_num} is not a palindrome")


# # #todo: check is a number is Armstrong or not 
# #?An Armstrong number (also called a Narcissistic number) is:
# #?A number that is equal to the sum of its own digits, each raised to the power of the number of digits.

# #? For example, 153 is an Armstrong number because:
# #? 1^3 + 5^3 + 3^3 = 153
# #?3-digit: 153, 370, 371, 407 are some of the Armstrong numbers.

# num = int(input("Enter a number: "))
# original_num = num
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum += digit ** 3
#     num //= 10
# if original_num == sum:
#     print(f"{original_num} is an Armstrong number")
# else:
#     print(f"{original_num} is not an Armstrong number")


# # #? print 1
# # #?       2 3
# # #?       4 5 6
# # #?       7 8 9 10
# num = 1
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     print()
    

# #? print  10
# #?        9 8
# #?        7 6 5
# #?        4 3 2 1
# num = 10
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num -= 1
#     print()



# #todo:print multiplication table
# num = int(input("Enter a number: "))   
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# # #? print 2 
# # #?       4
# # #?       6 
# # #?       8
# # #?       10 8 6 4 2
# # #?       8
# # #?       6 
# # #?       4
# # #?       2

# num = 2
# for i in range(1, 6):
#     if i < 5:
#         print(num * i)
#     else:
#         for j in range(5, 0, -1):
#             print(num * j, end=" ")
#         print()

# for i in range(4,0,-1):
#         print(num * i)


# #TODO: format specifiers
# value = 42
# print("The answer is %d" % value)  # Using %d for integers
# print("The answer is %o" % value)  # Using %o for octal
# print("The answer is %x" % value)  # Using %x for hexadecimal
# print("The answer is %X" % value)  # Using %X for uppercase hexadecimal
# print("The answer is %.2f" % value)  # Using %.2f for floating-point with 2 decimal places
# print("The answer is %e" % value)  # Using %e for scientific notation
# print("The answer is %E" % value)  # Using %E for uppercase scientific notation
# print("The answer is %c" % value)  # Using %c for character representation
# print("The answer is %s" % value)  # Using %s for string representation
# print("The answer is %%")  # Using %% to print a literal percent sign
# print("The answer is %10d" % value)  # Width of 10, right-aligned
# print("The answer is %-10d" % value)  # Width of 10, left-aligned
# print("The answer is %010d" % value)  # Width of 10, zero-padded
# print("The answer is %.5d" % value)  # Precision of 5, leading zeros
# print("The answer is %*.*f" % (8, 3, 3.14159))  # Width of 8, precision of 3
# print("The answer is %(value)d" % {'value': value})  # Using named placeholders
# print("The answer is %%(value)d" % {'value': value})  # Literal percent sign with named placeholder



# # #todo: formated string literals (f-strings)
# name = "Alice"
# age = 30
# print(f"My name is {name} and I am {age} years old.")
# #OR 
# print("My name is {} and I am {} years old.".format(name, age))
# #OR
# print("My name is %s and I am %d years old." % (name, age))


# print(r"C:\Users\ASUS\Downloads\PEP Classes\notes.txt") ##?r: raw string


# #todo: convert lowercase to uppercase
# name = "Lpu"
# print(name.upper())
# #?convert uppercase to lowercase
# print(name.lower())

# #?convert first character to uppercase
# print(name.capitalize())

# #?convert first character of each word to uppercase
# print(name.title())

# #?convert uppercase to lowercase and vice-versa
# print(name.swapcase())

# #?remove whitespace from start and end
# name_with_spaces = "  Lpu  "
# print(name_with_spaces.strip())

# #?remove whitespace from start
# print(name_with_spaces.lstrip())

# #?remove whitespace from end
# print(name_with_spaces.rstrip())

# #?replace substring
# print(name.replace("L", "P"))

# #?find substring index
# print(name.find("p"))

# #?check if all characters are alphabetic
# print(name.isalpha())

# #?check if all characters are digits
# print(name.isdigit())

# #?check if all characters are alphanumeric
# print(name.isalnum())

# #?split string into list
# print(name.split("p"))

# #?join list into string
# print("-".join(["L", "p", "u"]))

# #?count occurrences of substring
# print(name.count("u"))

# #?length of string
# print(len(name))

# #?reverse a string
# print(name[::-1])

# #?check if string starts with substring
# print(name.startswith("Lp"))

# #?check if string ends with substring
# print(name.endswith("pu"))

# #?center a string with padding
# print(name.center(10, "*"))

# #Todo: list methods
# lst = [1, 2, 3, 4, 5]
# lst.append("grrrr")
# print(lst)

# #?for reverse the list
# lst.reverse()
# for i in lst:
#     print(i)
    
#?to pop the last element
# item = ['a', 'b', 'c', 'd']
# item.pop()
# print(item)
# #?to pop element at specific index
# item.pop(1)
# print(item)
# #?to remove specific element
# item.remove('a')
# print(item)
# #?to sort the list
# item.sort()
# print(item)


#?# Shopping List Program

#create an empty shopping list
# item = []
# #now store number of items in the list
# n = int(input("Enter number of items: "))
# for i in range(n):
#     value = input("Enter item: ")
#     item.append(value)
# print("Items in the list:")
# for i in item:
#     print(i)
# #add a new item to the list
# new_item = input("Enter a new item to add: ")
# item.append(new_item)
# #print first item
# print("First item:", item[0])
# #print last item
# print("Last item:", item[-1])
# #print total number of items
# print("Total number of items:", len(item))
# #print the enire shopping list
# print("Shopping list:", item)
# #print the item that are impoartant to buy from the shopping list:print"Laptop" and "shoes"
# important_items = ["Laptop", "shoes"]
# print("Important items to buy:")
# for i in item:
#     if i in important_items:
#         print(i)
# #change the item from the shopping list: Instead of "pen" I want to buy "Notebook"lets change the item stored in the list.
# if "pen" in item:
#     index = item.index("pen")
#     item[index] = "Notebook"
# print("Updated shopping list:", item)

# #delete the item from the shopping list that is not required. lets delete items that are unimportant, such as: I dont want to buy Clothes, lets delete it.
# if "Clothes" in item:
#     item.remove("Clothes")
# print("Shopping list after deleting unimportant items:", item)
# #print the final shopping list
# print("Final shopping list:", item)




# #todo: Dictionary methods
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# # #?get value by key
# print(my_dict.get('b'))
# # #?get all keys
# print(my_dict.keys())
# # #?get all values
# print(my_dict.values())
# # #?get all items
# print(my_dict.items())
# # #?add or update key-value pair
# my_dict.update({'d': 4})
# print(my_dict)
# # #?remove key-value pair
# my_dict.pop('a')
# print(my_dict)
# # #?clear dictionary
# my_dict.clear()
# print(my_dict)


#Create an empty dictionary: first you need to create an empty dictionary, where you willbestoring the product details.
# products = {} 
# #OR
# # products = dict()

# #Store the first prodcut details in variable 
# #product name = Mobile Phone 
# #Prodcut quantity = 5
# #product price = 20000
# #product Release Year = 2020
# products['Mobile Phone'] = {
#     'quantity': 5,
#     'price': 20000,
#     'release_year': 2020
# }
# #Add the second product details in a variable
# #product name = Laptop
# #Prodcut quantity = 10
# #product price = 50000
# #product Release Year = 2023
# products['Laptop'] = {
#     'quantity': 10,
#     'price': 50000,
#     'release_year': 2023
# }
# #add the item detail into the inventory
# #Display the product presents in the inventory.Use print statement to show the product details stored in the dictionary.
# print("Products in Inventory:")
# for product, details in products.items():
#     print(f"Product: {product}")
#     for key, value in details.items():
#         print(f"  {key.capitalize()}: {value}")
# #check if ProductN01_releaseYear and ProductN02_price are present in the inventory
# product_name_1 = 'Mobile Phone'
# product_name_2 = 'Laptop'
# if product_name_1 in products:
#     print(f"{product_name_1} release year: {products[product_name_1]['release_year']}")
# if product_name_2 in products:
#     print(f"{product_name_2} price: {products[product_name_2]['price']}")
#     #delete release year of both the products from the inventory
# del products[product_name_1]['release_year']
# del products[product_name_2]['release_year']
# print("Updated Products in Inventory after deleting release year:")
# for product, details in products.items():
#     print(f"Product: {product}")
#     for key, value in details.items():
#         print(f"  {key.capitalize()}: {value}")


# #OR
# dct = {}
# dct["Product1Name"] = "Mobile Phone"
# dct["Product1Quantity"] = 5
# dct["Product1Price"] = 20000
# dct["Product1ReleaseYear"] = 2020

# print(dct)



# #?using dict() with two lists(zip)
# keys = ['name', 'age', 'city']        #?zip function is used to combine two lists into a dictionary 
# values = ['Alice', 30, 'New York']
# person = dict(zip(keys, values))


# # #?using dict() with list of tuples
# d = dict([("a", 1), ("b", 2), ("c", 3)])
# print(d)

# # #todo: set methods

# s = set()     #?empty set
# print(type(s))          #<class 'set'>

# a={1,2,3,4,5}   #?set with elements
# b={6,7,8,9,10}
# print(a&b)   #OR print(a.intersection(b))  #?intersection
# print(a|b)   #OR print(a.union(b))         #?union
# print(a-b)   #OR print(a.difference(b))    #?difference

#create a list that contains first 10 natural numbers
# natural_numbers = list(range(1, 11))
# print("Natural Numbers:", natural_numbers)


# #OR
# natural_numbers = []
# for i in range(1, 11):
#     natural_numbers.append(i)
# print("Natural Numbers:", natural_numbers)


# print("Even No: ")
# lst2 = [x for x in range(1,11)]
# for x in lst2:
#           if x % 2 == 0:       
#             #  print(x, end=" ")   #?end=" " is used to print in same line with space between them

     

# #todo: functions
# def function_name(parameters):
#     # function body
#     # code to be executed
#     return value  # optional    
# #function call


# #?create a function that accepts number from user as an argument and it returns a list of odd numbers upto that number
# n = int(input("Enter a number: "))

# def odd_numbers(n):
#     odd_nums = []
#     for i in range(1, n + 1):
#         if i % 2 != 0:
#             odd_nums.append(i)
#     return odd_nums
# print(odd_numbers(n))


# #?create a function that accepts a string as an argument and it returns the reverse of that string
# def reverse_string(s):   
#     return s[::-1]
# str_input = input("Enter a string: ")
# print("Reversed String:", reverse_string(str_input))


# def add(a=10, b=8):   #default arguments
#     return a+b

# print(add(b=100,a=9)) #if only b=100 is passed then the fxn. will take default value of a since it has been not passed 


# def add(*b):     # #? *b means variable-length positional arguments. It allows the function to accept any number of arguments.
#     sum =0
#     for i in b:
#         sum += i
#     return sum
# print(add(10,20,70,100,50))


#Create an Employee Salary Calculator 
#given that, HRA=20% of basic, DA = 10% of basic, Tax = 12% of total salary
#Return net salary= gross salary(base +HRA+ DA)- tax 
# def calc():
#     basic = float(input("Enter basic salary: "))
#     hra = 0.20 * basic
#     da = 0.10 * basic
#     gross_salary = basic + hra + da
#     tax = 0.12 * gross_salary
#     net_salary = gross_salary - tax
#     print(f"Gross Salary: {gross_salary}")
#     print(f"Tax: {tax}")
#     print(f"Net Salary: {net_salary}")
# calc()


# #create a function calculate_bill(amount,gst=18,discount=0) for a SaaS product 
# #Logic: gst applied on amount, discount applied after gst, return final payable amount 
# def cacluclate_bill(amt,gst=18, discount=0):   #default arguments
#    gst_amt = amt*gst/100
#    total = amt + gst_amt
#    final_amt = total - (total*discount/100)
#    return final_amt

# print(cacluclate_bill(1000))
# print(cacluclate_bill(1000,discount=10))
# print(cacluclate_bill(1000, gst=12, discount=15))



#Create a list that will contain some values from 1-10 
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(lst)
# # #todo: Create another two list that will extract the even and odd number from the existing list and print the two separate lists
# even_numbers = []
# odd_numbers = []
# for i in lst:
#     if i % 2 == 0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)
# print("Even Numbers:", even_numbers)
# print("Odd Numbers:", odd_numbers)


# #todo: do this using functions
# def extract_even_odd(numbers):
#     even_nums = []
#     odd_nums = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_nums.append(num)
#         else:
#             odd_nums.append(num)
#     return even_nums, odd_nums
# even_numbers, odd_numbers = extract_even_odd(lst)
# print("Even Numbers:", even_numbers)
# print("Odd Numbers:", odd_numbers)


#? **global vs local variable**
# x = 10  # global variable
# def my_function():
#     y = 5  # local variable
#     print("Inside function, y =", y)
#     print("Inside function, x =", x)  # accessing global variable
# my_function()
# print("Outside function, x =", x)
# print("Outside function, y =", y)  # This will raise an error because y is not defined outside the function


# a= 10  # global variable
# def add():

#     global a
#     a = 20  # modifying global variable
#     print(globals())   #?globals() is a built-in function in Python that returns a dictionary representing the current global symbol table. It contains all global variables and their values.
#     globals()['a'] = 900
#     print("inside function, a =", a)
# add()       
# print("Outside function, a =", a )





#create a fxn. calculate_cart_total(*prices)
#requirements:
#1. it should accept any number of item prices
#2. Apply: 5% discount if total price > 5000
#3. return final payable amt.
#Example: calculate_cart_total(1200,2500,900)

# def calculate_cart_total(*prices):
#     total = sum(prices)
#     if total > 5000:
#         discount = total * 0.05
#         total -= discount
#     return total
# print(calculate_cart_total(1200,2500,900))
# print(calculate_cart_total(2000,3500,1800,900))


# #todo: * and **kwargs in functions (kwargs= keyword arguments)
# def func(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
# func(1, 2, 3, name="Alice", age=30)
# print(func('adi'))    #arguments
#info() #?info() is used to get the information about the function such as its name, docstring, module, and other attributes.





# #todo: Create a fxn. update_profile(user_id, **details)
#requirements:
#1. mandatory parameter: user_id
#2. optional fields via **kwargs: name, email, phone, location
#store & return profile data as dictionary 
#Example: update_profile(101, name="Adi", email="adi@example.com",city="Delhi")
# def update_profile(user_id, **details):
#     profile = {'user_id': user_id}  
#     for key, value in details.items():  #?items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
#         profile[key] = value
#     return profile
# print(update_profile(101, name="Adi", email="adi@example.com",city="Delhi"))


#or
# def update_profile(user_id, **details):
#     profile = {'user_id': user_id}
#     profile.update(details)   #?The update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.
#     return profile
# print(update_profile(101, name="Adi", email="adi@example.com",city="Delhi"))



# #todo: lambda function
#?lambda functions are small anonymous functions
#syntax: lambda arguments: expression
#example:
# x = lambda a : a + 10
# print(x(5))


#Ex-> 1: regular function to calculate square of a number
# def func(num):
#     return num*num
# print(func(4))


# func1 = lambda num: num * num 
# print(func1(4))

# add = lambda x, y: x + y
# print(add(5, 3))  # Output: 8
# subtract = lambda x, y: x - y
# print(subtract(5, 3))  # Output: 2


# #Todo: filter() method   #used to filter elements from an iterable based on a condition
# ?syntax: filter(function, iterable)   #or filter(lambda x: condition, iterable)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4, 6, 8, 10]


# #todo: Design a fxn. process_applications(*candidates,**criteria)
#requirements:
#1. each candidate is represented as a dictionary:
#{"name":"Ravi","experience":2,"skills":["Python","Django"]"}
#Criteria via **kwargs:
#min_experience
#required_skills
#Example:
#c1 = {"name":"Ravi","experience":2,"skills":["Python","Django"]}

# def process_applications(*candidates, **criteria):
#     selected_candidates = []
#     min_experience = criteria.get('min_experience', 0)        #?0 is default value if min_experience is not provided
#     required_skills = criteria.get('required_skills', [])     #?[] is default value if required_skills is not provided
#     for candidate in candidates:
#         if candidate['experience'] >= min_experience and required_skills in candidate['skills']:
#             selected_candidates.append(candidate)
#     return selected_candidates

# c1 = {"name":"Ravi","experience":2,"skills":["Python","Django"]}
# c2 = {"name":"Anita","experience":5,"skills":["Java","Spring"]}
# print(process_applications(c1,c2,min_experience=3, required_skills="Python"))





# #todo: reduce() method
# ?The reduce() function is used to apply a specified function to the elements of an iterable, cumulatively reducing the iterable to a single value.
# ?syntax: reduce(function, iterable)
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # Output: 120

# # #Example 2: Find the maximum value in a list
# max_value = reduce(lambda x, y: x if x > y else y, numbers) 
# print(max_value)  # Output: 5

# # #Example 3: Concatenate a list of strings
# strings = ["Hello", " ", "World", "!"]
# concatenated = reduce(lambda x, y: x + y, strings)
# print(concatenated)  # Output: Hello World!



# #todo: Recursion
# ?Recursion is a programming technique where a function calls itself.
# ?It's used to solve problems that can be broken down into smaller, similar subproblems.
# ?A recursive function typically has two parts:
# ?1. Base case: A condition that stops the recursion.
# ?2. Recursive case: A call to the same function with modified arguments.

# Example: #?Calculate factorial of a number using recursion
# def factorial(n):
#     if n == 0:     #base case
#         return 1
#     else:
#         return n * factorial(n-1)    #recursive case

# print(factorial(5))  # Output: 120

# # Example: #?Calculate the nth Fibonacci number using recursion
# def fibonacci(n):
#     if n <= 0:      #base case
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)   #recursive case

# print(fibonacci(10))   


# def fun(n):
#     if n<5:
#         return fun(n+1)
#     print(n)
#     return
# fun(2)


# #?create a recursion fxn to print 5,4,3,2,1
# def print_reverse(n):
#     if n == 0:
#         return     #?return statement to exit the function when n reaches 0
#     else:
#         print(n, end=" ")
#         print_reverse(n - 1)

# print_reverse(5)  




# #todo: Higher-Order Functions
# ?Higher-order functions are functions that can take other functions as arguments or return functions as results
# #Example: A function that takes another function as an argument

# def apply_function(func, value):
#     return func(value)
# def square(x):
#     return x * x
# def cube(x):
#     return x * x * x

# result = apply_function(square, 5)
# print(result)  # Output: 25
# result = apply_function(cube, 3)
# print(result)  # Output: 27


#example->
# def cube(n):
#     return n*n*n
# def square(n):
#     return n*n

# def operative(value,func):
#     for i in value:
#         result = func(i)
#         print(result)

# val = [1,2,3,4]
# res = operative(val,cube)
# print(res)
# res = operative(val,square)
# print(res)


#todo: Student Result Analyzer
#Given a list of student marks:
# marks = [45,78,90,32,67,88,54]
#Tasks:
#1. use filter() to get passing marks(>=40)
#2. use map() to add grace marks of 5 to each passing mark
#3. use reduce() to calculate total marks
# from functools import reduce
# marks = [45,78,90,32,67,88,54]

# passing_marks = list(filter(lambda x: x >= 40, marks))
# print("Passing Marks:", passing_marks)

# grace_marks = list(map(lambda x: x + 5, passing_marks))
# print("Grace Marks:", grace_marks)

# total_marks = reduce(lambda x, y: x + y, grace_marks)
# print("Total Marks:", total_marks)




# #todo: Role-based salary Modifier
#create a higher-order fxn. salary_processor(func, salaries)
#requirements:
#func defines salary modification
#salaries is a list of base salaries

#Exsample:
# def increment(salary):
#     return salary + 5000            
# def salary_processor(func, salaries):
#     modified_salaries = []
#     for sal in salaries:
#         modified_salaries.append(func(sal))
#     return modified_salaries


# print(salary_processor(increment, [30000,40000,50000]))




# #todo: inner() and outer() fxn.
#inner fxn. is defined inside the outer fxn.
#inner fxn. can access variables from outer fxn.

#ex1.
# def outer():  
#     print("outer fxn.")

#     def inner():
#         print("inner fxn.")

#     return inner
    
# res = outer()
# res()


#ex2.   
# def outer():
#     print("outeer fxn.")

#     def inner():
#         print("inner fxn.")

# outer()
# inner() #?inner is not defined 

#ex3.
# def outer():  
#     print("outer fxn.")

#     def inner():
#         print("inner fxn.")

#     return inner

# res = outer()
# print(res)   #?You are printing the function object, not calling it.
# res()          #?Now you call the function stored in res.


#ex4.
# def outer():  
#     print("outer fxn.")

#     def inner(n):
#         print("inner fxn.",n)

#     return inner
    
# res = outer()
# print(res)
# res(50)




# #todo: Decorators
#?A decorator is a special type of higher-order function that modifies the behavior of another function without changing its code.
#?Decorators are often used for logging, access control, caching, and other cross-cutting concerns.
#Example:
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(f"Wrapper executed before {original_function.__name__}")
#         return original_function(*args, **kwargs)
#     return wrapper_function
# @decorator_function
# def display():
#     print("Display function executed.")
# display()

# #OR

# # def display():
# #     print("Display function executed.")
# # decorated_display = decorator_function(display)
# # decorated_display()
# #Output:
# # Wrapper executed before display
# # Display function executed.


# #Example 2:
# def uppercase_decorator(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper  
# @uppercase_decorator   #?using @ syntax to apply decorator.  @ = decorator. It adds extra behavior
# def greet():
#     return "Hello, welcome to the world of decorators!"
# print(greet())  # Output: "HELLO, WELCOME TO THE WORLD OF DECORATORS!"



#ex3.
# def check(func):
#     def wrap(a,b):
#         if a<b:
#             a,b=b,a
#             return func(a,b)
#         return wrap()
    
# def div(a,b):
#     return a/b

# def sub(a,b):
#     return a-b

# sub = check(sub)  #decorator 


#? ==========================UNDERSTANDING===============================

#when you write-

#@uppercase_decorator
# def greet():
#     ...

# #python rewrites your code internally as: 
# def greet():
#     return "Hello, welcome to the world of decorators!"

# greet = uppercase_decorator(greet)

# print(greet())

#So greet is replaced by the wrapper function returned by uppercase_decorator.


# #todo: create a new file to find the squared root of 25

# def squared_root(func):
#     def wrapper(n):
#         result = func(n)
#         return result ** 0.5
#     return wrapper
# @squared_root
# def get_number(n):
#     return n
# print(get_number(25))  


# #todo: Math fxn. 
# import math 
# a = int(input("enter a number: "))
# print(a**(0.5))
# print(math.pow(4,2))
# print(math.sqrt(a))
# print(math.floor(3.5))
# print(math.ceil(3.5))


# import random as r

# print(r.random())
# print(r.randint(2, 9))        #inclusive of both 2 and 9
# print(r.randrange(2, 9))        #exclusive of 9
# print(r.choice(['apple', 'banana', 'cherry']))       #random choice from the list
# print(r.sample(range(1, 50), 5))  #?lottery numbers   #random sample of 5 numbers from 1 to 49



# #todo: take an input from user and let him guess the number..if the number matches the random number generated by the system then print "You Win" else "Try Again" 
# #todo: and also count the number of attempts made by the user to guess the correct number
# import random as r
# random_number = r.randint(1,5)
# attempts = 0
# while True:   #infinite loop until break
#     user_guess = int(input("Guess a number between 1 and 5: "))
#     attempts += 1
#     if user_guess == random_number:
#         print(f"You Win! The correct number was {random_number}.")
#         print(f"Number of attempts: {attempts}")
#         break
#     elif user_guess < random_number:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")




# #todo: EMI Calculator for Loan Portal 
#create a fxn. calculate_emi(principal,rate,tenure) using math
#Logic:
#  EMI formula: EMI= p*r*(1+r)^n/ ((1+r)^n-1)
# where r = monthly interest rate
#       n = tenure in months  

# import math
# def emi_calc(principal,rate,tenure):
#     r = rate / (12 * 100)  #monthly interest rate
#     n = tenure * 12        #tenure in months
#     emi = principal * r * math.pow((1 + r),n) /math.pow((1 + r),n - 1)
#     return emi
# principal = float(input("Enter principal amount: "))
# rate = float(input("Enter annual interest rate (in %): "))
# tenure = int(input("Enter tenure (in years): "))
# emi = emi_calc(principal, rate, tenure)
# print(f"Your monthly EMI is: {emi:.2f}")

    

# #todo: Random Module -OTP & Load Generator
#Create a fxn. generate_otp()
#Requirements:
# generate 6 digit numeric OTP
# should be random every time 
# simulate 5 OTP Generations

# import random as r 
# count = 0

# def generate_otp():
#     global count  # Need to declare global to modify it
    
#     if count >= 5:
#         print("Today's limit Reached!!")
#         return
    
#     otp = r.randint(100000, 999999)
#     count += 1
#     print(f"OTP {count}: {otp}")

# Simulate 5 OTP generations (try 7 times to test the limit)

#_ is a convention meaning "I don't need this variable"
#Use when you only care about repeating an action, not the counter value
# for _ in range(0,7):    #? for i in range(0,7):   ==both r almost same==
#     generate_otp()



#  #todo: Assignment6: Inner Fxn. - Access control Logic
#Prblm Statement: Bank Transaction Authorization
#create a fxn. bank_transaction(user_role)
#Logic:
# inner fxn. authorize(amt.)
# Rules:
#   admin -> unlimited transaction
#   user  -> max $5,000
# return approval or denial 

# def bank_transaction(user_role):


#     def authorize(amt):
#         if user_role == 'admin':
#             return "Transaction Approved!"
#         elif user_role == 'user' and amt <=5000:
#             return "Transaction Approved"
#         else:
#             return "Transaction not Approved"
#     return authorize
    
# transaction = bank_transaction('admin')
# print(transaction(7000))



# #todo: DATETIME 
# import datetime     #?datetime module is used to work with dates and times in Python.
# print(datetime.datetime.now())
# print(datetime.date.today())
            
# print(datetime.date(2026,1,30))
# print(datetime.time(10,30,45))

# now = datetime.datetime.now()
# print(now.strftime("%d-%m-%Y"))   #strftime=formatting date to string
# print(now.strftime("%H:%M:%S"))   #strftime=formatting time to string

# print(now.strftime("%A, %B %d, %Y"))   #Full weekday name, full month name, day and year
# print(now.strftime("%I:%M %p"))        #12-hour format with AM/PM



# #todo: topic: Modules and Packages

# from cal import parent    #or import cal.parent as parent
 #cal is the package name(folder inside PEP Classes) and parent is the module name inside the package cal
# parent is the module name

# print(parent.add(10,20))
# print(parent.sub(50,30))

# from cal import parent
# print(__name__)   #?__name__ is a special built-in variable in Python that represents the name of the current module. When a module is run directly, __name__ is set to "__main__". When the module is imported, __name__ is set to the module's name.
# print(parent.__name__)  #?prints the name of the module parent



# #todo:Assignment4: datetime Module- Attendance Tracker
#problem statememt: Employee Login Tracker
#create a fxn. calculate_work_hours(login_time, logout_time)
#input format: "2026-01-30 09:00:00"
#O/p: 
#total work hours: HH MM
# def calculate_work_hours(login_time, logout_time):
#     from datetime import datetime

#     login_dt = datetime.strptime(login_time, "%Y-%m-%d %H:%M:%S")
#     logout_dt = datetime.strptime(logout_time, "%Y-%m-%d %H:%M:%S")

#     work_duration = logout_dt - login_dt
#     total_seconds = work_duration.total_seconds()
#     hours = int(total_seconds // 3600)
#     minutes = int((total_seconds % 3600) // 60)

#     return hours, minutes

# #todo:Assignment8: Decorators + datetime (Security & Auth)
#Problem Statement: Role-Based Access Control 
#create a decorator @require_login
#Logic:
#if user not logged in ->deny access
#log access time using datetime
#Apply on view_dashboard()

# import datetime
# from functools import wraps

# current_user = {"logged_in": True, "username": "aditya"}  # Simulated user data

# def require_login(func):
    
#     def wrapper(*args, **kwargs):
#         if current_user["logged_in"]:
#             return "Access Denied: Please log in to access this page."
#         access_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         print(f"User '{current_user['username']}' accessed at {access_time}")
#         return func(*args, **kwargs)
#     return wrapper
    


# @require_login
# def view_dashboard():
#     return "Welcome to the Dashboard!"

# # Simulate user trying to access the dashboard without logging in
# print(view_dashboard())
# # Simulate user logging in
# current_user["logged_in"] = False
# # Simulate user accessing the dashboard after logging in
# print(view_dashboard())

#OR


# import datetime
# def require_login(func):
#     def wrap(its_login):
#         if not its_login:
#             return "Access Denied: Please log in to access this page."
#         access_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")   #?strftime=formatting date to string
#         print(f"User accessed at {access_time}")
#         return func(its_login)
#     return wrap
# @require_login
# def view_dashboard(its_login):
#     return "Welcome to the Dashboard!"

# # Simulate user trying to access the dashboard without logging in
# print(view_dashboard(False))
# print(view_dashboard(True))   #Simulate user accessing the dashboard after logging in



#?============================================OOPSConcepts===================================================

# #todo: OOPS Concepts in Python
# #?Class: A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that the objects created from the class will have.
# class Dog:
#     #?Attributes
#     species = "Canis familiaris"   #class attribute
#     def __init__(self, name, age):   #?__init__ is a special method called constructor
#         self.name = name    #instance attribute
#         self.age = age     #instance attribute
#     #?Method
#     def bark(self):
#         return f"{self.name} says Woof!"
# #?Creating an object of the class
# my_dog = Dog("Buddy", 3)
# print(my_dog.bark())
# print(f"{my_dog.name} is {my_dog.age} years old.")

# #?Inheritance: Inheritance is a mechanism where a new class (child class) can inherit attributes and methods from an existing class (parent class).
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         raise NotImplementedError("Subclasses must implement this method")
# class Cat(Animal):   #?Cat class inherits from Animal class
#     def speak(self):
#         return f"{self.name} says Meow!"
# class Dog(Animal):   #?Dog class inherits from Animal class
#     def speak(self):
#         return f"{self.name} says Woof!"
# my_cat = Cat("Whiskers")   
# my_dog = Dog("Buddy")
# print(my_cat.speak())
# print(my_dog.speak())


# #?Encapsulation: Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class. It restricts direct access to some of the object's components.
# class BankAccount:
#     def __init__(self, account_number, balance):    #?__init__ is constructor & self is the instance 
#         self.__account_number = account_number   #private attribute
#         self.__balance = balance                 #private attribute
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#     def get_balance(self):
#         return self.__balance
# my_account = BankAccount("123456789", 1000)
# my_account.deposit(500)
# my_account.withdraw(200)
# print(f"Account Balance: {my_account.get_balance()}")



# #?Polymorphism: Polymorphism allows methods to do different things based on the object it is acting upon, even though they share the same name.
# class Bird:
#     def fly(self):
#         return "Flying in the sky!"
# class Airplane:
#     def fly(self):
#         return "Flying with jet engines!"
# def perform_flight(entity):
#     print(entity.fly())
# my_bird = Bird()
# my_plane = Airplane()
# perform_flight(my_bird)     #will call Bird's fly method
# perform_flight(my_plane)    #will call Airplane's fly method


##?Abstraction: Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# my_rectangle = Rectangle(5, 10)
# print(f"Area of Rectangle: {my_rectangle.area()}")
# #?The Shape class is an abstract base class with an abstract method area(). The Rectangle class inherits from Shape and provides a concrete implementation of the area() method.
# #?You cannot create an instance of the Shape class directly because it contains an abstract method. You must create a subclass that implements the abstract method.
# #?This ensures that all subclasses of Shape will have their own implementation of the area() method, enforcing a contract for derived classes.




# class abc:
#     def hello():
#         print("After Noon")

# obj = abc() #creating an object of class abc
# obj.hello()  #calling the method using the object   #?TypeError: hello() takes 0 positional arguments but 1 was given because the method hello() is defined without self parameter, but when called on an instance , Python automatically passes the instance as the first argument.


# class abc:
#     def hello(lpu):
#         print("After Noon")

# obj = abc() #creating an object of class abc
# obj.hello() #calling the method using the object   #?Output: After Noon because here lpu acts as self parameter which refers to the instance obj./




# class abc:
#     #dunder Method __init__
#     def __init__(self):    #?Without self, Python wouldn’t know which object is calling the method.
#         print("Constructor called")

#     def hello(self):
#         print("After Noon")

# #?__init__() runs once per object creation, not per method call.

# obj = abc()  #?while creating an object, __init__ method is called automatically
# obj.hello() 
# abc.hello(obj)  #?calling hello method using class name by passing the object as an argument


#?instance is an individual object of a class. When a class is defined, no memory is allocated until an instance of the class is created.

#? class variable vs instance variable
# class variable_example:
#     class_var = "I am a class variable"   #?class variable are shared across all instances of the class
#     def __init__(self, instance_var):
#         self.instance_var = instance_var   #?instance variable are unique to each instance of the class
#?instance variable are mentioned with the help of self operator


# class emp:
#     company_name = "LPU"   #class variable
#     no_employees = 0  
#     increment = 1.5

#     def __init__(self, fname, lname, sal):
#         #instance variables
#         self.fname = fname
#         self.lname = lname
#         self.sal = sal
#         self.company_name = "IBM"
#         emp.no_employees += 1

#     def info(self):
#         print("Employee",self.fname,"",self.lname,"having",self.sal,"salary.")
#         print("works in",self.company_name)  #accessing instance variable using self
#         print("works in",emp.company_name)   #accessing class variable using class name'

#     def increase(self):
#         self.sal = self.sal * self.increment
#         return self.sal
# # e1 = emp("Aditya","verma",50000)
# # e1.info()

# obj = emp("Ravi","Kumar",60000)
# # # obj1 = emp("Anita","Sharma",70000)  
# # obj.info()
# # print(obj.no_employees)
# # print(emp.no_employees)

# lpu = emp("Aman","Singh",55000)
# # emp.increment = 2.5  
# lpu.increment = 2.5  #?this creates an instance variable increment for lpu object only, it does not modify the class variable emp.increment
# lpu.increase()
# obj.increase()

# print(lpu.__dict__)   #?__dict__ is a built-in attribute in Python that returns a dictionary representation of an object's attributes and their values.
# print(obj.__dict__)


#todo: classmethod and staticmethod
#classmethods are useful when you need to work with class itself rather tham any particular instance of the class.
# staticmethods are used when you want to define a method that doesn't need access to instance or class-specific data.

# @classmethod     #?built-in decorator to define a class method
# def class_method(cls):
#     print("This is a class method.")
#     print("Accessing class variable:", cls.company_name)
# @staticmethod    #?built-in decorator to define a static method
# def static_method():
#     print("This is a static method.")
#     print("It doesn't access instance or class variables.")


 #Example:
# class Employee:
#     increment = 1.5

#     def __init__(self, sal):
#         self.sal = sal

#     def apply_raise(self):            # instance
#         self.sal *= self.increment

#     @classmethod
#     def set_increment(cls, value):    # class
#         cls.increment = value

#     @staticmethod
#     def is_valid_salary(sal):         # static
#         return sal > 0



# #todo: Assignment3: Static Method(Utility Logic)
#Problem Statement: banking utility system
# create a class BanksUtils
#requirements:
#1. static method: is_valid_account(account_number)
#2. Logic: account number must be  numeric  and 12 digits 

# class BanksUtils:
#     @staticmethod
#     def is_valid_account(account_number):
#         if len(account_number) == 12 and account_number.isdigit():
#             return True
#         else:
#             return False 
# # Test the static method
# print(BanksUtils.is_valid_account("123456789012"))  # Output: True




# #todo: Assignment4: Class Method(Factory Pattern)
# Create a class User
#requirements:
# Attributes: username, role
# Class method: create_admin(username)
# Default role: "ADMIN"
# 
# class User:
#     def __init__(self, username, role):
#         self.username = username
#         self.role = role

#     @classmethod
#     def create_admin(cls, username):
#         return cls(username, "ADMIN")
# # # Test the class method
# admin_user = User.create_admin("superuser")
# print(f"Username: {admin_user.username}, Role: {admin_user.role}")  # Output: Username: superuser, Role: ADMIN



# #todo: Assignment5: Combined Static + Class Method
# Problem Statement: Product Pricing Engine 
# Requirements:
# Class Variable: tax_rate
# Instance Variable: price
#Static Method: update_tax(rate)
#Class Method: update_tax(rate)
#Instance method:
#final_price()

# class Product:
#     tax_rate = 0  # class variable
    
#     def __init__(self, price):
#         self.price = price  # instance variable
        
#     @staticmethod               #static method
#     def is_valid_price(price):
#         return price>0
    
#     @classmethod                    #class method
#     def update_tax(cls, rate):
#         cls.tax_rate = rate
    
    
#     def final_price(self):    #instance method
#         tax = (self.price * self.tax_rate) / 100
#         return self.price + tax

# # Test the Product class
# Product.update_tax(10)  # Update tax rate to 10%
# product = Product(1000) # Create a product with price 1000
# print(f"Final Price: {product.final_price()}") 

# #todo: Assignment6: Real-World OOP-E-Commerce Cart
#Problem Statememt: Shopping Cart System 
# Design a class Cart
#Requirements:
# Instance Variable: items(list of prices)
#Methods: add_item(price)
# total_price()
# Class Variable: discount_rate
#Class method:  update_discount(rate)

# class Cart:
#     discount_rate = 0   #class variable
    
#     def __init__(self):
#         self.items = []     #instance variable - list of prices
    
#     def add_item(self, price):        #instance method
#         self.items.append(price)
    
#     def total_price(self):      #instance method
#         total = sum(self.items)
#         discount = (total * self.discount_rate) / 100
#         return total - discount
    
#     @classmethod
#     def update_discount(cls, rate):
#         cls.discount_rate = rate


# # Test the Cart class
# Cart.update_discount(10)  # Set discount rate to 10%
# cart = Cart()       #create a cart instance to add items 
# #or
# #cart = cart(300,600)  #?but for this make the __init__ method to accept parameters: def __init__(self, *items):
# cart.add_item(500)
# cart.add_item(300)
# cart.add_item(200)
# print(f"Total Price: {cart.total_price()}")

        
# #todo: Assignment7:OOPs + Validation(Placement Guidance)
#problem Statement: Login System
# Design a class AuthSystem
#requirements:
#static method: validate_password(password)
#instance method: login(password)
#Logic:
# Password must be at least 8 characters long and One uppercase character & lower case & One digit must be there
#store login status 

# class AuthSystem:
#     def __init__(self):  #constructor
#         self.logged_in = False   #instance variable to store login status

#     @staticmethod
#     def validate_password(password):
#         if (len(password) >= 8 and 
#             any(char.isupper() for char in password) and 
#             any(char.islower() for char in password) and
#             any(char.isdigit() for char in password)):
#             return True
#         return False

#     def login(self, password):    #instance method
#         if self.validate_password(password):
#             self.logged_in = True
#             return "Login Successful!"
#         else:
#             return "Invalid Password. Login Failed."
        
# # Test the AuthSystem class
# auth = AuthSystem()
# print(auth.login("galeechInsaan"))  
# print(auth.login("DKBoss DKboss..."))        
# print(auth.login("Ch&DBHangra@123"))



# #todo: Problem Statememt: College ERP Backend Model
# Design classes:
#       Student
#       Faculty
#       Course 
#Requirements:
#       class variable: college_name
#       Methods to: Enrollcourse() in student
#       Assigncourse() in faculty 
#       Use classMethod to update college name

# class Course:
#     college_name = "LPU"  # class variable
    
#     def __init__(self, name):
#         self.name = name
    
#     @classmethod
#     def update_college_name(cls, name):
#         cls.college_name = name

# class Student(Course):
#     def __init__(self, student_name):
#         self.student_name = student_name
#         self.courses = []
    
#     def Enrollcourse(self, course):
#         self.courses.append(course)
#         print(f"{self.student_name} enrolled in {course}")

# class Faculty(Course):
#     def __init__(self, faculty_name):
#         self.faculty_name = faculty_name
#         self.assigned_courses = []
    
#     def Assigncourse(self, course):
#         self.assigned_courses.append(course)
#         print(f"{self.faculty_name} assigned to teach {course}")

# # Test the College ERP system
# Course.update_college_name("Hogwards")
# student = Student("hermoine")
# faculty = Faculty("professor snape")
# student.Enrollcourse("Occlumency")
# faculty.Assigncourse("Defence Against the Dark Arts")
# print(f"College Name: {Course.college_name}")






# #todo: super()
# # ?The super() function in Python is used to call a method from a parent class. It is commonly used in inheritance to access methods and attributes of the parent class from the child class.
# #Example:
# class Parent:
#     def greet(self):
#         return "Hello from Parent"
# class Child(Parent):
#     def greet(self):
#         parent_greet = super().greet()  # Calling the parent class method using super()
#         return f"{parent_greet} and Child"
# child = Child()
# print(child.greet())  # Output: "Hello from Parent and Child"
# In this example, the Child class overrides the greet() method of the Parent class. Inside the Child's greet() method, we use super().greet() to call the Parent's greet() method and combine its result with additional text.


# #todo: create 3 classes: A,B,C
# class a have a fxn. dsiplay
# class b have a fxn display1
# with the object of C class you have to call display & display1 fxn. & c has a show fxn that is also called by the c object


# class A:
#     def display(self):    
#         print("Display from class A")

# class B:
#     def display1(self):
#         print("Display1 from class B")

# class C(A, B):
#     def show(self):
#         print("Show from class C")

# # Creating an object of class C
# c = C()
# c.display()   # Calling display() from class A
# c.display1()  # Calling display1() from class B
# c.show()      # Calling show() from class C 


##todo:============== inheritence type: single, multiple, multilevel, hierarchical, hybrid=====================

#?single inheritance      #1 child & 1 parent
# class A:
#     def display(self):    
#         print("Display from class A")
# class B(A):
#     def display1(self):
#         print("Display1 from class B")
# b = B()
# b.display()
# b.display1()


#?multiple inheritance      #1 child & multiple parent
# class A:
#     def display(self):
#         print("Display from class A")
# class B:
#     def display1(self):
#         print("Display1 from class B")
# class C(A, B):
#     def show(self):
#         print("Show from class C")
# c = C()
# c.display()
# c.display1()
# c.show()

#?multilevel inheritance     #grandparent, parent, child
# class A:
#     def display(self):
#         print("Display from class A")
# class B(A):
#     def display1(self):
#         print("Display1 from class B")
# class C(B):
#     def show(self):
#         print("Show from class C")
# c = C()
# c.display()
# c.display1()
# c.show()

#?hierarchical inheritance     #1 parent & multiple child
# class A:
#     def display(self):
#         print("Display from class A")
# class B(A):
#     def display1(self):
#         print("Display1 from class B")
# class C(A):
#     def show(self):
#         print("Show from class C")
# b = B()
# b.display()
# b.display1()
# c = C()
# c.display()
# c.show()


#?hybrid inheritance     #combination of 2 or more types of inheritance
# class A:
#     def display(self):
#         print("Display from class A")
# class B(A):
#     def display1(self):
#         print("Display1 from class B")
# class C(A):
#     def show(self):
#         print("Show from class C")
# class D(B, C):
#     def info(self):
#         print("Info from class D")
# d = D()
# d.display()
# d.display1()
# d.show()
# d.info()
# In this example, class D inherits from both B and C, which in turn inherit from A. This creates a hybrid inheritance structure.


# #todo: ambiguity in multiple inheritance or diamond problem 
# class A:   
#     def display(self):
#         print("Display from class A")
# class B:
#     def display(self):
#         print("Display from class B")
# class C(A, B):
#     def show(self):
#         print("Show from class C")
# c = C()
# c.display()  # Output: "Display from class A" #?because A is listed before B in the inheritance list of C, so A's display() method is called due to the method resolution order (MRO) in Python.

#?due to this problem of ambiguity, super() is used to resolve the ambiguity in multiple inheritance scenarios.
#? thaswhy multiple inheritence does not exist in java & c#

#?MRO(Method Resolution Order) is the sequence in which Python looks for a method in a hierarchy of classes when it is called on an instance of a class.
#?It means its importance with the multiple inheritance where a class inherits from multiple classes and completes, if method with the same name exists in diff. parent classes.

# print(C.mro())   #?prints the method resolution order for class C
# #Output: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]


# #todo: Problem Statement: Employee Management System
# Design a base class Employee
#Requirements:
# Attributes: emp_id,name,base_salary
# Method: calculate_salary()
#create child classes:
# 1. FullTimeEmployee
# 2. ContractEmployee

# class Employee:
#     def __init__(self, emp_id, name, base_salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.base_salary = base_salary

#     def calculate_salary(self):
#         return self.base_salary
    
# class FullTimeEmployee(Employee):
#     def __init__(self, emp_id, name, base_salary, incentive):
#         super().__init__(emp_id, name, base_salary)
#         self.incentive = incentive

#     def calculate_salary(self):
#         return self.base_salary + self.incentive

# class ContractEmployee(Employee):
#     def __init__(self, emp_id, name, base_salary, contract_duration):
#         super().__init__(emp_id, name, base_salary)
#         self.contract_duration = contract_duration

#     def calculate_salary(self):
#         return self.base_salary * self.contract_duration
    
# # Test the Employee Management System
# full_time_emp = FullTimeEmployee(1, "Alice", 50000, 10000)
# contract_emp = ContractEmployee(2, "Bob", 3000, 12)
# print(f"Full-Time Employee Salary: {full_time_emp.calculate_salary()}")
# print(f"Contract Employee Salary: {contract_emp.calculate_salary()}")


# #todo: OVERRIDING: when a child class provides a specific implementation of a method that is already defined in its parent class, it is known as method overriding.
# class Parent:
#     def greet(self):
#         return "Hello from Parent"
# class Child(Parent):
#     def greet(self):
#         return "Hello from Child"
# child = Child()
# print(child.greet())  # Output: "Hello from Child"
#? In this example, the Child class overrides the greet() method of the Parent class. When greet() is called on an instance of Child, the overridden method in Child is executed instead of the one in Parent.
#?It occurs at runtime & is a run-time polymorphism.

# #todo: OVERLOADING: Method overloading is a feature that allows a class to have multiple methods with the same name but different parameters (different type or number of parameters).
# class MathOperations:
#     def add(self, a, b):
#         return a + b
#     def add(self, a, b, c):
#         return a + b + c
# math_ops = MathOperations()
# print(math_ops.add(2, 3, 4))  # Output: 9
#? In this example, the MathOperations class has two add() methods with different parameters. However, Python does not support method overloading in the traditional sense. The second definition of add() overwrites the first one. Therefore, when add() is called with two arguments, it will result in a TypeError because the method expects three arguments.
#? It occurs at compile-time & is a compile-time polymorphism.

#example:
# class Calculator:
#     def multiply(self, a, b, *args):
#         result = a * b
#         for n in args:
#             result *= n
#         return result

# cal = Calculator()
# print(cal.multiply(2, 3))
# print(cal.multiply(2, 3, 4, 5))   



# #todo: Mangling:
#?In Python, name mangling is a mechanism that alters the name of class attributes that are intended to be private. This is done to avoid naming conflicts in subclasses. When an attribute name starts with two underscores (__) and does not end with two underscores, Python changes its name by prefixing it with _ClassName. This makes it harder to accidentally access or modify the attribute from outside the class.
#Example: 
# class MyClass:
#     def __init__(self):
#         self.__private_attr = "I am private"
#     def get_private_attr(self):
#         return self.__private_attr
# obj = MyClass()
# print(obj.get_private_attr())  # Output: "I am private"
# # print(obj.__private_attr)  # This will raise an AttributeError
# print(obj._MyClass__private_attr)  # Output: "I am private
#?In this example, __private_attr is a private attribute of MyClass. It can be accessed within the class using the get_private_attr() method. However, trying to access it directly from outside the class will raise an AttributeError. The attribute can still be accessed using its mangled name _MyClass__private_attr, but this is generally discouraged as it goes against the intention of making the attribute private.


# #todo: Assignment 9: Combined Placement Challenge
#Problem Statement: Backend Configuration Manager
# Create a class AppConfig
#Requirements:
#Class Variable: app_name
#class method: load_defaults()
#static method: validate_config(config_dict)
#instance method: display_config() 

# class AppConfig:
#     app_name = "LPU TOUCH"  # class variable

#     def __init__(self, config):
#         self.config = config  # instance variable

#     @classmethod
#     def load_defaults(cls):
#         return cls({"testing": "done", "version":"1.3"})
    
#     @staticmethod
#     def validate_config(config):
#        return "version" in config and "testing" in config

#     def display_config(self):
#         return self.config
    
# # Test the AppConfig class
# con = AppConfig.load_defaults()
# print(AppConfig.validate_config(con.config))  #O/p: True
# print(con.display_config())  #O/p: {'testing': 'done', 'version': '1.3'}


# #todo: Assignment2: Method Overriding(Runtime Polymorphism)
# Problem Statement: Notification System
# Design a base class Notification
# Method: send(message)
#child classes:
# 1. EmailNotification
# 2. SMSNotification
#each child overrides send() method

# class Notification:
#     def send(self, message):
#         return f"Notification: {message}"

# class EmailNotification(Notification): 
#     def send(self, message): 
#         return f"Email sent: {message}"

# class SMSNotification(Notification):
#     def send(self, message):
#         return f"SMS sent: {message}"


# message = Notification()
# email = EmailNotification()
# sms = SMSNotification()
# print(message.send("Hello! This is a notification."))   #?.send() is used to call the send method of the respective class
# print(email.send("Hello! This is a notification."))
# print(sms.send("Hello! This is a notification."))



# #todo: Problem Statement: Shape Area Calculator
#create a base class Shape
#Method: area()
#child classes:
# 1. Rectangle & circle
#call area() on different objects using same interface

# import math

# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width): #?variable are declared inside __init__ method are called instance variables
#         self.length = length
#         self.width = width
    
#     def area(self):
#         rect_area = self.length * self.width
#         return f"Area of Rectangle: {rect_area}"

# class Circle(Shape):
#     def __init__(self, radius):   #?variable are declared inside __init__ method are called instance variables
#         self.radius = radius
    
#     def area(self):
#         circle_area = math.pi * pow(self.radius,2)
#         return f"Area of Circle: {circle_area:.2f}"

# # Test the Shape classes
# rect = Rectangle(5, 4)
# circ = Circle(3)
# print(rect.area())
# print(circ.area())


# #todo: Example:  
# class Emp:
#     def __init__(self,fname,lname,sal):
#         self.fname = fname
#         self.lname = lname
#         self.sal = sal
#         self.email = fname + "." + lname + "@lpu.com"
    
# johan = Emp("Johan","David",50000)
# ritik = Emp("Ritik","Kumar",60000)
# print(ritik.email)
# ritik.lname = "Singh"
# print(ritik.email)  #?email will not change because it was created during the initialization and is not dynamically linked to the fname and lname attributes.

# #?To make email dynamic, we can use a property decorator
# @property    #?property decorator is used to define a method as a property, allowing you to access it like an attribute.
# def email(self):
#     return f"{self.fname}.{self.lname}@lpu.com"

# Emp.email = email  #?adding the email property to the Emp class
# print(ritik.email)
# ritik.lname = "Sharma"
# print(ritik.email)


# #todo: Assignment 5: Property Decorator(@property) - Data Protection
#Problem Statement: User Account Balance
#create class BankAccount
#Requirements:
# Attribute is balance
# @property balance ->getter
# @balance.setter ->prevent negative balance

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance  # This will use the setter to validate

#     @property
#     def balance(self):
#         return self._balance

#     @balance.setter    #?setter decorator is used to define a method that sets the value of a property.
#     def balance(self, amount):
#         if amount < 0:
#             print("Error: Balance cannot be negative.")
#             self._balance = 0
#         else:
#             self._balance = amount

# acc = BankAccount(1000)
# print(acc.balance)  # Output: 1000
# acc1 = BankAccount(-500)  # Will print error and set balance to 0
# print(acc1.balance)  # Output: 0


# #todo: Assignment 6: Setter & Deleter (Security Critical)
#Problem Statement: Employee Salary Protection
# create class Employee
#Requirements:
# salary is an attribute 
#setter: salary must be >= minimum wage 
#deleter: prevent deletion of salary directly

# class Employee:
#     MIN_WAGE = 20000 # Class variable for minimum wage

#     def __init__(self, salary):
#         self.salary = salary  # This will use the setter to validate

#     @property  
#     def salary(self):
#         return self._salary

#     @salary.setter 
#     def salary(self, amount):
#         if amount < self.MIN_WAGE:
#             print(f"Salary cannot be less than minimum wage of {self.MIN_WAGE}.")
#             self._salary = self.MIN_WAGE
#         else:
#             self._salary = amount

#     @salary.deleter
#     def salary(self):
#         print("Direct deletion of salary is not allowed.")

# emp = Employee(25000)
# print(emp.salary)  # Output: 25000
# emp.salary = 15000  # Will print error and set salary to minimum wage
# print(emp.salary)  # Output: 20000
# del emp.salary  # Will print error message


# #todo: Assignment 7: Combined Inheritance & Property(placement Grade)
#Problem Statement: Product pricing  System
# base class: product
#child class: DiscountedProduct

# class product:
#     def __init__(self,price):
#         self.price = price
#     @property
#     def final_price(self):
#         return self.price

# class DiscountedProduct(product):
#     def __init__(self,price,discount):
#         super().__init__(price)
#         self.discount = discount
    
#     @property
#     def final_price(self):
#         return self.price - (self.price * self.discount/100)
    
# p1 = DiscountedProduct(1000,30)
# print(p1.final_price) #O/p: 700.0


# #todo: DUCK TYPING
#?Duck typing is a concept in programming, particularly in dynamically typed languages like Python, where the type or class of an object is determined by the methods and properties it has, rather than its actual class or inheritance hierarchy. The idea is summarized by the saying "If it looks like a duck and quacks like a duck, it's a duck."
#Example:
# class Dog:
#     def speak(self):
#         return "Woof!"
    
# class Cat:
#     def speak(self):
#         return "Meow!"

# def animal_sound(animal):
#     print(animal.speak())

# dog = Dog()
# cat = Cat()

# animal_sound(dog)  # Output: Woof!
# animal_sound(cat)  # Output: Meow!

# from abc import ABC, abstractmethod #? abc module is used to create abstract base classes in Python.

# class PayementGateway(ABC):   #?ABC is the base class for defining Abstract Base Classes in Python.
#     @abstractmethod
#     def pay(self):
#         pass

# class phonepay(PayementGateway):
#     def pay(self):
#         print("Payment done by PhonePay")

# class Paypal:
#     def payment(self):
#         print("Payment done by Paypal")

# class purchase:
#     def __init__(self,gateway):
#         self.gateway = gateway

#     def checkout(self):
#         print("Checked out")
#         self.gateway.pay()   #? here pay() method is called on gateway object, which is expected to have a pay() method.

# p1 = phonepay()
# p2 = Paypal()
# pur = purchase(p1)
# pur2 = purchase(p2)
# pur.checkout()

# #todo: Assignment 3: Database Layer Abstraction(Backend Favourite)
#Problem Statement: Design an abstract database layer.
# Requirements:
# Abstract Class: Database
# Abstract Methods: connect(), fetch(), close()
# Implementations:
# 1. MySQLDatabase
# 2. MongoDBDatabase


# from abc import ABC, abstractmethod
# class Database(ABC):
#     @abstractmethod
#     def connect(self):
#         pass

#     @abstractmethod
#     def fetch(self, query):
#         pass

#     @abstractmethod
#     def close(self):
#         pass

# class MySQLDatabase(Database):
#     def connect(self):
#         print("Connected to MySQL Database")

#     def fetch(self, query):
#         print(f"Fetching data from MySQL with query: {query}")

#     def close(self):
#         print("MySQL Database connection closed")

# class MongoDBDatabase(Database):
#     def connect(self):
#         print("Connected to MongoDB Database")

#     def fetch(self, query):
#         print(f"Fetching data from MongoDB with query: {query}")

#     def close(self):
#         print("MongoDB Database connection closed")

# # Test the Database implementations
# mysql_db = MySQLDatabase()
# mysql_db.connect()
# mysql_db.fetch("SELECT * FROM users")
# mysql_db.close()
# mongo_db = MongoDBDatabase()
# mongo_db.connect()
# mongo_db.fetch("{ find: 'users' }")
# mongo_db.close()


# #todo: =================================File Handling====================================================== 

#?file handling is a mechanism for storing data permanently on a storage device like a hard drive or SSD. It allows you to create, read, update, and delete files on your computer using programming languages like Python.
# In Python, you can handle files using built-in functions and methods. Here are some common operations:

# #?1. Opening a file 
# file = open("example.txt", "r")  # Open a file in read mode

# #?2. Reading from a file
# content = file.read()  # Read the entire content of the file
# print(content)

# #?3. Writing to a file
# file = open("example.txt", "w")  # Open a file in write mode
# file.write("Hello, World!")  # Write data to the file

# #?4. Closing a file
# file.close()  # Close the file to free up resources

# #?5. Using 'with' statement for file handling
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)
#?The 'with' statement automatically handles closing the file for you, even if an error occurs while working with the file.

#example:
# with open("sample.txt", "w") as f:     #?this will create a file named sample.txt in write mode
#     f.write("This is a sample file.\nIt contains multiple lines of text.")
# with open("sample.txt", "r") as f:
#     content = f.read()
#     print(content)


# file = open('sample.txt','r')
# content = file.read()
# print(content)
# file.close()

# file = open('sample.txt','a')  #?append mode
# file.write("\nThis line is appended to the file.")
# file.close()

# file = open('sample.txt','w') #?write mode
# file.write("This will overwrite the existing content.")
# file.close()

# file = open('sample.txt','r') 
# content = file.read()
# print(content)  

#?To create a new file in Python, you can use the open() function with the 'w' (write) mode or 'x' (exclusive creation) mode. If the file does not exist, it will be created. If it already exists, using 'w' will overwrite the existing file, while 'x' will raise a FileExistsError. 


#todo: rb mode:
#?In Python, 'rb' mode stands for "read binary" mode. It is used when you want to read binary files, such as images, audio files, or any other non-text files. When you open a file in 'rb' mode, the data is read as raw bytes, which is essential for binary files to ensure that the data is not altered during the reading process.

# file = open("Gemini_generated.png",'rb')   #?open the binary file in read binary mode
# print(file.read())

#this will not open the img file in a viewable format, it will display the binary data of the file. To view the image, you would typically use an image viewer or a library that can handle image files, such as PIL (Pillow) in Python.


#todo: wb mode:
#?In Python, 'wb' mode stands for "write binary" mode. It is used when you want to write binary data to a file, such as images, audio files, or any other non-text files. When you open a file in 'wb' mode, the data is written as raw bytes, which is essential for binary files to ensure that the data is not altered during the writing process.

# f1 = open('new_img.png',"wb")
# for i in file:
#     f1.write(i)

# file.close()
# f1.close()

# #todo: Assignment1: User Data Reader
#Problem Description 
#you are working on a backend system that stores registered user data in a text file.
#the file users.txt contains user records in the following format:
# 101,Amit,amit@gmail.com
# 102,Neha,neha@gmail.com
# 103,Ravi,ravi@gmail.com

#Tasks
#1 open the file using read mode(r)
#2 Read the entire content
#3 Display each user record line by line'
#4 Ensure the file is properly closed 

# file = open('users.txt','w')
# file.write("101,Amit,amit@gmail.com\n102,Neha,neha@gmail.com\n103,Ravi,ravi@gmail.com")
# file.close()
# file = open('users.txt','r')   #1
# content = file.read()          #2
# for line in content.split('\n'):  #3     #?line is used to iterate through each line of the content
#     print(line)  # Display each user record line by line
# file.close()  #4


# #todo: Assignment2: Server Log Analyzer(Reading lie by line)
#Problem Statement: A backend server generates a log file server.log
#each line represents one server request:
#INFO: Request received
#ERROR: Database connection failed
#INFO: Request processed successfully
#ERROR: Timeout occurred

#Tasks:
#1 read the line by line
#2 Count:
#   a. total log entries
#   b. total error entries
#3 Display the count Summary

# total_log = 0
# error_log = 0
# file = open('server.log','w')
# file.write("INFO: Request received\nERROR: Database connection failed\nINFO: Request processed successfully\nERROR: Timeout occurred")
# file.close()

# file = open('server.log','r')   #1
# for line in file:                #1
#     total_log += 1               #2a
#     if "ERROR" in line:          #2b
#         error_log += 1

# print(f"Total log entries: {total_log}")
# print(f"Total error entries: {error_log}")
# file.close()




# #todo: Assignment3: Student Registration System(w)
# Problem Description:
# you are building a student registration module 
#Tasks:
#1 Ask the user to enter:Student ID, Name, Course
#2 write the data into students.txt
#3 Each student record should be on a new line
#4 If the file already exists, it should be overwritten with new data

# with open('students.txt','a') as file:   #3 (append new records)
#     count = int(input("How many students to register? "))
#     for _ in range(count):  
#         user = input("Enter Student ID, Name, Course : ") 
#         file.write(user + "\n")                  



# #todo: Assignment4: File Append- Feedback Collector(a)
#Problem Description: your application collects user feedback and store it in feedback.txt
#Tasks:
#1 Append new feedback to the file
#2 Ensure old feedback is not deleted
#3 Add a timestamp before each feedback entry

from datetime import datetime
with open('feedback.txt','a') as file:
    feedback = input("Enter your feedback: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{timestamp} - {feedback}\n")

   