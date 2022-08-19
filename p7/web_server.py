#Imports required : sqlite3, bottle
import sqlite3
from bottle import route, run

#Establishing connection with the database
conn = sqlite3.connect('academy.db')

"""
Function Name:

Startpage ('/')
--------------------
Operation:

Defines the HTML view of the homepage of the webserver.
Contains hyperlinks to all the other pages in the server.
--------------------
return:

html: html content of the page
"""
@route('/')
def startpage():
    print("Welcome to Academy Awards Database")
    html = """ <h1> Home Page </h1> <br> 
    <a href = '/Info'> Go to Project Abstract Page </a>
    <br> <a href = '/Data'> Go to Table overview Page </a> <br>
    <a href = '/view'> Go to Data sample view Page </a><br> 
    <a href = '/Credits'> Go to Credits  </a>"""

    return html

"""
Function Name:

Info ('/Info')
--------------------
Operation:

Contains the information about the project, in this case that is the abstract of the project.
Contains hyperlink to the home page.
--------------------
return:

html: html content of the page
"""
@route('/Info')
def Info():
    print("Information")
    html = """ <h1> Info page </h1> <p> This page contains information about the database </p>
        <br><br> PROJECT PROPOSAL: <br><br>

        Idea: Academy Awards Database<br>

        The objective of this project is to create a database of information on Oscar awards.
        The database includes tables such as, and not limited to:<br> 
        1) table containing information on award winning actors, <br>
        2) table on movies, <br>
        3) table on nomination of awards, <br>
        4) table for genre of movies,<br>
        5) table for box office ratings of movies,<br> 
        6) table for producers<br>
        7) table for technical staff<br><br>


        In this project, I want to use my passion for movies to collect and make sense
        of data about the Academy Awards. I have always loved watching movies, and over the
        lockdown I had the chance to rekindle my passion for the visual art. I believe this
        project is feasible because of the wide availability of data online. Most of this 
        data is available in a fragmented form, and I believe through this project I will be
        able to leverage the database management skills taught in this course to tabulate
        the data in a user friendly manner.<br>

        An example of the kind of interesting questions that I believe can be answered in
        this project:<br>
        1) How often do academy award winners work with each other (Do they work with each 
        other more often than they work with other artists, thus increasing their chances 
        to win more awards in the future?)<br>
        2) Has the longevity of actors increased in the last few decades? (based solely on 
        awards data, can we say anything about the career spans of actors?)<br>
        3) Does having a lot of award nominations translate to good box office revenue?<br><br>

        The user will be able to interact with the tables using a UI that I will build using django
        framework. The user will be able to see interesting data points and graphs related to the actors 
        and upon request can be shown the relationship between different tables. They will be able to
        gather and accumulate all data relating to their favorite movies, actors, and production houses 
        in one database.<br><br>
        <a href = '/'> Go back to home Page </a>"""
    
    return html

"""
Function Name:

Data ('/Data')
--------------------
Operation:

Contains the names of all the tables contained in the database.
Contains hyperlink to the home page.
--------------------
return:

html: html content of the page
"""
@route('/Data')
def Data():
    print("Schema overview")
    html = """ <h1> Data page </h1> <p> This page contains data about the database </p>
        <br><br> Table names: <br><br>

        Tables: <br><br>
       "ACTOR" <br>
       "BOXOFFICE"<br>
       "MOVIE"<br>
       "REVIEW"<br>
       "GENRE"<br>
       "PRODUCER"<br>
       "NOMINATION"<br>
       "TECHNICAL_TEAM"<br>
       "MOVIE_NOMINATION_BRIDGE"<br>
       "ACTOR_MOVIE_BRIDGE"<br>
       "ACTOR_NOMINATION_BRIDGE"<br>
       "PRODUCER_MOVIE_BRIDGE"<br>
       "GENRE_MOVIE_BRIDGE"<br>
       "MOVIE_TECHNICAL_TEAM_BRIDGE"<br><br>
        <a href = '/'> Go back to home Page </a>"""
    return html

"""
Function Name:

Credits ('/Credits')
--------------------
Operation:

Contains the Credits section of the project.
Contains hyperlink to the home page.
--------------------
return:

html: html content of the page
"""
@route('/Credits')
def Credits():
    print("Credits: Project by Shrikanth Subramanian for MPCS 53001")
    html = """ <h1> Project by Shrikanth Subramanian for MPCS 53001 </h1><br>
        I hope you enjoy it. <br>
        <a href = '/'> Go back to home Page </a>"""

    return html

"""
Function Name:

view ('/view')
--------------------
Operation:

Contains the sample database queries.
Contains hyperlink to the home page.
--------------------
Variables:

conn : Database connection objects

c : cursor of db connection object

result: Result of all the sql queries
--------------------
return:

html: html content of the page
"""
@route('/view')
def view():
    conn = sqlite3.connect('academy.db')
    c = conn.cursor()
    print("Viewing sample data")
    html = " <h1> Sample data </h1><br><br>"
    c.execute("SELECT * FROM MOVIE ORDER BY MovieID ASC LIMIT 10")
    result = c.fetchall()
    print(result, "\n")
    html += "<h2> Command: <br>SELECT * FROM MOVIE ORDER BY MovieID ASC LIMIT 10 </h2><br><br>"
    for row in result:
        html += "<b>"+ "".join(str(row)) +"<br></b>\n" 
    html += "<br><br> <a href = '/'> Go back to home Page </a>"
    c.execute("""SELECT PRODUCER.Name, sum(BOXOFFICE.Budget) FROM PRODUCER, MOVIE, 
    PRODUCER_MOVIE_BRIDGE, BOXOFFICE WHERE PRODUCER.Prod_ID = PRODUCER_MOVIE_BRIDGE.Prod_ID 
    and PRODUCER_MOVIE_BRIDGE.MovieID = MOVIE.MovieID AND BOXOFFICE.CertificateNo = 
    MOVIE.Box_office_no GROUP BY PRODUCER.Prod_ID ORDER BY sum(BOXOFFICE.Budget) 
    DESC LIMIT 5;""")
    result = c.fetchall()
    print(result, "\n")
    html += """<br><br><h2> Command: <br>SELECT PRODUCER.Name, sum(BOXOFFICE.Budget) FROM PRODUCER, MOVIE, 
    PRODUCER_MOVIE_BRIDGE, BOXOFFICE <br> WHERE PRODUCER.Prod_ID = PRODUCER_MOVIE_BRIDGE.Prod_ID 
    and PRODUCER_MOVIE_BRIDGE.MovieID = MOVIE.MovieID AND BOXOFFICE.CertificateNo = 
    MOVIE.Box_office_no <br> GROUP BY PRODUCER.Prod_ID ORDER BY sum(BOXOFFICE.Budget) 
    DESC LIMIT 5; </h2><br><br>"""
    for row in result:
        html += "<b>"+ "".join(str(row)) +"<br></b>\n" 
    html += "<br><br> <a href = '/'> Go back to home Page </a>"
    c.close()
    print(html)
    return html

#run object
run(host='127.0.0.1', port=8080)