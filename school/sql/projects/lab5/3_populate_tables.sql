-- Populate Sales2019 table
INSERT INTO Sales2019 (CustomerID, TransactionDate, SalesAmount, ProfitAmount)
VALUES
  (1, TO_DATE('2019-01-01', 'YYYY-MM-DD'), 1000, 200),
  (2, TO_DATE('2019-01-02', 'YYYY-MM-DD'), 1500, 300),
  (3, TO_DATE('2019-01-03', 'YYYY-MM-DD'), 800, 150);

-- Populate Projections2020 table
INSERT INTO Projections2020 (CustomerID, QuarterlyPurchaseAmount, QuarterlyProfitAmount, Confidence)
VALUES
  (1, 2500, 500, 0.8),
  (2, 1800, 350, 0.9),
  (3, 1200, 200, 0.7);

-- Populate Customers table
INSERT INTO Customers (CustomerID, CustomerLastName, CustomerFirstName, CustomerEmail, CustomerPhone, CustomerCellPhone)
VALUES
  (1, 'Doe', 'John', 'john.doe@example.com', '1234567890', '0987654321'),
  (2, 'Smith', 'Jane', 'jane.smith@example.com', '9876543210', '0123456789'),
  (3, 'Johnson', 'Robert', 'robert.johnson@example.com', '5555555555', NULL);
