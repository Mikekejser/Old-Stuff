import tkinter as tk
import tkinter.messagebox
import sqlite3


def login():
    if usernameE.get():
        if passwordE.get():
            conn = sqlite3.connect('login_db.db')
            c = conn.cursor()
            for row in c.execute('select password from Login_info where username=?', (usernameE.get(),)):
                password = row[0]
                if password == passwordE.get():
                    print('Password verified!')
                    text = 'You\'re logged in as {}'.format(usernameE.get())
                    top = tk.Toplevel()
                    top.title('Logged in!')
                    top.geometry('100x100+100+100')
                    tk.Label(top, text=text).grid(row=0, sticky=tk.W)
                else:
                    print('Wrong password!')
                    tkinter.messagebox.showerror('Error', 'Wrong password!')
            conn.commit()
            conn.close()
        else:
            print('Enter a password!')
    else:
        print('Enter a username!')


conn = sqlite3.connect('login_db.db')


def create():
    conn = sqlite3.connect('login_db.db')
    c = conn.cursor()
    if newUsernameE.get():
        if newPasswordE.get() == confNewPasswordE.get():
            try:
                c.execute('insert into Login_info values(?, ?)', (newUsernameE.get(), newPasswordE.get()))
                print('New user created:', newUsernameE.get())
            except sqlite3.IntegrityError:
                print('Username already exists. Choose another!')
        else:
            print('Password does not match')
    else:
        print('Enter a username!')
    conn.commit()
    conn.close()


def show_all():
    conn = sqlite3.connect('login_db.db')
    c = conn.cursor()
    for row in c.execute('select * from Login_info'):
        print(row)
    conn.commit()
    conn.close()


root = tk.Tk()
root.title('Login UI')

# ----- MENU
menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu, underline=0)
filemenu.add_command(label='Exit', command=root.destroy)

root.config(menu=menubar)
# ----- LOGIN
loginFrame = tk.LabelFrame(root, text='Login', padx=15)
loginFrame.grid(row=0, padx=15)
loginFrame.config(font=('Time', 10, 'bold'))

usernameL = tk.Label(loginFrame, text='Username:')
usernameL.grid(row=0, column=0)
usernameE = tk.Entry(loginFrame)
usernameE.grid(row=0, column=1)

passwordL = tk.Label(loginFrame, text='Password:')
passwordL.grid(row=1)
passwordE = tk.Entry(loginFrame, show='*')
passwordE.grid(row=1, column=1)

loginButton = tk.Button(loginFrame, text='Login', command=login, width=15)
loginButton.grid(row=2, column=1, pady=5)

# ----- CREATE NEW USER
createNewFrame = tk.LabelFrame(root, text='Create new user', padx=15)
createNewFrame.grid(row=1, padx=15, pady=15)
createNewFrame.config(font=('Time', 10, 'bold'))

newUsernameL = tk.Label(createNewFrame, text='Username:')
newUsernameL.grid(row=0)
newUsernameE = tk.Entry(createNewFrame)
newUsernameE .grid(row=0, column=1)

newPasswordL = tk.Label(createNewFrame, text='Password:')
newPasswordL.grid(row=1)
newPasswordE = tk.Entry(createNewFrame, show='*')
newPasswordE.grid(row=1, column=1)

confNewPasswordL = tk.Label(createNewFrame, text='Confirm:')
confNewPasswordL.grid(row=2)
confNewPasswordE = tk.Entry(createNewFrame, show='*')
confNewPasswordE.grid(row=2, column=1)

createButton = tk.Button(createNewFrame, text='Create', command=create, width=15)
createButton.grid(row=3, column=1, pady=5)

showAll = tk.Button(root, text='Show all users', command=show_all)
showAll.grid(row=2)

root.mainloop()
