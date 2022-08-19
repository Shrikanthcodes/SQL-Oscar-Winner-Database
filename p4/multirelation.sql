--Display all the actors who have acted with other oscar winners:
SELECT ACTOR.name as Name FROM ACTOR, MOVIE, ACTOR_MOVIE_BRIDGE
WHERE ACTOR_MOVIE_BRIDGE.ActorID = ACTOR.ActorID AND
ACTOR_MOVIE_BRIDGE.MovieID = MOVIE.MovieID
GROUP BY MOVIE.MovieID
ORDER BY count(ACTOR.ActorID);


--Producers who have the highest budget for their movies. (Top 5)
SELECT PRODUCER.Name, sum(BOXOFFICE.Budget) FROM PRODUCER, MOVIE, PRODUCER_MOVIE_BRIDGE, BOXOFFICE
WHERE PRODUCER.Prod_ID = PRODUCER_MOVIE_BRIDGE.Prod_ID and PRODUCER_MOVIE_BRIDGE.MovieID = MOVIE.MovieID
AND BOXOFFICE.CertificateNo = MOVIE.Box_office_no
GROUP BY PRODUCER.Prod_ID
ORDER BY sum(BOXOFFICE.Budget) DESC LIMIT 5;


--Display Name and count of nominations received by the Technical Teams working in award winning movies (Top 3)
SELECT Name, count(NOMINATIONS.N_ID) as awards FROM TECHNICAL_TEAM, NOMINATIONS, 
MOVIE_TECHNICAL_TEAM_BRIDGE, MOVIE_NOMINATION_BRIDGE
WHERE NOMINATIONS.N_ID = MOVIE_NOMINATION_BRIDGE.N_ID AND MOVIE_TECHNICAL_TEAM_BRIDGE.Tech_ID = TECHNICAL_TEAM.Tech_ID AND MOVIE_TECHNICAL_TEAM_BRIDGE.MovieID = MOVIE_NOMINATION_BRIDGE.MovieID
GROUP BY TECHNICAL_TEAM.Tech_ID
ORDER BY count(NOMINATIONS.N_ID) DESC LIMIT 3;

--Display the name of the genre that has produced the movie with the highest profit
SELECT description FROM GENRE where GenreID = 
(SELECT GenreID FROM GENRE_MOVIE_BRIDGE WHERE MovieID =
(SELECT MovieID FROM MOVIE where Box_office_no =
(SELECT CertificateNo from BOXOFFICE ORDER BY (Revenue - Budget) DESC LIMIT 1)));

--Name of Producer who has directed movies that have won more than 1 awards
SELECT PRODUCER.Name FROM PRODUCER where Prod_ID = 
(SELECT Prod_ID from PRODUCER_MOVIE_BRIDGE WHERE MovieID =
(SELECT MovieID from MOVIE WHERE No_of_awards > 1));

