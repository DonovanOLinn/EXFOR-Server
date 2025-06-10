from app import create_app
from dotenv import load_dotenv
from tasks.scraper_tasks import run_all_scrapers
from app.models import db


load_dotenv()
app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # run_all_scrapers()
    app.run(debug=True)