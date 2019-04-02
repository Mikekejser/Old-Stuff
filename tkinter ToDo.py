import tkinter as tk
import sqlite3
import time


def today():
    global dayVar
    current_weekday = time.localtime()[6]
    if current_weekday == 0:
        dayVar.set('Monday')
    elif current_weekday == 1:
        dayVar.set('Tuesday')
    elif current_weekday == 2:
        dayVar.set('Wednesday')
    elif current_weekday == 3:
        dayVar.set('Thursday')
    elif current_weekday == 4:
        dayVar.set('Friday')
    elif current_weekday == 5:
        dayVar.set('Saturday')
    elif current_weekday == 6:
        dayVar.set('Sunday')


def todo_func():
    conn = sqlite3.connect('ToDo.db')
    c = conn.cursor()
    c.execute('insert into ToDoTable values(?, ?)', (todoE.get(), dayVar.get()))
    conn.commit()
    conn.close()


def show_all():

    def done():
        delVar = tk.StringVar()
        delVar.set('**' + deleteE.get() + ' deleted**')
        conn = sqlite3.connect('ToDo.db')
        c = conn.cursor()
        c.execute('delete from ToDoTable where todo=?', (deleteE.get(),))
        conn.commit()
        conn.close()
        tk.Label(top, textvariable=delVar).grid(row=1, column=3, sticky=tk.W)

    conn = sqlite3.connect('ToDo.db')
    c = conn.cursor()

    top = tk.Toplevel()
    top.title(dayVar.get())

    tk.Label(top, text='Day:').grid(row=0, column=0, sticky=tk.E)
    day_title = tk.Entry(top)
    day_title.grid(row=0, column=1, pady=5)
    day_title.insert(0, dayVar.get())

    deleteL = tk.Label(top, text='Delete:')
    deleteL.grid(row=0, column=2)
    deleteE = tk.Entry(top)
    deleteE.grid(row=0, column=3)

    row_count = 1
    tk.Button(top, text='Done', command=done).grid(row=0, column=4, padx=5)
    tk.Button(top, text='Show', command=show_all).grid(row=1, column=4, padx=5)

    for row in c.execute('select todo from ToDoTable where day=?', (dayVar.get(),)):
        show_row = tk.Entry(top)
        show_row.grid(row=row_count, column=1)
        show_row.insert(0, row[0])

        row_count += 1

    conn.commit()
    conn.close()


# ----- UI -----
root = tk.Tk()
root.title('ToDo')

# ----- menu
menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=filemenu, underline=0)

root.config(menu=menubar)

# ----- entry

# row 0
todoL = tk.Label(root, text='What to do?:')
todoL.grid(row=0, column=0)
todoE = tk.Entry(root)
todoE.grid(row=0, column=1)

todayButton = tk.Button(root, text='Today', command=today)
todayButton.grid(row=0, column=2, padx=2)

dayVar = tk.StringVar()
day = tk.OptionMenu(root, dayVar, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
day.grid(row=0, column=3, padx=2)

# row 1
tk.Button(root, text='Add', command=todo_func).grid(row=1, column=1, sticky=tk.W)
tk.Button(root, text='Show all', command=show_all).grid(row=1, column=1, sticky=tk.E)


root.mainloop()