from bs4 import BeautifulSoup
import requests
from app.models import db
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
from app.models.ships import Ships
from util import parent_child_parser, species_dictionary

def ship_name_scraper(parser):
    try:
        name = parser.find('span', class_='mw-page-title-main').text
        return name
    except:
        pass

def ship_type_scraper(parser):
    return parent_child_parser(parser, "Type of Ship")
    # type_finder = parser.find('h3', string='Type of Ship')
    # type_ = type_finder.parent.find('div')
    # return type_.text
def ship_status_scraper(parser):
    return parent_child_parser(parser, "Status")
    # status_finder = parser.find('h3', string='Status')
    # status_ = status_finder.parent.find('div')
    # return status_.text
def ship_species_scraper(parser):
    species = parent_child_parser(parser, "Species" )
    species_id = species_dictionary.get(species, 15)
    return species_id


    
# def data_error_wrapper()

def add_to_db(ships_dict):
    for ship, info in ships_dict.items():
        with Session(db.engine) as session:
            with session.begin():
                query = select(Ships).filter(Ships.ship_id == info['ship_id'])
                result = session.execute(query).scalars().first()
                print(ship, result)

                # If result is None, so if there is no result with that id present.
                if result == None:
                    # ship_id, ship_name, ship_type, status, species_id
                    new_ship = Ships(
                        ship_id = info['ship_id'],
                        ship_name=info['ship_name'],
                        ship_type=info['ship_type'],
                        status=info['status'],
                        species_id=info['species_id']
                    )
                    print(new_ship)

                    session.add(new_ship)
                    session.commit()
                    session.close()
                else:
                    ship = result
                    for field, value in info.items():
                        setattr(ship, field, value)
                    session.commit()

def ship_scraper():
    ships = ['/wiki/The_Flying_Dutchman', '/wiki/The_Flying_Dutchman#Version_2.0', '/wiki/The_Flying_Dutchman#Version_3.0', '/wiki/The_Flying_Dutchman#Version_4.0']
    ships_dict = {}

    html_content = requests.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Category:Ships')
    soup = BeautifulSoup(html_content.text, 'html.parser')
    ship_content_container = soup.find('div', class_='category-page__members')

    nested_ships = ship_content_container.find_all('a', class_='category-page__member-link')

    for ship in nested_ships:
        ships.append(ship.get('href'))
    print(ships)

    id = 1

    for ship in ships:
        specific_ship_request = requests.get(f'https://expeditionary-force-by-craig-alanson.fandom.com{ship}')
        print(ship)
        if specific_ship_request.status_code == 200:
            print('Connected successfully')
        else: 
            print(f"Error with {ship} page being parsed.")
            return f"Error with {ship} page being parsed."
        
        if ship == '/wiki/Spacecraft':
            continue
        
        
        # Setting up the Soup and grabbing the info
        ship_soup = BeautifulSoup(specific_ship_request.text, 'html.parser')
        ship_id = id
        ship_name = ship_name_scraper(ship_soup)
        ship_type = ship_type_scraper(ship_soup)
        status = ship_status_scraper(ship_soup)
        species = ship_species_scraper(ship_soup)

        # Storing the info inside of a dictionary
        ships_dict[ship_name] = {
            'ship_id': ship_id,
            'ship_name': ship_name,
            'ship_type': ship_type,
            'status': status, 
            'species_id': species
        }
        if species == "No Data":
            species == 15
        print(f"Ship name: {ship_name}, Type: {ship_type}, Status: {status}, Species: {species}, Ship_id: {ship_id}")

        id += 1
    add_to_db(ships_dict)



