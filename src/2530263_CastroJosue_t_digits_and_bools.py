"""
Cover:
    Name: Josue de Jesus Castro Martinez
    ID: 2530263
    Group: IM 1-1
"""

"""
Executive Summary:
    In Python, the int type represents whole numbers while the float type
    represents real numbers with decimal parts, which are essential for
    precise calculations like temperatures, salaries and ratios.
    Boolean values (True and False) are produced mainly by comparisons
    between numeric expressions and are used to control decision making
    with if statements.
    It is very important to validate ranges (for example, non-negative
    income or hours) and avoid division by zero before performing numeric
    operations to prevent runtime errors and invalid results.
    This document covers six problems that use integers, floats and
    booleans to convert temperatures, compute payments, validate discounts,
    calculate basic statistics, evaluate loan eligibility and compute BMI.
    Each problem includes a description of inputs and outputs, data
    validation rules and test cases (normal, border and error) to verify
    correctness.
"""

"""
Principles and Good Practices:
    - Use appropriate types: int for counters or discrete quantities and
      float for values with decimal precision such as money or measurements.
    - Avoid duplicating complex expressions by storing intermediate results
      in descriptive variables that can be reused and easily read.
    - Validate data before operating on it (for example, check that hours,
      salaries and incomes are not negative and that denominators are non-zero).
    - Use descriptive variable names and clear user messages like
      "Error: invalid input" to make the program easy to understand.
    - Document clearly what boolean flags mean in each context, indicating
      what True and False represent (e.g., eligible, has_overtime).
"""

# --------------------------------------------------
# Problem 1: Temperature converter and range flag
# --------------------------------------------------
"""
Problem 1: Temperature converter and range flag
Description:
    Converts a temperature in Celsius to Fahrenheit and Kelvin, and creates
    a boolean flag is_high_temperature that is True if the Celsius value is
    greater than or equal to 30.0 and False otherwise.

Inputs:
    - temp_c (float): temperature in degrees Celsius.

Outputs:
    - "Fahrenheit:" <temp_f>
    - "Kelvin:" <temp_k>
    - "High temperature:" true|false

Validations:
    - Verify that temp_c can be converted to float.
    - Do not allow physically impossible Kelvin temperatures (temp_k < 0.0).
      In that case, print "Error: invalid input".

Test cases:
    1) Normal:
        Input: temp_c = 30.0
        Output:
            Fahrenheit: 86.0
            Kelvin: 303.15
            High temperature: True
    2) Border:
        Input: temp_c = -273.15
        Output:
            Fahrenheit: -459.66999999999996
            Kelvin: 0.0
            High temperature: False
    3) Error:
        Input: temp_c = -300.0
        Output:
            Error: invalid input
"""

def problem_1():
    print("Temperature converter and range flag")

    try:
        temp_c = float(input("Enter the temperature in Celsius: "))
    except:
        print("Error: invalid input")
        return

    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15

    if temp_k >= 0.0:
        print(f"Fahrenheit: {temp_f}")
        print(f"Kelvin: {temp_k}")
        is_high_temperature = (temp_c >= 30.0)
        print(f"High temperature: {is_high_temperature}")
    else:
        print("Error: invalid input")


# --------------------------------------------------
# Problem 2: Work hours and overtime payment
# --------------------------------------------------
"""
Problem 2: Work hours and overtime payment
Description:
    Calculates the weekly total pay for a worker. Up to 40 hours are paid at
    the regular hourly_rate. Extra hours (> 40) are paid at 150% of the
    regular rate. Also generates a boolean has_overtime that indicates
    whether the worker has overtime hours.

Inputs:
    - hours_worked (float): hours worked in the week.
    - hourly_rate (float): pay per hour.

Outputs:
    - "Regular pay:" <regular_pay>
    - "Overtime pay:" <overtime_pay>
    - "Total pay:" <total_pay>
    - "Has overtime:" true|false

Validations:
    - hours_worked >= 0
    - hourly_rate > 0
    - If any validation fails, print "Error: invalid input".

Test cases:
    1) Normal:
        Input: hours_worked = 45, hourly_rate = 100
        Output:
            Regular pay: 4000.0
            Overtime pay: 750.0
            Total pay: 4750.0
            Has overtime: True
    2) Border:
        Input: hours_worked = 40, hourly_rate = 80
        Output:
            Regular pay: 3200.0
            Overtime pay: 0.0
            Total pay: 3200.0
            Has overtime: False
    3) Error:
        Input: hours_worked = -5, hourly_rate = 100
        Output:
            Error: invalid input
"""

