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
import backend

def view_all():
    record_list.delete(0, END)
    for row in backend.view():
        record_list.insert(END, row)

def get_selected_row(event):
    try:
        global g_selected_record 
        selected_index = record_list.curselection()
        g_selected_record = record_list.get(selected_index[0])
        ent_title.delete(0, END)
        ent_title.insert(END, g_selected_record[1])
        ent_author.delete(0, END)
        ent_author.insert(END, g_selected_record[2])
        ent_year.delete(0, END)
        ent_year.insert(END, g_selected_record[3])
        ent_isbn.delete(0, END)
        ent_isbn.insert(END, g_selected_record[4])
    except IndexError:
        pass

def search_list():
    record_list.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        record_list.insert(END, row)

def add_record():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    record_list.delete(0, END)
    record_list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_record():
    backend.delete(g_selected_record[0])

def update_record():
    backend.update(g_selected_record[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()

window.title("Bookstore")

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

record_list = Listbox(window, height=6, width=35)
record_list.grid(row=2, rowspan=6, columnspan=2)


record_scrollbar = Scrollbar(window)
record_scrollbar.grid(row=2, column=2, rowspan=6)

record_list.configure(yscrollcommand=record_scrollbar.set)
record_scrollbar.configure(command=record_list.yview)

record_list.bind('<<ListboxSelect>>', get_selected_row)

btn_view_all = Button(window, text="View All", width=12, command=view_all)
btn_view_all.grid(row=2, column=3)

btn_search = Button(window, text="Search entry", width=12, command=search_list)
btn_search.grid(row=3, column=3)

btn_add = Button(window, text="Add entry", width=12, command=add_record)
btn_add.grid(row=4, column=3)

btn_update = Button(window, text="Update selected", width=12, command=update_record)
btn_update.grid(row=5, column=3)

btn_delete = Button(window, text="Delete selected", width=12, command=delete_record)
btn_delete.grid(row=6, column=3)

btn_close = Button(window, text="Close", width=12, command=window.destroy)
btn_close.grid(row=7, column=3)

window.mainloop()