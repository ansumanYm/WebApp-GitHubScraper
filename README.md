# WebApp-GitHubScraper
Developed a Web-App using Streamlit and BeautifulSoup that can scrap GitHub and Display the Top Repositories in each Topic.

![image](https://user-images.githubusercontent.com/96365389/167301961-c08dd5cf-1f55-4711-ba6b-1505e192c21d.png)

## Scraping GitHub Topics page.
We will scrape the Github topic page to collect the names of the Top Topic titles, their description and their url.
To do this:
- We will use requests library to collect the html file for the topic page.
- We will then create a soup using BeautifulSoup which will have all the html tags present in it.
- Right click on any of the topic title and select inspect.
![image](https://user-images.githubusercontent.com/96365389/167302313-ecbe1bf6-eb8c-4308-b19e-7da9fd0ed8ea.png)
- We will note the tag and the class in which the title of the topic is present. This tag and class will be same for every topic.
- We will then provide this tag to bs4 and find_all('p') tags which we require.
- We will do this similar steps to collect the description and url.
- We will then put all these info into a pandas dataframe.
![image](https://user-images.githubusercontent.com/96365389/167302979-73f0255a-5bfa-4e3e-89f1-12db8e8a8fea.png)
- Then we will define some functions that can do all the above steps automatically.
- We will define another set of functions that can find out info(username, repo_name, starts, url) about the top Repositories in any topics.

## Developing a WebApp.
We will develop a web app using Streamlit, which will allow us to select a Topic for which it will provide us information of the Top Repositories.
![image](https://user-images.githubusercontent.com/96365389/167303242-c53c5a09-004a-4f7e-8a9f-6bf98269e8ac.png)
![image](https://user-images.githubusercontent.com/96365389/167303265-c04022ef-2540-458c-b98c-216613419364.png)

Note:- To Run this web app, please download main.py file and run it in the terminal by using the command, streamlit run main.py.


