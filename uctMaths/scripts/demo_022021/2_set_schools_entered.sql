DO $$
    BEGIN 
        BEGIN
            UPDATE competition_school SET "Entered"=1 WHERE "id"<>390; 
        END;
    END;
$$