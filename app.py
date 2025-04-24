
# with app.app_context():
#     # db.drop_all()
#     db.create_all()
#     # book_scraper()
#     # species_scraper()
#     # ship_scraper() # Issue popping up with the ship_scraper. Error at ship_id of 84. Ship Types of Converyance. FK constraint with species.
#     # planet_scraper()
#     # character_scraper() #Foreign key constraing fails on teh connection with first_book_appearance id


# # @app.route("/ships", methods=['GET'])
# # def get_ships():
# #     rows = select(Ships)

# #     result = db.session.execute(rows).scalars()
# #     ships = result.all()
# #     return ships_schema.dump(ships)

# # @app.route("/ships/<int:id>", methods=['GET'])
# # def get_single_ship(id):
# #     rows = select(Ships).where(Ships.ship_id == id)

# #     result = db.session.execute(rows).scalars()