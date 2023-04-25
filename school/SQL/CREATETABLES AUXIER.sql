--FILE NAME: CREATETABLES TABLES
--AUTHOR NAME:ANDREW AUXIER
--CLASS:CMIS302 
--DATE: 20230422

CREATE TABLE ACTOR (
  ActorID           VARCHAR2(10) , 
  FirstName         VARCHAR2(30) , 
  LastName          VARCHAR2(30) , 
  CONSTRAINT ACTOR_PK PRIMARY KEY (ActorID)  
);

CREATE TABLE DIRECTOR (
  DirectorID        VARCHAR2(10) , 
  FirstName         VARCHAR2(30) , 
  LastName          VARCHAR2(30) , 
  CONSTRAINT DIRECTOR_PK PRIMARY KEY (DirectorID)  
);

CREATE TABLE AWARD (
  AwardID           VARCHAR2(10) ,   
  DateReceived      DATE , 
  TypeOfAward       VARCHAR2(10) , 
  CONSTRAINT AWARD_PK PRIMARY KEY (AwardID)  
);

---MOVIE TABLE
CREATE TABLE MOVIE (
  MovieID           VARCHAR2(10) ,    
  DistributorID     VARCHAR2(30) , 
  RunningLength     NUMBER(6) , 
  Genre             VARCHAR2(30) , 
  Rating            VARCHAR2(30) , 
  ReleaseDate       DATE , 
  CONSTRAINT MOVIE_PK PRIMARY KEY (MovieID)  
);

CREATE TABLE CUSTOMER (
  CustomerID        VARCHAR2(10) ,   
  FirstName         VARCHAR2(30) , 
  LastName          VARCHAR2(30) ,
  DateOfBirth       DATE , 
  StreetAddress     VARCHAR2(30) ,
  City              VARCHAR2(30) ,
  StateID           VARCHAR2(2) ,
  ZipCode           NUMBER(30) ,
  Telephone         NUMBER(10) ,

  CONSTRAINT CUSTOMER_PK PRIMARY KEY (CustomerID)  
);

CREATE TABLE DVD (
  DVDID             VARCHAR2(10) ,    
  Title             VARCHAR2(30) , 
  RunningLength     NUMBER(6) , 
  Genre             VARCHAR2(30) , 
  RentalFee         NUMBER(10) ,
  Discount          NUMBER(2) ,
  CONSTRAINT DVD_PK PRIMARY KEY (DVDID)  
);

CREATE TABLE VHS (
  VHSID             VARCHAR2(10) ,    
  Title             VARCHAR2(30) , 
  RunningLength     NUMBER(6) , 
  Genre             VARCHAR2(30) , 
  RentalFee         NUMBER(10) ,
  Discount          NUMBER(2) ,
  CONSTRAINT VHS_PK PRIMARY KEY (VHSID)  
);

CREATE TABLE RENTAL (
  RentalID          VARCHAR2(10) ,    
  DistributorID     VARCHAR2(30) , 
  DateOut           DATE , 
  DateIn            DATE , 
  DateDue           DATE ,
  RentalFee         NUMBER(10) ,
  LateFee           NUMBER(10) ,
  DamageFee         NUMBER(10) ,
  RewindFee         NUMBER(10) ,
  OtherFee          NUMBER(10) ,
  CONSTRAINT RENTAL_PK PRIMARY KEY (RentalID)  
);

----------------------

--RELATIONAL TABLES
CREATE TABLE ACTOR_MOVIE (
  ActorID           VARCHAR2(10) , 
  MovieID           VARCHAR2(10) ,
  CONSTRAINT ActorID_ACTOR_MOVIE_FK1    FOREIGN KEY (ActorID) REFERENCES ACTOR(ActorID) ,
  CONSTRAINT MovieID_ACTOR_MOVIE_FK2    FOREIGN KEY (MovieID) REFERENCES MOVIE(MovieID) 
);

CREATE TABLE DIRECTOR_MOVIE (
  DirectorID        VARCHAR2(10) , 
  MovieID           VARCHAR2(10) ,
  CONSTRAINT DirectorID_DIRECTOR_MOVIE_FK1 FOREIGN KEY (DirectorID) REFERENCES DIRECTOR(DirectorID)  ,
  CONSTRAINT MovieID_DIRECTOR_MOVIE_FK2    FOREIGN KEY (MovieID)   REFERENCES MOVIE(MovieID) 
);

CREATE TABLE AWARD_MOVIE (
  AwardID           VARCHAR2(10) , 
  MovieID           VARCHAR2(10) ,
  CONSTRAINT AwardID_AWARD_MOVIE_FK1    FOREIGN KEY (AwardID) REFERENCES AWARD(AwardID) ,
  CONSTRAINT MovieID_AWARD_MOVIE_FK2    FOREIGN KEY (MovieID) REFERENCES MOVIE(MovieID) 
);

CREATE TABLE DVD_MOVIE (
  DVDID             VARCHAR2(10) , 
  MovieID           VARCHAR2(10) ,
  CONSTRAINT DVDID_DVD_MOVIE_FK1      FOREIGN KEY (DVDID) REFERENCES DVD(DVDID) ,
  CONSTRAINT MovieID_DVD_MOVIE_FK2    FOREIGN KEY (MovieID) REFERENCES MOVIE(MovieID) 
);
CREATE TABLE VHS_MOVIE (
  VHSID             VARCHAR2(10) , 
  MovieID           VARCHAR2(10) ,
  CONSTRAINT VHSID_VHS_MOVIE_FK1      FOREIGN KEY (VHSID) REFERENCES VHS(VHSID) ,
  CONSTRAINT MovieID_VHS_MOVIE_FK2    FOREIGN KEY (MovieID) REFERENCES MOVIE(MovieID) 
);
CREATE TABLE VHS_RENTAL (
  VHSID             VARCHAR2(10) , 
  RentalID          VARCHAR2(10) ,
  CONSTRAINT VHSID_VHS_RENTAL_FK1      FOREIGN KEY (VHSID) REFERENCES VHS(VHSID) ,
  CONSTRAINT RentalID_VHS_RENTAL_FK2   FOREIGN KEY (RentalID) REFERENCES RENTAL(RentalID) 
);
CREATE TABLE DVD_RENTAL (
  DVDID             VARCHAR2(10) , 
  RentalID           VARCHAR2(10) ,
  CONSTRAINT DVDID_DVD_RENTAL_FK1      FOREIGN KEY (DVDID) REFERENCES DVD(DVDID) ,
  CONSTRAINT RentalID_DVD_RENTAL_FK2   FOREIGN KEY (RentalID) REFERENCES RENTAL(RentalID) 
);
CREATE TABLE CUSTOMER_RENTAL (
  CustomerID        VARCHAR2(10) , 
  RentalID           VARCHAR2(10) ,
  CONSTRAINT CustomerID_CUSTOMER_RENTAL_FK1 FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID) ,
  CONSTRAINT RentalID_CUSTOMER_RENTAL_FK2   FOREIGN KEY (RentalID) REFERENCES RENTAL(RentalID) 
);
