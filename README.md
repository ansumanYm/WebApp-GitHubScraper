# WebApp-GitHubScraper
Developed a Web-App using Streamlit and BeautifulSoup that can scrap GitHub and Display the Top Repositories in each Topic.

![image](https://user-images.githubusercontent.com/96365389/167301961-c08dd5cf-1f55-4711-ba6b-1505e192c21d.png)

## Scraping GitHub Topics page.
We will scrape the Github topic page to collect the names of the Top Topic titles, their description and their url.
To do this:
- We will use requests library to collect the html file for the topic page.
- We will then create a soup using BeautifulSoup which will have all the html tags present in it.
- Right click on any of the topic title and select inspect.
- ![image](https://user-images.githubusercontent.com/96365389/167302313-ecbe1bf6-eb8c-4308-b19e-7da9fd0ed8ea.png)
- We will note the tag and the class in which the title of the topic is present. This tag and class will be same for every topic.
- 
