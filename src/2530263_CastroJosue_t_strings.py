"""
Cover:
    Name: Josue de Jesus Castro Martinez
    ID: 2530263
    Group: IM 1-1
"""

"""
Executive Summary:
    In Python, a string is an immutable sequence of characters used to represent text.
    Because strings are immutable, any modification such as replace, strip or lower
    creates a new string instead of changing the original one in place.
    Basic operations on strings include concatenation, measuring length, extracting
    substrings with slicing, searching for patterns, replacing parts of the text,
    and splitting or joining by delimiters.
    Validating and normalizing text input (for example, emails, names and passwords)
    is very important to avoid incorrect formats, extra spaces and inconsistent
    capitalization that can cause logical errors.
    This document presents six problems that use string methods for formatting names,
    validating emails, checking palindromes, analyzing sentences, classifying password
    strength and formatting product labels, including inputs, outputs, validations
    and test cases for each problem.
"""

"""
String Principles and Good Practices:
    - Strings are immutable: every "change" actually creates a new string.
    - It is good practice to normalize user input with strip() and lower()
      before comparing values or checking conditions.
    - Avoid "magic numbers" in indices and slicing; document what each slice extracts.
    - Prefer using built-in string methods (strip, split, replace, etc.)
      instead of reimplementing basic logic manually.
    - Design validations clearly: first check that the input is not empty,
      then check simple format constraints such as presence of '@' in emails.
    - Write readable code with descriptive variable names and understandable
      error messages like "Error: invalid input".
"""

# --------------------------------------------------
# Problem 1: Full name formatter (name + initials)
# --------------------------------------------------
"""
Problem 1: Full name formatter (name + initials)
Description:
    Given the full name of a person in a single string, the program:
        1) Normalizes the text (strip spaces, remove extra spaces, fix case).
        2) Prints the formatted name in Title Case.
        3) Prints the initials in the format X.X.X.

Inputs:
    - full_name (string): full name possibly in any case and with extra spaces.

Outputs:
    - "Formatted name: <Name In Title Case>"
    - "Initials: <X.X.X.>"

Validations:
    - full_name must not be empty after strip().
    - The name must contain at least two words (name and last name).
    - The input must not be only spaces.

Test cases:
    1) Normal:
        Input: "  juan carlos tovar  "
        Output:
            Formatted name: Juan Carlos Tovar
            Initials: J.C.T.
    2) Border:
        Input: "ana   lopez"
        Output:
            Formatted name: Ana Lopez
            Initials: A.L.
    3) Error:
        Input: "   singleName   "
        Output:
            Error: invalid input
"""

def problem_1():
    print("Full name formatter")
    full_name = input("Enter your full name: ")

    # Normalize input
    full_name = full_name.strip().lower()
    name_parts = full_name.split()
    initials = ""

    # Validations
    if full_name != "" and len(name_parts) >= 2:
        formatted_name = " ".join(name_parts).title()
        print(f"Formatted name: {formatted_name}")

        for name in name_parts:
            initials += name[0].upper() + "."
        print(f"Initials: {initials}")
    else:
        print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Simple email validator (structure + domain)
# --------------------------------------------------
"""
Problem 2: Simple email validator (structure + domain)
Description:
    Validates whether an email address has a basic correct format:
        - Contains exactly one '@'.
        - After '@' there is at least one '.'.
        - Contains no spaces.
    If the email is valid, it also prints the domain part (after '@').

Inputs:
    - email_text (string): email address entered by the user.

Outputs:
    - "Valid email: true" or "Valid email: false"
    - If valid: "Domain: <domain_part>"

Validations:
    - email_text must not be empty after strip().
    - There must be exactly one '@' character.
    - There must be no spaces in the email.
    - After '@' there must be at least one '.'.

Test cases:
    1) Normal:
        Input: "user@example.com"
        Output:
            Valid email: true
            Domain: example.com
    2) Border:
        Input: "a@b.co"
        Output:
            Valid email: true
            Domain: b.co
    3) Error:
        Input: "  invalid email@domain  "
        Output:
            Valid email: false
"""

