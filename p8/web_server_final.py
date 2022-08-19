
#Imports required : sqlite3, bottle
import sqlite3
from bottle import route, run, template, post, get, request
import os.path
import re
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "academy.db")
con = sqlite3.connect(db_path)
cur = con.cursor()
global numbers


#Establishing connection with the database
#conn = sqlite3.connect('academy.db')
#c = conn.cursor()
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
    <a href = '/proj8'> Go to Project 8 full DB page </a><br> 
    <a href = '/search'> Go to Project 8 search </a><br> 
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

    print("Viewing sample data")
    html = " <h1> Sample data </h1><br><br>"
    cur.execute("SELECT * FROM MOVIE ORDER BY MovieID ASC LIMIT 20")
    result = cur.fetchall()
    print(result, "\n")
    html += "<h2> Command: <br>SELECT * FROM MOVIE ORDER BY MovieID ASC LIMIT 10 </h2><br><br>"
    for row in result:
        html += "<b>"+ "".join(str(row)) +"<br></b>\n" 
    html += "<br><br> <a href = '/'> Go back to home Page </a>"
    cur.execute("""SELECT * FROM ACTOR ORDER BY ActorID ASC LIMIT 20;""")
    result = cur.fetchall()
    print(result, "\n")
    html += """<br><br><h2> Command: <br>SELECT * FROM ACTOR ORDER BY MovieID ASC LIMIT 20; </h2><br><br>"""
    for row in result:
        html += "<b>"+ "".join(str(row)) +"<br></b>\n" 
    html += "<br><br> <a href = '/'> Go back to home Page </a>"
    print(html)
    return html


numbers = [3001,3002,3003,3004,3005,3006,3007,3008,3009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020]




@post('/insert')
def insert():
    actorid = request.forms.get('actorid')
    name = request.forms.get('name')
    no_of_awards = request.forms.get('no_of_awards')
    date = request.forms.get('DOB')
    if actorid.isdigit() == False or int(actorid) <1:
        return str(actorid) + " is not a number. </br>Please provide a unique number as Actor ID.  </br>Return to update <a href = \"/proj8\">page</a>"
    if int(actorid) in numbers:
        return str(actorid) + " is not a unique number. </br>Please provide a unique number as Actor ID.  </br>Return to update <a href = \"/proj8\">page</a>"
    
    numbers.append(int(actorid))

    actorid = int(actorid)
    if no_of_awards != "":
        if no_of_awards.isdigit() == False or int(no_of_awards) <0:
            return str(no_of_awards) + " is not an acceptable format for number of awards. </br>The input should have been an integer greater than 0. </br>Return to update page <a href = \"/proj8\">page</a>"

    if name.replace(" ", "").isalpha() == False and name != "":
        return str(name) + " is not a string of an acceptable format </br> Return to update page <a href = \"/proj8\">page</a>"
    if no_of_awards != "":
        if no_of_awards.isdigit() == False or int(no_of_awards) <0:
            return str(no_of_awards) + " is not an acceptable format for number of awards. </br>The input should have been an integer greater than 0. </br>Return to update page <a href = \"/proj8\">page</a>"
    
    if date.replace("/","").isdigit() == False:
        return str(date) + " is not an acceptable format DOB. </br>The input should be of the form MM/DD/YYYY </br>Return to update page <a href = \"/proj8\">page</a>"
    date1 = str(date).split("/")
    #print(date)
    newdate = date1[1] + "/" + date1[0] + "/" + date1[2]  
    #print(newdate)

    pattern = r"^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|19[0-9][0-9])$|^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$"

    if re.fullmatch(pattern, newdate) == False:
        return str(date) + " is not an acceptable format DOB. </br>The input should be of the form MM/DD/YYYY </br>Return to update page <a href = \"/\">page</a>"

    
    cur.execute("insert into actor values ({0}, '{1}', {2}, '{3}');".format(int(actorid), name, int(no_of_awards), date))
    con.commit()
    return str(name) +  " inserted </br> return to main <a href = \"/proj8\">page</a>"

@route('/delete/<actorid>')
def delete(actorid):
    cur.execute("delete from actor where actorid = "+ actorid)
    con.commit()
    return "Actor with ActorID:" +str(actorid) + " has been deleted </br> return to main <a href = \"/proj8\">page</a>"
