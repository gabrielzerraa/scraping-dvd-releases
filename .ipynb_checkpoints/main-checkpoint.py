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