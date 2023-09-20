from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "Add User - Name: ",
    },
]

def add_user(*args):
    infos = prompt(user_questions)

    with open('users.csv', 'a', newline='') as csvfile:

        fieldnames = ['Name']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'Name': infos['name']})

    print("User Added !")
    return True
