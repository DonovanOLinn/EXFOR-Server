from app.scrapers.species_scraper import species_scraper
from app.scrapers.book_scraper import book_scraper
from app.scrapers.ship_scraper import ship_scraper
from app.scrapers.planets_scraper import planet_scraper
from app.scrapers.characters_scraper import character_scraper


def run_all_scrapers():
    try:
        # species_scraper()
        # ship_scraper()
        # planet_scraper()
        book_scraper()
        # character_scraper()
    except Exception as e:
        print(f"Error: {e}")

# if __name__ == '__main__':
#     run_all_scrapers()