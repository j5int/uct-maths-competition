--$psql  <DBNAME> -a -f /scripts/add_location_column_27012017.sql

DO $$
	BEGIN
		BEGIN
			ALTER TABLE competition_competition ADD COLUMN  "prizegiving_date" DATE DEFAULT '9999-12-31';
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column prizegiving_date already exists in competition_competition.';
		END;
		BEGIN
			ALTER TABLE competition_responsibleteacher ADD COLUMN  "Report_downloaded" TIMESTAMP;
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column Report_downloaded already exists in competition_responsibleteacher.';
		END;
		BEGIN
			ALTER TABLE competition_responsibleteacher ADD COLUMN  "Answer_sheet_downloaded" TIMESTAMP;
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column Answer_sheet_downloaded already exists in competition_responsibleteacher.';
		END;
		BEGIN
			ALTER TABLE competition_school ADD COLUMN "answer_sheets_emailed" TIMESTAMP;
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column answer_sheets_emailed already exists in competition_school';
		END;
		BEGIN
			ALTER TABLE competition_school ADD COLUMN "report_emailed" TIMESTAMP;
		EXCEPTION
			WHEN duplicate_column THEN RAISE NOTICE 'column report_emailed already exists in competition_school';
		END;
	END;
$$
