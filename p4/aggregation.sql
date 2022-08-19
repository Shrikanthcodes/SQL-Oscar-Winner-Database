--How many awards on average do Actors with "Christ" in their name have?
select avg(No_of_awards) from Actor where Actor.Name like "%Christ%";

--Total number of movies with a rating of over 6.
SELECT count(MovieID) from Review WHERE Score > 6;

--Maximum Revenue for a movie whose budget is more than 10 million.
select max(Revenue) from BOXOFFICE where Budget > 1000000;