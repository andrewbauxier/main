-- Create Role R5AndrewAuxier
CREATE ROLE R5AndrewAuxier;

-- Create Users
CREATE USER Lab5_1AndrewAuxier IDENTIFIED BY password;
CREATE USER Lab5_2AndrewAuxier IDENTIFIED BY password;
CREATE USER Lab5_3AndrewAuxier IDENTIFIED BY password;

-- Grant privileges to Role R5AndrewAuxier
GRANT CONNECT, RESOURCE, CREATE SESSION TO R5AndrewAuxier;

-- Assign Role R5AndrewAuxier to Users
GRANT R5AndrewAuxier TO Lab5_1AndrewAuxier;
GRANT R5AndrewAuxier TO Lab5_2AndrewAuxier;
GRANT R5AndrewAuxier TO Lab5_3AndrewAuxier;

-- Grant table privileges through the role
GRANT SELECT, INSERT, UPDATE, DELETE ON Sales2019 TO R5AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Projections2020 TO R5AndrewAuxier;
GRANT SELECT, INSERT, UPDATE, DELETE ON Customers TO R5AndrewAuxier;

-- -- Revoke Role R5AndrewAuxier from Users
-- REVOKE R5AndrewAuxier FROM Lab5_1AndrewAuxier;
-- REVOKE R5AndrewAuxier FROM Lab5_2AndrewAuxier;
-- REVOKE R5AndrewAuxier FROM Lab5_3AndrewAuxier;

-- -- Drop Users
-- DROP USER Lab5_1AndrewAuxier CASCADE;
-- DROP USER Lab5_2AndrewAuxier CASCADE;
-- DROP USER Lab5_3AndrewAuxier CASCADE;

-- -- Drop Role R5AndrewAuxier
-- DROP ROLE R5AndrewAuxier;