--ACTOR TABLE
CREATE TABLE ACTOR (
  ActorID           VARCHAR2(30) NOT NULL, 
  FirstName         VARCHAR2(30), 
  LastName          VARCHAR2(30), 
  CONSTRAINT ACTORS_PK PRIMARY KEY (ActorID) ENABLE 
);

--MOVIE TABLE
CREATE TABLE MOVIE (
  MovieID           VARCHAR2(30) NOT NULL, 
  DistributorID     VARCHAR2(30), 
  RunningLength     NUMBER, 
  Genre             VARCHAR2(30), 
  Rating            VARCHAR2(30), 
  ReleaseDate       DATE, 
  CONSTRAINT MOVIE_PK PRIMARY KEY (MovieID) ENABLE 
);

--MOVIE TABLE
CREATE TABLE ACTOR_MOVIE (
  ActorID           VARCHAR2(30) NOT NULL, 
  MovieID           VARCHAR2(30) NOT NULL,
  CONSTRAINT ActorID_FK1 FOREIGN KEY (ActorID) REFERENCES ACTOR(ActorID)
  CONSTRAINT MovieID_FK2 FOREIGN KEY (MovieID) REFERENCES MOVIE(MovieID) 
);

