from bs4 import BeautifulSoup
import requests
from util import parent_child_parser
# from database import db
# from sqlalchemy.orm import Session
# from sqlalchemy import select
# from datetime import datetime
# from models.planets import Planets
# from util import parent_child_parser

def character_name_scraper(parser):
    f_name = parent_child_parser(parser, "First Name")
    l_name = parent_child_parser(parser, "Last Name")
    return f"{f_name} {l_name}"
def character_description_scraper(parser):
    parent = parser.find("td", class_="gradient")
    descriptions = [child for child in parent.children if child.name == 'p']
    descriptions.pop(0)
    text_holder = []
    for description in descriptions:
        text_holder.append(description.text.strip())
    # print(" ".join(text_holder))
    return " ".join(text_holder)

def character_status_scraper(parser):
    return parent_child_parser(parser, "Status")

def character_last_known_location_scraper(parser):
    return parent_child_parser(parser, "Last Known Location")

def character_sex_scraper(parser):
    return parent_child_parser(parser, "Sex")

def character_first_appearance_scraper(parser):
    return parent_child_parser(parser, "First Appearance")

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
    for name in raw_names:
        if name.find('a'):
            characters.append(name.find('a').get('href'))
    
    excluded_names = ('#The_Merry_Band_of_Pirates', '/wiki/The_Mavericks_(group)', '/wiki/Humans', '/wiki/Earth', '/wiki/UNEF', '/wiki/Alien_Legion', '/wiki/Keepers_of_the_Faith', 
                      '/wiki/Verd-kris', '/wiki/Jeraptha', '/wiki/Maxolhx', '/wiki/Bosphuraq', '/wiki/Rindhalu', '/wiki/Thuranin', '/wiki/Wurgalan')
    
    for character in characters:
        if character not in excluded_names:
            character_page = requests.get(f'https://expeditionary-force-by-craig-alanson.fandom.com{character}')
            if character_page.status_code == 200:
                character_soup = BeautifulSoup(character_page.text, 'html.parser')
                name = character_name_scraper(character_soup)
                
                print(name)
                character_dict[name] = {
                    'name': name,
                    'description': character_description_scraper(character_soup),
                    'status': character_status_scraper(character_soup),
                    'last_known_location': character_last_known_location_scraper(character_soup),
                    'sex': character_sex_scraper(character_soup),
                    'first_appearance': character_first_appearance_scraper(character_soup)
                }
                print(character_dict[name])
                break
            else:
                print("Connection was unsuccessful")

character_scraper()


    