#int(no_of_awards) <0
@post('/update/<actorid>')
def update(actorid):
    name = request.forms.get('name')
    no_of_awards = request.forms.get('no_of_awards')
    #no_of_awards = int(no_of_awards)

    if name.replace(" ", "").isalpha() == False and name != "":
        return str(name) + " is not a string of an acceptable format </br> Return to update page <a href = \"/view/{}\">page</a>".format(str(actorid))
    if no_of_awards != "":
        if no_of_awards.isdigit() == False or int(no_of_awards) <0:
            return str(no_of_awards) + " is not an acceptable format for number of awards. </br>The input should have been an integer greater than 0. </br>Return to update page <a href = \"/view/{}\">page</a>".format(str(actorid))
    if name != "" and no_of_awards == "":
        cur.execute("Update actor set name ='" + str(name) +"' where actorid = " + actorid)
    if name == "" and no_of_awards != "":
        cur.execute("Update actor set no_of_awards = "+no_of_awards+" where actorid = " + actorid)
    if name != "" and no_of_awards != "":
        cur.execute("Update actor set name ='" + str(name) +"', no_of_awards = "+no_of_awards+" where actorid = " + actorid)
    con.commit()
    return "Actor with ActorID:"+str(actorid) + "has been updated </br> return to main <a href = \"/proj8\">page</a>"
    #return name + " Updated </br> return to main <a href = \"/\">page</a>"

@route('/view/<actorid>')
def view(actorid):
    html = "<h2> Selected Actor</h2> <br /> <table>"
    for row in cur.execute("select * from actor where actorid =" + actorid):
        html += "<tr>"
        for cell in row:
            html += "<td>" + str(cell) + "</td>"      
    html += "</table>"

    html += "<br /><br /><br /><br /><br />"
    formname = "/update/" + str(actorid)
    html += '''
        <form action = '{0}' method = "post">
            Name: <input name = "name" type="text" >
            No of awards: <input name = "no_of_awards" type="integer" >
            <input value = "Update!" type = "submit" />        
        </form>'''.format(formname)
    html += " No updates, please return to main <a href = \"/proj8\">page</a>"
    return html
    #<input type="hidden" id="actorid" name="actorid" value= {code1}>
    #<input type="hidden" name="name" value= '<?=$name?>'>
@route('/search')
def search():
    html = "Search <br>"
    html += '''
        <form action = "/searchresults" method = "post">
            Like search for Actor Name: <input name = "likesearch" type="text" />
            No_of_awards: <input name = "no_of_awards" type="integer" />
            <input value = "Search!" type = "submit" />
        </form>
    '''
    html += " No searches, please return to Full database view <a href = \"/proj8\">page</a>"
    return html

@post('/searchresults')
def searchresults():
    html = "Search results <br></br>"
    likesearch = request.forms.get('likesearch')
    no_of_awards = request.forms.get('no_of_awards')
    if likesearch != "" and no_of_awards != "":
        for row in cur.execute("Select * from actor where name like '%" +likesearch +"%' and no_of_awards = "+no_of_awards):
            html += "<table>"
            html += "<tr>"
            for cell in row:
                html += "<td>" + str(cell) + "</td> <br>"
            html += "</table>"
        for row in cur.execute("Select Count(*) from actor where name like '%" +likesearch +"%' and no_of_awards = "+no_of_awards):
            if row[0] == 0:
                html += "No results were returned. Search failed."
    elif likesearch != "" and no_of_awards == "":
        for row in cur.execute("Select * from actor where name like '%" +likesearch +"%'"):
            html += "<tr>"
            for cell in row:
                html += "<td>" + str(cell) + "</td>"
        for row in cur.execute("Select Count(*) from actor where name like '%" +likesearch +"%'"):
            if row[0] == 0:
                html += "No results were returned. Search failed."
    elif likesearch == "" and no_of_awards != "":
        for row in cur.execute("Select * from actor where no_of_awards = "+no_of_awards):
            html += "<table>"
            html += "<tr>"
            for cell in row:
                html += "<td>" + str(cell) + "</td>"
            html += "</table>"
        for row in cur.execute("Select Count(*) from actor where no_of_awards = "+no_of_awards):
            if row[0] == 0:
                html += "No results were returned. Search failed. <br>"
    
    html += "</br> Results shared, please return to Full database view <a href = \"/proj8\">page</a>"
    return html

    

@route('/proj8')
def hello():
    html = "<h2> Actors</h2> <br /> <table>"
    html += "Create a new actor to the database: <a href = '/insertrow'> Insert  </a> "
    for row in cur.execute('select ActorID, name, no_of_awards from actor ORDER BY actorid ASC LIMIT 20'):
        html += "<tr>"
        for cell in row:
            html += "<td>" + "&nbsp;"+ str(cell) + "&nbsp;"+ "</td>"
        html += "<td><a href=\"/delete/" + str(row[0]) + "\">delete</a>   </td> "
        html += "<td><a href=\"/view/" + str(row[0]) + "\">view/update</a>   </td> "
        html += "<td><a href=\"/relationY/" + str(row[0]) + "/"+str(row[2]) +"\">Related Column</a>   </td>  </tr>"

    html += "</table>"

    html += "<br /><br /><br /><br /><br />"
    return html

