INSERT INTO Engineers (Lastname, Firstname, Email, Graddate)
SELECT 
    'Last'||(ROWNUM) AS Lastname,
    'First'||(ROWNUM) AS Firstname,
    'example'||(ROWNUM)||'@example.com' AS Email,
    TO_DATE('01-JAN-'||(2023+ROWNUM), 'DD-MON-YYYY') AS Graddate
FROM
    dual
CONNECT BY
    LEVEL <= 15;
