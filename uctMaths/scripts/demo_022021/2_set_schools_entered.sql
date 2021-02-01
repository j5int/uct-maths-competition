DO $$
    BEGIN 
        BEGIN
            UPDATE competition_school SET "Entered"=1;
        END;
    END;
$$