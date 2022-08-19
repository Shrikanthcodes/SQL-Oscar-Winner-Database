-- Trigger 1 : Trigger for validating Box office no. and technical team information of a movie,
-- These are foreign keys of the table and we are therefore checking the Referential Integrity Constraint

drop trigger if exists validate_boxoffice_techteam;
create trigger validate_boxoffice_techteam
before insert on movie
begin
select
case
when NOT EXISTS (SELECT * FROM boxoffice WHERE certificateNo = NEW.Box_office_no) THEN
RAISE (ABORT, 'You cannot record entries for movies without a box office certificate')
when NOT EXISTS (SELECT * FROM technical_team WHERE tech_id = NEW.tech_team_id) THEN
RAISE (ABORT, 'You cannot make a movie without a valid technical team')
end;
end;


-- Trigger 2: 3 triggers for saving log table for update, insert and deletion of table actor 
-- (log table creation required)

drop trigger if exists log_actor_update;
create trigger log_actor_update
after update on actor
when old.actorID <> new.actorID OR old.name <> new.name
begin
insert into actor_logs (old_actorid,new_actorid,old_name,new_name,old_DOB,new_DOB,action,timestamp)
values(old.actorid,new.actorid,old.name,new.name,old.DOB,new.DOB,'UPDATE',DATETIME('NOW'));END;

drop trigger if exists log_actor_insert;
create trigger log_actor_insert
after insert on actor
begin
insert into actor_logs (new_actorid,new_name,new_DOB,action,timestamp)
values(new.actorid,new.name,new.DOB,'INSERT',DATETIME('NOW'));END;

drop trigger if exists log_actor_delete;
create trigger log_actor_delete
after delete on actor
begin
insert into actor_logs (old_actorid,old_name,old_DOB,action,timestamp)
values(old.actorid,old.name,old.DOB,'DELETE',DATETIME('NOW'));END;


-- Trigger 3: Maintains integrity constraint when Box office certificate no. entry is updated

drop trigger if exists boxoffice_integrity;
create trigger boxoffice_integrity
after update on boxoffice
when old.CertificateNo <> new.CertificateNo
begin
update movie set Box_office_no = new.CertificateNo 
where Box_office_no = old.CertificateNo;
update review set Box_office_no = new.CertificateNo 
where Box_office_no = old.CertificateNo;
end;
