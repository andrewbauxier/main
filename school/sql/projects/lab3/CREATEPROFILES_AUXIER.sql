--create the profile
CREATE PROFILE PANDREWAUXIER LIMIT
    FAILED_LOGIN_ATTEMPTS       4
    PASSWORD_LIFE_TIME          120
    PASSWORD_LOCK_TIME          1
    PASSWORD_GRACE_TIME         0
    PASSWORD_REUSE_TIME         UNLIMITED
    PASSWORD_REUSE_MAX          UNLIMITED
    PASSWORD_VERIFY_FUNCTION    ora12c_strong_verify_function
--https://www.oradba.ch/wordpress/2013/07/oracle-12c-new-password-verify-function/


--query profile to ensure creation
SELECT profile, resource_name, limit
FROM dba_profiles
WHERE profile = 'PANDREWAUXIER';


--drop profiles
DROP PROFILE PAndrewAuxier


--CREATE USERS
CREATE USER U1ANDREWAUXIER
    IDENTIFIED BY "STRONG!!!Password111"
    --new password
    --COMPLEX!!!Password111
    DEFAULT TABLESPACE USERS
    QUOTA 30M ON USERS
    PROFILE PANDREWAUXIER
    ACCOUNT UNLOCK
    PASSWORD EXPIRE;

CREATE USER U2ANDREWAUXIER
    IDENTIFIED BY "STRONG!!!Password222"
    --new password
    --COMPLEX!!!Password222
    DEFAULT TABLESPACE USERS
    QUOTA 30M ON USERS
    PROFILE PANDREWAUXIER
    ACCOUNT UNLOCK
    PASSWORD EXPIRE;

--give users new passwords; uncomment when needed
-- ALTER USER U1ANDREWAUXIER IDENTIFIED BY "COMPLEX!!!Password111";
-- ALTER USER U2ANDREWAUXIER IDENTIFIED BY "COMPLEX!!!Password222";

--drop users; uncomment when needed
-- DROP USER U1ANDREWAUXIER CASCADE; 
-- DROP USER U2ANDREWAUXIER CASCADE;
--cascade means delete all user stuff too, like their tables, etc


--check user session; uncomment when needed
-- SELECT USER,SYS_CONTEXT ('USERENV', 'SESSION_USER') FROM dual


--create role for users
CREATE ROLE R1ANDREWAUXIER;


--grant role to users
GRANT ROLE R1ANDREWAUXIER TO U1ANDREWAUXIER
GRANT ROLE R1ANDREWAUXIER TO U2ANDREWAUXIER


--create tables, insert values
CREATE TABLE User1Data (
    id NUMBER PRIMARY KEY,
    column1 VARCHAR2(50),
    column2 VARCHAR2(50),
    column3 VARCHAR2(50)
);

CREATE TABLE User2Data (
    id NUMBER PRIMARY KEY,
    column1 VARCHAR2(50),
    column2 VARCHAR2(50),
    column3 VARCHAR2(50)
);


-- insert records into User1Data
INSERT INTO User1Data (id, column1, column2, column3)
VALUES (1, 'Value1', 'Value2', 'Value3');

INSERT INTO User1Data (id, column1, column2, column3)
VALUES (2, 'Value4', 'Value5', 'Value6');

INSERT INTO User1Data (id, column1, column2, column3)
VALUES (3, 'Value7', 'Value8', 'Value9');

-- insert records into User2Data
INSERT INTO User2Data (id, column1, column2, column3)
VALUES (1, 'Value10', 'Value11', 'Value12');

INSERT INTO User2Data (id, column1, column2, column3)
VALUES (2, 'Value13', 'Value14', 'Value15');

INSERT INTO User2Data (id, column1, column2, column3)
VALUES (3, 'Value16', 'Value17', 'Value18');


-- grant U1ANDREWAUXIER
GRANT CREATE SESSION, CREATE TABLE TO U1ANDREWAUXIER;
GRANT SELECT, INSERT ON User1Data TO U1ANDREWAUXIER;

-- grant U2ANDREWAUXIER
GRANT CREATE SESSION, CREATE TABLE TO U2ANDREWAUXIER;
GRANT SELECT ON USER1DATA TO U2ANDREWAUXIER;
GRANT SELECT, INSERT ON USER2DATA TO U2ANDREWAUXIER;


-- verify U2ANDREWAUXIER can select from User1Data
SELECT * FROM User1Data;
SELECT * FROM User2Data;

--stuck. user cannot see table. check course materials further to identify issue

--Could not figure it out, and late on assignment. submitting work.