"""
Cover:
    Name: Josue de Jesus Castro Martinez
    ID: 2530263
    Group: IM 1-1
"""

"""
Executive Summary:
    In Python, collections such as lists, tuples and dictionaries are used to
    store and process groups of related data. A list is an ordered and mutable
    sequence, which means elements can be added, removed or updated in place.
    A tuple is also ordered but immutable, so its elements cannot be changed
    after creation, making it useful for fixed records like coordinates.
    A dictionary stores key-value pairs and allows fast lookups by key, for
    example mapping product names to prices or student names to grades.
    This document presents six problems that use lists, tuples and dictionaries
    to build shopping lists, work with points, manage product catalogs and
    student grades, count word frequencies and implement a simple contact book.
    Each problem includes descriptions, input and output design, validations
    and test cases to illustrate practical uses of Python collections.
"""

"""
Principles and Good Practices:
    - Use lists when you need an ordered collection that can be frequently
      modified by adding, removing or updating elements.
    - Use tuples for data that should not change, such as coordinates, fixed
      configuration values or records that must stay constant.
    - Use dictionaries when you need to look up information by a key, such
      as searching by product name, student name or contact name.
    - Avoid modifying a list while iterating over it with a for loop unless
      you fully understand the side effects.
    - Use descriptive key names in dictionaries (for example, "name", "grades",
      "price") to make the data structure self-explanatory.
    - Write readable code and clear user messages like "Error: invalid input"
      to make programs easier to understand and debug.
"""

# --------------------------------------------------
# Problem 1: Shopping list basics (list operations)
# --------------------------------------------------
"""
Problem 1: Shopping list basics (list operations)
Description:
    Works with a shopping list of product names stored as strings. The program:
        1) Creates an initial list of items based on a comma-separated string.
        2) Adds a new product to the end of the list.
        3) Shows the total number of elements in the list.
        4) Checks if a specific product is in the list (boolean is_in_list).

Inputs:
    - initial_items_text (string): comma-separated items,
      for example "apple,banana,orange".
    - new_item (string): product to add.
    - search_item (string): product to search in the list.

Outputs:
    - "Items list:" <items_list>
    - "Total items:" <len_list>
    - "Found item:" true|false

Validations:
    - initial_items_text must not be empty after strip().
    - Split the string by commas and strip spaces around each element.
    - new_item and search_item must not be empty.
    - In this implementation an empty initial list is considered invalid
      input and produces an error message.

Test cases:
    1) Normal:
        Input:
            initial_items_text = "apple, banana, orange"
            new_item = "grape"
            search_item = "banana"
        Output:
            Items list: ['apple', 'banana', 'orange', 'grape']
            Total items: 4
            Found item: True
    2) Border:
        Input:
            initial_items_text = "milk"
            new_item = "eggs"
            search_item = "bread"
        Output:
            Items list: ['milk', 'eggs']
            Total items: 2
            Found item: False
    3) Error:
        Input:
            initial_items_text = "   "
            new_item = "eggs"
            search_item = "milk"
        Output:
            Error: invalid input
"""

def problem_1():
    print("Shopping list basics (list operations)")

    initial_items_text = input("Enter your initial items separated by commas: ").strip()
    new_item = input("Enter your item to add: ").strip()
    search_item = input("Enter your item to search: ").strip()

    # Validations
    if not initial_items_text or not new_item or not search_item:
        print("Error: invalid input")
        return

    # Build initial list and normalize spaces
    raw_items = initial_items_text.split(",")
    items_list = []
    for item in raw_items:
        cleaned_item = item.strip()
        if cleaned_item != "":
            items_list.append(cleaned_item)

    # If after cleaning we got an empty list, treat as invalid
    if len(items_list) == 0:
        print("Error: invalid input")
        return

    # Add new item
    items_list.append(new_item)

    found_item = search_item in items_list

    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {found_item}")


# --------------------------------------------------
# Problem 2: Points and distances with tuples
# --------------------------------------------------
"""
Problem 2: Points and distances with tuples
Description:
    Uses tuples to represent two points in a 2D plane: (x1, y1) and (x2, y2).
    The program creates the tuples from numeric input, calculates the
    Euclidean distance between them and computes the midpoint between the
    two points.

Inputs:
    - x1, y1, x2, y2 (float): coordinates of the two points.

Outputs:
    - "Point A:" (x1, y1)
    - "Point B:" (x2, y2)
    - "Distance:" <distance>
    - "Midpoint:" (mx, my)

Validations:
    - All four inputs must be convertible to float.
    - No additional range restrictions are required.

Test cases:
    1) Normal:
        Input: x1 = 0, y1 = 0, x2 = 3, y2 = 4
        Output:
            Point A: (0.0, 0.0)
            Point B: (3.0, 4.0)
            Distance: 5.0
            Midpoint: (1.5, 2.0)
    2) Border:
        Input: x1 = 1, y1 = 1, x2 = 1, y2 = 1
        Output:
            Distance: 0.0
            Midpoint: (1.0, 1.0)
    3) Error:
        Input: x1 = "a", y1 = 0, x2 = 1, y2 = 1
        Output:
            Error: invalid input
"""

