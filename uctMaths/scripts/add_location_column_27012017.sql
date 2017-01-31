--$psql  <DBNAME> -a -f /scripts/add_location_column_27012017.sql

DO $$
	BEGIN
		BEGIN
			ALTER TABLE competition_school ADD COLUMN  "Location" varchar(3) NOT NULL DEFAULT 'CPT';
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column Location already exists in competition_school.';
		END;
		BEGIN
			ALTER TABLE competition_schoolstudent ADD COLUMN  "Location" varchar(3) NOT NULL DEFAULT 'CPT';
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column Location already exists in competition_schoolstudent.';
		END;
		BEGIN
			ALTER TABLE competition_venue ADD COLUMN  "Location" varchar(3) NOT NULL DEFAULT 'CPT';
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column Location already exists in competition_venue.';
		END;
		BEGIN
			ALTER TABLE competition_invigilator ADD COLUMN  "Location" varchar(3) NOT NULL DEFAULT 'CPT';
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column Location already exists in competition_invigilator.';
		END;
		BEGIN
			ALTER TABLE competition_schoolstudentarchive ADD COLUMN  "Location" varchar(3) NOT NULL DEFAULT 'CPT';
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column Location already exists in competition_schoolstudentarchive.';
		END;
		BEGIN
			ALTER TABLE competition_invigilatorarchive ADD COLUMN  "Location" varchar(3) NOT NULL DEFAULT 'CPT';
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column Location already exists in competition_invigilatorarchive.';
		END;

		BEGIN
			ALTER TABLE competition_school ALTER COLUMN  "Location" DROP DEFAULT;
			ALTER TABLE competition_schoolstudent ALTER COLUMN "Location" DROP DEFAULT;
			ALTER TABLE competition_venue ALTER COLUMN "Location" DROP DEFAULT;
			ALTER TABLE competition_invigilator ALTER COLUMN "Location" DROP DEFAULT;
			ALTER TABLE competition_schoolstudentarchive ALTER COLUMN "Location" DROP DEFAULT;
			ALTER TABLE competition_invigilatorarchive ALTER COLUMN "Location" DROP DEFAULT;
		END;
	END;
$$
