-- Create Customers table
CREATE TABLE Customers (
  CustomerID INTEGER NOT NULL PRIMARY KEY,
  CustomerLastName VARCHAR2(40) NOT NULL,
  CustomerFirstName VARCHAR2(40) NOT NULL,
  CustomerEmail VARCHAR2(80) NOT NULL,
  CustomerPhone VARCHAR2(12),
  CustomerCellPhone VARCHAR2(12)
);


-- Create Sales2019 table
CREATE TABLE Sales2019 (
  CustomerID INTEGER NOT NULL REFERENCES Customers(CustomerID),
  TransactionDate DATE NOT NULL,
  SalesAmount NUMBER(10, 2) NOT NULL,
  ProfitAmount NUMBER(10, 2) NOT NULL,
  PRIMARY KEY (CustomerID, TransactionDate)
);

-- Create Projections2020 table
CREATE TABLE Projections2020 (
  CustomerID INTEGER NOT NULL REFERENCES Customers(CustomerID),
  QuarterlyPurchaseAmount NUMBER(10, 2) NOT NULL,
  QuarterlyProfitAmount NUMBER(10, 2) NOT NULL,
  Confidence NUMBER(4, 2) NOT NULL,
  PRIMARY KEY (CustomerID)
);



-- Create User 1
CREATE USER Lab5_1AndrewAuxier IDENTIFIED BY password;
GRANT CONNECT, RESOURCE, CREATE SESSION TO Lab5_1AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Sales2019 TO Lab5_1AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Projections2020 TO Lab5_1AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Customers TO Lab5_1AndrewAuxier;
GRANT R5AndrewAuxier TO Lab5_1AndrewAuxier;

-- Create User 2
CREATE USER Lab5_2AndrewAuxier IDENTIFIED BY password;
GRANT CONNECT, RESOURCE, CREATE SESSION TO Lab5_2AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Sales2019 TO Lab5_2AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Projections2020 TO Lab5_2AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Customers TO Lab5_2AndrewAuxier;
GRANT R5AndrewAuxier TO Lab5_2AndrewAuxier;

-- Create User 3
CREATE USER Lab5_3AndrewAuxier IDENTIFIED BY password;
GRANT CONNECT, RESOURCE, CREATE SESSION TO Lab5_3AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Sales2019 TO Lab5_3AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Projections2020 TO Lab5_3AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Customers TO Lab5_3AndrewAuxier;
GRANT R5AndrewAuxier TO Lab5_3AndrewAuxier;
