/*
1. Create a unique Profile based on the following requirements:
    a. Password complexity should meet requirements for Ora12 Verify function.
    b. User may have up to 3 concurrent sessions.
    c. User may have up to 4 consecutive failed attempts to log in before the account is
    locked.
    d. User may wait up till 120 days before their password must be changed.
    e. User account will be locked for 1 hours after the specified number of consecutive failed
    login attempts.
    f. Default values for other Profile parameters is acceptable
    g. You should name the Profile PFirstnameLastname where Lastname and Firstname are
    your First and Lastname
*/
--create the profile
CREATE PROFILE PAndrewAuxier LIMIT
    FAILED_LOGIN_ATTEMPTS       4
    PASSWORD_LIFE_TIME          120
    PASSWORD_LOCK_TIME          1
    PASSWORD_GRACE_TIME         0
    PASSWORD_REUSE_TIME         UNLIMITED
    PASSWORD_REUSE_MAX          UNLIMITED
    PASSWORD_VERIFY_FUNCTION    ora12c_strong_verify_function
--https://www.oradba.ch/wordpress/2013/07/oracle-12c-new-password-verify-function/

--query the profile to ensure successful creation
SELECT profile, resource_name, limit
FROM dba_profiles
WHERE profile = 'PANDREWAUXIER';

--ora12c_strong_verify_function
CREATE OR REPLACE FUNCTION ora12c_verify_function (
    username IN VARCHAR2,
    password IN VARCHAR2,
    old_password IN VARCHAR2
) RETURN BOOLEAN IS
BEGIN
    IF NOT complexity_check(password, chars => 9, upper => 2, lower => 2,
                        digit => 2, special => 2) THEN
    RETURN(FALSE);
    END IF;
    RETURN TRUE;
END;


