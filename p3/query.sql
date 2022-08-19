-- Query to choose actors whose name contains the characters "Di"
SELECT * FROM ACTOR where Name like "%Di%";

-- Query to select movies that are recent(after 2010)
SELECT * FROM MOVIE where YEAR > 2010;

-- Query to find movies that released in the 21st century and have gotten more than 2 awards
SELECT * FROM MOVIE where No_of_awards > 2 and Year > 1999;