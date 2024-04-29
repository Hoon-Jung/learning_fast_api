#1 use beautiful soup and find the href per name and then href of the school website
#2 Use selenium in order to scrape data about counsellors 

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from bs4 import BeautifulSoup
import requests

print("responding...")
# Fetch the webpage
url = 'https://www.usnews.com/education/best-high-schools/new-jersey/rankings'

response = requests.get(url, verify=True)
print("requesting url")
# Create a Beautiful Soup object
soup = BeautifulSoup(response.content, 'html.parser')
print("initialized beautifulsoup")
# Find all links and print them
ol_tag = soup.find('ol', class_='item-list__OrderedListStyled-sc-18yjqdy-0 kFQUBh')
print("found ol tag")
li_tags = ol_tag.find_all('li')
print("found li tag")
for li_tag in li_tags:
    section_tag = li_tag.find('section')
    div_tag = section_tag.find("div")
    headertwo_tag = div_tag.find("h2")
    a_tag = headertwo_tag.find("a")
    print(a_tag.get("href"))
    print(a_tag.text)

        

# DATABASE_URL = "mysql+pymysql://root:Drag oN #o@localhost/schoollist"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
