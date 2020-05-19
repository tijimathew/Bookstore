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
from backend import Database

class BookstoreApp:

    def __init__(self):    
        self.db = Database("books.db")

        self.window = Tk()

        self.window.title("Bookstore")

        self.lbl_title = Label(self.window, text="Title")
        self.lbl_title.grid(row=0, column=0)

        self.lbl_author = Label(self.window, text="Author")
        self.lbl_author.grid(row=0, column=2)

        self.lbl_year = Label(self.window, text="Year")
        self.lbl_year.grid(row=1, column=0)

        self.lbl_isbn = Label(self.window, text="ISBN")
        self.lbl_isbn.grid(row=1, column=2)

        self.title_text = StringVar()
        self.ent_title = Entry(self.window, textvariable=self.title_text)
        self.ent_title.grid(row=0, column=1)

        self.author_text = StringVar()
        self.ent_author = Entry(self.window, textvariable=self.author_text)
        self.ent_author.grid(row=0, column=3)

        self.year_text = StringVar()
        self.ent_year = Entry(self.window, textvariable=self.year_text)
        self.ent_year.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.ent_isbn = Entry(self.window, textvariable=self.isbn_text)
        self.ent_isbn.grid(row=1, column=3)

        self.record_list = Listbox(self.window, height=6, width=35)
        self.record_list.grid(row=2, rowspan=6, columnspan=2)


        self.record_scrollbar = Scrollbar(self.window)
        self.record_scrollbar.grid(row=2, column=2, rowspan=6)

        self.record_list.configure(yscrollcommand=self.record_scrollbar.set)
        self.record_scrollbar.configure(command=self.record_list.yview)

        self.record_list.bind('<<ListboxSelect>>', self.get_selected_row)

        self.btn_view_all = Button(self.window, text="View All", width=12, command=self.view_all)
        self.btn_view_all.grid(row=2, column=3)

        self.btn_search = Button(self.window, text="Search entry", width=12, command=self.search_list)
        self.btn_search.grid(row=3, column=3)

        self.btn_add = Button(self.window, text="Add entry", width=12, command=self.add_record)
        self.btn_add.grid(row=4, column=3)

        self.btn_update = Button(self.window, text="Update selected", width=12, command=self.update_record)
        self.btn_update.grid(row=5, column=3)

        self.btn_delete = Button(self.window, text="Delete selected", width=12, command=self.delete_record)
        self.btn_delete.grid(row=6, column=3)

        self.btn_close = Button(self.window, text="Close", width=12, command=self.window.destroy)
        self.btn_close.grid(row=7, column=3)

        self.window.mainloop()

    def view_all(self):
        self.record_list.delete(0, END)
        for row in self.db.view():
            self.record_list.insert(END, row)

    def get_selected_row(self, event):
        try:
            global g_selected_record 
            selected_index = self.record_list.curselection()
            g_selected_record = self.record_list.get(selected_index[0])
            self.ent_title.delete(0, END)
            self.ent_title.insert(END, g_selected_record[1])
            self.ent_author.delete(0, END)
            self.ent_author.insert(END, g_selected_record[2])
            self.ent_year.delete(0, END)
            self.ent_year.insert(END, g_selected_record[3])
            self.ent_isbn.delete(0, END)
            self.ent_isbn.insert(END, g_selected_record[4])
        except IndexError:
            pass

    def search_list(self):
        self.record_list.delete(0, END)
        for row in self.db.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.record_list.insert(END, row)

    def add_record(self):
        self.db.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.record_list.delete(0, END)
        self.record_list.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_record(self):
        self.db.delete(g_selected_record[0])

    def update_record(self):
        self.db.update(g_selected_record[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())


BookstoreApp()