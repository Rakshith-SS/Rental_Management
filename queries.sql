CREATE TABLE "customer" (
	"customer_id"	INTEGER NOT NULL,
	"customer_name"	VARCHAR(100) NOT NULL,
	"customer_phone"	INTEGER NOT NULL UNIQUE,
	"customer_email"	VARCHAR(120) NOT NULL UNIQUE,
	"rental_date"	DATETIME NOT NULL,
	"vehicle_type"	varchar(20) NOT NULL,
	"return_date"	DATETIME DEFAULT NULL,
	PRIMARY KEY("customer_id" AUTOINCREMENT)
);


CREATE TABLE "vehicle" (
	"vehicle_id"	INTEGER NOT NULL,
	"vehicle_type"	VARCHAR(20) NOT NULL UNIQUE,
	"inventory"	INTEGER NOT NULL,
	PRIMARY KEY("vehicle_id" AUTOINCREMENT)
);


