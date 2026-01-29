# Python Concepts & Assignments

A comprehensive collection of Python programming concepts, exercises, and practical object-oriented programming assignments.

## Overview

This repository contains Python learning materials and assignments covering fundamental to intermediate programming concepts, with a focus on Object-Oriented Programming (OOP).

## Contents

### Core Python Concepts
- **Input/Output Operations**: Input functions, multiple inputs, data type conversions
- **Variables & Data Types**: Swapping values, boolean operations, type conversions
- **Operators**: Arithmetic, comparison, logical, assignment operators
- **Control Flow**: if-else statements, ternary operators, switch case (match statements)
- **Loops**: for loops, while loops, nested loops, break/continue statements

### Intermediate Concepts
- **String Manipulation**: Case conversions, trimming, splitting, joining, finding substrings
- **Collections**: Lists, dictionaries, sets, tuples
- **Pattern Problems**: Triangles, multiplication tables, number patterns, palindromes
- **Number Problems**: Prime numbers, Armstrong numbers, reverse digits
- **Format Specifiers**: String formatting with %d, %s, %f, f-strings, .format()

### Object-Oriented Programming (OOP)
- **Classes & Objects**: Class variables vs instance variables
- **Methods**: Instance methods, static methods, class methods
- **Constructors**: `__init__()` method
- **Inheritance**: Single inheritance, method overriding
- **Practical OOP Examples**:
  - **AuthSystem**: User authentication with email and password validation
  - **Product Pricing Engine**: Static methods, class methods, and instance methods
  - **Shopping Cart System**: E-commerce cart with discount management
  - **College ERP Backend**: Student enrollment and faculty course assignment

### Validation Modules
- **Email Validation**: `is_valid_email()`
- **Mobile Number Validation**: `is_valid_mobile()`
- **Password Strength**: `is_strong_password()`
- **Banking Utils**: `is_valid_account()`

## How to Use

1. **View Examples**: Open `python concepts.py` and uncomment the sections you want to explore
2. **Run Exercises**: Execute individual code blocks to see output
3. **Study OOP Patterns**: Review the class implementations (Product, Cart, Student, Faculty, etc.)
4. **Practice Assignments**: Complete the uncommented assignments and modify them

## Key Assignments

| Assignment | Description | File Location |
|-----------|-------------|----------------|
| Assignment 1 | Email, Mobile, Password Validation Module | Line ~150 |
| Assignment 2 | Employee Salary Calculator | Line ~635 |
| Assignment 3 | Static Methods (Bank Utils) | Line ~1560 |
| Assignment 4 | Class Methods (Factory Pattern) | Line ~1575 |
| Assignment 5 | Product Pricing Engine | Line ~1595 |
| Assignment 6 | E-Commerce Shopping Cart | Line ~1632 |
| Assignment 7 | College ERP Backend | Line ~1710 |

## Running the Code

```bash
# Run the entire file
python python\ concepts.py

# Run specific sections by uncommenting them in the editor
```

## Example Outputs

### Product Pricing
```python
Product.update_tax(10)
product = Product(1000)
print(f"Final Price: {product.final_price()}")  # Final Price: 1100
```

### Shopping Cart
```python
Cart.update_discount(10)
cart = Cart()
cart.add_item(500)
cart.add_item(300)
print(f"Total Price: {cart.total_price()}")  # Total Price: 720
```

### College ERP
```python
Course.update_college_name("Lovely Professional University")
student = Student("Ravi Kumar")
student.Enrollcourse("Data Structures")
```

## Key Concepts Covered

- **Instance Variables**: Unique to each object
- **Class Variables**: Shared across all instances
- **Static Methods**: Don't access instance or class data
- **Class Methods**: Access and modify class variables
- **Inheritance**: Creating parent-child relationships between classes

## Requirements

- Python 3.6+
- No external dependencies

## Learning Path

1. Start with basic input/output and operators
2. Progress to loops and control flow
3. Move to string and collection manipulation
4. Learn OOP concepts with class and static methods
5. Apply OOP patterns in real-world scenarios (e-commerce, ERP)

## License

MIT License

## Author

Created as part of PEP Classes curriculum at Lovely Professional University (LPU)

---

**Note**: Some code sections are commented out. Uncomment the sections you want to run or test.
