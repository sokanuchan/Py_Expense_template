from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    }
]



def new_expense(*args):
    if (len(args) == 3):
        amount, label, spender = args
    else:
        amount, label, spender = prompt(expense_questions)
    with open('expense_report.csv', 'a') as csvfile_append:
        with open('expense_report.csv', 'r') as csvfile_read:
            spamreader = csv.reader(csvfile_read, delimiter=',')
            if len(list(spamreader)) == 0:
                # file is empty, we must fill the header
                csv.writer(csvfile_append).writerow(["amount", "label", "spender"])
        csv.writer(csvfile_append).writerow([amount, label, spender])
    print("Expense Added !")
    return True