DO $$
    BEGIN 
        BEGIN
            UPDATE competition_school SET "Entered"=0;
        END;
    END;
$$