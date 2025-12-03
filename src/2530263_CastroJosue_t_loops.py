"""
Cover:
    Name: Josue de Jesus Castro Martinez
    ID: 2530263
    Group: IM 1-1
"""

"""
Executive Summary:
    In Python, loops are control structures that allow repeating blocks of code
    multiple times. A for loop is typically used when the number of iterations
    is known in advance, such as iterating over a range of numbers or over the
    elements of a sequence. A while loop is more natural when repetition depends
    on a condition, like reading values until a sentinel is entered or until the
    user chooses to exit a menu.
    Counters and accumulators are variables that track how many iterations have
    occurred or the running total of values inside a loop. It is very important
    to define clear exit conditions and update control variables correctly to
    avoid infinite loops. This document presents six problems using for and
    while loops for ranges, tables, sentinel-based inputs, password attempts,
    text menus and pattern printing, including inputs, outputs, validations and
    concrete test cases.
"""

"""
Principles and Good Practices:
    - Use for loops when you know the number of iterations in advance, such as
      summing from 1 to n or printing a multiplication table.
    - Use while loops when the number of iterations depends on a condition,
      such as reading until a sentinel value or until the correct password is
      entered.
    - Always initialize counters and accumulators before entering the loop so
      that they start from a known value.
    - In while loops, make sure to update the variables that appear in the
      condition to avoid infinite loops and to guarantee termination.
    - Keep the body of loops as simple as possible; if the logic is complex,
      move it into helper functions for better readability.
"""

# --------------------------------------------------
# Problem 1: Sum of range with for
# --------------------------------------------------
"""
Problem 1: Sum of range with for
Description:
    Calculates the sum of all integers from 1 to n (inclusive) using a for loop.
    Also calculates the sum of only the even numbers in that same range.

Inputs:
    - n (int): upper limit of the range.

Outputs:
    - "Sum 1..n:" <total_sum>
    - "Even sum 1..n:" <even_sum>

Validations:
    - n must be convertible to int.
    - n must be greater than or equal to 1.
    - If validation fails, print "Error: invalid input".

Test cases:
    1) Normal:
        Input: n = 5
        Output:
            Sum 1..n: 15
            Even sum 1..n: 6
    2) Border:
        Input: n = 1
        Output:
            Sum 1..n: 1
            Even sum 1..n: 0
    3) Error:
        Input: n = 0
        Output:
            Error: invalid input
"""

def problem_1():
    print("Sum of range with for")
    try:
        n = int(input("Enter the upper limit: "))
    except:
        print("Error: invalid input")
        return

    if n >= 1:
        total_sum = 0
        even_sum = 0

        for value in range(1, n + 1):
            total_sum += value
            if value % 2 == 0:
                even_sum += value

        print(f"Sum 1..n: {total_sum}")
        print(f"Even sum 1..n: {even_sum}")
    else:
        print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Multiplication table with for
# --------------------------------------------------
"""
Problem 2: Multiplication table with for
Description:
    Generates and prints the multiplication table of a base number from 1 to m.
    Each line shows the multiplication in the form "base x i = result".

Inputs:
    - base (int): base number of the multiplication table.
    - m (int): upper limit of the table.

Outputs:
    - One line per multiplication:
        - "base x 1 = result"
        - ...
        - "base x m = result"

Validations:
    - base and m must be convertible to int.
    - m must be greater than or equal to 1.
    - If validation fails, print "Error: invalid input".

Test cases:
    1) Normal:
        Input: base = 5, m = 4
        Output:
            5 x 1 = 5
            5 x 2 = 10
            5 x 3 = 15
            5 x 4 = 20
    2) Border:
        Input: base = 3, m = 1
        Output:
            3 x 1 = 3
    3) Error:
        Input: base = 2, m = 0
        Output:
            Error: invalid input
"""

def problem_2():
    print("Multiplication table with for")

    try:
        base = int(input("Enter base of multiplication table: "))
        m = int(input("Enter the upper limit: "))
    except:
        print("Error: invalid input")
        return

    if m < 1:
        print("Error: invalid input")
        return

    for value in range(1, m + 1):
        result = base * value
        print(f"{base} x {value} = {result}")


# --------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
# --------------------------------------------------
"""
Problem 3: Average of numbers with while and sentinel
Description:
    Reads numbers one by one until the user enters a sentinel value (-1).
    Calculates the count, total sum and average of all valid numbers entered
    before the sentinel. If the user only enters the sentinel without any
    valid numbers, prints an error message.

Inputs:
    - number (float): read repeatedly.
    - SENTINEL_VALUE (float): fixed in the code, e.g. -1.

Outputs:
    - "Count:" <count>
    - "Total sum:" <sum_value>
    - "Average:" <average_value>
    - If there is no valid data:
        - "Error: no data"

Validations:
    - Each input must be convertible to float.
    - The sentinel value is not included in the calculations.

Test cases:
    1) Normal:
        Input: 10, 20, 30, -1
        Output:
            Count: 3
            Total sum: 60.0
            Average: 20.0
    2) Border:
        Input: 5, -1
        Output:
            Count: 1
            Total sum: 5.0
            Average: 5.0
    3) Error:
        Input: -1
        Output:
            Error: no data
"""

def problem_3():
    print("Average of numbers with while and sentinel")

    count = 0
    sum_value = 0.0
    SENTINEL_VALUE = -1.0

    while True:
        try:
            number = float(input("Enter number to add (or -1 to finish): "))
        except:
            print("Error: invalid input")
            continue

        if number == SENTINEL_VALUE:
            if count == 0:
                print("Error: no data")
            else:
                average_value = sum_value / count
                print(f"Count: {count}")
                print(f"Total sum: {sum_value}")
                print(f"Average: {average_value}")
            break
        else:
            count += 1
            sum_value += number


