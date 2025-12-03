"""
Cover:
    Name: Josue de Jesus Castro Martinez
    ID: 2530263
    Group: IM 1-1
"""

"""
Executive Summary:
    In Python, a function is a reusable block of code that has a name, can receive
    parameters and can return values using the return statement. Parameters are the
    variable names defined in the function header, while arguments are the concrete
    values passed when calling the function. Separating logic into functions makes
    programs easier to read, test and reuse, reducing code duplication.
    A return value allows functions to produce results that can be stored or
    combined with other calculations instead of only printing to the screen.
    This document presents six problems that define and use functions for geometry,
    grade classification, list statistics, discounts, greetings and factorial
    calculations, including input validation and test cases (normal, border and
    error) for each problem.
"""

"""
Principles and Good Practices:
    - Prefer small functions that do one clear task (single responsibility),
      making them easier to understand and test.
    - Avoid repeating code: if you copy/paste logic, consider extracting it
      into a function that can be called from multiple places.
    - Try to keep functions as "pure" as possible: given the same inputs,
      they should return the same outputs without causing external side effects.
    - Document each function with short comments explaining what it does and
      what parameters it expects and returns.
    - Use clear, descriptive names for functions and parameters, such as
      calculate_bmi or apply_discount, instead of vague names like f1 or do_it.
"""

# --------------------------------------------------
# Problem 1: Rectangle area and perimeter (basic functions)
# --------------------------------------------------
"""
Problem 1: Rectangle area and perimeter (basic functions)
Description:
    Defines two functions:
        - calculate_area(width, height): returns the area of a rectangle.
        - calculate_perimeter(width, height): returns the perimeter.
    The main code reads width and height, validates them, calls the functions
    and prints the results.

Inputs:
    - width (float)
    - height (float)

Outputs:
    - "Area:" <area_value>
    - "Perimeter:" <perimeter_value>

Validations:
    - width > 0
    - height > 0
    - If any condition is not met or input conversion fails, print
      "Error: invalid input" and do not call the functions.

Test cases:
    1) Normal:
        Input: width = 5.0, height = 3.0
        Output:
            Area: 15.0
            Perimeter: 16.0
    2) Border:
        Input: width = 0.1, height = 10.0
        Output:
            Area: 1.0
            Perimeter: 20.2
    3) Error:
        Input: width = -2.0, height = 3.0
        Output:
            Error: invalid input
"""

def problem_1():
    # Inner function: calculates area of a rectangle
    def calculate_area(width, height):
        return width * height

    # Inner function: calculates perimeter of a rectangle
    def calculate_perimeter(width, height):
        return 2 * (width + height)

    print("Rectangle area and perimeter")

    try:
        width = float(input("Enter the width of rectangle: "))
        height = float(input("Enter the height of rectangle: "))
    except:
        print("Error: invalid input")
        return

    if width > 0 and height > 0:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    else:
        print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Grade classifier (function with return string)
# --------------------------------------------------
"""
Problem 2: Grade classifier (function with return string)
Description:
    Defines a function classify_grade(score) that receives a numeric score
    between 0 and 100 and returns a letter category:
        - "A" if score >= 90
        - "B" if 80 <= score < 90
        - "C" if 70 <= score < 80
        - "D" if 60 <= score < 70
        - "F" if score < 60
    The main code reads the score, validates it, calls the function and prints
    the score and category.

Inputs:
    - score (float or int)

Outputs:
    - "Score:" <score>
    - "Category:" <grade_letter>

Validations:
    - 0 <= score <= 100
    - If validation fails or conversion fails, print "Error: invalid input"
      and do not classify.

Test cases:
    1) Normal:
        Input: score = 95
        Output:
            Score: 95.0
            Category: A
    2) Border:
        Input: score = 80
        Output:
            Score: 80.0
            Category: B
    3) Error:
        Input: score = 120
        Output:
            Error: invalid input
"""

def problem_2():
    # Inner function: returns the grade category for a score
    def classify_grade(score):
        if score >= 90:
            return "A"
        elif 80 <= score < 90:
            return "B"
        elif 70 <= score < 80:
            return "C"
        elif 60 <= score < 70:
            return "D"
        else:
            return "F"

    print("Grade classifier")

    try:
        score = float(input("Enter the score: "))
    except:
        print("Error: invalid input")
        return

    if not 0 <= score <= 100:
        print("Error: invalid input")
        return

    print(f"Score: {score}")
    print(f"Category: {classify_grade(score)}")


