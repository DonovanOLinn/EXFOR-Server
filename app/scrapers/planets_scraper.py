from bs4 import BeautifulSoup
import requests
from app.models import db
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
from app.models.planets import Planets
from util import parent_child_parser
# planet_id planet_name planet_nickname

def parent_child_parser(parser, string_to_find, attribute_to_find='h3'):
    try:

        finder = parser.find(attribute_to_find, string=string_to_find)
        found = finder.parent.find("a")
        if not found:
            found = finder.parent.find("div")
        return found.text
    except:
        return "No Data"

def planet_name_scraper(parser):
    try:
        name = parser.find('span', class_='mw-page-title-main').text
        return name
    except:
        # TODO BUILD OUT THIS EXCEPT BLOCK TO RETURN A NAME
        pass

def planet_nickname_scraper(parser):
    return parent_child_parser(parser, "Nickname")

def add_to_db(planet_dict):
    for planet, info in planet_dict.items():
        with Session(db.engine) as session:
            with session.begin():
                query = select(Planets).filter(Planets.planet_id == info['planet_id'])
                result = session.execute(query).scalars().first()
                print(planet, result)

                # If result is None, so if there is no result with that id present.
                if result == None:
                    # planet_id, ship_name, ship_type, status, species_id
                    new_planet = Planets(
                        planet_id = info['planet_id'],
                        planet_name=info['planet_name'],
                        planet_nickname=info['planet_nickname']
                    )
                    print(new_planet)

                    session.add(new_planet)
                    session.commit()
                    session.close()
                else:
                    planet = result
                    for field, value in info.items():
                        setattr(planet, field, value)
                    session.commit()

def planet_scraper():
    planets = []
    planets_dict = {}
    id = 1

    planets_page = requests.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Category:Planets')
    if planets_page.status_code != 200:
        return 'Error with parsing page'
    soup = BeautifulSoup(planets_page.text, 'html.parser')
    planet_page_list = soup.find_all('a', class_='category-page__member-link')
    for planet in planet_page_list:
        if planet.get('href') == '/wiki/Planets_/_Space' or planet.get('href') == '/wiki/Sculptor_Dwarf_Galaxy':
            continue
        planets.append(planet.get('href'))
    
    print(planets)

    for planet in planets:
        planet_info = requests.get(f'https://expeditionary-force-by-craig-alanson.fandom.com{planet}')
        if planet_info.status_code == 200:
            print("Connection Successful")
        else:
            print(f"Error with connection to {planet}")
            continue

        planet_soup = BeautifulSoup(planet_info.text, 'html.parser')

        planet_name = planet_name_scraper(planet_soup)
        planet_nickname = planet_nickname_scraper(planet_soup)
        planet_id = id
        print(planet_name, planet_nickname if planet_nickname != 'No Data' else planet_name, planet_id)
        id += 1

        planets_dict[planet_name] = {
            'planet_name' : planet_name,
            # TODO: planet_nickname is returning None. Might need to manually enter information on original name or find another source.
            'planet_nickname' : planet_nickname if planet_nickname != 'No Data' else planet_name,
            'planet_id' : planet_id
        }
    
    add_to_db(planets_dict)



# planet_scraper()