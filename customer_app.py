import sqlite3
import re
import phonenumbers
from datetime import datetime

conn = sqlite3.connect('customer.db')
cur = conn.cursor()

for row in cur.execute("select * from vehicle"):
    for item in row:
        print(item, end="\t")
    print(end="\n")


class Customer:
    """
    Add customer manage rentals
    and get details of a customer as well
    """
    def __init__(self, name, email, phone_number, vehicle_type):
        """TODO: to be defined. """
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.vehicle_type = vehicle_type

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
            print("Invalid email")
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
                print("Invalid phone number")
                return False

    def make_commit(self):
        if self.check_email():
            pass
        else:
            print("Enter a valid email")
        if self.check_phone_number():
            pass
        else:
            print("Enter a valid phone number")

        # DECREMENT VEHICLE count and check if it is less than 0
        cur.execute(
                    "SELECT inventory from vehicle where vehicle_type=?;",
                    (self.vehicle_type, )
                    )
        inventory = cur.fetchone()[0]
        if inventory > 0:
            if (self.check_email() and self.check_phone_number()):
                cur.execute(
                        """ INSERT INTO customer(
                                                customer_name,
                                                customer_phone,
                                                customer_email,
                                                rental_date,
                                                vehicle_type,
                                                return_date
                                                ) VALUES
                                                (?, ?, ?, ?, ?, ?);
                        """,
                        (
                                self.name,
                                self.phone_number,
                                self.email,
                                datetime.now(),
                                self.vehicle_type,
                                "NULL"
                            )
                        )
                inventory -= 1
                cur.execute(
                        "UPDATE vehicle SET inventory=? where vehicle_type=?;",
                        (inventory, self.vehicle_type)
                        )
                conn.commit()
                print("Commited to database successfully")
        else:
            print(f"{self.vehicle_type} cannot be rented as it already booked")

    def __str__(self):
        return f'Customer Name - {self.name}'


"""
The following customer details must me asked
customer name, email, phonenumber
"""

# name = input("Customer name: ")
# email = input("Customer email: ")
# phone_number = input("Customer phone number: ")
# vehicle_type = input("Vehicle Type: ")

# customer = Customer(name, email, phone_number, vehicle_type)
customer = Customer("Rakshith", "ssrakshith@protonmail.ch", "7259012437", "boat")
customer.make_commit()
