from PyInquirer import prompt
import csv


def load_users():
    users = []
    with open('users.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row['Name'])
    return users


users = load_users()
choices_involved_users = [
    {'name': user, 'value': user, 'checked': True} for user in users]

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "list",
        "name": "spender",
        "message": "New Expense - Spender: ",
        "choices": users,
    },
    {
        "type": "checkbox",
        "name": "involved_users",
        "message": "New Expense - Involved Users: ",
        "choices": choices_involved_users
    },
]


def new_expense(*args):
    infos = prompt(expense_questions)

    with open('expenses.csv', 'a', newline='') as csvfile:
        fields = ['Amount', 'Label', 'Spender', 'Payback']

        writer = csv.DictWriter(csvfile, fieldnames=fields)

        if csvfile.tell() == 0:
            writer.writeheader()

        payback = ', '.join(infos['involved_users'])

        writer.writerow(
            {'Amount': infos['amount'], 'Label': infos['label'], 'Spender': infos['spender'], 'Payback': payback})

    print("Expense Added !")
    return True