def problem_2():
    print("Work hours and overtime payment")

    try:
        hours_worked = float(input("Enter your hours worked: "))
        hourly_rate = float(input("Enter your hourly rate: "))
    except:
        print("Error: invalid input")
        return

    if hours_worked >= 0 and hourly_rate > 0:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = (overtime_hours > 0)

        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")
        print(f"Has overtime: {has_overtime}")
    else:
        print("Error: invalid input")


# --------------------------------------------------
# Problem 3: Discount eligibility with booleans
# --------------------------------------------------
"""
Problem 3: Discount eligibility with booleans
Description:
    Determines whether a customer is eligible for a discount. A discount is
    granted if:
        - is_student is True OR
        - is_senior is True OR
        - purchase_total >= 1000.0
    If eligible, a 10% discount is applied to the purchase total.

Inputs:
    - purchase_total (float): total amount of the purchase.
    - is_student_text (string): "YES" or "NO".
    - is_senior_text (string): "YES" or "NO".

Outputs:
    - "Discount eligible:" true|false
    - "Final total:" <final_total>

Validations:
    - purchase_total >= 0.0
    - Normalize is_student_text and is_senior_text to uppercase.
    - Convert them to booleans is_student and is_senior.
    - If any text is not "YES" or "NO", print "Error: invalid input".

Test cases:
    1) Normal:
        Input: purchase_total = 1200.0, is_student_text = "NO", is_senior_text = "NO"
        Output:
            Discount eligible: True
            Final total: 1080.0
    2) Border:
        Input: purchase_total = 1000.0, is_student_text = "NO", is_senior_text = "NO"
        Output:
            Discount eligible: True
            Final total: 900.0
    3) Error:
        Input: purchase_total = -50.0, is_student_text = "YES", is_senior_text = "NO"
        Output:
            Error: invalid input
"""

def problem_3():
    print("Discount eligibility with booleans")

    try:
        purchase_total = float(input("Enter your purchase total: "))
    except:
        print("Error: invalid input")
        return

    if purchase_total < 0.0:
        print("Error: invalid input")
        return

    is_student_text = input("Are you a student? (YES/NO): ")
    is_student_text = is_student_text.strip().upper()

    if is_student_text == "YES":
        is_student = True
    elif is_student_text == "NO":
        is_student = False
    else:
        print("Error: invalid input")
        return

    is_senior_text = input("Are you a senior? (YES/NO): ")
    is_senior_text = is_senior_text.strip().upper()

    if is_senior_text == "YES":
        is_senior = True
    elif is_senior_text == "NO":
        is_senior = False
    else:
        print("Error: invalid input")
        return

    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total

    print(f"Discount eligible: {discount_eligible}")
    print(f"Final total: {final_total}")


# --------------------------------------------------
# Problem 4: Basic statistics of three integers
# --------------------------------------------------
"""
Problem 4: Basic statistics of three integers
Description:
    Reads three integers and calculates the sum, the average (as a float),
    the maximum value, the minimum value and a boolean all_even that indicates
    whether all three numbers are even.

Inputs:
    - n1 (int)
    - n2 (int)
    - n3 (int)

Outputs:
    - "Sum:" <sum_value>
    - "Average:" <average_value>
    - "Max:" <max_value>
    - "Min:" <min_value>
    - "All even:" true|false

Validations:
    - Verify that the three values can be converted to int.
    - No additional range restrictions (negative values are allowed).

Test cases:
    1) Normal:
        Input: n1 = 2, n2 = 4, n3 = 6
        Output:
            Sum: 12
            Average: 4.0
            Max: 6
            Min: 2
            All even: True
    2) Border:
        Input: n1 = -1, n2 = 0, n3 = 3
        Output:
            Sum: 2
            Average: 0.6666...
            Max: 3
            Min: -1
            All even: False
    3) Error:
        Input: n1 = "a", n2 = 2, n3 = 3
        Output:
            Error: invalid input
"""

def problem_4():
    print("Basic statistics of three integers")

    try:
        n1 = int(input("Enter your first integer value: "))
        n2 = int(input("Enter your second integer value: "))
        n3 = int(input("Enter your third integer value: "))
    except:
        print("Error: invalid input")
        return

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")