# --------------------------------------------------
# Problem 3: List statistics function (min, max, average)
# --------------------------------------------------
"""
Problem 3: List statistics function (min, max, average)
Description:
    Defines a function summarize_numbers(numbers_list) that receives a list
    of numbers and returns a dictionary with:
        - "min": minimum value
        - "max": maximum value
        - "average": average (float)
    The main code builds the list from a comma-separated string, calls the
    function and prints the results.

Inputs:
    - numbers_text (string), e.g. "10,20,30"
    - Internally: numbers_list (list of float)

Outputs:
    - "Min:" <min_value>
    - "Max:" <max_value>
    - "Average:" <average_value>

Validations:
    - numbers_text must not be empty after strip().
    - The list must not be empty after conversion.
    - All elements must be convertible to float; otherwise print
      "Error: invalid input".

Test cases:
    1) Normal:
        Input: numbers_text = "10,20,30"
        Output:
            Min: 10.0
            Max: 30.0
            Average: 20.0
    2) Border:
        Input: numbers_text = "5"
        Output:
            Min: 5.0
            Max: 5.0
            Average: 5.0
    3) Error:
        Input: numbers_text = "10,abc,30"
        Output:
            Error: invalid input
"""

def problem_3():
    print("List statistics function (min, max, average)")

    # Pure function: receives a numeric list and returns stats dictionary
    def summarize_numbers(numbers_list):
        if len(numbers_list) == 0:
            return None
        stats_dict = {
            "min": min(numbers_list),
            "max": max(numbers_list),
            "average": sum(numbers_list) / len(numbers_list)
        }
        return stats_dict

    numbers_text = input("Enter the numbers separated by commas: ").strip()

    if not numbers_text:
        print("Error: invalid input")
        return

    parts = numbers_text.split(",")
    numbers_list = []

    for part in parts:
        value_text = part.strip()
        if value_text == "":
            print("Error: invalid input")
            return
        try:
            value = float(value_text)
        except:
            print("Error: invalid input")
            return
        numbers_list.append(value)

    if len(numbers_list) == 0:
        print("Error: invalid input")
        return

    numbers_dict = summarize_numbers(numbers_list)

    if numbers_dict is None:
        print("Error: invalid input")
        return

    min_value = numbers_dict["min"]
    max_value = numbers_dict["max"]
    average_value = numbers_dict["average"]

    print(f"Min: {min_value}")
    print(f"Max: {max_value}")
    print(f"Average: {average_value}")


# --------------------------------------------------
# Problem 4: Apply discount list (pure function)
# --------------------------------------------------
"""
Problem 4: Apply discount list (pure function)
Description:
    Defines a function apply_discount(prices_list, discount_rate) that:
        - receives a list of prices (float) and a discount rate (0 to 1),
        - returns a new list with discounted prices,
        - does not modify the original list (pure function).
    The main code reads prices from a comma-separated string, reads the
    discount_rate, validates inputs, calls the function and prints both
    the original and discounted lists.

Inputs:
    - prices_text (string; e.g. "100,200,300")
    - discount_rate (float between 0 and 1)

Outputs:
    - "Original prices:" <original_list>
    - "Discounted prices:" <discounted_list>

Validations:
    - prices_text not empty and resulting list not empty.
    - Each price convertible to float and > 0.
    - 0 <= discount_rate <= 1.
    - On failure, print "Error: invalid input".

Test cases:
    1) Normal:
        Input: prices_text = "100,200,300", discount_rate = 0.1
        Output:
            Original prices: [100.0, 200.0, 300.0]
            Discounted prices: [90.0, 180.0, 270.0]
    2) Border:
        Input: prices_text = "50", discount_rate = 0
        Output:
            Original prices: [50.0]
            Discounted prices: [50.0]
    3) Error:
        Input: prices_text = "100,-20,300", discount_rate = 0.2
        Output:
            Error: invalid input
"""

def problem_4():
    print("Apply discount list")

    # Pure function: returns a new list, does not modify the original
    def apply_discount(prices_list, discount_rate):
        discounted_list = []
        for price in prices_list:
            discounted_price = price * (1 - discount_rate)
            discounted_list.append(discounted_price)
        return discounted_list

    prices_text = input("Enter the prices separated by commas: ").strip()

    if not prices_text:
        print("Error: invalid input")
        return

    try:
        discount_rate = float(input("Enter the discount rate (0 to 1): "))
    except:
        print("Error: invalid input")
        return

    if not 0 <= discount_rate <= 1:
        print("Error: invalid input")
        return

    prices_parts = prices_text.split(",")
    prices_list = []

    for part in prices_parts:
        price_text = part.strip()
        if price_text == "":
            print("Error: invalid input")
            return
        try:
            price_value = float(price_text)
        except:
            print("Error: invalid input")
            return
        if price_value <= 0:
            print("Error: invalid input")
            return
        prices_list.append(price_value)

    if len(prices_list) == 0:
        print("Error: invalid input")
        return

    discounted_list = apply_discount(prices_list, discount_rate)

    print(f"Original prices: {prices_list}")
    print(f"Discounted prices: {discounted_list}")


