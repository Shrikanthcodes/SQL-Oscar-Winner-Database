INSERT INTO GENRE values (4001, 'Action');
INSERT INTO GENRE values (4002, 'Sports');
INSERT INTO GENRE values (4003, 'Documentary');
INSERT INTO GENRE values (4004, 'Rom-Com');
INSERT INTO GENRE values (4005, 'Drama');
INSERT INTO GENRE values (4006, 'Thriller');
INSERT INTO GENRE values (4007, 'Suspense');


.mode csv
.import data/Actor.csv Actor
.import data/Movie.csv Movie
.import data/Actor_movie_bridge.csv Actor_movie_bridge
.import data/Movie_nomination_bridge.csv Movie_nomination_bridge
.import data/Actor_nomination_bridge.csv Actor_nomination_bridge
.import data/Review.csv Review
.import data/nomination.csv Nominations
.import data/Box_office.csv Boxoffice
.import data/producer.csv Producer
.import data/technical_team.csv technical_team
.import data/producer_movie_bridge.csv producer_movie_bridge
.import data/movie_technical_team_bridge.csv movie_technical_team_bridge
.import data/genre_movie_bridge.csv genre_movie_bridge
