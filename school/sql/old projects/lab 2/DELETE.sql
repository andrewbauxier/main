DELETE FROM ClassEnrollments
WHERE EnID = (
    SELECT MIN(EnID)
    FROM ClassEnrollments
);
