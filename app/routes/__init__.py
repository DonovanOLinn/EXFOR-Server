from .ships import ships_bp
from .books import books_bp
from .character import characters_bp
from .planet import planets_bp
from .species import species_bp

def init_routes(app):
    app.register_blueprint(ships_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(characters_bp)
    app.register_blueprint(planets_bp)
    app.register_blueprint(species_bp)