def problem_2():
    print("Simple email validator")
    email_text = input("Enter your email: ")

    # Normalize input
    email_text = email_text.strip()

    # Basic validation: not empty
    if email_text == "":
        print("Valid email: false")
        return

    at_position = email_text.find("@")

    # Check basic format rules
    if (
        email_text.count("@") == 1
        and " " not in email_text
        and at_position != -1
        and "." in email_text[at_position + 1 :]
    ):
        print("Valid email: true")
        domain_part = email_text[at_position + 1 :]
        print(f"Domain: {domain_part}")
    else:
        print("Valid email: false")


# --------------------------------------------------
# Problem 3: Palindrome checker (ignoring spaces and case)
# --------------------------------------------------
"""
Problem 3: Palindrome checker (ignoring spaces and case)
Description:
    Determines whether a phrase is a palindrome, meaning it reads the same
    from left to right and from right to left, ignoring spaces and case.

Inputs:
    - phrase (string): phrase entered by the user.

Outputs:
    - "Is palindrome: true" or "Is palindrome: false"
    - (Optional) "Normalized phrase: <text_without_spaces_and_lowercase>"

Validations:
    - phrase must not be empty after strip().
    - After removing spaces, length must be at least 3 characters.

Test cases:
    1) Normal:
        Input: "Anita lava la tina"
        Output:
            Normalized phrase: anitalavalatina
            Is palindrome: true
    2) Border:
        Input: "a b a"
        Output:
            Normalized phrase: aba
            Is palindrome: true
    3) Error:
        Input: "  a  "
        Output:
            Error: invalid input
"""

def problem_3():
    print("Palindrome checker")
    phrase = input("Enter your phrase: ")

    # Normalize input
    phrase = phrase.strip()

    # Validate not empty
    if phrase == "":
        print("Error: invalid input")
        return

    # Remove spaces and lower the case
    normalized_phrase = phrase.replace(" ", "").lower()

    # Validate minimal length after cleaning
    if len(normalized_phrase) < 3:
        print("Error: invalid input")
        return

    reversed_phrase = normalized_phrase[::-1]

    print(f"Normalized phrase: {normalized_phrase}")
    if normalized_phrase == reversed_phrase:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")


# --------------------------------------------------
# Problem 4: Sentence word stats (lengths and first/last word)
# --------------------------------------------------
"""
Problem 4: Sentence word stats (lengths and first/last word)
Description:
    Given a sentence, the program:
        1) Normalizes spaces (removes leading and trailing spaces).
        2) Splits the sentence into words by spaces.
        3) Prints:
            - Total number of words.
            - First word.
            - Last word.
            - Shortest word (by length).
            - Longest word (by length).

Inputs:
    - sentence (string): sentence entered by the user.

Outputs:
    - "Word count: <n>"
    - "First word: <...>"
    - "Last word: <...>"
    - "Shortest word: <...>"
    - "Longest word: <...>"

Validations:
    - sentence must not be empty after strip().
    - There must be at least one valid word after split().

Test cases:
    1) Normal:
        Input: "  this is a simple test  "
        Output:
            Word count: 5
            First word: this
            Last word: test
            Shortest word: a
            Longest word: simple
    2) Border:
        Input: "word"
        Output:
            Word count: 1
            First word: word
            Last word: word
            Shortest word: word
            Longest word: word
    3) Error:
        Input: "   "
        Output:
            Error: invalid input
"""

def problem_4():
    print("Sentence word stats")
    sentence = input("Enter your sentence: ")

    # Normalize input
    sentence = sentence.strip()
    words = sentence.split()

    # Validations
    if sentence == "" or len(words) == 0:
        print("Error: invalid input")
        return

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")

    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# --------------------------------------------------
