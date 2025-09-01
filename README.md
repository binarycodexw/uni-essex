# Income & Expense Tracker Assignment

---

## Python Code

```python
# Income and Expense Tracker

# List to store all our transactions
transactions = []

# Function to show the menu
def show_menu():
    print("\n--- Money Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show All Transactions")
    print("4. Filter by Category")
    print("5. Delete Transaction")
    print("6. Show Summary")
    print("7. Exit")

# Function to add income
def add_income():
    print("\nAdding Income...")
    
    # Ask for category
    print("1. Salary")
    print("2. Other")
    
    while True:
        category_choice = input("Choose 1 or 2: ")
        
        if category_choice == "1":
            category = "Salary"
            break
        elif category_choice == "2":
            category = "Other"
            break
        else:
            print("Please choose 1 or 2")
    
    # Ask for amount
    amount = float(input("How much money? "))
    
    # Ask for date
    date = input("Date (or press Enter): ")
    if date == "":
        date = "Today"
    
    # Make a transaction
    new_transaction = {}
    new_transaction["type"] = "income"
    new_transaction["category"] = category
    new_transaction["amount"] = amount
    new_transaction["date"] = date
    
    # Add to list
    transactions.append(new_transaction)
    print("Income added!")

# Function to add expense
def add_expense():
    print("\nAdding Expense...")
    
    # Ask for category
    print("1. Rent")
    print("2. Food")
    print("3. Other")
    
    while True:
        category_choice = input("Choose 1, 2, or 3: ")
        
        if category_choice == "1":
            category = "Rent"
            break
        elif category_choice == "2":
            category = "Food"
            break
        elif category_choice == "3":
            category = "Other"
            break
        else:
            print("Please choose 1, 2, or 3")
    
    # Ask for amount
    amount = float(input("How much did you spend? "))
    
    # Ask for date
    date = input("Date (or press Enter): ")
    if date == "":
        date = "Today"
    
    # Make a transaction
    new_transaction = {}
    new_transaction["type"] = "expense"
    new_transaction["category"] = category
    new_transaction["amount"] = amount
    new_transaction["date"] = date
    
    # Add to list
    transactions.append(new_transaction)
    print("Expense added!")

# Function to show all transactions
def show_all():
    print("\n--- All Transactions ---")
    
    if len(transactions) == 0:
        print("No transactions yet!")
        return
    
    for i in range(len(transactions)):
        t = transactions[i]
        print(str(i+1) + ". " + t['type'] + " - " + t['category'] + " - £" + str(t['amount']) + " - " + t['date'])

# Function to calculate totals
def calculate_totals():
    total_income = 0
    total_expenses = 0
    
    # Look at each transaction
    for transaction in transactions:
        if transaction["type"] == "income":
            total_income = total_income + transaction["amount"]
        else:
            total_expenses = total_expenses + transaction["amount"]
    
    return total_income, total_expenses

# Function to find highest and lowest expense categories
def find_high_low_expenses():
    # Count expenses by category
    rent_total = 0
    food_total = 0
    other_total = 0
    
    for transaction in transactions:
        if transaction["type"] == "expense":
            if transaction["category"] == "Rent":
                rent_total = rent_total + transaction["amount"]
            elif transaction["category"] == "Food":
                food_total = food_total + transaction["amount"]
            else:
                other_total = other_total + transaction["amount"]
    
    # Find highest
    highest_amount = 0
    highest_category = ""
    
    if rent_total > highest_amount:
        highest_amount = rent_total
        highest_category = "Rent"
    
    if food_total > highest_amount:
        highest_amount = food_total
        highest_category = "Food"
    
    if other_total > highest_amount:
        highest_amount = other_total
        highest_category = "Other"
    
    # Find lowest (only if we have expenses)
    lowest_amount = 999999  # Big number
    lowest_category = ""
    
    if rent_total > 0 and rent_total < lowest_amount:
        lowest_amount = rent_total
        lowest_category = "Rent"
    
    if food_total > 0 and food_total < lowest_amount:
        lowest_amount = food_total
        lowest_category = "Food"
    
    if other_total > 0 and other_total < lowest_amount:
        lowest_amount = other_total
        lowest_category = "Other"
    
    return highest_category, highest_amount, lowest_category, lowest_amount

# Function to filter by category
def filter_by_category():
    print("\n--- Filter by Category ---")
    
    if len(transactions) == 0:
        print("No transactions yet!")
        return
    
    # First ask if they want income or expense categories
    print("What type?")
    print("1. Income categories")
    print("2. Expense categories")
    
    type_choice = input("Choose 1 or 2: ")
    
    if type_choice == "1":
        print("\nIncome Categories:")
        print("1. Salary")
        print("2. Other")
        
        category_choice = input("Choose 1 or 2: ")
        
        if category_choice == "1":
            chosen_category = "Salary"
        else:
            chosen_category = "Other"
            
    else:
        print("\nExpense Categories:")
        print("1. Rent")
        print("2. Food")
        print("3. Other")
        
        category_choice = input("Choose 1, 2, or 3: ")
        
        if category_choice == "1":
            chosen_category = "Rent"
        elif category_choice == "2":
            chosen_category = "Food"
        else:
            chosen_category = "Other"
    
    print("\n--- Transactions for " + chosen_category + " ---")
    
    found = False
    for i in range(len(transactions)):
        t = transactions[i]
        if t["category"] == chosen_category:
            print(str(i+1) + ". " + t['type'] + " - £" + str(t['amount']) + " - " + t['date'])
            found = True
    
    if not found:
        print("No transactions found for " + chosen_category + "!")

# Function to delete a transaction
def delete_transaction():
    print("\n--- Delete Transaction ---")
    
    if len(transactions) == 0:
        print("No transactions to delete!")
        return
    
    # Show all transactions first
    print("Current transactions:")
    for i in range(len(transactions)):
        t = transactions[i]
        print(str(i+1) + ". " + t['type'] + " - " + t['category'] + " - £" + str(t['amount']) + " - " + t['date'])
    
    # Ask which one to delete
    while True:
        try:
            choice = int(input("Which transaction to delete (1 to " + str(len(transactions)) + ")? "))
            
            if choice >= 1 and choice <= len(transactions):
                # Delete the transaction
                deleted = transactions.pop(choice - 1)  # Remove from list
                print("Deleted: " + deleted['type'] + " - " + deleted['category'] + " - £" + str(deleted['amount']))
                break
            else:
                print("Please choose a number between 1 and " + str(len(transactions)))
        except:
            print("Please enter a valid number")

# Function to show summary
def show_summary():
    print("\n--- Summary ---")
    
    if len(transactions) == 0:
        print("No transactions to show!")
        return
    
    # Get totals
    total_income, total_expenses = calculate_totals()
    balance = total_income - total_expenses
    
    # Show results
    print("Total Income: £" + str(total_income))
    print("Total Expenses: £" + str(total_expenses))
    print("Balance: £" + str(balance))
    
    if balance > 0:
        print("Good! You have money left.")
    elif balance == 0:
        print("You spent exactly what you earned.")
    else:
        print("Warning! You spent more than you earned.")
    
    # Show highest and lowest expense categories
    highest_cat, highest_amt, lowest_cat, lowest_amt = find_high_low_expenses()
    
    if highest_cat != "":
        print("You spent most on: " + highest_cat + " (£" + str(highest_amt) + ")")
    
    if lowest_cat != "":
        print("You spent least on: " + lowest_cat + " (£" + str(lowest_amt) + ")")

# Main program
print("Welcome to Money Tracker!")

while True:
    show_menu()
    choice = input("What do you want to do? ")
    
    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        show_all()
    elif choice == "4":
        filter_by_category()
    elif choice == "5":
        delete_transaction()
    elif choice == "6":
        show_summary()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, 4, 5, 6, or 7")
    
    input("Press Enter to continue...")
```

