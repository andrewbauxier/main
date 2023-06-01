--Engineer table inserts
INSERT INTO Engineers (Lastname, Firstname, Email, Graddate)
SELECT 
    'Last'||(ROWNUM) AS Lastname,
    'First'||(ROWNUM) AS Firstname,
    'example'||(ROWNUM)||'@example.com' AS Email,
    DATE '2023-01-01' + (ROWNUM-1) AS Graddate
FROM
    dual
CONNECT BY
    LEVEL <= 15;

--Faculty table inserts
INSERT INTO Faculty (Lastname, Firstname, Email, Hiredate)
SELECT 
    'Last'||(ROWNUM) AS Lastname,
    'First'||(ROWNUM) AS Firstname,
    'example'||(ROWNUM)||'@example.com' AS Email,
    DATE '2023-01-01' + (ROWNUM-1) AS Hiredate
FROM
    dual
CONNECT BY
    LEVEL <= 3;


--Class table inserts
INSERT INTO Classes (Subject, Catalognbr, Title)
VALUES ('AAAA', 101, 'ClassTitle1');

INSERT INTO Classes (Subject, Catalognbr, Title)
VALUES ('BBBB', 201, 'ClassTitle2');

INSERT INTO Classes (Subject, Catalognbr, Title)
VALUES ('CCCC', 301, 'ClassTitle3');



--Enrollment table inserts
-- Enrollment table inserts
INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (1, 1, 1);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (1, 2, 2);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (1, 3, 3);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (2, 1, 4);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (2, 2, 5);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (2, 3, 6);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (3, 1, 7);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (3, 2, 8);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (3, 3, 9);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (1, 1, 10);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (2, 2, 11);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (3, 3, 12);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (1, 1, 13);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (2, 2, 14);

INSERT INTO ClassEnrollments (CID, FID, EID)
VALUES (3, 3, 15);
