CREATE TABLE Engineers (
    EID NUMBER GENERATED BY DEFAULT AS IDENTITY (START WITH 1) PRIMARY KEY,
    Lastname VARCHAR2(30),
    Firstname VARCHAR2(30),
    Email VARCHAR2(30),
    Graddate DATE
);

CREATE TABLE FACULTY (
    FID NUMBER GENERATED BY DEFAULT AS IDENTITY (START WITH 1) PRIMARY KEY,
    Lastname VARCHAR2(30),
    Firstname VARCHAR2(30),
    Email VARCHAR2(30),
    Hiredate DATE
);

CREATE TABLE CLASSES (
    CID NUMBER GENERATED BY DEFAULT AS IDENTITY (START WITH 1) PRIMARY KEY,
    Subject VARCHAR2(4), /*'Subject' is a keyword. Not my fault if it does something funny, it was in the assignment guidelines*/
    Catalognbr NUMBER(3),
    Title VARCHAR2(30)
);

CREATE TABLE ClassEnrollments (
    EnID NUMBER GENERATED BY DEFAULT AS IDENTITY (START WITH 1) PRIMARY KEY,
    CID NUMBER,
    FID NUMBER,
    EID NUMBER,
    FOREIGN KEY (EID) REFERENCES Engineers (EID)
    FOREIGN KEY (FID) REFERENCES Faculty (FID),
    FOREIGN KEY (CID) REFERENCES Classes (CID),
);