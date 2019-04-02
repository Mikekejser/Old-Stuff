import tkinter as tk
import requests
from bs4 import BeautifulSoup


# ----- FUNCTIONS -----
def calculate(event=None):
    amount = 0
    if amountE.get():
        if amountE.get().find('.') == -1:
            try:
                amount = int(amountE.get())
            except ValueError:
                print('Entered value cannot be a string. Only int or float')
                amountE.delete(0, 'end')


        elif '.' in amountE.get():
            amount = float(amountE.get())

        id = ''

        if currenciesVar.get() == 'Dollar':
            id = 'USD'

        if currenciesVar.get() == 'Norske kroner':
            id = 'NOK'

        if currenciesVar.get() == 'Svenske kroner':
            id = 'SEK'

        elif currenciesVar.get() == 'Euro':
            id ='EUR'

        elif currenciesVar.get() == 'Pund':
            id = 'GBP'

        elif currenciesVar.get() == 'Yen':
            id = 'JPY'

        var1 = soup.find(id=id).text
        decimal_index = var1.find(',')
        var2 = var1[:decimal_index]
        var3 = var1[decimal_index+1:]
        var = round(((float(var2 + '.' + var3))/100) * amount, 2)
        result.set(var)
        exchangeRate.set(round(((float(var2 + '.' + var3))/100), 2))
    else:
        result.set('Enter float or int')


def clear():
    amountE.delete(0, 'end')
    resultE.delete(0, 'end')
    exchangeE.delete(0, 'end')


# ----- RETRIEVED DATA -----
page = requests.get('http://www.valutakurser.dk/')
print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')

# ----- UI -----
root = tk.Tk()
root.title('Currency converter')
root.geometry('400x100')

exchangeRate = tk.IntVar()
result = tk.IntVar()

# ----- menubar
menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Exit', command=root.destroy)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label='Clear', command=clear)

menubar.add_cascade(label='File', menu=filemenu, underline=0)
menubar.add_cascade(labe='Edit', menu=editmenu, underline=0)


root.config(menu=menubar)

# ----- entry

# row 1
amountL = tk.Label(root, text='Amount:')
amountL.grid(row=0, sticky=tk.E)
amountE = tk.Entry(root)
amountE.grid(row=0, column=1, padx=5)
amountE.focus_set()
amountE.insert(0, 1234)

amountE.bind('<Return>', calculate)

tk.Button(root, text='calculate',command=calculate).grid(row=0, column=2, padx=2)

currenciesVar = tk.StringVar()
currenciesVar.set('Euro')
currencies = tk.OptionMenu(root, currenciesVar, 'Dollar', 'Pund', 'Euro', 'Norske kroner', 'Svenske kroner', 'Yen')
currencies.grid(row=0, column=3, padx=2)

tk.Button(root, text='clear', command=clear).grid(row=0, column=4, padx=2)

# row 2
tk.Label(root, text='Exchange rate:').grid(row=1, column=0, sticky=tk.E)
exchangeE = tk.Entry(root, textvariable=exchangeRate)
exchangeE.grid(row=1, column=1, padx=5)

# row 3
resultL = tk.Label(root, text='DKK:')
resultL.grid(row=2, column=0, sticky=tk.E)
resultE = tk.Entry(root, textvariable=result)
resultE.grid(row=2, column=1, padx=5)

root.mainloop()