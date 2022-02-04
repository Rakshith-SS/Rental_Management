import sqlite3

# make a Connection
conn = sqlite3.connect('customer.db')

# create a cursor
cur = conn.cursor()
cur.execute("""
        CREATE TABLE "customer" (
        "customer_id"	INTEGER NOT NULL,
        "customer_name"	VARCHAR(100) NOT NULL,
        "customer_phone"	INTEGER NOT NULL,
        "customer_email"	VARCHAR(120) NOT NULL,
        "rental_date"	TIMESTAMP NOT NULL,
        "vehicle_type"	varchar(20) NOT NULL,
        "return_date"	TIMESTAMP DEFAULT NULL,
        PRIMARY KEY("customer_id" AUTOINCREMENT)
    )
""")

cur.execute("""
        CREATE TABLE "vehicle" (
        "vehicle_id"	INTEGER NOT NULL,
        "vehicle_type"	VARCHAR(20) NOT NULL UNIQUE,
        "inventory"	INTEGER NOT NULL,
        PRIMARY KEY("vehicle_id" AUTOINCREMENT)
        );
""")


vehicle_list = [
        ("bikes", 2),
        ("cycle", 3),
        ("car", 1),
        ("boat", 2),
    ]

cur.executemany(
        "INSERT INTO vehicle (vehicle_type, inventory) VALUES (?, ?)",
        vehicle_list
        )

conn.commit()
# cur.execute("delete from vehicle where vehicle_type is 'cycle'")
#cur.execute("select * from vehicle")
# print(cur.fetchall())

conn.close()
