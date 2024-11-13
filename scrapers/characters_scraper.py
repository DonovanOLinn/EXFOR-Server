from bs4 import BeautifulSoup
import requests
# from database import db
# from sqlalchemy.orm import Session
# from sqlalchemy import select
# from datetime import datetime
# from models.planets import Planets
# from util import parent_child_parser

def character_name_scraper():
    pass
def character_description_scraper():
    pass
def character_status_scraper():
    pass
def character_last_known_location_scraper():
    pass
def character_sex_scraper():
    pass
def character_first_appearance_scraper():
    pass
def add_to_db(character_dict):
    pass
def character_scraper():
    characters = []
    character_dict = {}

    characters_page = requests.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Notable_Characters')
    if characters_page.status_code == 200:
        result = characters_page.text
    else:
        print("Connection was unsuccessful")
        
    soup = BeautifulSoup(result, 'html.parser')
    print("Before raw names")
    raw_names = soup.find_all('td')
    print(raw_names)

character_scraper()


    