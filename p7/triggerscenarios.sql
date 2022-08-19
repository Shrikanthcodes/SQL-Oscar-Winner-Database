.nullvalue N/A

-- Trigger 1: Trigger validate_boxoffice_techteam
-- Trigger 1 a: Modification not affected by trigger because tech_team_id and box_office_no values are valid
insert into movie values(2987782, 'Telephone Line 3', 2017, 0, 1002,500243);

-- Query 1: Verifying whether the changes made by Trigger 1 a is reflected in the table (They are)
select Name from movie where MovieID = 2987782;

-- Trigger 1 b: Modification affected by trigger because tech_team_id is invalid
-- Error message (Error: stepping, You cannot make a movie without a valid technical team (19)) is thrown
insert into movie values(2987781, 'Telephone Line 5', 2017, 0, 1002,50024333);

-- Trigger 1 c: Modification affected by trigger because box_office_no is invalid
-- Error message (Error: stepping, You cannot record entries for movies without a box office certificate (19)) is thrown
insert into movie values(2987780, 'Telephone Line 3', 2017, 0, 1002221,500243);

-- Query 2: Verifying whether the changes made by Trigger 1 c is reflected in the table (They are not)
select Name from movie where MovieID = 2987780;




-- Triggers 2: log_actor_update, log_actor_insert, log_actor_delete
-- Trigger 2 a: Log table creation
DROP TABLE IF EXISTS actor_logs;
CREATE TABLE actor_logs (logID int, old_actorid int, new_actorid int, old_name varchar(255),
new_name varchar(255), old_DOB varchar(255), new_DOB varchar(255), action varchar(255), 
timestamp varchar(255), PRIMARY KEY(logID));

-- Trigger 2 b: Deletion affected by trigger because actor_logs table now exists
delete from actor where actorid = 3009996;

-- Trigger 2 c: Updation affected by trigger because actorID updated
update actor set Name = 'Raul Gomez' where ActorID = 3009971;

-- Query 3: Verifying whether the updation from trigger 2 b and 2 c are stored in the log table (They are)
select * from actor_logs;

-- Trigger 2 d: Updation not affected by trigger because actorID, name not updated even though log table exists
update actor set No_of_awards = 3 where ActorID = 3009973;

-- Query 4: Verifying whether the updation from trigger 2 d is stored in the log table by
-- counting the total number of rows in table (it isn't, only 2b and 2c are reflected))
SELECT COUNT(*) FROM actor_logs;





-- Trigger 3: boxoffice_integrity 
-- Query 5: Demonstrating movie table before the action of the trigger (We have demonstrated that
-- there is no entry in movie or review tables with Box_office_no = 122334455)
select * from movie where Box_office_no = 922334455;
select * from review where Box_office_no = 922334455;

-- Trigger 3 a: update the certificateno for boxoffice entry
update boxoffice set certificateno = 922334455 where certificateno = 10996;

-- Query 6: Verifying whether the changes made in boxoffice tables are reflected on movie and review tables
select * from movie where Box_office_no = 922334455;
select * from review where Box_office_no = 922334455;

-- Trigger 3 b: Example where trigger does not affect database
-- We do this by updating the budget for a boxoffice entry, but keep the CertificateNo constant 
update boxoffice set certificateno = 1003, budget = 10000000 where certificateno = 1003;

-- Query 7: Verifying whether the changes made in boxoffice tables make any changes on movie and review tables
-- we see no changes in movie and review tables
select * from movie where Box_office_no = 1003;
select * from review where Box_office_no = 1003;
