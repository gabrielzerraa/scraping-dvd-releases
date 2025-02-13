# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# %%
url = 'https://www.dvdsreleasedates.com/releases/2024/1/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, features='html.parser')
print(soup)

# %%
# Todas as URLs
x = range(1, 13)
for i in x:
    print(f'https://www.dvdsreleasedates.com/releases/2024/{i}/')

# %% Título do Filme
titulo_filme = []
for i in soup.find_all('img', class_='movieimg'):
    titulo_filme.append(i['title'].replace('DVD Release Date', ' ').strip())
print(titulo_filme)

# %% Nota IMDB
nota_filme = []
for i in soup.find_all('td', class_='imdblink left'):
    nota_filme.append(i.a.text.strip())
print(nota_filme)

# %% Info do filme

# Links dos filmes
links_filmes = []
for i in soup.find_all('td', class_='dvdcell'):
    link = i.find('a')
    if link:
        links_filmes.append(link['href'])
for i in links_filmes:
    print(i)
    

# %%

url = 'https://www.dvdsreleasedates.com/movies/11177/the-holdovers'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, features='html.parser')
print(soup)

# %%
for i in soup.find_all('span',class_='medlargeboldtext'):
    print(i.text)

# %%

for i in soup.find_all('span', class_='medlargetext'):
    print(i.text)