def problem_2():
    print("Points and distances with tuples")

    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
    except:
        print("Error: invalid input")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance}")
    print(f"Midpoint: {midpoint}")


# --------------------------------------------------
# Problem 3: Product catalog with dictionary
# --------------------------------------------------
"""
Problem 3: Product catalog with dictionary
Description:
    Manages a simple product catalog using a dictionary where:
        - key: product name (string)
        - value: unit price (float)
    The program reads a product name and a quantity to buy, and if the product
    exists, calculates the total price.

Inputs:
    - product_name (string): product name to buy.
    - quantity (int): quantity to buy.

Outputs:
    - If the product exists:
        - "Unit price:" <unit_price>
        - "Quantity:" <quantity>
        - "Total:" <total_price>
    - If the product does not exist:
        - "Error: product not found"

Validations:
    - product_name must not be empty after strip().
    - quantity must be an integer and greater than 0.
    - Check if product_name exists as a key in the dictionary.

Test cases:
    1) Normal:
        Input: product_name = "ARDUINO UNO", quantity = 2
        Output:
            Unit price: 199.99
            Quantity: 2
            Total: 399.98
    2) Border:
        Input: product_name = "DISPLAY", quantity = 1
        Output:
            Unit price: 79.99
            Quantity: 1
            Total: 79.99
    3) Error:
        Input: product_name = "SENSOR", quantity = 3
        Output:
            Error: product not found
"""

def problem_3():
    print("Product catalog with dictionary")

    product_catalog = {
        "ARDUINO UNO": 199.99,
        "ESP32": 169.99,
        "DISPLAY": 79.99
    }

    product_name = input("Enter your product to buy: ").strip().upper()

    try:
        quantity = int(input("Enter the quantity to buy: "))
    except:
        print("Error: invalid input")
        return

    if not product_name or quantity <= 0:
        print("Error: invalid input")
        return

    if product_name in product_catalog:
        unit_price = product_catalog[product_name]
        total_price = unit_price * quantity
        print(f"Unit price: {unit_price}")
        print(f"Quantity: {quantity}")
        print(f"Total: {total_price}")
    else:
        print("Error: product not found")


# --------------------------------------------------
# Problem 4: Student grades with dict and list
# --------------------------------------------------
"""
Problem 4: Student grades with dict and list
Description:
    Manages the grades of several students using a dictionary where:
        - key: student name (string)
        - value: list of grades (list of float)
    The program reads a student name, calculates the average of their grades
    and indicates whether the student passed (average >= 70.0).

Inputs:
    - student_name (string): name of the student.

Outputs:
    - If the student exists and has grades:
        - "Grades:" <grades_list>
        - "Average:" <average>
        - "Passed:" true|false
    - If the student exists but has no grades:
        - "Error: no grades available for this student"
    - If the student does not exist:
        - "Error: student not found"

Validations:
    - student_name must not be empty after strip().
    - Check if student_name is a key in the dictionary.
    - Check that the list of grades is not empty before computing the average.

Test cases:
    1) Normal:
        Input: student_name = "Charly"
        Output:
            Grades: [100, 85, 90]
            Average: 91.666...
            Passed: True
    2) Border (no grades yet):
        Input: student_name = "Noe"
        Output:
            Error: no grades available for this student
    3) Error:
        Input: student_name = "Unknown"
        Output:
            Error: student not found
"""

def problem_4():
    print("Student grades with dict and list")

    grades = {
        "Charly": [100, 85, 90],
        "Oscar": [78, 60, 54],
        "Noe": []
    }

    student_name = input("Enter the student name to search: ").strip()

    if not student_name:
        print("Error: invalid input")
        return

    if student_name not in grades:
        print("Error: student not found")
        return

    student_grades = grades[student_name]

    if len(student_grades) == 0:
        print("Error: no grades available for this student")
        return

    average = sum(student_grades) / len(student_grades)
    is_passed = average >= 70.0

    print(f"Grades: {student_grades}")
    print(f"Average: {average}")
    print(f"Passed: {is_passed}")


# --------------------------------------------------
# Problem 5: Word frequency counter (list + dict)
# --------------------------------------------------
"""
Problem 5: Word frequency counter (list + dict)
Description:
    Counts the frequency of each word in a sentence. The program:
        1) Reads a sentence.
        2) Converts it to lowercase and splits it into a list of words.
        3) Builds a dictionary where each key is a word and each value is its
           frequency in the sentence.
        4) Displays the full frequency dictionary and the most common word.

Inputs:
    - sentence (string): input sentence.

Outputs:
    - "Words list:" <words_list>
    - "Frequencies:" <freq_dict>
    - "Most common word:" <word>

Validations:
    - sentence must not be empty after strip().
    - After splitting, the words list must not be empty.
    - In this implementation, punctuation is not removed; words are separated
      simply by spaces.

Test cases:
    1) Normal:
        Input: "this is a test this is only a test"
        Output:
            Words list: [...]
            Frequencies: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
            Most common word: this (or any with max frequency)
    2) Border:
        Input: "hello"
        Output:
            Words list: ['hello']
            Frequencies: {'hello': 1}
            Most common word: hello
    3) Error:
        Input: "   "
        Output:
            Error: invalid input
"""

