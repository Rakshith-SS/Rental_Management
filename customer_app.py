import sqlite3
import re
import phonenumbers
from datetime import datetime

conn = sqlite3.connect('customer.db')
cur = conn.cursor()


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
        if (self.check_email() and self.check_phone_number()):

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
        else:
            print("\nInvalid email or phone Number")
            print("Enter valid credentials")

    def __str__(self):
        return f'Customer Name - {self.name}'


def get_all():
    """
    Fetch all records from The
    customer table
    """
    print(129*"-")
    print("|ID\t|Name\t|\tMobile\t|\tEmail\t\t|\tRental Date\t\t|Vehicle Type\t|\tReturn Date\t|")
    print(129*"-")
    for row in cur.execute("select * from customer"):
        print(f"|{row[0]}", end="\t| ")
        print(row[1], end="\t| ")
        print(row[2], end="\t| ")
        print(row[3], end="\t| ")
        print(row[4], end="\t| ")
        print(row[5], end="\t\t| ")
        print(row[6], end="\t\t\t| ")
        print()
    print(129*"-")


print("1. Add a rental: ?")
print("2. See the customer table: ?")
print("3. Exit ")
choice = int(input("Your Option? [Enter a number(1-3)]: "))

match choice:
    case 1:
        print("Customer Details")
        name = input("Customer Name: ")
        phone = input("Phone Number: ")
        email = input("Email Id: ")
        vehicle = input("Vehicle [boat, cycle, car, bikes]: ")
        customer = Customer(name, email, phone, vehicle)
        customer.make_commit()
    case 2:
        get_all()
    case 3:
        print("Exited App successfully...")
