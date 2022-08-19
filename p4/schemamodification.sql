--Adding a Flops column to each actor to indicate the number of movies that flopped.
ALTER TABLE ACTOR ADD COLUMN Flops int;

--Removing the previously added flops column
ALTER TABLE ACTOR DROP COLUMN Flops;