# --------------------------------------------------
# Problem 5: Loan eligibility (income and debt ratio)
# --------------------------------------------------
"""
Problem 5: Loan eligibility (income and debt ratio)
Description:
    Determines whether a person is eligible for a loan based on:
        - monthly_income (float)
        - monthly_debt (float)
        - credit_score (int)
    The debt ratio is defined as: debt_ratio = monthly_debt / monthly_income.
    A person is eligible if:
        - monthly_income >= 8000.0 AND
        - debt_ratio <= 0.4 AND
        - credit_score >= 650.

Inputs:
    - monthly_income (float): monthly income.
    - monthly_debt (float): monthly debt payments.
    - credit_score (int): credit score.

Outputs:
    - "Debt ratio:" <debt_ratio>
    - "Eligible:" true|false

Validations:
    - monthly_income > 0.0 (to avoid division by zero).
    - monthly_debt >= 0.0
    - credit_score >= 0
    - If any validation fails, print "Error: invalid input".

Test cases:
    1) Normal:
        Input: monthly_income = 10000.0, monthly_debt = 3000.0, credit_score = 700
        Output:
            Debt ratio: 0.3
            Eligible: True
    2) Border:
        Input: monthly_income = 8000.0, monthly_debt = 3200.0, credit_score = 650
        Output:
            Debt ratio: 0.4
            Eligible: True
    3) Error:
        Input: monthly_income = 0.0, monthly_debt = 2000.0, credit_score = 700
        Output:
            Error: invalid input
"""

def problem_5():
    print("Loan eligibility (income and debt ratio)")

    try:
        monthly_income = float(input("Enter your monthly income: "))
        monthly_debt = float(input("Enter your monthly debt: "))
        credit_score = int(input("Enter your credit score: "))
    except:
        print("Error: invalid input")
        return

    if monthly_income > 0.0 and monthly_debt >= 0.0 and credit_score >= 0:
        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )
        print(f"Debt ratio: {debt_ratio}")
        print(f"Eligible: {eligible}")
    else:
        print("Error: invalid input")


# --------------------------------------------------
# Problem 6: Body Mass Index (BMI) and category flag
# --------------------------------------------------
"""
Problem 6: Body Mass Index (BMI) and category flag
Description:
    Calculates the body mass index (BMI) using the formula:
        bmi = weight_kg / (height_m * height_m)
    and generates boolean flags indicating:
        - is_underweight (bmi < 18.5)
        - is_normal (18.5 <= bmi < 25.0)
        - is_overweight (bmi >= 25.0)

Inputs:
    - weight_kg (float): weight in kilograms.
    - height_m (float): height in meters.

Outputs:
    - "BMI:" <bmi_rounded_to_2_decimals>
    - "Underweight:" true|false
    - "Normal:" true|false
    - "Overweight:" true|false

Validations:
    - weight_kg > 0.0
    - height_m > 0.0
    - If any validation fails, print "Error: invalid input".

Test cases:
    1) Normal:
        Input: weight_kg = 70, height_m = 1.75
        Output:
            BMI: 22.86
            Underweight: False
            Normal: True
            Overweight: False
    2) Border:
        Input: weight_kg = 50, height_m = 1.65
        Output:
            BMI: 18.37
            Underweight: True
            Normal: False
            Overweight: False
    3) Error:
        Input: weight_kg = -60, height_m = 1.7
        Output:
            Error: invalid input
"""

def problem_6():
    print("Body Mass Index (BMI) and category flag")

    try:
        weight_kg = float(input("Enter your weight in kg: "))
        height_m = float(input("Enter your height in meters: "))
    except:
        print("Error: invalid input")
        return

    if weight_kg > 0.0 and height_m > 0.0:
        bmi = weight_kg / (height_m ** 2)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print(f"BMI: {round(bmi, 2)}")
        print(f"Underweight: {is_underweight}")
        print(f"Normal: {is_normal}")
        print(f"Overweight: {is_overweight}")
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
    Integers and floats are used together to model real-world quantities
    such as temperatures, working hours, salaries, debts and health metrics.
    Comparisons between numeric values produce booleans that enable decision
    making through if statements, for example to decide eligibility or to
    classify values into categories.
    Validating numeric ranges and avoiding division by zero is essential to
    prevent runtime errors and logically invalid results in financial and
    physical calculations.
    Designing combined conditions using and, or and not allows building more
    realistic rules, such as loan eligibility or discount policies, in a
    compact and readable way.
    These patterns appear repeatedly in payroll systems, discount engines,
    loan screening processes and medical calculations like BMI, showing how
    fundamental numeric types and booleans are in programming.
"""

"""
References:
    1) Python documentation - Built-in Types: Numeric Types — int, float, complex
    2) Python documentation - Built-in Types: Boolean Type — bool
    3) Python tutorial - 3.1.2. Numbers (docs.python.org)
    4) "Automate the Boring Stuff with Python" by Al Sweigart — chapters on numbers and flow control
    5) Real Python - "Python Numbers: Integers, Floats, and Complex Numbers"
"""