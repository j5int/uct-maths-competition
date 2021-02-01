DO $$
    BEGIN
        BEGIN
            UPDATE competition_school
                SET answer_sheets_emailed = '1971-01-01 00:00:00';
        END;
    END;
$$