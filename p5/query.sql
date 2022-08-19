-- Query to find movies with rating less than 7 and a box office loss
SELECT MOVIE.Name FROM MOVIE INNER JOIN BOXOFFICE on MOVIE.Box_office_no = BOXOFFICE.CertificateNo
INNER JOIN REVIEW on MOVIE.Box_office_no = REVIEW.Box_office_no
WHERE REVIEW.Score < 7 and BOXOFFICE.Budget > BOXOFFICE.Revenue;

--Movies with more than 1 award given that the cast has more than 1 award
SELECT MULTIPLE_AWARD_WINNING_ACTORS.Name, MOVIE.Name FROM MULTIPLE_AWARD_WINNING_ACTORS
INNER JOIN ACTOR_MOVIE_BRIDGE ON MULTIPLE_AWARD_WINNING_ACTORS.ActorID = ACTOR_MOVIE_BRIDGE.ActorID
INNER JOIN MOVIE ON ACTOR_MOVIE_BRIDGE.MovieID = MOVIE.MovieID
WHERE MOVIE.No_of_awards > 1;

--Query to find experience of technical team working on big budget fiolms
SELECT e.Name, e.Year,f.Experience FROM HIGH_BUDGET_FILMS e JOIN MOVIE_TECHNICAL_TEAM_BRIDGE USING(MovieID)
JOIN TECHNICAL_TEAM f USING(Tech_ID)
ORDER BY f.Experience;

-- Genre with highest no of awards
SELECT a.Description as Genre, COUNT(No_of_awards) as No_of_awards FROM NOMINATIONS_GENRE_MOVIE a
INNER JOIN MOVIE b ON a.MovieID = b.MovieID
GROUP BY a.Description HAVING a.Year>2000
ORDER BY COUNT(b.No_of_awards);

-- temp table for actors, to find most nominations by year
CREATE TEMP TABLE ActTemp AS select * from ACTOR;;
SELECT a.NAME, c.Year FROM ActTemp a
INNER JOIN ACTOR_NOMINATION_BRIDGE b on a.ActorID = b.ActorID
INNER JOIN NOMINATIONS c on b.N_ID = c.N_ID;

