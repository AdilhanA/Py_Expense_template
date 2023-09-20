import csv

def load_expenses():
    expenses = []
    with open('expenses.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            expenses.append({
                'Amount': row['Amount'],
                'Label': row['Label'],
                'Spender': row['Spender'],
                'Payback': row['Payback'],
            })
    return expenses

def load_users():
    users = []
    with open('users.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row['Name'])
    return users

def print_status_report():
    expenses = load_expenses()
    users_owes = []

    for expense in expenses:
        spender = expense["Spender"]
        payback = expense["Payback"]
        amount = int(expense["Amount"]) / len(payback)

        for user in payback:
            users_owes.append({"Spender": spender, "Amount": amount, "Payback_User": user})
    
    users = load_users()

    for user in users:
        total = 0
        to = ""
        for owes in users_owes:
            if owes["Payback_User"] == user:
                total += int(owes["Amount"])
                to = owes["Spender"]
        print(user + " owes " + str(total) + " to " + to)

    
    #print(users_owes)

print_status_report()