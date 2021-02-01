DO $$
    BEGIN
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person1', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 8, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person2', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 8, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person3', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 8, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person4', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 8, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person5', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 8, 'New LT', false, "Location" FROM competition_school;
        END;

        
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'A', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 8, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'B', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 8, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'C', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 8, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'D', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 8, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'E', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 8, 'New LT', true, "Location" FROM competition_school;
        END;




        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person1', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 9, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person2', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 9, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person3', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 9, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person4', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 9, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person5', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 9, 'New LT', false, "Location" FROM competition_school;
        END;

        
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'A', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 9, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'B', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 9, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'C', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 9, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'D', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 9, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'E', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 9, 'New LT', true, "Location" FROM competition_school;
        END;
        
        
        
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person1', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 10, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person2', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 10, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person3', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 10, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person4', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 10, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person5', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 10, 'New LT', false, "Location" FROM competition_school;
        END;

        
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'A', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 10, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'B', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 10, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'C', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 10, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'D', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 10, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'E', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 10, 'New LT', true, "Location" FROM competition_school;
        END;
        
        
        
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person1', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 11, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person2', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 11, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person3', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 11, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person4', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 11, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person5', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 11, 'New LT', false, "Location" FROM competition_school;
        END;

        
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'A', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 11, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'B', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 11, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'C', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 11, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'D', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 11, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'E', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 11, 'New LT', true, "Location" FROM competition_school;
        END;
        
        
        
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person1', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 12, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person2', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 12, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person3', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 12, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person4', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 12, 'New LT', false, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Test', 'Person5', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 12, 'New LT', false, "Location" FROM competition_school;
        END;

        
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'A', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 12, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'B', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 12, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'C', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 12, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'D', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 12, 'New LT', true, "Location" FROM competition_school;
        END;
        BEGIN
            INSERT INTO competition_schoolstudent ("First_name", "Surname", "Language", "Reference", "School", "Grade", "Venue", "Paired", "Location")
                SELECT 'Pair', 'E', "Language", CAST(CAST(RANDOM() * 10000 AS INT) AS VARCHAR), "id", 12, 'New LT', true, "Location" FROM competition_school;
        END;
    END;
$$