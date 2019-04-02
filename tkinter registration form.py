import tkinter as tk
import sqlite3
import tkinter.messagebox


def submit_data():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    table_query = 'create table if not exists {}("First name" text, surname text, address text, gender integer, country text)'.format(surnameE.get())
    c.execute(table_query)
    values_query = 'insert into {} values(?, ?, ?, ?, ?)'.format(surnameE.get())
    c.execute(values_query, (firstNameE.get(), surnameE.get(), addressE.get(), radioVar.get(), optionVar.get()))
    conn.commit()
    conn.close()


def show_data():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    try:
        print(('_' * (23 + len(showE.get()))),
              '\nData for table', showE.get() + ':',
              '\n' + ('-' * (23 + len(showE.get()))))
        query = 'select * from {}'.format(showE.get())
        for row in c.execute(query):
            if row[3] == 1:
                gender = 'male'
            else:
                gender = 'female'
            print('\nFirst name:', row[0],
                  '\nSurname:', row[1],
                  '\nAddress:', row[2],
                  '\nGender:', gender,
                  '\nCountry:', row[4],
                  '\n'+('_'*(23+len(showE.get()))))
    except sqlite3.OperationalError:
        print('Table {} not in database'.format(showE.get()))
    conn.commit()
    conn.close()


def show_all_tables():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    count = 0
    print('Number  |  Name',
          '\n---------------')
    for row in c.execute('select name from sqlite_master where type="table"'):
        print('Table', str(count) + ':', row[0])
        count += 1

    conn.commit()
    conn.close()


def delete_table():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    yes_or_no = tk.messagebox.askquestion('Delete table', 'Are you sure you want to delete table?')
    if yes_or_no == 'yes':
        try:
            query = 'drop table {}'.format(deleteE.get())
            c.execute(query)
            print(deleteE.get(), 'was deleted from database')
        except sqlite3.OperationalError:
            print('Table {} doesn\'t exist'.format(deleteE.get()))
    conn.commit()
    conn.close()


def about():
    top = tk.Toplevel()
    top.title('About')
    top.geometry('300x300')
    tk.Message(top, text='About').grid(row=0, column=1)


def popup(event):
    aboutmenu.post(event.x_root, event.y_root)

####
def callback(event):
    print("clicked at", event.x, event.y)

def key(event):
    print('pressed', repr(event.char))
####

root = tk.Tk()
root.title('Registration Form')
root.geometry('400x600')
####
root.bind('<Key>', key)
root.bind('<Button-1>', callback)
####
# VARIABLES
radioVar = tk.IntVar()
radioVar.set(1)
optionVar = tk.StringVar(root)
optionVar.set('Denmark')

# MENUBAR
menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=filemenu, underline=0)

menubar.add_command(label='Exit', command=root.destroy, underline=0)

aboutmenu = tk.Menu(menubar, tearoff=0)
aboutmenu.add_command(label='About', command=about, underline=0, accelerator='Ctrl+a')
aboutmenu.add_checkbutton(label='ost')
aboutmenu.bind('<Control-a>', about)
menubar.add_cascade(label='About', menu=aboutmenu, underline=0)
root.bind('<Button-3>', popup)

root.config(menu=menubar)

# ENTRIES
entries = tk.Label(root, text='Entries')
entries.grid(row=0, column=0, sticky=tk.W, pady=5)
entries.config(font=('Time', 10, 'bold'))

firstNameL = tk.Label(root, text='First name:')
firstNameL.grid(row=1, sticky=tk.E)
firstNameE = tk.Entry(root)
firstNameE.grid(row=1, column=1, pady=2)

surnameL = tk.Label(root, text='Surname:')
surnameL.grid(row=2, sticky=tk.E)
surnameE = tk.Entry(root)
surnameE.grid(row=2, column=1, pady=2)

addressL = tk.Label(root, text='Address:')
addressL.grid(row=3, sticky=tk.E)
addressE = tk.Entry(root)
addressE.grid(row=3, column=1, pady=2)

tk.Label(root, text='Select a gender:').grid(row=4, sticky=tk.E)
male = tk.Radiobutton(root, text='Male', variable=radioVar, value=1)
male.grid(row=4, column=1, sticky=tk.W, pady=2)
female = tk.Radiobutton(root, text='Female', variable=radioVar, value=2)
female.grid(row=5, column=1, sticky=tk.W)

tk.Label(root, text='Select a country:').grid(row=6, sticky=tk.E)
countries = tk.OptionMenu(root, optionVar, 'Albania', 'Denmark', 'England', 'France')
countries.grid(row=6, column=1, sticky=tk.W, pady=2)

submitForm = tk.Button(root, text='Submit Form', command=submit_data)
submitForm.grid(row=7, column=1, sticky=tk.W, pady=15)

# SHOW TABLES
show = tk.Label(root, text='Show tables')
show.grid(row=8, column=0, sticky=tk.W, pady=5)
show.config(font=('Time', 10, 'bold'))

showL1 = tk.Label(root, text='Show person:')
showL1.grid(row=9, sticky=tk.E)
showE = tk.Entry(root)
showE.grid(row=9, column=1)

showButton = tk.Button(root, text='Show', command=show_data)
showButton.grid(row=9, column=2, padx=2)

showL2 = tk.Label(root, text='(table name)')
showL2.grid(row=10, column=1, sticky=tk.W)
showL2.config(font=('Time', 8))

tk.Button(root, text='Show all tables', command=show_all_tables).grid(row=11, column=1, sticky=tk.W, pady=2)


# DELETE TABLES
delete = tk.Label(root, text='Delete tables')
delete.grid(row=12, column=0, sticky=tk.W, pady=5)
delete.config(font=('Time', 10, 'bold'))

deleteL1 = tk.Label(root, text='Delete table:')
deleteL1.grid(row=13, sticky=tk.E)
deleteE = tk.Entry(root)
deleteE.grid(row=13, column=1)

deleteButton = tk.Button(root, text='Delete', command=delete_table)
deleteButton.grid(row=13, column=2, padx=5)

deleteL2 = tk.Label(root, text='(Entire table will be deleted)')
deleteL2.grid(row=14, column=1)
deleteL2.config(font=('Time', 8, 'bold'))
root.mainloop()
