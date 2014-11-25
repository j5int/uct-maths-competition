=====================
Admin actions
=====================

This section contains a few examples of actions that you might be required to do during the different stages of the competition.

Registration stage
------------------

- A teacher has chosen the wrong school at the school selection page.

    When this happens, the teacher will be unable to change their selection. They will be directed to send an email to the administrator explaining the situation. You will have to go to remove the association that the school has with the user. You can do this by going to the schools table of the Admin. interface and find the school that the user had selected incorrectly. From there, the **assigned to** field should show the teacher's username. Change this to '--------------' to remove the association. Then tell the teacher to log in again where they will be prompted to select another school.

    .. ::note Any students that were signed up by the teacher will still be there. 

- A teacher cannot find a school on the school selection page.

   At this point, the teacher will be prompted to email the administrator. You can add a new school by going to the Schools table in the Admin interface. See the Admin section of this documentation to understand what fields to fill in and how.  

- A teacher cannot register with his/her email address

   This is usually when the teacher has already created another username with the same email address. If a teacher comes to you with this query, you can just tell them to request a "Forgotten password". This process will send an email to the entered address with the username and a link to change a password.

- As an administrator, I need to enter information for multiple schools. Do I need to create a username for each school?

    No. You can sign up multiple schools with a single username if you are an administrator. You do, however, need to be careful here.

    First, log in to the teacher's interface with your username and password. You can then select a school and fill out and submit the entry. Then you can go back to the *Schools* table in the Admin interface and remove your username's association with that school. The next time you go to the teacher's interface you will be prompted to select another school. 

.. warning:: It is good practice to only **remove** a user's association with a school from the Admin interface. If a user becomes associated with more than one school at a time, this will end badly.


Results and ranking
-------------------

For specific actions, see the Admin interface section of this document. 
