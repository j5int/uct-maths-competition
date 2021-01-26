--$psql  <DBNAME> -a -f /scripts/add_location_column_27012017.sql

DO $$
	BEGIN
		BEGIN
			ALTER TABLE competition_competition ADD COLUMN  "prizegiving_date" DATE NOT NULL DEFAULT '9999-12-31';
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column prizegiving_date already exists in competition_competition.';
		END;
		BEGIN
			ALTER TABLE competition_responsibleteacher ADD COLUMN  "Report_downloaded" DATE NOT NULL DEFAULT '9999-12-31';
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column Report_downloaded already exists in competition_responsibleteacher.';
		END;
		BEGIN
			ALTER TABLE competition_responsibleteacher ADD COLUMN  "Answer_sheet_downloaded" DATE NOT NULL DEFAULT '9999-12-31';
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column Answer_sheet_downloaded already exists in competition_responsibleteacher.';
		END;
	END;
$$
