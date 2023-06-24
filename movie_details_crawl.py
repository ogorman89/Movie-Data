import requests
import csv
import json
import time
from bs4 import BeautifulSoup

#function defs
def createList(dict, key):
    '''
    Provided a dictionary object and a key
    Creates a list object of sub-elements
    '''
    subList = []
    for i in dict:
        subList.append(i[key])
    return subList

def addPerson(person,id,role):
    '''
    Provided a person, id and role adds them to the list of lists
    that will be used to create the 'people' table
    '''
    for i in zip(person,id):
        #parse the id from the url
        personId = i[1][-10:-1]
        name = i[0]
        people.append([personId,name,role,titleId])

def writeCsv(fname,list):
    '''
    Accepts filename and list name
    Loops over list and writes to csv
    '''
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in list:
            writer.writerow(i)
        f.close()

#define lists of lists for our tables
people = [['person_id','name','role','title_id']]
title_details = [['title_id', 'aggregate_rating', 'description', 'num_ratings', 
                      'duration', 'content_rating', 'date_published']]
keywords = [['title_id','keyword']]
genres = [['title_id','genre']]

#base url used by imdb
baseUrl = "https://www.imdb.com/title/"

#IMDB seems to block GET requests that have python headers
#Set headers to look like a user
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

#open our top 1000 movies csv and read it in
with open('box_office.csv',"r") as file:
    movies = list(csv.reader(file))[1:11]

    #loop over movies, get id slug and use it to scrape their detail page
    for movie in movies: #just doing first 5 for debugging
        url = baseUrl + movie[0]
        titleId = movie[0]
    # url = 'https://www.imdb.com/title/'+ str(movies[0][0]) #this is for testing only

        #request the page content for a given movie
        page = requests.get(url,headers=HEADERS)
        soup = BeautifulSoup(page.content, "html.parser")

        #get JSON soup for the movie
        jsonSoup = json.loads(soup.find("script", type="application/ld+json").text)

        #parse target variables using json as source dict
        #items for the 'title_details' table
        aggregateRating = jsonSoup["aggregateRating"]["ratingValue"]
        description = jsonSoup["description"]
        description = description.replace('"','') #some descriptions encased in quotation marks
        numRatings = jsonSoup["aggregateRating"]["ratingCount"]
        duration = jsonSoup["duration"]
        contentRating = jsonSoup["contentRating"]
        datePublished = jsonSoup["datePublished"]

        #convert duration string to minutes
        duration = duration.split('H')
        duration = int(duration[0].replace('PT',''))*60 + int(duration[1].replace('M',''))

        #items for the 'genres' table
        genre = jsonSoup['genre']
        for i in genre:
            genres.append([titleId, i])

        #append movie details to the movie_details list
        title_details.append([titleId, aggregateRating, description, numRatings, 
                            duration, contentRating, datePublished])

        #items for the 'keywords' table
        keywordItems = jsonSoup["keywords"].split(",") #this is a list
        for i in keywordItems:
            keywords.append([titleId, i])

        #parse people items for the 'people' table
        cast = createList(jsonSoup['actor'],'name') #this is a list
        castId = createList(jsonSoup['actor'],'url') #this is a list
        director = createList(jsonSoup['director'],'name') #this could be a list
        directorId = createList(jsonSoup['director'],'url') #this could be a list

        #add people items to the people list
        addPerson(cast,castId,'actor')
        addPerson(director,directorId,'director')
        
        #outputting a status to the terminal
        print('\r'+ str(round(movies.index(movie)/len(movies)*100)) + "% complete",end='')

        #10s time delay to avoid spamming request server
        time.sleep(10)

#write results to csv
writeCsv('people.csv',people)
writeCsv('keywords.csv',keywords)
writeCsv('movie_details.csv',title_details)
writeCsv('genres.csv',genres)