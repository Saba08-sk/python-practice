"""A tiny expense tracker demonstration (data stays in memory)."""

expenses = []

print("Simple Expense Tracker")
print("Type 'done' when you have finished adding expenses.\n")

while True:
    name = input("What did you spend money on? ").strip()

    if name.lower() == "done":
        break

    if not name:
        print("Please enter an item name.\n")
        continue

    try:
        amount = float(input("How much did it cost? "))
        if amount < 0:
            print("Please enter zero or a positive amount.\n")
            continue
    except ValueError:
        print("Please enter the amount as a number.\n")
        continue

    expenses.append((name, amount))
    print("Added!\n")

print("\nYour expenses:")
if not expenses:
    print("No expenses entered.")
else:
    for name, amount in expenses:
        print(f"- {name}: Rs.{amount:.2f}")

    total = sum(amount for _, amount in expenses)
    print(f"Total: Rs.{total:.2f}")
