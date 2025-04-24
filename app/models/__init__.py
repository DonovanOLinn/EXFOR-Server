from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .ships import Ships
from .books import Books
from .species import Species
from .planets import Planets
from .characters import Characters