from tkinter import *
from db import Database
db = Database('store.db')
def populate_list():
    part_list.delete(0,END)
    for  row in db.fetch():
        part_list.insert(END,row)
def add_item():
    print('Add')

def remove_item():
    print('Remove')

def update_item():
    print('Update')

def clear_text():
    print('Clear')

app = Tk()
app.title('Part Manager')
app.geometry('700x350')

# Create a dictionary to hold all the labels, entries, and text variables
widgets = {
    'part': {'text': 'Part Name', 'row': 0, 'column': 0},
    'customer': {'text': 'Customer', 'row': 0, 'column': 2},
    'retailer': {'text': 'Retailer', 'row': 1, 'column': 0},
    'price': {'text': 'Price', 'row': 1, 'column': 2}
}

for key, value in widgets.items():
    value['text_var'] = StringVar()
    Label(app, text=value['text'], font=('bold', 14)).grid(row=value['row'], column=value['column'], sticky=W)
    Entry(app, textvariable=value['text_var']).grid(row=value['row'], column=value['column']+1)

# Part list (listbox)
part_list = Listbox(app, height=8, width=50, border=0)
part_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Set scroll to listbox
part_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=part_list.yview)

# Buttons
Button(app, text='Add Part', width=12, command=add_item).grid(row=2, column=0, pady=20)
Button(app, text='Remove Part', width=12, command=remove_item).grid(row=2, column=1)
Button(app, text='Update Part', width=12, command=update_item).grid(row=2, column=2)
Button(app, text='Clear Input', width=12, command=clear_text).grid(row=2, column=3)

# Populate data
populate_list()

app.mainloop()
