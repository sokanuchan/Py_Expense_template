from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"user_name",
        "message":"New User - Name: ",
    },
]

def add_user(*args):
    # creates a new user, asking for its name
    if (len(args) == 1):
        user_name = args[0]
    else:
        user_name = prompt(user_questions)
    with open('users.csv', 'a') as csvfile_append:
        with open('users.csv', 'r') as csvfile_read:
            spamreader = csv.reader(csvfile_read, delimiter=',')
            if len(list(spamreader)) == 0:
                # file is empty, we must fill the header
                csv.writer(csvfile_append).writerow(["user_name"])
        csv.writer(csvfile_append).writerow([user_name])
    print("User Added !")
    return True