# Problem 5: Password strength classifier
# --------------------------------------------------
"""
Problem 5: Password strength classifier
Description:
    Classifies a password as "weak", "medium" or "strong" based on simple rules.

    Example rules used:
        - Weak:
            - Length < 8, or
            - All lowercase, or
            - All uppercase.
        - Medium:
            - Length >= 8, and
            - Has a mix of letters (uppercase/lowercase) or includes digits,
              but does not meet all "strong" conditions.
        - Strong:
            - Length >= 8, and contains at least:
                * one uppercase letter,
                * one lowercase letter,
                * one digit,
                * one non-alphanumeric symbol.

Inputs:
    - password_input (string): password entered by the user.

Outputs:
    - "Password strength: weak"
    - "Password strength: medium"
    - "Password strength: strong"
    - Or: "Error: invalid input" if empty.

Validations:
    - Password must not be empty after strip().
    - Length is checked with len().

Test cases:
    1) Normal (strong):
        Input: "Abc123!@"
        Output:
            Password strength: strong
    2) Border (medium):
        Input: "Password1"
        Output:
            Password strength: medium
    3) Error:
        Input: "   "
        Output:
            Error: invalid input
"""

def problem_5():
    print("Password strength classifier")
    password_input = input("Enter your password: ")

    # Normalize input
    password_input = password_input.strip()

    # Validation: not empty
    if password_input == "":
        print("Error: invalid input")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    length_ok = len(password_input) >= 8

    # Strong password
    if length_ok and has_lower and has_upper and has_digit and has_symbol:
        print("Password strength: strong")
    # Medium password
    elif length_ok and ((has_lower and has_upper) or has_digit):
        print("Password strength: medium")
    # Weak password
    else:
        print("Password strength: weak")


# --------------------------------------------------
# Problem 6: Product label formatter (fixed-width text)
# --------------------------------------------------
"""
Problem 6: Product label formatter (fixed-width text)
Description:
    Given a product name and its price, generate a single-line label:

        Product: <NAME> | Price: $<PRICE>

    The entire label must be exactly 30 characters long:
        - If shorter than 30, pad with spaces at the end.
        - If longer than 30, truncate to the first 30 characters.

Inputs:
    - product_name (string): name of the product.
    - price_value (string, converted to number): product price.

Outputs:
    - 'Label: "<exactly_30_characters>"'
      (Quotes are used to visualize spaces.)

Validations:
    - product_name must not be empty after strip().
    - price_value must be convertible to a positive float.

Test cases:
    1) Normal:
        Input:
            product_name = "Bread"
            price_value = "12.5"
        Output:
            Label: "Product: Bread | Price: $12.5   "
    2) Border (exactly 30 chars after format):
        Input:
            product_name = "LongProductName"
            price_value = "99"
        Output:
            Label: "<30-character-exact-label>"
    3) Error:
        Input:
            product_name = "   "
            price_value = "abc"
        Output:
            Error: invalid input
"""

def problem_6():
    print("Product label formatter")
    product_name = input("Enter your product name: ").strip()
    price_value = input("Enter the price of your product: ").strip()

    # Validate product_name
    if product_name == "":
        print("Error: invalid input")
        return

    # Validate price_value as positive number
    try:
        price_number = float(price_value)
        if price_number <= 0:
            print("Error: invalid input")
            return
    except:
        print("Error: invalid input")
        return

    # Create base label
    label = f"Product: {product_name} | Price: ${price_value}"

    # Adjust label to exactly 30 characters
    if len(label) > 30:
        label = label[:30]
    elif len(label) < 30:
        label = label.ljust(30)

    print(f'Label: "{label}"')


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
    Handling strings in Python is essential for almost all input and output
    operations, including names, emails, passwords and formatted text labels.
    Methods like lower(), upper(), strip(), split() and join() are very useful
    to normalize user input before applying comparisons or validations.
    Normalizing text avoids errors caused by extra spaces or inconsistent
    capitalization and makes the program behavior more predictable.
    Designing validation rules carefully helps prevent invalid data and
    reduces the risk of logical bugs caused by unexpected formats.
    Through these problems, it becomes clear that string immutability and
    slicing operations are powerful tools for building clean and reusable code.
"""

"""
References:
    1) Python documentation - Built-in Types: Text Sequence Type — str
    2) Python documentation - Built-in Functions (len, print, etc.)
    3) Python Tutorial - 3.1.3. Strings (docs.python.org)
    4) "Automate the Boring Stuff with Python" by Al Sweigart – Chapters on strings
    5) Real Python - "Strings and Character Data in Python"
"""