# --------------------------------------------------
# Problem 4: Password attempts with while
# --------------------------------------------------
"""
Problem 4: Password attempts with while
Description:
    Implements a simple password check system. A correct password is stored
    in the code and the user has a limited number of attempts to enter it.
    If the user enters the correct password within the maximum number of
    attempts, a success message is shown. Otherwise, the account is locked.

Inputs:
    - user_password (string): entered in each attempt.

Outputs:
    - On success:
        - "Login success"
    - On exhausting attempts:
        - "Account locked"

Validations:
    - MAX_ATTEMPTS > 0 (constant in the code).
    - Count attempts correctly and stop when the limit is reached.

Test cases:
    1) Normal (success on second attempt):
        Password in code: "1234"
        Input: "0000", "1234"
        Output:
            Incorrect password
            Login success
    2) Border (success on last attempt):
        Input: "0000", "1111", "1234"
        Output:
            Incorrect password
            Incorrect password
            Login success
    3) Error (all attempts fail):
        Input: "0000", "1111", "2222"
        Output:
            Incorrect password
            Incorrect password
            Incorrect password
            Account locked
"""

def problem_4():
    print("Password attempts with while")

    MAX_ATTEMPTS = 3
    PASSWORD = "1234"
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        user_password = input("Enter the password: ")
        attempts += 1

        if user_password == PASSWORD:
            print("Login success")
            break
        else:
            print("Incorrect password")

    if attempts == MAX_ATTEMPTS and user_password != PASSWORD:
        print("Account locked")


# --------------------------------------------------
# Problem 5: Simple menu with while
# --------------------------------------------------
"""
Problem 5: Simple menu with while
Description:
    Implements a simple text menu that repeats until the user selects the
    exit option. The menu allows the user to show a greeting, show the
    current counter value, increment the counter or exit.

Menu:
    1) Show greeting
    2) Show current counter value
    3) Increment counter
    0) Exit

Inputs:
    - option (string): user choice.

Outputs:
    - For option "1":
        - "Hello!"
    - For option "2":
        - "Counter:" <counter_value>
    - For option "3":
        - "Counter incremented"
    - For option "0":
        - "Bye!"
    - For invalid options:
        - "Error: invalid option"

Validations:
    - Accept only options "0", "1", "2" and "3" as valid.
    - Keep asking until the user selects "0" to exit.

Test cases:
    1) Normal:
        Input: 1, 3, 2, 0
        Output:
            Hello!
            Counter incremented
            Counter: 1
            Bye!
    2) Border:
        Input: 2, 0
        Output:
            Counter: 0
            Bye!
    3) Error:
        Input: 9, 0
        Output:
            Error: invalid option
            Bye!
"""

def problem_5():
    print("Simple menu with while")

    counter = 0

    while True:
        print("""
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
        """)
        option = input("Enter the number of the option to do: ").strip()

        if option == "1":
            print("Hello!")
        elif option == "2":
            print(f"Counter: {counter}")
        elif option == "3":
            counter += 1
            print("Counter incremented")
        elif option == "0":
            print("Bye!")
            break
        else:
            print("Error: invalid option")


# --------------------------------------------------
# Problem 6: Pattern printing with nested loops
# --------------------------------------------------
"""
Problem 6: Pattern printing with nested loops
Description:
    Uses nested loops to print a right triangle pattern of asterisks with n
    rows. Additionally, prints an inverted triangle pattern using the same
    value of n.

Inputs:
    - n (int): number of rows of the pattern.

Outputs:
    - First pattern (increasing):
        *
        **
        ***
        ...
    - Second pattern (decreasing):
        ****
        ***
        **
        *

Validations:
    - n must be convertible to int.
    - n must be greater than or equal to 1.
    - If validation fails, print "Error: invalid input".

Test cases:
    1) Normal:
        Input: n = 4
        Output:
            Pattern line by line:
            *
            **
            ***
            ****
            Inverted pattern:
            ****
            ***
            **
            *
    2) Border:
        Input: n = 1
        Output:
            Pattern line by line:
            *
            Inverted pattern:
            *
    3) Error:
        Input: n = 0
        Output:
            Error: invalid input
"""

def problem_6():
    print("Pattern printing with nested loops")

    try:
        n = int(input("Enter n: "))
    except:
        print("Error: invalid input")
        return

    if n < 1:
        print("Error: invalid input")
        return

    print("Pattern line by line:")
    for i in range(1, n + 1):
        print("*" * i)

    print("Inverted pattern:")
    for i in range(n, 0, -1):
        print("*" * i)


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
    For loops are very convenient when the number of iterations is known,
    such as iterating over a range or printing a table of values, while
    while loops are more flexible when repetition depends on conditions
    like sentinels or menu choices. Counters and accumulators inside loops
    help track the number of inputs and the running total of values,
    which are important in tasks like computing sums and averages.
    When using while loops, failing to update control variables correctly
    can easily create infinite loops, so careful design of exit conditions
    is essential. Text menus and password retry systems are classic examples
    where while loops are the most natural choice.
    Nested loops and simple patterns like triangles of asterisks provide a
    good way to practice reasoning about rows and columns and loop ranges.
"""

"""
References:
    1) Python documentation - The for statement (docs.python.org)
    2) Python documentation - The while statement (docs.python.org)
    3) Python tutorial - Control Flow Tools
    4) "Automate the Boring Stuff with Python" by Al Sweigart – chapters on flow control and loops
    5) Real Python - "Python for Loops" and "Python while Loops"
"""