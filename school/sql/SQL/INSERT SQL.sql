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