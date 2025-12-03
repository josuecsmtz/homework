"""
Cover:
    Name: Josue de Jesus Castro Martinez
    ID: 2530263
    Group: IM 1-1
"""

"""
Executive Summary:
    A CRUD (Create, Read, Update, Delete) system allows basic management of data:
    creating new records, reading existing ones, updating their fields, and
    deleting them. In this program, an in-memory inventory is implemented using
    a Python dictionary where each item is identified by a unique id and stores
    name, price and quantity. Each CRUD operation is implemented as a function,
    while a main loop provides a simple text menu to interact with the user.
    The program validates user inputs such as menu options, ids and numeric
    fields, and prints clear messages after each action to indicate the result.
"""

"""
Problem: In-memory CRUD manager with functions

Description:
    Program that implements a simple CRUD (Create, Read, Update, Delete) for
    items stored in memory. The chosen data structure is a dictionary (Option A),
    where:
        - key: item_id (string)
        - value: a dictionary with fields "NAME", "PRICE" and "QUANTITY".
    Each CRUD operation (create, read, update, delete, and list) is implemented
    as a separate function. A text-based menu in the main loop lets the user
    choose operations and enter the corresponding data.

Data structure choice:
    - Option A: dict[item_id] -> {"NAME": name, "PRICE": price, "QUANTITY": quantity}
    - This option is convenient for fast access by id and simple updates.

Inputs:
    - User menu options (string: "0".."5").
    - For CREATE:
        - item_id (string)
        - name (string)
        - price (int)
        - quantity (int)
    - For READ/UPDATE/DELETE:
        - item_id (string)

Outputs:
    - Messages indicating the result of each operation, for example:
        - "Item created"
        - "Item updated"
        - "Item deleted"
        - "Error: item not found"
        - "Error: invalid input"
        - Printed dictionary for "List all items".

Validations:
    - Menu option must be one of: "0", "1", "2", "3", "4", "5".
    - item_id must not be empty after strip().
    - price and quantity must be integers and greater than or equal to 0.
    - For CREATE:
        - If item_id is empty, show "Error: invalid input".
        - If price or quantity are invalid or negative, show "Error: invalid input".
        - If the id already exists, in this implementation the item is overwritten
          silently (allowed, and this decision is documented).
    - For READ/UPDATE/DELETE:
        - If item_id is empty, show "Error: invalid input".
        - If the id does not exist in the dictionary, show "Error: item not found"
          and do not perform the operation.
    - For LIST:
        - The whole data_structure dictionary is printed directly.

Test cases:
    1) Normal:
        - Steps:
            1) Create item with id="1", name="Apple", price=10, quantity=5.
            2) Read item id="1".
            3) Update item id="1" with new name="Green Apple", price=12, quantity=7.
            4) Delete item id="1".
        - Expected messages:
            - "Item created"
            - "Item found"
            - "Item updated"
            - "Item deleted"
        - Final state: item id="1" no longer exists in data_structure.

    2) Border:
        - Create item with id="X", name="ZeroStock", price=0, quantity=0.
        - List items.
        - Expected:
            - "Item created"
            - Printed dictionary including {"NAME": "ZeroStock", "PRICE": 0, "QUANTITY": 0}.

    3) Error:
        - Try to create item with empty id ("").
        - Try to create item with price = -5.
        - Try to read item with id that does not exist.
        - Expected messages:
            - "Error: invalid input"
            - "Error: invalid input"
            - "Error: item not found"
"""

# -----------------------------
# CRUD implementation (original code)
# -----------------------------

def create_item(data_structure, item_id, name, price, quantity):
    name = {
        "NAME" : name,
        "PRICE" : price,
        "QUANTITY" : quantity
    }
    data_structure[item_id] = name
    return data_structure

def read_item(data_structure, item_id):
    if item_id in data_structure:
        return "Item found"
    else:
        return "Item not found"
    
def update_item(data_structure, item_id, new_name, new_price, new_quantity):
    new_name = {
        "NAME" : new_name,
        "PRICE" : new_price,
        "QUANTITY" : new_quantity
    }
    data_structure[item_id] = new_name
    return data_structure

def delete_item(data_structure, item_id):
    data_structure.pop(item_id)
    return data_structure

def list_items(data_structure):
    print(data_structure)      

data_structure = {}
while True:
    print("""
    - 1) Create item
    - 2) Read item by id
    - 3) Update item by id
    - 4) Delete item by id
    - 5) List all items
    - 0) Exit
    """)
    option = input("Enter a option to do: ").strip()
    if option == "1":
        item_id = input("Enter the item id: ").strip()
        if item_id == "":
            print("Error: invalid input")
            continue
        name = (input("Enter the name of the item: "))
        try:
            price = int(input("Enter the price of the item: "))
            quantity = int(input("Enter the quantity of the item: "))
            if price < 0 or quantity < 0:
                raise ValueError
        except:
            print("Error: invalid input")
            continue
        create_item(data_structure, item_id, name, price, quantity)
        print("Item created")
    elif option == "2":
        item_id = input("Enter the id of the item to SEARCH: ")
        if item_id == "":
            print("Error: invalid input")
            continue
        if not item_id in data_structure:
            print("Error: item not found")
            continue
        print(read_item(data_structure, item_id))
    elif option == "3":
        item_id = input("Enter the id of the item to UPDATE: ")
        if item_id == "":
            print("Error: invalid input")
            continue
        if not item_id in data_structure:
            print("Error: item not found")
            continue
        new_name = input("Enter the new name of the item: ")
        try:
            new_price = int(input("Enter the price of the item: "))
            new_quantity = int(input("Enter the quantity of the item: "))
            if new_price < 0 or new_quantity < 0:
                raise ValueError
        except:
            print("Error: invalid input")
            continue
        update_item(data_structure, item_id, new_name, new_price, new_quantity)
        print("Item updated")
    elif option == "4":
        item_id = input("Enter the id of the item to DELETE: ").strip()
        if item_id == "":
            print("Error: invalid input")
            continue
        if not item_id in data_structure:
            print("Error: item not found")
            continue
        delete_item(data_structure, item_id)
        print("Item deleted")
    elif option == "5":
        list_items(data_structure)
    elif option == "0":
        print("Exiting...")
        break
    else:
        print("Error: invalid input")

"""
Conclusions:
    Using functions for each CRUD operation (create, read, update, delete and
    list) helped to keep the main menu loop simpler and easier to read. The
    dictionary structure allowed fast access to items by their id and made
    updates and deletions straightforward. Input validation was important to
    prevent invalid ids and negative numeric values from corrupting the data.
    This simple in-memory CRUD could be extended by adding persistence, such
    as saving the data_structure to a file or database, or by adding more
    fields and search features without changing the overall design pattern.
"""

"""
References:
    1) Python documentation - Data structures (lists and dictionaries), docs.python.org
    2) Python documentation - Defining functions and calling functions, docs.python.org
    3) Online tutorials and class notes about basic CRUD patterns in Python
"""