--FILE NAME:    INSERT DATA
--AUTHOR NAME:  ANDREW AUXIER
--CLASS:        CMIS302 
--DATE:         20230422

--MAIN TABLES
--ACTOR
INSERT INTO ACTOR (ActorID, FirstName, LastName) VALUES (1001, 'ActorFirstName1', 'ActorLastName1');
INSERT INTO ACTOR (ActorID, FirstName, LastName) VALUES (1002, 'ActorFirstName2', 'ActorLastName2');
INSERT INTO ACTOR (ActorID, FirstName, LastName) VALUES (1003, 'ActorFirstName3', 'ActorLastName3');
INSERT INTO ACTOR (ActorID, FirstName, LastName) VALUES (1004, 'ActorFirstName4', 'ActorLastName4');
INSERT INTO ACTOR (ActorID, FirstName, LastName) VALUES (1005, 'ActorFirstName5', 'ActorLastName5');

--DIRECTOR
INSERT INTO DIRECTOR (DirectorID, FirstName, LastName) VALUES (1001, 'DirectorFirstName1', 'DirectorLastName1');
INSERT INTO DIRECTOR (DirectorID, FirstName, LastName) VALUES (1002, 'DirectorFirstName2', 'DirectorLastName2');
INSERT INTO DIRECTOR (DirectorID, FirstName, LastName) VALUES (1003, 'DirectorFirstName3', 'DirectorLastName3');
INSERT INTO DIRECTOR (DirectorID, FirstName, LastName) VALUES (1004, 'DirectorFirstName4', 'DirectorLastName4');
INSERT INTO DIRECTOR (DirectorID, FirstName, LastName) VALUES (1005, 'DirectorFirstName5', 'DirectorLastName5');

--AWARD
INSERT INTO AWARD (AwardID, AwardName, DateReceived, FirstName, LastName)
VALUES (1001, 'AwardName1', TO_DATE('2022-12-01', 'YYYY-MM-DD'), 'FirstName1', 'LastName1');

INSERT INTO AWARD (AwardID, AwardName, DateReceived, FirstName, LastName)
VALUES (1002, 'AwardName2', TO_DATE('2023-05-15', 'YYYY-MM-DD'), 'FirstName2', 'LastName2');

INSERT INTO AWARD (AwardID, AwardName, DateReceived, FirstName, LastName)
VALUES (1003, 'AwardName3', TO_DATE('2024-01-22', 'YYYY-MM-DD'), 'FirstName3', 'LastName3');

INSERT INTO AWARD (AwardID, AwardName, DateReceived, FirstName, LastName)
VALUES (1004, 'AwardName4', TO_DATE('2025-07-10', 'YYYY-MM-DD'), 'FirstName4', 'LastName4');

INSERT INTO AWARD (AwardID, AwardName, DateReceived, FirstName, LastName)
VALUES (1005, 'AwardName5', TO_DATE('2026-11-18', 'YYYY-MM-DD'), 'FirstName5', 'LastName5');


--MOVIE
INSERT INTO MOVIE (MovieID, DistributorID, MovieName, DistributorName)
VALUES (1001, 1001, 'MovieName1', 'DistributorName1');

INSERT INTO MOVIE (MovieID, DistributorID, MovieName, DistributorName)
VALUES (1002, 1002, 'MovieName2', 'DistributorName2');

INSERT INTO MOVIE (MovieID, DistributorID, MovieName, DistributorName)
VALUES (1003, 1003, 'MovieName3', 'DistributorName3');

INSERT INTO MOVIE (MovieID, DistributorID, MovieName, DistributorName)
VALUES (1004, 1004, 'MovieName4', 'DistributorName4');

INSERT INTO MOVIE (MovieID, DistributorID, MovieName, DistributorName)
VALUES (1005, 1005, 'MovieName5', 'DistributorName5');


--CUSTOMER
INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, StreetAddress, ZipCode)
VALUES (1001, 'CustomerFirstName1', 'CustomerLastName1', '101 ExampleStreet', 10001);

INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, StreetAddress, ZipCode)
VALUES (1002, 'CustomerFirstName2', 'CustomerLastName2', '102 ExampleStreet', 10002);

INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, StreetAddress, ZipCode)
VALUES (1003, 'CustomerFirstName3', 'CustomerLastName3', '103 ExampleStreet', 10003);

INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, StreetAddress, ZipCode)
VALUES (1004, 'CustomerFirstName4', 'CustomerLastName4', '104 ExampleStreet', 10004);

INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, StreetAddress, ZipCode)
VALUES (1005, 'CustomerFirstName5', 'CustomerLastName5', '105 ExampleStreet', 10005);

--DVD
INSERT INTO DVD (DVDID, Title)
VALUES (1001, 'ExampleMovie1');

INSERT INTO DVD (DVDID, Title)
VALUES (1002, 'ExampleMovie2');

INSERT INTO DVD (DVDID, Title)
VALUES (1003, 'ExampleMovie3');

INSERT INTO DVD (DVDID, Title)
VALUES (1004, 'ExampleMovie4');

INSERT INTO DVD (DVDID, Title)
VALUES (1005, 'ExampleMovie5');


--VHS
-- Example 1
INSERT INTO VHS (VHSID, Title)
VALUES (1001, 'ExampleMovie1');

INSERT INTO VHS (VHSID, Title)
VALUES (1002, 'ExampleMovie2');

INSERT INTO VHS (VHSID, Title)
VALUES (1003, 'ExampleMovie3');

INSERT INTO VHS (VHSID, Title)
VALUES (1004, 'ExampleMovie4');

INSERT INTO VHS (VHSID, Title)
VALUES (1005, 'ExampleMovie5');

--DISTRIBUTOR
INSERT INTO DISTRIBUTOR (DistributorID, DistributorName)
VALUES (1001, 'DistributorName1');

INSERT INTO DISTRIBUTOR (DistributorID, DistributorName)
VALUES (1002, 'DistributorName2');

INSERT INTO DISTRIBUTOR (DistributorID, DistributorName)
VALUES (1003, 'DistributorName3');

INSERT INTO DISTRIBUTOR (DistributorID, DistributorName)
VALUES (1004, 'DistributorName4');

INSERT INTO DISTRIBUTOR (DistributorID, DistributorName)
VALUES (1005, 'DistributorName5');


--RENTAL
INSERT INTO RENTAL (RentalID, MovieID, DistributorID, CustomerID, DateOut, DateDue)
VALUES (1001, 1001, 1001, 1001, TO_DATE('2022-02-01', 'YYYY-MM-DD'), TO_DATE('2022-03-01', 'YYYY-MM-DD'));

INSERT INTO RENTAL (RentalID, MovieID, DistributorID, CustomerID, DateOut, DateDue)
VALUES (1002, 1002, 1002, 1002, TO_DATE('2022-02-02', 'YYYY-MM-DD'), TO_DATE('2022-03-02', 'YYYY-MM-DD'));

INSERT INTO RENTAL (RentalID, MovieID, DistributorID, CustomerID, DateOut, DateDue)
VALUES (1003, 1003, 1003, 1003, TO_DATE('2022-02-03', 'YYYY-MM-DD'), TO_DATE('2022-03-03', 'YYYY-MM-DD'));

INSERT INTO RENTAL (RentalID, MovieID, DistributorID, CustomerID, DateOut, DateDue)
VALUES (1004, 1004, 1004, 1004, TO_DATE('2022-03-04', 'YYYY-MM-DD'), TO_DATE('2022-04-04', 'YYYY-MM-DD'));

INSERT INTO RENTAL (RentalID, MovieID, DistributorID, CustomerID, DateOut, DateDue)
VALUES (1005, 1005, 1005, 1005, TO_DATE('2023-04-05', 'YYYY-MM-DD'), TO_DATE('2023-04-05', 'YYYY-MM-DD'));

--RELATIONAL TABLES

--ACTOR_MOVIE


--DIRECTOR_MOVIE


--AWARD_MOVIE


--DVD_MOVIE


--VHS_MOVIE


--VHS_RENTAL


--DVD_RENTAL


--CUSTOMER_RENTAL