DROP TABLE IF EXISTS "ACTOR";
DROP TABLE IF EXISTS "BOXOFFICE";
DROP TABLE IF EXISTS "MOVIE";
DROP TABLE IF EXISTS "REVIEW";
DROP TABLE IF EXISTS "GENRE";
DROP TABLE IF EXISTS "PRODUCER";
DROP TABLE IF EXISTS "NOMINATION";
DROP TABLE IF EXISTS "TECHNICAL_TEAM";
DROP TABLE IF EXISTS "MOVIE_NOMINATION_BRIDGE";
DROP TABLE IF EXISTS "ACTOR_MOVIE_BRIDGE";
DROP TABLE IF EXISTS "ACTOR_NOMINATION_BRIDGE";
DROP TABLE IF EXISTS "PRODUCER_MOVIE_BRIDGE";
DROP TABLE IF EXISTS "GENRE_MOVIE_BRIDGE";
DROP TABLE IF EXISTS "MOVIE_TECHNICAL_TEAM_BRIDGE";

CREATE TABLE ACTOR (
    	ActorID int,
    	Name varchar(255),
    	No_of_awards int,
    	DOB varchar(255),
	PRIMARY KEY(ActorID)	
);
CREATE TABLE BOXOFFICE (
    	CertificateNo int,
    	Revenue int,
    	Budget int,
	PRIMARY KEY(CertificateNo)
);
CREATE TABLE MOVIE (
    	MovieID int,
    	Name varchar(255),
    	Year int,
    	No_of_awards int,
	Box_office_no int,
	Tech_team_ID int,
    	PRIMARY KEY(MovieID),
	FOREIGN KEY(Box_office_no) references BOXOFFICE(CertificateNo)
	FOREIGN KEY(Tech_team_ID) references TECHNICAL_TEAM(Tech_ID)
);

CREATE TABLE REVIEW (
    	Score int,
	Review_text varchar(255),
	Box_office_no int,
	MovieID int,
	FOREIGN KEY(MovieID) references MOVIE(MovieID),
	FOREIGN KEY(Box_office_no) references BOXOFFICE(CertificateNo)
);

CREATE TABLE GENRE (
    	GenreID int,
    	Description varchar(255),
	PRIMARY KEY(GenreID)	
);

CREATE TABLE PRODUCER (
    	Prod_ID int,
    	Name varchar(255),
    	No_of_movies int,
	PRIMARY KEY(Prod_ID)
);
CREATE TABLE NOMINATIONS (
    	N_ID int,
    	Year int,
	Category varchar(255),
    	MovieID int,
    	PRIMARY KEY(N_ID),
	FOREIGN KEY(MovieID) references MOVIE(MovieID)
);
CREATE TABLE TECHNICAL_TEAM (
    	Tech_ID int,
	Name varchar(255),  
	Roles varchar(255),
	Experience int,  
	PRIMARY KEY(Tech_ID)	
);

CREATE TABLE MOVIE_NOMINATION_BRIDGE (
    	MovieID int, 
	N_ID int,	
	FOREIGN KEY(MovieID) references MOVIE(MovieID),
	FOREIGN KEY(N_ID) references NOMINATION(N_ID)
);
 
CREATE TABLE ACTOR_MOVIE_BRIDGE (
    	ActorID int,
	MovieID int,    	
	FOREIGN KEY(ActorID) references ACTOR(ActorID)
	FOREIGN KEY(MovieID) references MOVIE(MovieID)
);

CREATE TABLE ACTOR_NOMINATION_BRIDGE (
    	ActorID int,
	N_ID int,  	
	FOREIGN KEY(ActorID) references ACTOR(ActorID)
	FOREIGN KEY(N_ID) references NOMINATION(N_ID)
);

CREATE TABLE PRODUCER_MOVIE_BRIDGE (
    	Prod_ID int,
	MovieID int,    	
	FOREIGN KEY(Prod_ID) references PRODUCER(Prod_ID)
	FOREIGN KEY(MovieID) references MOVIE(MovieID)
);

CREATE TABLE MOVIE_TECHNICAL_TEAM_BRIDGE (
    	MovieID int, 
	Tech_ID int,	
	FOREIGN KEY(MovieID) references MOVIE(MovieID),
	FOREIGN KEY(Tech_ID) references TECHNICAL_TEAM(Tech_ID)
);

CREATE TABLE GENRE_MOVIE_BRIDGE (
    	GenreID int,
	MovieID int,    	
	FOREIGN KEY(GenreID) references GENRE(GenreID)
	FOREIGN KEY(MovieID) references MOVIE(MovieID)
);