def problem_5():
    print("Word frequency counter")

    sentence = input("Enter your sentence: ").strip().lower()

    if not sentence:
        print("Error: invalid input")
        return

    words_list = sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
        return

    freq_dict = {}
    most_common_word = None
    highest_count = 0

    # Build frequency dictionary
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

        if freq_dict[word] > highest_count:
            highest_count = freq_dict[word]
            most_common_word = word

    print(f"Words list: {words_list}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common_word}")


# --------------------------------------------------
# Problem 6: Simple contact book (dictionary CRUD)
# --------------------------------------------------
"""
Problem 6: Simple contact book (dictionary CRUD)
Description:
    Implements a mini contact book using a dictionary where:
        - key: contact name (string)
        - value: phone number (string)
    The program:
        1) Creates an initial dictionary with some contacts.
        2) Reads an action_text ("ADD", "SEARCH" or "DELETE").
        3) For "ADD": reads name and phone, and adds or updates the contact.
        4) For "SEARCH": reads name and prints the phone if it exists.
        5) For "DELETE": reads name and deletes the contact if it exists.

Inputs:
    - action_text (string): "ADD", "SEARCH" or "DELETE".
    - name (string): contact name (for all actions).
    - phone (string): contact phone (only for "ADD").

Outputs:
    - For "ADD":
        - "Contact saved:" name, phone
    - For "SEARCH":
        - If exists: "Phone:" <phone>
        - If not: "Error: contact not found"
    - For "DELETE":
        - If exists: "Contact deleted:" name
        - If not: "Error: contact not found"

Validations:
    - Normalize action_text to uppercase.
    - action_text must be one of the three valid options.
    - name must not be empty after strip().
    - For "ADD": phone must not be empty after strip().

Test cases:
    1) Normal (ADD then SEARCH):
        Input:
            action_text = "ADD", name = "Alice", phone = "1234567890"
        Output:
            Contact saved: Alice, 1234567890
    2) Border (SEARCH existing):
        Input:
            action_text = "SEARCH", name = "Charly"
        Output:
            Phone: 8341520000
    3) Error (invalid action):
        Input:
            action_text = "UPDATE", name = "Bob"
        Output:
            Error: invalid input
"""

def problem_6():
    print("Simple contact book (dictionary CRUD)")

    contacts = {
        "Gerardo": "8341231234",
        "Charly": "8341520000",
        "Oscar": "8349801523"
    }

    action_text = input("Enter the action to do (ADD/SEARCH/DELETE): ")
    action_text = action_text.strip().upper()

    add_flag = (action_text == "ADD")
    search_flag = (action_text == "SEARCH")
    delete_flag = (action_text == "DELETE")

    if not (add_flag or search_flag or delete_flag):
        print("Error: invalid input")
        return

    name = input("Enter the name of the contact: ").strip()

    if not name:
        print("Error: invalid input")
        return

    # Normalize names to title case to match dictionary keys
    name = name.lower().title()

    phone = None
    if add_flag:
        phone = input("Enter the contact's phone to add: ").strip()
        if not phone:
            print("Error: invalid input")
            return

    if add_flag:
        contacts[name] = phone
        print(f"Contact saved: {name}, {phone}")
        print(f"Contacts: {contacts}")
    elif search_flag:
        if name in contacts:
            print(f"Phone: {contacts[name]}")
        else:
            print("Error: contact not found")
    elif delete_flag:
        if name in contacts:
            contacts.pop(name)
            print(f"Contact deleted: {name}")
            print(f"Contacts: {contacts}")
        else:
            print("Error: contact not found")
    else:
        print("Error: invalid input")


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
    Lists, tuples and dictionaries each solve different needs when working
    with collections of data in Python. Lists are flexible and allow adding
    and removing elements, which is useful for shopping lists or dynamic
    sets of values. Tuples provide an immutable, ordered structure that works
    well for fixed data such as coordinates or configuration points.
    Dictionaries enable very fast lookup of values by key, which makes them
    ideal for catalogs, student grade records, word frequency maps and
    contact books. Combining these structures, such as dictionaries of lists,
    is a powerful pattern for organizing more complex information in a
    readable and efficient way.
"""

"""
References:
    1) Python documentation - Built-in Types: list, tuple, dict
    2) Python tutorial - Data Structures (docs.python.org)
    3) "Automate the Boring Stuff with Python" by Al Sweigart – chapters on lists and dictionaries
    4) Real Python - "Lists and Tuples in Python"
    5) Real Python - "Dictionaries in Python"
"""