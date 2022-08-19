--Adding a new Actor to our database
INSERT INTO ACTOR VALUES (2353, 'Sarah Wilson', 3, '03/07/1991');

--Adding a new movie to our database
INSERT INTO MOVIE VALUES (34, 'Oh my love', 2015, 4, 2352, 12);

--Updating Tim Robbins' tuple
UPDATE ACTOR SET No_of_awards= 6, where Name = "Tim Robbins";

--Updating one of the Movies called Room
UPDATE MOVIE SET Name="Rooms", Year = 2018 where MovieID = 22;

--Adding Leonardo Di-Caprio as a producer, since he is both an actor as well as a producer
INSERT INTO PRODUCER SELECT 9021,Name,No_of_awards from ACTOR where Name="Leonardo DiCaprio";

--Adding Movie "Oh My Love" to BoxOffice
INSERT INTO BOXOFFICE SELECT Box_office_no, 3000000, 2500000 FROM MOVIE WHERE MovieID = 34;

--Deleting the data entry of Sarah Wilson from Actors
DELETE FROM ACTOR where ACTOR.Name="Sarah Wilson";

--Deleting the data entry of movie named 'oh my love' from Movie Table
DELETE FROM MOVIE where MOVIE.Name="Oh my love";

--Deleting the data entry of movie named 'oh my love' from Box Office Table
DELETE FROM BOXOFFICE WHERE BOXOFFICE.CertificateNo = 2352;



