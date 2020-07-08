# Creating a Web Scrapper

import requests
from requests import get
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

headers = {"Accept-Language" : "en-US, en; q=0.5"}

url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"
results = requests.get(url,headers=headers)

soup = BeautifulSoup(results.text , "html.parser")

# print(soup.prettify())

# initializing empty list for storing data

titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div',class_='lister-item mode-advanced')

# for loop that loops through all the div container
for container in movie_div:

    name = container.h3.a.text
    titles.append(name)

    year = container.h3.find('span', class_='lister-item-year').text
    years.append(year)

    runtime = container.find('span',class_='runtime').text if container.p.find('span',class_='runtime') else '-'
    time.append(runtime)

    imdb = float(container.strong.text)
    imdb_ratings.append(imdb)

    m_score = container.find('span', class_='metascore').text if container.find('span',class_='metascore') else '-'
    metascores.append(m_score)

    nv = container.find_all('span',attrs ={'name': 'nv'})

    vote = nv[0].text
    votes.append(vote)

    grosses = nv[1].text if len(nv)>1 else '-'
    us_gross.append(grosses)


#print(titles)
#print(years)
#print(time)
#print(imdb_ratings)
#print(metascores)
#print(votes)
#print(us_gross)

movies = pd.DataFrame({'movie': titles,
                       'year': years,
                       'timeinMin': time,
                       'IMDB_R': imdb_ratings,
                       'Metascore': metascores,
                       'Votes': votes,
                       'US_GrossinMillions': us_gross})
#print(movies)

# Data Cleaning
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['timeinMin'] = movies['timeinMin'].str.extract('(\d+)').astype(int)
movies['Metascore'] = movies['Metascore'].astype(int)
movies['Votes'] = movies['Votes'].str.replace(',', '').astype(int)
movies['US_GrossinMillions'] = movies['US_GrossinMillions'].map(lambda x:x.lstrip('$').rstrip('M'))
movies['US_GrossinMillions'] = pd.to_numeric(movies['US_GrossinMillions'], errors='coerce')

#print(movies)
#print(movies.dtypes)

movies.to_csv('movies.csv')