import requests
import csv
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
    

#IMDB seems to be blocking get request that originate from python
#Set headers to look like a user
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

file = open('box_office.csv')
movies = list(csv.reader(file))

#print(data)
baseUrl = "https://www.imdb.com/title/"

#loop over movies using id to crawl their rating
# for movie in movies:
# url = baseUrl + movies[0]
url = 'https://www.imdb.com/title/'+ str(movies[0][0]) #this is for testing only

# page = requests.get(url,headers=HEADERS)
# soup = BeautifulSoup(page.content, "html.parser")

#get JSON soup for the movie
# jsonSoup = soup.find("script", type="application/ld+json").text
jsonSoup = {'@context': 'https://schema.org', '@type': 'Movie', 'url': 'https://www.imdb.com/title/tt0499549/', 'name': 'Avatar', 'image': 'https://m.media-amazon.com/images/M/MV5BZDA0OGQxNTItMDZkMC00N2UyLTg3MzMtYTJmNjg3Nzk5MzRiXkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg', 'description': 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.', 'review': {'@type': 'Review', 'itemReviewed': {'@type': 'Movie', 'url': 'https://www.imdb.com/title/tt0499549/'}, 'author': {'@type': 'Person', 'name': 'miruleyall'}, 'dateCreated': '2009-12-16', 'inLanguage': 'English', 'name': 'Visually Spellbinding!', 'reviewBody': 'I am sure my comment will be lost in a sea of blue but anyways here goes...\n\nJust attended the Advanced Screening at my local &quot;Event Cinema&quot; BCC in 3D\n\nNow this movies graphics are gorgeous, everything is so real, the 3D just adds to the effect beautifully without distracting you.\n\nFrom a technical standpoint this movie is amazing, just the detail on the Navi&apos;s faces are amazing, they feel more real then their real life counterparts!\n\nWithout giving anything away about the story, the plot itself is very solid, very character driven and perfectly executed by Jim, safe to say this is his best original story since &quot;The Terminator&quot; and &quot;Terminator 2&quot; and is definitely one of his best movies, so good it ties with T2 which is my most favorite movie of all time...\n\nSo for those of you who have not seen this yet... WHAT ARE YOU WAITING FOR?!\n\n5/5', 'reviewRating': {'@type': 'Rating', 'worstRating': 1, 'bestRating': 10, 'ratingValue': 8}}, 'aggregateRating': {'@type': 'AggregateRating', 'ratingCount': 1347050, 'bestRating': 10, 'worstRating': 1, 'ratingValue': 7.9}, 'contentRating': 'PG-13', 'genre': ['Action', 'Adventure', 'Fantasy'], 'datePublished': '2009-12-18', 'keywords': 'paraplegic,spiritualism,marine,future,forest protection', 'trailer': {'@type': 'VideoObject', 'name': 'Avatar: Trailer #2 ', 'embedUrl': 'https://www.imdb.com/video/imdb/vi531039513', 'thumbnail': {'@type': 'ImageObject', 'contentUrl': 'https://m.media-amazon.com/images/M/MV5BMjM2OTkyNTY3N15BMl5BanBnXkFtZTgwNzgzNDc2NjE@._V1_.jpg'}, 'thumbnailUrl': 'https://m.media-amazon.com/images/M/MV5BMjM2OTkyNTY3N15BMl5BanBnXkFtZTgwNzgzNDc2NjE@._V1_.jpg', 'url': 'https://www.imdb.com/video/vi531039513/', 'description': 'Jake Sully (Worthington) is a paraplegic war veteran who is brought to the planet Pandora to participate in a program designed to help him walk again. The program introduces him to his avatar, a creature whose genetics are half human and half Na&apos;vi, a sentient humanoid race who inhabit Pandora. In time, Jake will find himself in the middle of an escalating conflict between the two races.', 'duration': 'PT3M36S', 'uploadDate': '2009-10-31T11:31:45Z'}, 'actor': [{'@type': 'Person', 'url': 'https://www.imdb.com/name/nm0941777/', 'name': 'Sam Worthington'}, {'@type': 'Person', 'url': 'https://www.imdb.com/name/nm0757855/', 'name': 'Zoe Saldana'}, {'@type': 'Person', 'url': 'https://www.imdb.com/name/nm0000244/', 'name': 'Sigourney Weaver'}], 'director': [{'@type': 'Person', 'url': 'https://www.imdb.com/name/nm0000116/', 'name': 'James Cameron'}], 'creator': [{'@type': 'Organization', 'url': 'https://www.imdb.com/company/co0000756/'}, {'@type': 'Organization', 'url': 'https://www.imdb.com/company/co0174373/'}, {'@type': 'Organization', 'url': 'https://www.imdb.com/company/co0038663/'}, {'@type': 'Person', 'url': 'https://www.imdb.com/name/nm0000116/', 'name': 'James Cameron'}], 'duration': 'PT2H42M'}
# movie.append(rating) 

genre = jsonSoup['genre']
cast = createList(jsonSoup['actor'],'name') #this is a list
castId = createList(jsonSoup['actor'],'url')
aggregateRating = jsonSoup["aggregateRating"]["ratingValue"]
description = jsonSoup["description"] 
numRatings = jsonSoup["aggregateRating"]["ratingCount"]
director = createList(jsonSoup['director'],'name') #this could be a list
duration = jsonSoup["duration"]
contentRating = jsonSoup["contentRating"]
datePublished = jsonSoup["datePublished"]
keywords = jsonSoup["keywords"].split(",") #this is a list

#create list of lists of people with id, name, appearance
people = []
for i in zip(cast,castId):
    people.append([i[1][-10:-1],i[0]]) 
aggregateRating = jsonSoup["aggregateRating"]["ratingValue"]
description = jsonSoup["description"] 
numRatings = jsonSoup["aggregateRating"]["ratingCount"]
director = createList(jsonSoup['director'],'name') #this could be a list
duration = jsonSoup["duration"]
contentRating = jsonSoup["contentRating"]
datePublished = jsonSoup["datePublished"]
keywords = jsonSoup["keywords"].split(",") #this is a list





# print(genre,people, aggregateRating, description, numRatings,director,duration, contentRating, datePublished, keywords
# )
print(people)



        