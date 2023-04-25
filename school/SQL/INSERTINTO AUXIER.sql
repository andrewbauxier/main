--FILE NAME: DROP TABLES
--AUTHOR NAME:ANDREW AUXIER
--CLASS:CMIS302 
--DATE: 20230422

--MAIN TABLES
--ACTOR
INSERT INTO ACTOR (ActorID, FirstName, LastName) VALUES (1001, 'Tom', 'Hanks');

INSERT INTO ACTOR (ActorID, FirstName, LastName) VALUES (1002, 'Meryl', 'Streep');

INSERT INTO ACTOR (ActorID, FirstName, LastName) VALUES (1003, 'Brad', 'Pitt');

INSERT INTO ACTOR (ActorID, FirstName, LastName) VALUES (1004, 'Emma', 'Stone');

INSERT INTO ACTOR (ActorID, FirstName, LastName) VALUES (1005, 'Denzel', 'Washington');

--DIRECTOR
INSERT INTO DIRECTOR (DirectorID, FirstName, LastName) VALUES (1001, 'Christopher', 'Nolan');

INSERT INTO DIRECTOR (DirectorID, FirstName, LastName) VALUES (1002, 'Steven', 'Spielberg');

INSERT INTO DIRECTOR (DirectorID, FirstName, LastName) VALUES (1003, 'Steven', 'Spielberg');

INSERT INTO DIRECTOR (DirectorID, FirstName, LastName) VALUES (1004, 'Ava', 'DuVernay');

INSERT INTO DIRECTOR (DirectorID, FirstName, LastName) VALUES (1005, 'Jordan', 'Peele');

--AWARD
INSERT INTO AWARD (AwardID, AwardName, DateReceived, ActorFirstName, ActorLastName)
VALUES (1001, 'Best Supporting Actor', TO_DATE('2022-03-15', 'YYYY-MM-DD'), 'Tom', 'Hanks');

INSERT INTO AWARD (AwardID, AwardName, DateReceived, ActorFirstName, ActorLastName)
VALUES (1002, 'Best Director', TO_DATE('2022-03-15', 'YYYY-MM-DD'), 'Chloe', 'Zhao');

INSERT INTO AWARD (AwardID, AwardName, DateReceived, ActorFirstName, ActorLastName)
VALUES (1003, 'Best Picture', TO_DATE('2022-03-15', 'YYYY-MM-DD'), 'Steven', 'Spielberg');

INSERT INTO AWARD (AwardID, AwardName, DateReceived, ActorFirstName, ActorLastName)
VALUES (1004, 'Best Original Screenplay', TO_DATE('2022-03-15', 'YYYY-MM-DD'), 'Aaron', 'Sorkin');

INSERT INTO AWARD (AwardID, AwardName, DateReceived, ActorFirstName, ActorLastName)
VALUES (1005, 'Best Cinematography', TO_DATE('2022-03-15', 'YYYY-MM-DD'), 'Roger', 'Deakins');


--MOVIE
INSERT INTO MOVIE (DistributorID, MovieName, RunningLength, Genre, Rating, ReleaseDate)
VALUES (1001, 'The Avengers', 120, 'Action', 'PG-13', TO_DATE('2022-05-15', 'YYYY-MM-DD'));

INSERT INTO MOVIE (DistributorID, MovieName, RunningLength, Genre, Rating, ReleaseDate)
VALUES (1002, 'The Dark Knight', 150, 'Drama', 'R', TO_DATE('2022-07-20', 'YYYY-MM-DD'));

INSERT INTO MOVIE (DistributorID, MovieName, RunningLength, Genre, Rating, ReleaseDate)
VALUES (1003, 'Bridesmaids', 90, 'Comedy', 'PG', TO_DATE('2022-06-01', 'YYYY-MM-DD'));

INSERT INTO MOVIE (DistributorID, MovieName, RunningLength, Genre, Rating, ReleaseDate)
VALUES (1004, 'Wonder Woman', 130, 'Action', 'PG-13', TO_DATE('2022-06-15', 'YYYY-MM-DD'));

INSERT INTO MOVIE (DistributorID, MovieName, RunningLength, Genre, Rating, ReleaseDate)
VALUES (1005, 'Get Out', 120, 'Horror', 'R', TO_DATE('2022-08-05', 'YYYY-MM-DD'));


--CUSTOMER
INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, DateOfBirth, StreetAddress, City, StateID, ZipCode, Telephone)
VALUES (1001, 'John', 'Doe', TO_DATE('1985-06-12', 'YYYY-MM-DD'), '123 Main St', 'Anytown', 'NY', 12345, 5551234567);

INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, DateOfBirth, StreetAddress, City, StateID, ZipCode, Telephone)
VALUES (1002, 'Jane', 'Smith', TO_DATE('1990-02-15', 'YYYY-MM-DD'), '456 Oak St', 'Otherville', 'CA', 98765, 5559876543);

INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, DateOfBirth, StreetAddress, City, StateID, ZipCode, Telephone)
VALUES (1003, 'Bob', 'Johnson', TO_DATE('1980-11-20', 'YYYY-MM-DD'), '789 Maple Ave', 'Maplewood', 'NJ', 07040, 5555551212);

INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, DateOfBirth, StreetAddress, City, StateID, ZipCode, Telephone)
VALUES (1004, 'Sara', 'Lee', TO_DATE('1995-07-04', 'YYYY-MM-DD'), '101 Cherry Ln', 'Cherryville', 'GA', 30303, 5557778888);

INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, DateOfBirth, StreetAddress, City, StateID, ZipCode, Telephone)
VALUES (1005, 'Mike', 'Johnson', TO_DATE('1988-09-05', 'YYYY-MM-DD'), '246 Elm St', 'Elmtown', 'IL', 60601, 5559998888);


--DVD
-- Example 1
INSERT INTO DVD (DVDID, Title, RunningLength, Genre, RentalFee, Discount)
VALUES (1001, 'The Shawshank Redemption', 142, 'Drama', 3.99, 10);

-- Example 2
INSERT INTO DVD (DVDID, Title, RunningLength, Genre, RentalFee, Discount)
VALUES (1002, 'The Dark Knight', 152, 'Action', 4.99, 5);

-- Example 3
INSERT INTO DVD (DVDID, Title, RunningLength, Genre, RentalFee, Discount)
VALUES (1003, 'Forrest Gump', 142, 'Drama', 3.99, 15);

-- Example 4
INSERT INTO DVD (DVDID, Title, RunningLength, Genre, RentalFee, Discount)
VALUES (1004, 'The Godfather', 175, 'Drama', 3.99, 10);

-- Example 5
INSERT INTO DVD (DVDID, Title, RunningLength, Genre, RentalFee, Discount)
VALUES (1005, 'The Lord of the Rings: The Fellowship of the Ring', 178, 'Fantasy', 4.99, 5);


--VHS
-- Example 1
INSERT INTO VHS (VHSID, Title, RunningLength, Genre, RentalFee, Discount)
VALUES (1001, 'The Lion King', 89, 'Animation', 2.99, 10);

-- Example 2
INSERT INTO VHS (VHSID, Title, RunningLength, Genre, RentalFee, Discount)
VALUES (1002, 'Ghostbusters', 105, 'Comedy', 2.99, 5);

-- Example 3
INSERT INTO VHS (VHSID, Title, RunningLength, Genre, RentalFee, Discount)
VALUES (1003, 'Terminator 2: Judgment Day', 137, 'Action', 2.99, 15);

-- Example 4
INSERT INTO VHS (VHSID, Title, RunningLength, Genre, RentalFee, Discount)
VALUES (1004, 'Pretty Woman', 119, 'Romance', 2.99, 10);

-- Example 5
INSERT INTO VHS (VHSID, Title, RunningLength, Genre, RentalFee, Discount)
VALUES (1005, 'The Silence of the Lambs', 118, 'Thriller', 2.99, 5);


--RENTAL
INSERT INTO RENTAL (RentalID, DistributorID, DateOut, DateIn, DateDue, RentalFee, LateFee, DamageFee, RewindFee, OtherFee)
VALUES (1001, 1001, TO_DATE('2022-02-01', 'YYYY-MM-DD'), TO_DATE('2022-02-02', 'YYYY-MM-DD'), TO_DATE('2022-02-08', 'YYYY-MM-DD'), 5.99, 1.50, 0.00, 0.00, 0.00);

INSERT INTO RENTAL (RentalID, DistributorID, DateOut, DateIn, DateDue, RentalFee, LateFee, DamageFee, RewindFee, OtherFee)
VALUES (1002, 1002, TO_DATE('2022-03-15', 'YYYY-MM-DD'), TO_DATE('2022-03-16', 'YYYY-MM-DD'), TO_DATE('2022-03-22', 'YYYY-MM-DD'), 3.99, 0.00, 0.00, 0.50, 0.00);

INSERT INTO RENTAL (RentalID, DistributorID, DateOut, DateIn, DateDue, RentalFee, LateFee, DamageFee, RewindFee, OtherFee)
VALUES (1003, 1003, TO_DATE('2022-05-10', 'YYYY-MM-DD'), TO_DATE('2022-05-13', 'YYYY-MM-DD'), TO_DATE('2022-05-17', 'YYYY-MM-DD'), 2.99, 1.50, 0.00, 0.00, 0.00);

INSERT INTO RENTAL (RentalID, DistributorID, DateOut, DateIn, DateDue, RentalFee, LateFee, DamageFee, RewindFee, OtherFee)
VALUES (1001, 1004, TO_DATE('2023-04-23', 'YYYY-MM-DD'), TO_DATE('2023-04-25', 'YYYY-MM-DD'), TO_DATE('2023-04-28', 'YYYY-MM-DD'), 5.99, 0, 0, 0.50, 0);

INSERT INTO RENTAL (RentalID, DistributorID, DateOut, DateIn, DateDue, RentalFee, LateFee, DamageFee, RewindFee, OtherFee)
VALUES (1002, 1005, TO_DATE('2023-04-20', 'YYYY-MM-DD'), TO_DATE('2023-04-25', 'YYYY-MM-DD'), TO_DATE('2023-04-27', 'YYYY-MM-DD'), 3.99, 1.50, 0, 0.50, 0);

--RELATIONAL TABLES

--ACTOR_MOVIE


--DIRECTOR_MOVIE


--AWARD_MOVIE


--DVD_MOVIE


--VHS_MOVIE


--VHS_RENTAL


--DVD_RENTAL


--CUSTOMER_RENTAL