# --------------------------------------------------
# Problem 5: Greeting function with default parameters
# --------------------------------------------------
"""
Problem 5: Greeting function with default parameters
Description:
    Defines a function greet(name, title="") that:
        - optionally concatenates a title before the name (e.g. "Dr. Alice"),
        - returns the message "Hello, <full_name>!".
    The main code reads name and an optional title, validates the name,
    calls the function using positional and named arguments and prints
    the greeting.

Inputs:
    - name (string)
    - title (string, optional)

Outputs:
    - "Greeting:" <greeting_message>

Validations:
    - name must not be empty after strip().
    - title may be empty, but if not, it is also stripped.

Test cases:
    1) Normal (with title):
        Input: name = "Alice", title = "Dr."
        Output:
            Greeting: Hello, Dr. Alice!
    2) Border (no title):
        Input: name = "Bob", title = ""
        Output:
            Greeting: Hello, Bob!
    3) Error:
        Input: name = "   "
        Output:
            Error: invalid input
"""

def problem_5():
    # Function with default parameter and formatted greeting
    def greet(name, title=""):
        full_name = f"{title} {name}".strip()
        return f"Hello, {full_name}!"

    print("Greeting function with default parameters")

    title = input("Enter the title (optional): ").strip()
    name = input("Enter the name: ").strip()

    if not name:
        print("Error: invalid input")
        return

    # Example using named arguments when title is provided
    if title:
        greeting_message = greet(name=name, title=title)
    else:
        # Example using positional argument
        greeting_message = greet(name)

    print(f"Greeting: {greeting_message}")


# --------------------------------------------------
# Problem 6: Factorial function (iterative)
# --------------------------------------------------
"""
Problem 6: Factorial function (iterative or recursive)
Description:
    Defines a function factorial(n) that returns n! (n factorial). In this
    implementation, an iterative approach with a for loop is used. The main
    code reads n, validates it, calls factorial(n) and prints the result.

Inputs:
    - n (int)

Outputs:
    - "n:" <n>
    - "Factorial:" <factorial_value>

Validations:
    - n must be an integer.
    - n must be greater than or equal to 0.
    - Optionally, n is limited to a maximum of 20 to keep results reasonable.
      If validation fails, print "Error: invalid input".

Test cases:
    1) Normal:
        Input: n = 5
        Output:
            n: 5
            Factorial: 120
    2) Border:
        Input: n = 0
        Output:
            n: 0
            Factorial: 1
    3) Error:
        Input: n = -3
        Output:
            Error: invalid input
"""

def problem_6():
    # Iterative factorial function
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    print("Factorial function")

    try:
        n = int(input("Enter n: "))
    except:
        print("Error: invalid input")
        return

    # Limit n to a reasonable range (0 to 20)
    if n < 0 or n > 20:
        print("Error: invalid input")
        return

    factorial_value = factorial(n)
    print(f"n: {n}")
    print(f"Factorial: {factorial_value}")


# --------------------------------------------------
# Uncomment one problem at a time to run it
# --------------------------------------------------

# problem_1()
# problem_2()
# problem_3()
# problem_4()
# problem_5()
# problem_6()

"""
Conclusions:
    Functions help organize and reuse code by grouping logic into named units
    that can be called multiple times with different arguments. Returning values
    with the return statement is more flexible than only printing because the
    results can be stored, combined and tested. Default parameters and named
    arguments make functions more convenient to use in different scenarios.
    Throughout these problems, encapsulating calculations like area, grades,
    statistics, discounts, greetings and factorials in functions made the main
    logic cleaner. The separation between main flow and helper functions also
    improves readability and simplifies debugging and testing.
"""

"""
References:
    1) Python documentation - Defining Functions (docs.python.org)
    2) Python tutorial - More on Defining Functions
    3) "Automate the Boring Stuff with Python" by Al Sweigart – chapters on functions
    4) Real Python - "Defining Your Own Python Function"
    5) W3Schools - Python Functions (online tutorial)
"""