---

### Approach to Modeling Transactions and Handling Calculations

For this assignment, I chose a simple and straightforward approach using basic Python concepts. The main data structure is a **global list called `transactions`** that stores dictionaries, where each dictionary represents one financial transaction with four key pieces of information: type (income or expense), category, amount, and date.

This approach was selected because it's easy to understand and manipulate - when users enter new transactions, I simply create a new dictionary and append it to the list using `transactions.append()`. 

For **calculations**, I implemented dedicated functions that iterate through the transaction list using basic `for` loops. The `calculate_totals()` function separates income from expenses using simple `if-else` statements, while `find_high_low_expenses()` uses manual category counting with separate variables for each category (rent_total, food_total, other_total).

**Input validation** is handled with `while` loops and `try-except` blocks to ensure users enter valid data. The program uses string concatenation with `str()` function for output formatting.

---

## Sample Program Output

### Example 1: Adding Income
```
--- Money Tracker ---
1. Add Income
2. Add Expense
3. Show All Transactions
4. Filter by Category
5. Delete Transaction
6. Show Summary
7. Exit

What do you want to do? 1

Adding Income...
1. Salary
2. Other
Choose 1 or 2: 1
How much money? 2000
Date (or press Enter): 01/03/2024
Income added!
```

### Example 2: Financial Summary
```
--- Summary ---
Total Income: £2500.0
Total Expenses: £1800.0
Balance: £700.0
Good! You have money left.
You spent most on: Rent (£800.0)
You spent least on: Food (£300.0)
```
