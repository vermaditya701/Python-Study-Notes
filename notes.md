**1)id()**

What is id() in Python?



id() is a built-in function that tells you the identity of an object.



👉 In simple words:

id() = memory address (unique ID) of an object while the program is running





x = 10

y = 10



print(id(x))

print(id(y))

👉 Output:



typescript

Copy code

same number

Why?

Python reuses small integers to save memory (called interning).





x = 1000

y = 1000



print(id(x))

print(id(y))

👉 Output:



nginx

Copy code

different numbers

Because larger integers are usually stored separately.











**2)types of loop** 

1️⃣ for loop

➤ When to use



When you know how many times the loop should run.

Used for ranges, lists, strings.



✅ Syntax

for i in range(5):

&nbsp;   print(i)



🧠 Key point



Iterates over a sequence

Entry-controlled loop (condition checked first)







2️⃣ while loop

➤ When to use



When you don’t know how many times the loop will run.

Depends on a condition.



✅ Syntax

i = 0

while i < 5:

&nbsp;   print(i)

&nbsp;   i += 1



🧠 Key point



Runs while condition is true.

Entry-controlled loop.







**3)in-built parameters**

sum() \_ returns the sum of all items in an iterable

len() — returns the length of an object (list, string, etc.)

max() — returns the largest item

min() — returns the smallest item

sorted() — returns a sorted list

abs() — returns the absolute value

round() — rounds a number

type() — returns the type of an object

str(), int(), float() — convert between types

enumerate() — returns index and value pairs from an iterable

zip() — combines multiple iterables

map() — applies a function to all items in an iterable

filter() — filters items using a function

any() — returns True if any item is True

all() — returns True if all items are True

input() — gets user input

print() — prints output







**4) \* \& \*\*** 

🔹 \*val (single asterisk)

➤ What it means



\*val is used for multiple positional arguments.



def add(\*val):     #\*args

&nbsp;   print(val)



add(10, 20, 30)



o/p: (10, 20, 30)

➡️ val becomes a tuple







🔹 \*\*val (double asterisk)

➤ What it means



\*\*val is used for multiple keyword arguments.



def details(\*\*val):      #\*\*kwargs    kw → keyword

&nbsp;                                     args → arguments

&nbsp;   print(val)



details(name="Aman", age=20)

o/p: {'name': 'Aman', 'age': 20}

➡️ val becomes a dictionary







| Feature       | `\*val`               | `\*\*val`           |

| ------------- | -------------------- | ----------------- |

| Accepts       | Positional arguments | Keyword arguments |

| Stored as     | Tuple                | Dictionary        |

| Uses          | `\*`                  | `\*\*`              |

| Order matters | Yes                  | No (keys matter)  |











**5) items() and update()** 



🔹 items() in Python (Dictionary)

➤ What it does



Returns all key–value pairs of a dictionary as a view object.



✅ Syntax

dict.items()



ex-

student = {"name": "Aman", "age": 20}

print(student.items())



o/p:dict\_items(\[('name', 'Aman'), ('age', 20)])





🔁 Common use: looping

for key, value in student.items():

&nbsp;   print(key, ":", value)



O/p: name : Aman

&nbsp;    age : 20









🔹 update() in Python (Dictionary)

➤ What it does



Adds new key–value pairs OR updates existing keys.



✅ Syntax

dict.update(other\_dict)



ex-

student = {"name": "Aman"}

student.update({"age": 20, "city": "Delhi"})

print(student)



O/p: {'name': 'Aman', 'age': 20, 'city': 'Delhi'}









| Feature       | `items()`            | `update()`          |

| ------------- | -------------------- | ------------------- |

| Purpose       | Read key–value pairs | Modify dictionary   |

| Returns value | Yes                  | ❌ No (returns None) |

| Changes dict  | ❌ No                 | ✅ Yes               |

| Used for      | Iteration            | Adding/updating     |













**6)filter()**

🔹 filter() in Python

➤ What it does



filter() filters elements from an iterable based on a condition.

Only elements for which the condition is True are kept.



✅ Syntax

***filter(function, iterable)***





function → returns True or False

iterable → list, tuple, set, etc.



ex->

nums = \[1, 2, 3, 4, 5, 6]



even\_nums = filter(lambda x: x % 2 == 0, nums)



print(list(even\_nums))



O/p: \[2, 4, 6]







**7)get()**



The .get() method is used with dictionaries in Python to safely retrieve the value for a given key.



syntax-

value = my\_dict.get(key, default\_value)



example->

person = {'name': 'Alice', 'age': 25}

print(person.get('name'))         # Output: Alice

print(person.get('city', 'N/A'))  # Output: N/A (since 'city' is not in the dictionary)







**8)reduce() method**

reduce() reduces an iterable to a single value by repeatedly applying a function.



Think:

Many values → one value



reduce() is not built-in.

You must import it:



***from functools import reduce***





syntax-

**reduce(function, iterable)**







***9) head vs tail Recursion*** 

🔹 Head Recursion

➤ Definition



In head recursion, the recursive call happens first, and processing happens after returning.



example->

def head(n):

&nbsp;   if n == 0:

&nbsp;       return

&nbsp;   head(n - 1)

&nbsp;   print(n)



O/p for head(3)

&nbsp;  : 1

&nbsp;    2

&nbsp;    3







how it works:

head(3)

&nbsp;→ head(2)

&nbsp;  → head(1)

&nbsp;    → head(0)

&nbsp;    ← print(1)

&nbsp;  ← print(2)

&nbsp;← print(3)







🔹 Tail Recursion

➤ Definition



In tail recursion, the recursive call is the LAST statement in the function.



def tail(n):

&nbsp;   if n == 0:

&nbsp;       return

&nbsp;   print(n)

&nbsp;   tail(n - 1)



O/p for tail(3):

3

2

1









🆚 Key Differences

Feature	Head Recursion	Tail Recursion

Recursive call	First	Last

Processing	After return	Before call

Output order	Ascending	Descending

Stack usage	More	Less (in theory)

Optimization	❌ No	✅ Yes (in some languages)









10\)









