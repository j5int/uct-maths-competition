# New features added in January 2021

## User changes
* School reports can now be emailed to all schools by the admin
* Answer sheets are automatically produced for all students
* Generated answer sheets can be automatically emailed to all schools by the admin
* Admins can download answer sheets and reports for any set of schools
* Teachers can log in to download their answer sheets or school reports manually
* The prizegiving date is declared in a new column in the competition table
* Reports can be downloaded by teachers from 21:00 on the prizegiving date
* Admin can generate PDFs of all students in a particular grade all together. This is emailed to the admin when ready.
* Added action buttons for actions that are independent of selection.
* Allow the competition admin to chose if invigilators are necessary, and if teachers may download answer sheets.
* Remove all reference to pairs in entry forms if no pair entries are allowed.

## Implementation changes
* Added new columns (see this [script](../uctMaths/scripts/add_new_columns_022021.sql))
* Added support for background tasks
* Answer sheet and result emails are handled by the background process
* Changed the way student IDs are generated