import sqlite3
import re
import phonenumbers

conn = sqlite3.connect('customer.db')
cur = conn.cursor()


class Customer:
    """
    Add customer manage rentals
    and get details of a customer as well
    """
    def __init__(self, name, email, phone_number):
        """TODO: to be defined. """
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def check_name(self, name):
        # write this later
        pass

    def check_email(self):
        # regular expression for email
        email_pattern = r"\w+[@][a-z]+(\.[a-z]+)?\.[a-z]{2,5}"
        email_check = re.compile(email_pattern)
        if email_check.match(self.email):
            return True
        else:
            return False

    def check_phone_number(self):
        # regular expression for an Indian Phone Number
        number_pattern = r"^(\+91|0|)[0-9]{10}$"
        phone = re.compile(number_pattern)
        if phone.match(self.phone_number):
            mobile = phonenumbers.parse(self.phone_number, "IN")
            check_number = phonenumbers.is_valid_number(mobile)
            if check_number:
                return True
            else:
                return False

    def __str__(self):
        return f'Customer Name - {self.name}'


"""
The following customer details must me asked
customer name, email, phonenumber
"""

name = input("Customer name: ")
email = input("Customer email: ")
phone_number = input("Customer phone number: ")

customer = Customer(name, email, phone_number)

valid_number = customer.check_phone_number()
print(customer.check_email())

if valid_number:
    print("Correct Phone Number")
else:
    print("Invalid Phone Number")

conn.close()
