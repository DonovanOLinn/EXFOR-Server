from bs4 import BeautifulSoup
import requests
from app.models import db
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
from app.models.species import Species
def species_apperance_(parser): 
    try: 
        species_finder = parser.find("h3",string="General Apperance" )
        species = species_finder.parent.find("a")
        if not species:
            species = species_finder.parent.find("div")
        return species.text
    except AttributeError as a:
        return f"Error fetching narrator {a}"

def species_patron(parser): 
    try: 
        patron_finder = parser.find("h3",string="Patron Species" )
        patron = patron_finder.parent.find("a")
        if not patron:
            patron = patron_finder.parent.find("div")
        return patron.text
    except AttributeError as a:
        return f"Error fetching narrator {a}"

def species_tech_level(parser): 
    try: 
        tech_level_finder = parser.find("h3",string="Tech Level" )
        tech_level = tech_level_finder.parent.find("a")
        if not tech_level:
            tech_level = tech_level_finder.parent.find("div")
        return tech_level.text
    except AttributeError as a:
        return f"Error fetching narrator {a}"

def species_nickname(parser): 
    try: 
        nickname_finder = parser.find("h3",string="MBoP Nickname" )
        nickname = nickname_finder.parent.find("a")
        if not nickname:
            nickname = nickname_finder.parent.find("div")
        return nickname.text
    except AttributeError as a:
        return f"Error fetching narrator {a}"

# species_id, species_name, appearance, patron, tech_level, nickname, coalition

def add_to_db(species_dict, species_list):
    for i in range(len(species_list)):
        current_species = species_list[i]
        species_info = species_dict[current_species]

        with Session(db.engine) as session:
            with session.begin():
                query = select(Species).filter(Species.species_id == species_info['species_id'])
                result = session.execute(query).scalars().first()
                print(current_species, result)

                # If result is None, so if there is no result with that id present.
                if result == None:
                    new_species = Species(
                        species_id = species_info['species_id'],
                        species_name=species_info['species_name'],
                        appearance=species_info['appearance'],
                        patron=species_info['patron'],
                        tech_level=species_info['tech_level'],
                        nickname=species_info['nickname'],
                        coalition=species_info['coalition']
                    )
                    print(new_species)

                    session.add(new_species)
                    session.commit()
                    session.close()
                else:
                    book = result
                    for field, value in species_info.items():
                        setattr(book, field, value)
                    session.commit()
        # break

def species_scraper():
    species_list = ['Humans', 'Kristang', 'Ruhar', 'Thuranin', 'Bosphuraq', 'Jeraptha', 'Rindhalu', 'Maxolhx', 'Elders', 'Lemoostra', 'Verd-kris', 'Wurgalan', 'Torgalau', 'Urgar']
    coalition_dict = {
        'Humans': "Human",
        'Kristang': "Maxolhx",
        'Thuranin': "Maxolhx",
        'Bosphuraq': "Maxolhx",
        'Maxolhx': "Maxolhx",
        'Wurgalan': "Maxolhx",
        'Ruhar': "Rindhalu",
        'Jeraptha': "Rindhalu",
        'Rindhalu': "Rindhalu",
        'Lemoostra': "Rindhalu",
        'Torgalau': "Rindhalu",
        'Urgar': 'Maxolhx',
        'Elders': "None",
        "Verd-kris": "Humans"
    }
    species_dict = {}
    id = 1
    for species in species_list:
        response = requests.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/{species}')

        if response.status_code == 200:
            html_content = response.text
            print("status code of 200")
        else:
            print("Error in code")

        soup = BeautifulSoup(html_content, 'html.parser')
        species_id = id
        species_name = species
        species_apperance = species_apperance_(soup)
        patron = species_patron(soup)
        tech_level = species_tech_level(soup)
        nickname = species_nickname(soup)
        coalition = coalition_dict[species]

        species_dict[species] = {
            "species_id": species_id, 
            "species_name": species_name,
            "appearance": species_apperance,
            "patron": patron,
            "tech_level": tech_level,
            "nickname": nickname,
            "coalition": coalition
        }
        id += 1

        print(f"Species_id: {species_id}")
        print(f"Species_name: {species_name}")
        print(f"Appearance: {species_apperance}")
        print(f"Patron: {patron}")
        print(f"tech_level: {tech_level}")
        print(f"nickname: {nickname}")
        print(f"Coalition: {coalition}")
        # break

    add_to_db(species_dict, species_list)
