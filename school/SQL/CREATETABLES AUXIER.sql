--FILE NAME: CREATETABLES TABLES
--AUTHOR NAME:ANDREW AUXIER
--CLASS:CMIS302 
--DATE: 20230422

CREATE TABLE ACTOR (
  ActorID           NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  FirstName         VARCHAR2(30) , 
  LastName          VARCHAR2(30) 
);

CREATE TABLE DIRECTOR (
  DirectorID        NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
  FirstName         VARCHAR2(30) , 
  LastName          VARCHAR2(30) 
);

CREATE TABLE AWARD (
  AwardID           NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,   
  DateReceived      DATE , 
  TypeOfAward       VARCHAR2(10)  
);

---MOVIE TABLE
CREATE TABLE MOVIE (
  MovieID           NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,    
  DistributorID     VARCHAR2(30) , 
  RunningLength     NUMBER(6) , 
  Genre             VARCHAR2(30) , 
  Rating            VARCHAR2(30) , 
  ReleaseDate       DATE 
);

CREATE TABLE CUSTOMER (
  CustomerID        NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,   
  FirstName         VARCHAR2(30) , 
  LastName          VARCHAR2(30) ,
  DateOfBirth       DATE , 
  StreetAddress     VARCHAR2(30) ,
  City              VARCHAR2(30) ,
  StateID           VARCHAR2(2) ,
  ZipCode           NUMBER(30) ,
  Telephone         NUMBER(10) 

);

CREATE TABLE DVD (
  DVDID             NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,    
  Title             VARCHAR2(30) , 
  RunningLength     NUMBER(6) , 
  Genre             VARCHAR2(30) , 
  RentalFee         NUMBER(10) ,
  Discount          NUMBER(2) 
);

CREATE TABLE VHS (
  VHSID             NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,    
  Title             VARCHAR2(30) , 
  RunningLength     NUMBER(6) , 
  Genre             VARCHAR2(30) , 
  RentalFee         NUMBER(10) ,
  Discount          NUMBER(2) 
);

CREATE TABLE RENTAL (
  RentalID          NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,    
  DistributorID     VARCHAR2(30) , 
  DateOut           DATE , 
  DateIn            DATE , 
  DateDue           DATE ,
  RentalFee         NUMBER(10) ,
  LateFee           NUMBER(10) ,
  DamageFee         NUMBER(10) ,
  RewindFee         NUMBER(10) ,
  OtherFee          NUMBER(10) 
);

----------------------

--RELATIONAL TABLES
CREATE TABLE ACTOR_MOVIE (
  ActorID           NUMBER(8) , 
  MovieID           NUMBER(8) ,
  CONSTRAINT ActorID_ACTOR_MOVIE_FK1    FOREIGN KEY (ActorID) REFERENCES ACTOR(ActorID) ,
  CONSTRAINT MovieID_ACTOR_MOVIE_FK2    FOREIGN KEY (MovieID) REFERENCES MOVIE(MovieID) 
);
CREATE TABLE ACTOR_MOVIE (
  ActorID           NUMBER, 
  MovieID           NUMBER,
  CONSTRAINT Actor_Movie_PK PRIMARY KEY (ActorID, MovieID),
  CONSTRAINT Actor_Movie_Actor_FK FOREIGN KEY (ActorID) REFERENCES Actor(ActorID),
  CONSTRAINT Actor_Movie_Movie_FK FOREIGN KEY (MovieID) REFERENCES Movie(MovieID)
);

CREATE TABLE DIRECTOR_MOVIE (
  DirectorID        NUMBER(8) , 
  MovieID           NUMBER(8) ,
  CONSTRAINT DirectorID_DIRECTOR_MOVIE_FK1 FOREIGN KEY (DirectorID) REFERENCES DIRECTOR(DirectorID)  ,
  CONSTRAINT MovieID_DIRECTOR_MOVIE_FK2    FOREIGN KEY (MovieID)   REFERENCES MOVIE(MovieID) 
);

CREATE TABLE AWARD_MOVIE (
  AwardID           NUMBER(8) , 
  MovieID           NUMBER(8) ,
  CONSTRAINT AwardID_AWARD_MOVIE_FK1    FOREIGN KEY (AwardID) REFERENCES AWARD(AwardID) ,
  CONSTRAINT MovieID_AWARD_MOVIE_FK2    FOREIGN KEY (MovieID) REFERENCES MOVIE(MovieID) 
);

CREATE TABLE DVD_MOVIE (
  DVDID             NUMBER(8) , 
  MovieID           NUMBER(8) ,
  CONSTRAINT DVDID_DVD_MOVIE_FK1      FOREIGN KEY (DVDID) REFERENCES DVD(DVDID) ,
  CONSTRAINT MovieID_DVD_MOVIE_FK2    FOREIGN KEY (MovieID) REFERENCES MOVIE(MovieID) 
);
CREATE TABLE VHS_MOVIE (
  VHSID             NUMBER(8) , 
  MovieID           NUMBER(8) ,
  CONSTRAINT VHSID_VHS_MOVIE_FK1      FOREIGN KEY (VHSID) REFERENCES VHS(VHSID) ,
  CONSTRAINT MovieID_VHS_MOVIE_FK2    FOREIGN KEY (MovieID) REFERENCES MOVIE(MovieID) 
);
CREATE TABLE VHS_RENTAL (
  VHSID             NUMBER(8) , 
  RentalID          NUMBER(8) ,
  CONSTRAINT VHSID_VHS_RENTAL_FK1      FOREIGN KEY (VHSID) REFERENCES VHS(VHSID) ,
  CONSTRAINT RentalID_VHS_RENTAL_FK2   FOREIGN KEY (RentalID) REFERENCES RENTAL(RentalID) 
);
CREATE TABLE DVD_RENTAL (
  DVDID             NUMBER(8) , 
  RentalID          NUMBER(8) ,
  CONSTRAINT DVDID_DVD_RENTAL_FK1      FOREIGN KEY (DVDID) REFERENCES DVD(DVDID) ,
  CONSTRAINT RentalID_DVD_RENTAL_FK2   FOREIGN KEY (RentalID) REFERENCES RENTAL(RentalID) 
);
CREATE TABLE CUSTOMER_RENTAL (
  CustomerID        NUMBER(8) , 
  RentalID          NUMBER(8) ,
  CONSTRAINT CustomerID_CUSTOMER_RENTAL_FK1 FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID) ,
  CONSTRAINT RentalID_CUSTOMER_RENTAL_FK2   FOREIGN KEY (RentalID) REFERENCES RENTAL(RentalID) 
);
