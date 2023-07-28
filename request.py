# import re
# import requests
# from bs4 import BeautifulSoup
# import os
#
# image_pattern = r'https:\/\/s3\.amazonaws\.com\/digilibraries\.com\/covers\/[0-9]+\.jpg'
# title_pattern = "([A-Za-z0-9- .,;?[\]{}():\'\"]+)"
# target_url = 'https://digilibraries.com/category/non-classifiable/page/'
# pattern = re.compile(title_pattern)
# images = []
# titles = []
# https://s3.amazonaws.com/digilibraries.com/covers/
#
# def ebook(href):
#     return href and re.compile("/ebook/").search(href)
#
#
# for number in range(1, 10):
#     target_url += str(number)
#     response = requests.get(target_url)
#     html_content = response.text
#     soup = BeautifulSoup(html_content, 'html.parser')
#     a = [link.get_text() for link in soup.find_all('a', href=ebook)]
#     images.extend(re.findall(image_pattern, html_content))
#     titles.extend(a)
# titles = [title.strip().lower() for title in titles]



print(titles)
print(images)







# import sqlite3
# DATABASE_PATH = 'C:/Users/Admin/Desktop/Projects/ACA_Library/instance/site.db'
# from website import db
# from main import app
# with sqlite3.connect(DATABASE_PATH) as connection:
#     c = connection.cursor()
#     c.execute("""ALTER TABLE book RENAME TO old_books""")
#     with app.app_context():
#         db.create_all()
#
#     c.execute("""SELECT id, title, isbn, year_first_published, genre, image_file
#     FROM old_books ORDER BY id ASC""")
#
#
#     data = [(row[0], title, row[2], row[3], row[4], image) for row, image, title in zip(c.fetchall(), images_url, titles)]
#     c.executemany("""INSERT INTO book (id, title, isbn, year_first_published, genre, image_file)
#                      VALUES (?, ?, ?, ?, ?, ?)""", data)
#     c.execute("""DROP TABLE old_books""")
#
#
# import sqlite3
# DATABASE_PATH = 'C:/Users/Admin/Desktop/Projects/ACA_Library/instance/site.db'
# from website import db
# from main import app
# with sqlite3.connect(DATABASE_PATH) as connection:
#     c = connection.cursor()
#     c.execute("""ALTER TABLE copy_book RENAME TO old_books""")
#     with app.app_context():
#         db.create_all()
#
#     c.execute("""SELECT id, book_id, isbn_copy, year_published, borrowed_date, condition_rating, loan
#     FROM old_books ORDER BY id ASC""")
#
#
#     data = [(row[0], row[1], row[2], row[3], row[4], row[5], boolean)
#             for row, boolean in zip(c.fetchall(), [False for i in range(85)])]
#
#     c.executemany("""INSERT INTO copy_book (id, book_id, isbn_copy, year_published, borrowed_date, condition_rating, loan)
#                      VALUES (?, ?, ?, ?, ?, ?, ?)""", data)
#     c.execute("""DROP TABLE old_books""")
# with open('c:/Users/Admin/Downloads/MOCK_DATA.csv', 'r') as filename:
#     student_id = filename.read().splitlines()
#
# import sqlite3
# DATABASE_PATH = 'C:/Users/Admin/Desktop/Projects/ACA_Library/instance/site.db'
# from website import db
# from main import app
# with sqlite3.connect(DATABASE_PATH) as connection:
#     c = connection.cursor()
#     c.execute("""ALTER TABLE copy_book RENAME TO old_books""")
#     with app.app_context():
#         db.create_all()
#
#     c.execute("""SELECT id, book_id, isbn_copy, year_published, borrowed_date, condition_rating, loan, student_id
#     FROM old_books ORDER BY id ASC""")
#
#
#     data = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], student)
#             for row, student in zip(c.fetchall(), student_id)]
#
#     c.executemany("""INSERT INTO copy_book (id, book_id, isbn_copy, year_published, borrowed_date, condition_rating, loan, student_id)
#                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", data)
#     c.execute("""DROP TABLE old_books""")


# import sqlite3
# DATABASE_PATH = 'C:/Users/Admin/Desktop/Projects/ACA_Library/instance/site.db'
# from website import db
# from main import app
# with sqlite3.connect(DATABASE_PATH) as connection:
#     c = connection.cursor()
#     c.execute("""ALTER TABLE copy_book RENAME TO old_copy_book""")
#     with app.app_context():
#         db.create_all()
#
#     c.execute("""SELECT id, book_id, student_id, isbn_copy, borrowed_date, year_published, condition_rating, loan
#     FROM old_copy_book ORDER BY id ASC""")
#
#
#     data = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
#             for row in c.fetchall()]
#     c.executemany("""INSERT INTO copy_book (id, book_id, student_id, isbn_copy, borrowed_date, year_published, condition_rating, loan)
#                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", data)
#     c.execute("""DROP TABLE old_copy_book""")