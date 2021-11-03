import unittest
from expense import new_expense
from user import add_user
import csv

class TestExpense(unittest.TestCase):

    def test_add_expense(self):
        # adds a simple row and tests if the last line of csv is equal to what was added
        new_expense(2, 'a', 'a')
        with open('expense_report.csv', 'r') as csvfile_read:
            spamreader = list(csv.reader(csvfile_read, delimiter=','))
            last_row = spamreader[-1]
        self.assertEqual(last_row, ['2', 'a', 'a'])

    def test_add_expense_header(self):
        # adds a simple row and tests if the last line of csv is equal to what was added
        new_expense(2, 'a', 'a')
        with open('expense_report.csv', 'r') as csvfile_read:
            spamreader = list(csv.reader(csvfile_read, delimiter=','))
            header = spamreader[0]
        self.assertEqual(header, ["amount", "label", "spender"])

    def test_add_user(self):
        # adds a simple user and tests if the last line of csv is equal to what was added
        add_user("user_test")
        with open('users.csv', 'r') as csvfile_read:
            spamreader = list(csv.reader(csvfile_read, delimiter=','))
            last_row = spamreader[-1]
        self.assertEqual(last_row, ["user_test"])

    def test_add_user_header(self):
        # adds a simple row and tests if the last line of csv is equal to what was added
        new_expense(2, 'a', 'a')
        with open('users.csv', 'r') as csvfile_read:
            spamreader = list(csv.reader(csvfile_read, delimiter=','))
            header = spamreader[0]
        self.assertEqual(header, ["user_name"])


if __name__ == '__main__':
    unittest.main()