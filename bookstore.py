"""
A program that stores information about the books in my personal library.
book attributes are Title, Author, Year, ISBN

User can:
 - View all records in the library
 - Search an entry
 - Add an entry
 - Update an entry
 - Delete an entry
 - Close the application.
"""

from tkinter import *

window = Tk()

lbl_title = Label(window, text="Title")
lbl_title.grid(row=0, column=0)

lbl_author = Label(window, text="Author")
lbl_author.grid(row=0, column=2)

lbl_year = Label(window, text="Year")
lbl_year.grid(row=1, column=0)

lbl_isbn = Label(window, text="ISBN")
lbl_isbn.grid(row=1, column=2)

title_text = StringVar()
ent_title = Entry(window, textvariable=title_text)
ent_title.grid(row=0, column=1)

author_text = StringVar()
ent_author = Entry(window, textvariable=author_text)
ent_author.grid(row=0, column=3)

year_text = StringVar()
ent_year = Entry(window, textvariable=year_text)
ent_year.grid(row=1, column=1)

isbn_text = StringVar()
ent_isbn = Entry(window, textvariable=isbn_text)
ent_isbn.grid(row=1, column=3)


window.mainloop()