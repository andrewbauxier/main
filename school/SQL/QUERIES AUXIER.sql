-- 1) Retrieve all of your customers' names, account numbers, and addresses
-- (street and zip code only), sorted by account number.
-- 2) Retrieve all of the videos rented in the last 30 days and sort in chronological
-- rental date order.
-- 3) Produce a list of your distributors and all their information sorted in order by
-- company name.
-- 4) Update a customer name to change their maiden name to a married name.
-- You can choose which row to update. Make sure that you use the primary
-- key column in your WHERE clause to affect only a specific row. You may want
-- to include a ROLLBACK statement to undo your data update.
-- 5) Delete a customer from the database. You can choose which row to delete.
-- Make sure that you use the primary key column in your WHERE clause to
-- affect only a specific row. You may want to include a ROLLBACK statement to
-- undo your data deletion.

--1
SELECT FirstName, LastName, CustomerID, StreetAddress, ZipCode
FROM CUSTOMER
ORDER BY CustomerID;

--2
SELECT * FROM rental 
WHERE DateOut >= SYSDATE - INTERVAL '30' DAY 
ORDER BY DateOut ASC;

--3
SELECT * FROM DISTRIBUTOR
ORDER BY DistributorName ASC;

--4
UPDATE CUSTOMER
SET LastName = 'FISH'
WHERE CustomerID = 1001;
--ROLLBACK;

DELETE FROM CUSTOMER
WHERE CustomerID = 1005;
--ROLLBACK;
