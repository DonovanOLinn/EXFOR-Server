from bs4 import BeautifulSoup
import requests
import mysql.connector
from mysql.connector import Error
from models.books import Books
from database import db
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime

# def connect_database():
#     db_name = "expeditionary_force"
#     user = "root"
#     password = "CodingTemple"
#     host = "localhost"

#     try:
#         conn = mysql.connector.connect(
#             database = db_name,
#             user = user,
#             password = password,
#             host = host
#         )
#         print("Connected to MySQL database successfully.")
#         return conn
#     except Error as e:
#         print(f"Error: {e}")
#         return None
#     except Exception as e:
#         print(f"General Error: {e}")
#         return None

def author_parser_book(parser):
    try:
        author_finder = parser.find("h3",string="Author" )
        author = author_finder.parent.find("a")
        if not author:
            author = author_finder.parent.find("div")
        return author.text
    except AttributeError as a:
        return f"Error fetching author {a}"

def narrator_parser_book(parser):
    try:
        narrator_finder = parser.find("h3",string="Narrator" )
        narrator = narrator_finder.parent.find("a")
        if not narrator:
            narrator = narrator_finder.parent.find("div")
        return narrator.text
    except AttributeError as a:
        return f"Error fetching narrator {a}"

def release_parser_book(parser):
    try:
        release_finder = parser.find("h3",string="Release" )
        release = release_finder.parent.find("a")
        if not release:
            release = release_finder.parent.find("div")
        return release.text
    except AttributeError as a:
        return f"Error fetching release date {a}"

def run_time_parser_book(parser):
    try:
        run_time_finder = parser.find("h3",string="Run Time" )
        run_time = run_time_finder.parent.find("a")
        if not run_time:
            run_time = run_time_finder.parent.find("div")
        return run_time.text
    except AttributeError as a:
        return f"Error fetching run time {a}"

def previous_parser_book(parser):
    try:
        previous_finder = parser.find("h3",string="Previous" )
        previous = previous_finder.parent.find("a")
        if not previous:
            previous = previous_finder.parent.find("div")
        return previous.text
    except AttributeError as a:
        return f"Error fetching previous book {a}"

def next_parser_book(parser):
    try:
        next_finder = parser.find("h3",string="Next" )
        next = next_finder.parent.find("a")
        if not next: 
            next = next_finder.parent.find("div")
        return next.text
    except AttributeError as a:
        return f"Error fetching next book {a}"
    
def author_summary_parser_book(parser):
    try:
        summary_finder = parser.find_all("blockquote")
        summary_organizer = []
        for summary in summary_finder:
            summary_organizer.append(summary.text)
        new_summary = " ".join(summary_organizer)
        new_summary = new_summary.strip('"')
        return new_summary
    except AttributeError as a:
        f"Error fetching author summary {a}"

def image_parser_book(parser):
    try: 
        h2_finder = parser.find("h2")
        img_finder = h2_finder.parent.find("img")
        print(img_finder)
        return img_finder["src"]

    except TypeError:
        print("Couldn't find Image. Please review HTML elements.")

def add_to_db(book_dict, book_title):
    
    for i in range(len(book_title)):
        current_book = book_title[i]
        book_info = book_dict[current_book]

        with Session(db.engine) as session:
            with session.begin():
                query = select(Books).filter(Books.book_id == book_info['book_id'])
                result = session.execute(query).scalars().first()
                print(current_book, result)

                # If result is None, so if there is no result with that id present.
                if result == None:
                    new_book = Books(
                        book_id = book_info['book_id'],
                        book_name=book_info['book_name'],
                        release_date=book_info['release_date'],
                        previous=book_info['previous'],
                        next=book_info['next'],
                        author_summary=book_info['author_summary'],
                        image=book_info['image'],
                        author=book_info['author'],
                        narrator=book_info['narrator'],
                        run_time=book_info['run_time']
                    )
                    print(new_book)

                    session.add(new_book)
                    session.commit()
                    session.close()
                else:
                    book = result
                    for field, value in book_info.items():
                        setattr(book, field, value)
                    session.commit()
                


def book_scraper():
    book_title = ['ExForce_1:_Columbus_Day', 'ExForce_2:_Spec_Ops', 'ExForce_3:_Paradise', 'ExForce_3.5:_Trouble_on_Paradise', 'ExForce_4:_Black_Ops',
              'ExForce_5:_Zero_Hour', 'ExForce_6:_Mavericks', 'ExForce_7:_Renegades', 'ExForce_7.5:_Homefront', 'ExForce_8:_Armageddon', 'ExForce_9:_Valkyrie',
              'ExForce_10:_Critical_Mass', 'ExForce_11:_Brushfire', 'ExForce_12:_Breakaway', 'ExForce_13:_Fallout', 'ExForce_14:_Match_Game', 'ExForce_15:_Failure_Mode', 
              'ExForce_16:_Aftermath', 'ExForce_17:_Task_Force_Hammer']

    book_dict = {}
    id = 1
    for book in book_title:

        response = requests.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/{book}')

        if response.status_code == 200:
            html_content = response.text
            print("status code of 200")
        else:
            print("Error in code")

        soup = BeautifulSoup(html_content, "html.parser")

        author = author_parser_book(soup)
        narrator = narrator_parser_book(soup)
        release_date_preformatted = release_parser_book(soup)
        release_date = datetime.strptime(release_date_preformatted, '%B %d, %Y')
        run_time = run_time_parser_book(soup)
        # run_time = datetime.strptime(run_time_preformatted, '%B %d, %Y')
        previous_book = previous_parser_book(soup)
        next_book = next_parser_book(soup)
        summary = author_summary_parser_book(soup)
        image = image_parser_book(soup)

        book_dict[book] = {
            "author": author,
            "book_name": book,
            "narrator": narrator,
            "release_date": release_date,
            "run_time": run_time,
            "previous": previous_book,
            "next": next_book,
            "author_summary": summary,
            "image": image,
            "book_id": id
        }
        id += 1

        print(f"BOOK: {book}")
        print(f"Author: {author}")
        print(f"Narrator: {narrator}")
        print(f"Release Date: {release_date}")
        print(f"Run Time: {run_time}")
        print(f"Previous Book: {previous_book}")
        print(f"Next Book: {next_book}")
        print(f"Summary: {summary}")
        print(f"Image location: {image}")
        print(f"id: {id}")
        print("-"*25)

    # return book_dict
    add_to_db(book_dict, book_title)

# book_scraper()