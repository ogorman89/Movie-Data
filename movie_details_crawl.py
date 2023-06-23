import requests
import csv
from bs4 import BeautifulSoup

#IMDB seems to be blocking get request that originate from python
#Set headers to look like a user-Agent
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

file = open('box_office.csv')
movies = list(csv.reader(file))

#print(data)
baseUrl = "https://www.imdb.com/title/"

#loop over movies using id to crawl their rating
# for movie in movies:
# url = baseUrl + movies[0]
url = 'https://www.imdb.com/title/'+ str(movies[0][0]) #this is for testing only

page = requests.get(url,headers=HEADERS)
soup = BeautifulSoup(page.content, "html.parser")

#find the span element that holds the rating
rating = soup.find("span", class_='sc-bde20123-1 iZlgcd').text
# movie.append(rating)
print(rating)



        