-- View to see  award winning actors

CREATE VIEW MULTIPLE_AWARD_WINNING_ACTORS AS
SELECT * FROM ACTOR
WHERE No_of_awards > 1;
SELECT * FROM MULTIPLE_AWARD_WINNING_ACTORS;

--view to see high budget films

CREATE VIEW HIGH_BUDGET_FILMS AS
SELECT MovieID, Name, Year, No_of_awards, Revenue, Budget FROM MOVIE LEFT JOIN BOXOFFICE ON MOVIE.Box_office_no = BOXOFFICE.CertificateNo
WHERE Year > 2010 and Budget > 1000000;
SELECT * FROM HIGH_BUDGET_FILMS_RECENT;

--view to see nominations by genre

CREATE VIEW NOMINATIONS_GENRE_MOVIE AS
SELECT Year, Category, b.MovieID, Description FROM NOMINATIONS a, MOVIE_NOMINATION_BRIDGE b, 
GENRE_MOVIE_BRIDGE c, GENRE d
WHERE a.N_ID = b.N_ID and b.MovieID = c.MovieID and c.GenreID = d.GenreID;
SELECT * FROM NOMINATIONS_GENRE_MOVIE;
