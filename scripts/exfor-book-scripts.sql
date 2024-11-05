select * from books;

ALTER TABLE books MODIFY COLUMN author_summary VARCHAR(5000);
    
INSERT INTO books (book_id, book_name, release_date, previous, next, author_summary, image, author, narrator, run_time)
VALUES (1, "Columbus Day", "2016-12-13", "None", "Spec Ops", "We were fighting on the wrong side, of a war we couldn't win. And that was the good news.The Ruhar hit us on Columbus Day. 
	There we were, innocently drifting along the cosmos on our little blue marble, like the native Americans in 1492. Over the horizon come ships of a technologically advanced, aggressive culture, and BAM! 
    There go the good old days, when humans only got killed by each other. So, Columbus Day. It fits. When the morning sky twinkled again, this time with Kristang starships jumping in to hammer the Ruhar, 
    we thought we were saved. The UN Expeditionary Force hitched a ride on Kristang ships to fight the Ruhar, wherever our new allies thought we could be useful. So, I went from fighting with the US Army in Nigeria, 
    to fighting in space. It was lies, all of it. We shouldn't even be fighting the Ruhar, they aren't our enemy, our allies are. I'd better start at the beginning....", 
    "https://static.wikia.nocookie.net/expeditionary-force-by-craig-alanson/images/9/98/ExForce_Book_1_Columbus_Day_2.jpg/revision/latest?cb=20201029202958", "Craig Alanson", "R.C. Bray", "16 hours 23 minutes");
INSERT INTO books (book_id, book_name, release_date, previous, next, author_summary, image, author, narrator, run_time)
VALUES (2, "Spec Ops", "2017-03-07", "Columbus Day", "Paradise", "Colonel Joe Bishop' made a promise, and he's going to keep it: taking the captured alien starship Flying Dutchman back out. 
He doesn't agree when the UN decides to send almost 70 elite Special Operations troops, hotshot pilots, and scientists with him; the mission is a fool's errand he doesn't expect to ever return from. 
At least this time, the Earth is safe, right? Not so much.", "https://static.wikia.nocookie.net/expeditionary-force-by-craig-alanson/images/f/f7/ExForce_Book_2_Spec_Ops_2.jpg/revision/latest?cb=20201029203035", 
"Craig Alanson", "R.C. Bray", "15 hours 49 minutes");
INSERT INTO books (book_id, book_name, release_date, previous, next, author_summary, image, author, narrator, run_time)
VALUES (3, "Paradise", "2017-03-07", "Spec Ops", "Trouble on Paradise (Novella)", "While the crew of the starship Flying Dutchman have been trying to assure that hostile aliens do not have access to Earth, the UN Expeditionary Force has been stranded
 on the planet they nicknamed 'Paradise'. The Flying Dutchman is headed back out on another mission, and the UN wants the ship to find out the status of the humans on Paradise. But Colonel Joe Bishop warns 
 that they might not like what they find, and they can't do anything about it without endangering Earth.", 
 "https://static.wikia.nocookie.net/expeditionary-force-by-craig-alanson/images/8/8b/ExForce_Book_3_Paradise_2.jpg/revision/latest?cb=20201029203055", "Craig Alanson", "R.C. Bray", "15 hours 53 minutes");
 
 select * from characters;
 INSERT INTO characters (character_id, character_name, description, status, last_known_location, sex, first_book_appearance_id)
 VALUES (1, "Joseph Bishop", "Joseph Arthur Bishop is an Army soldier from Maine, who finds himself in a whole heap of adventure due to no fault of his own. Joe is also the main character of the series 
 and the narrator of most parts of the books in the main series.", "alive", "valkyrie", "male", 1);
 
select * from planets;
INSERT INTO planets (planet_id, planet_name, planet_nickname, first_book_appearance_id)
VALUES(1, "Earch", "Home", 1);

UPDATE planets SET planet_name = "Earth" WHERE planet_id = 1;

select * from species;
INSERT INTO species (species_id, species_name, appearance, patron, tech_level, nickname, coalition)
VALUES (1, "Humans", "Roughly 2 meters tall, bi-pedal, with varying skin tone", "None", "Tier 1", "Monkeys", "Human Coalition");

select * from ships;
INSERT INTO ships (ship_id, ship_name, ship_type, status, species_id)
VALUES (1, "The Flying Dutchman V4", "Warship", "breaking apart in atmosphere", 1);