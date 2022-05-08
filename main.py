import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import requests

# Streamlit in display texts.
st.title('GitHub WebScraper')
st.write('This is a Webapp build using **Streamlit**.')
st.write('You can use this app to Find info about the **Top Repositories** present in **GitHub**.')
st.write('')

st.header('Select a GitHub Topic:')

# Read CSV which
df = pd.read_csv('Topic_info.csv')

# Streamlit selectbox command.
topic_selected = st.selectbox('From the First 30 Topics:',
     df.title.values)

st.write('You selected:', topic_selected)

# Functions:
# You can find more details about these functions by visiting the ipynb file.

base_url = 'https://github.com'
def star_count(stars_str):
    stars_str = stars_str.strip()
    if stars_str[-1] == 'k':
        return int(float(stars_str[:-1]) * 1000)
    return int(stars_str)

def get_topic_page(topic_url):
     # Download the page
     pg_url = requests.get(topic_url)
     # Check successful response
     if pg_url.status_code != 200:
          raise Exception('Failed to load page {}'.format(topic_url))
     # Parse using Beautiful soup
     soup3 = BeautifulSoup(pg_url.text, 'html.parser')
     return soup3


def get_repo_info(repo_tags, star_tag):
     # returns all the required info about a repository
     a_tags = repo_tags.find_all('a')
     username = a_tags[0].text.strip()
     repo_name = a_tags[1].text.strip()
     repo_url = base_url + a_tags[1]['href']
     stars = star_count(star_tag.text.strip())
     return username, repo_name, stars, repo_url


def get_topic_repos(soup3):
     # Get the h3 tags containing repo title, repo URL and username
     h3_selection_class = 'f3 color-fg-muted text-normal lh-condensed'
     repo_tags = soup3.find_all('h3', class_=h3_selection_class)
     # Get star tags
     star_tags = soup3.find_all('span', class_='Counter js-social-count')

     topic_repos_dict = {'username': [], 'repo_name': [], 'stars': [], 'repo_url': []}

     # Get repo info
     for i in range(len(repo_tags)):
          repo_info = get_repo_info(repo_tags[i], star_tags[i])
          topic_repos_dict['username'].append(repo_info[0])
          topic_repos_dict['repo_name'].append(repo_info[1])
          topic_repos_dict['stars'].append(repo_info[2])
          topic_repos_dict['repo_url'].append(repo_info[3])

     return pd.DataFrame(topic_repos_dict)


topic_arr = df.loc[df['title'] == topic_selected].url.values

st.write('View Top Repositories in Topic: ', topic_selected, '?')
if st.button('View:'):
     st.write(get_topic_repos(get_topic_page(topic_arr[0])))
