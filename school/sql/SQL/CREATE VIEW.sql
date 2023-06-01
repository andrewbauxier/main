CREATE VIEW EnrollmentDetails AS
SELECT
    E.Lastname AS Engineer_Lastname,
    E.Firstname AS Engineer_Firstname,
    F.Lastname AS Faculty_Lastname,
    F.Email AS Faculty_Email,
    C.Subject AS Class_Subject,
    C.Title AS Class_Title
FROM
    ClassEnrollments CE
    JOIN Engineers E ON CE.EID = E.EID
    JOIN Faculty F ON CE.FID = F.FID
    JOIN Classes C ON CE.CID = C.CID;

SELECT * FROM EnrollmentDetails;
