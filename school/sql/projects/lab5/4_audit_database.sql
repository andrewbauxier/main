-- Enable auditing for Sales2019 table
AUDIT SELECT, INSERT, UPDATE, DELETE ON Sales2019 BY ACCESS;

-- Enable auditing for Projections2020 table
AUDIT SELECT, INSERT, UPDATE, DELETE ON Projections2020 BY ACCESS;

-- Enable auditing for Customers table
AUDIT SELECT, INSERT, UPDATE, DELETE ON Customers BY ACCESS;

-- User: Lab5_1AndrewAuxier
-- Table: Sales2019
SELECT * FROM Sales2019 WHERE CustomerID = 1;
INSERT INTO Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount)
VALUES (1, TO_DATE('2023-07-12', 'YYYY-MM-DD'), 2000, 400);
UPDATE Sales2019 SET SalesAmount = 1500 WHERE CustomerID = 1;
DELETE FROM Sales2019 WHERE CustomerID = 1;

-- Table: Projections2020
SELECT * FROM Projections2020 WHERE CustomerID = 1;
INSERT INTO Projections2020 (CustomerID, QuarterlyPurchaseAmount, QuarterlyProfitAmount, Confidence)
VALUES (1, 3000, 600, 0.7);
UPDATE Projections2020 SET QuarterlyPurchaseAmount = 2500 WHERE CustomerID = 1;
DELETE FROM Projections2020 WHERE CustomerID = 1;

-- Table: Customers
SELECT * FROM Customers WHERE CustomerID = 1;
INSERT INTO Customers (CustomerID, CustomerLastName, CustomerFirstName, CustomerEmail, CustomerPhone, CustomerCellPhone)
VALUES (4, 'Johnson', 'Amy', 'amy.johnson@example.com', '5551112222', NULL);
UPDATE Customers SET CustomerLastName = 'Smith' WHERE CustomerID = 1;
DELETE FROM Customers WHERE CustomerID = 1;

-- User: Lab5_2AndrewAuxier
-- Table: Sales2019
SELECT * FROM Sales2019 WHERE CustomerID = 2;
INSERT INTO Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount)
VALUES (2, TO_DATE('2023-07-12', 'YYYY-MM-DD'), 3000, 600);
UPDATE Sales2019 SET SalesAmount = 2500 WHERE CustomerID = 2;
DELETE FROM Sales2019 WHERE CustomerID = 2;

-- Table: Projections2020
SELECT * FROM Projections2020 WHERE CustomerID = 2;
INSERT INTO Projections2020 (CustomerID, QuarterlyPurchaseAmount, QuarterlyProfitAmount, Confidence)
VALUES (2, 4000, 800, 0.9);
UPDATE Projections2020 SET QuarterlyPurchaseAmount = 3500 WHERE CustomerID = 2;
DELETE FROM Projections2020 WHERE CustomerID = 2;

-- Table: Customers
SELECT * FROM Customers WHERE CustomerID = 2;
INSERT INTO Customers (CustomerID, CustomerLastName, CustomerFirstName, CustomerEmail, CustomerPhone, CustomerCellPhone)
VALUES (5, 'Smith', 'Robert', 'robert.smith@example.com', '1112223333', NULL);
UPDATE Customers SET CustomerLastName = 'Doe' WHERE CustomerID = 2;
DELETE FROM Customers WHERE CustomerID = 2;

-- User: Lab5_3AndrewAuxier
-- Table: Sales2019
SELECT * FROM Sales2019 WHERE CustomerID = 3;
INSERT INTO Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount)
VALUES (3, TO_DATE('2023-07-12', 'YYYY-MM-DD'), 4000, 800);
UPDATE Sales2019 SET SalesAmount = 3500 WHERE CustomerID = 3;
DELETE FROM Sales2019 WHERE CustomerID = 3;

-- Table: Projections2020
SELECT * FROM Projections2020 WHERE CustomerID = 3;
INSERT INTO Projections2020 (CustomerID, QuarterlyPurchaseAmount, QuarterlyProfitAmount, Confidence)
VALUES (3, 5000, 1000, 0.8);
UPDATE Projections2020 SET QuarterlyPurchaseAmount = 4500 WHERE CustomerID = 3;
DELETE FROM Projections2020 WHERE CustomerID = 3;

-- Table: Customers
SELECT * FROM Customers WHERE CustomerID = 3;
INSERT INTO Customers (CustomerID, CustomerLastName, CustomerFirstName, CustomerEmail, CustomerPhone, CustomerCellPhone)
VALUES (6, 'Brown', 'Sarah', 'sarah.brown@example.com', '9998887777', NULL);
UPDATE Customers SET CustomerLastName = 'Johnson' WHERE CustomerID = 3;
DELETE FROM Customers WHERE CustomerID = 3;

SELECT * FROM DBA_AUDIT_TRAIL;