@route('/unlink/<actorid>/<movieid>/<no_of_awards>')
def unlink(actorid, movieid, no_of_awards):
    cur.execute("delete from actor_movie_bridge where actorid = " + actorid+ " and movieid ="+ movieid)
    if int(no_of_awards) > 0:
        cur.execute(" UPDATE actor SET no_of_awards = no_of_awards - 1 where actorid ="+actorid)
    con.commit()
    return "Actor with ActorID:"+str(actorid) + " Unlinked </br> return to main <a href = \"/proj8\">page</a>"

@route('/link/<actorid>/<movieid>/<no_of_awards>')
def link(actorid, movieid, no_of_awards):
    cur.execute("insert into actor_movie_bridge values("+str(actorid)+", "+str(movieid)+")")
    cur.execute("UPDATE actor SET no_of_awards = no_of_awards + 1 where actorid ="+actorid)
    con.commit()
    return "Actor with ActorID:"+str(actorid) + " " + str(movieid) + "linked </br> return to main <a href = \"/proj8\">page</a>"

@route('/relationY/<actorid>/<no_of_awards>')
def relationY(actorid, no_of_awards):
    html = "<h2> Related Movies for actor chosen</h2> <br /> <table>"
    for row in cur.execute('''select movie.MovieID, movie.name, movie.year from movie inner join
    actor_movie_bridge on movie.movieID = actor_movie_bridge.movieID inner join actor on
    actor.actorid = actor_movie_bridge.actorid where actor.actorid ='''+ actorid +''' ORDER BY movie.movieid ASC LIMIT 20'''):
        html += "<tr>"
        for cell in row:
            html += "<td>" + str(cell) + "</td>"
        html += "<td><a href=/unlink/{0}/{1}/{2}>Unlink</a>   </td> ".format(actorid, row[0], no_of_awards)
    html += "</table>"
    html += "<br /><br /><br /><br /><br />"

    html += "<h2> Unrelated Movies for actor chosen</h2> <br /> <table>"
    for row in cur.execute('''select DISTINCT movie.MovieID, movie.name, movie.year from movie inner join
    actor_movie_bridge on movie.movieID = actor_movie_bridge.movieID inner join actor on
    actor.actorid = actor_movie_bridge.actorid where actor.actorid !='''+ actorid +''' ORDER BY movie.movieid ASC LIMIT 20'''):
        html += "<tr>"
        for cell in row:
            html += "<td>" + str(cell) + "</td>"
        html += "<td><a href=/link/{0}/{1}/{2}>link</a>   </td> ".format(actorid, row[0], no_of_awards)
    html += "</table>"
    html += "<br /><br /><br /><br /><br />"

    html += "Add a new movie for this actor:"
    html += '''
        <form action = "/insertrelationY/{0}/{1}" method = "post">
            Movie Name: <input name = "name" type="text" />
            Year: <input name = "year" type="integer" />
            <input value = "Insert Movie!" type = "submit" />
        </form>
    '''.format(actorid, no_of_awards)
    html += " No changes, please return to main <a href = \"/proj8\">page</a>"
    return html


    
@post('/insertrelationY/<actorid>/<no_of_awards>')
def insertrelationY(actorid, no_of_awards):
    movieid = random.randint(1,10000)
    name = request.forms.get('name')
    year = request.forms.get('year')
    if name == "":
        return str(name) + " is not a string of an acceptable format </br> Return to update page <a href = \"/relationY/{}/{}\">page</a>".format(actorid,no_of_awards)
    if int(year) > 2022 or int(year) < 1900:
        return str(year) + " is not an acceptable year. We can't record movies from the future. </br> Return to update page <a href = \"/relationY/{}/{}\">page</a>".format(actorid,no_of_awards)
    cur.execute("insert into movie values ({0}, '{1}', {2}, {3}, {4}, {5});".format(int(movieid), name, int(year), random.randint(1, 7), random.randint(347222, 92898282),random.randint(347222, 92898282)))
    cur.execute("insert into actor_movie_bridge values("+str(actorid)+", "+str(movieid)+")")
    cur.execute("UPDATE actor SET no_of_awards = no_of_awards + 1 where actorid ="+actorid)
    return "Actor with ActorID:"+str(actorid) + " and movie with movieid=  " + str(movieid) + " have been linked </br> return to main <a href = \"/proj8\">page</a>"
    


@route('/insertrow')
def insertrow():
    html = "Insert <br>"
    html += '''
        <form action = "/insert" method = "post">
            Actor ID: <input name = "actorid" type="integer" />
            Name: <input name = "name" type="text" />
            No_of_awards: <input name = "no_of_awards" type="integer" />
            DOB: (MM/DD/YYYY) <input name = "DOB" type="text" />
            <input value = "Insert!" type = "submit" />
        </form>
    '''
    html += " No changes, please return to main <a href = \"/proj8\">page</a>"
    return html

run(host='localhost', port=8080, debug = True)

