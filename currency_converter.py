from tkinter import *
from currency_converter import CurrencyConverter

c = CurrencyConverter()
expression = ''


def convert():
    global expression
    expression = textbox_1.get()
    converted = c.convert(expression, 'KRW', 'USD')
    textbox_2.insert(1, converted)


def clear():
    textbox_1.delete(0, 'end')
    textbox_2.delete(0, 'end')


def toggle_state(*_):
    if s.get():
        convert['state'] = 'normal'
    else:
        convert['state'] = 'disabled'


# Driver code
if __name__ == '__main__':
    # create application window
    app = Tk()
    s = StringVar()

    # title
    app.title("Won to Dollar Converter")

    # geometry
    app.geometry('400x200')

    # background color
    app.configure(bg='lightblue')

    # image
    img = PhotoImage(file=r"C:\Users\Muffin\Desktop\python\projects\cc.png")
    img1 = img.subsample(2, 2)

    Label(app, image=img1).grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)
    Label(app, text="Korean WON", wraplength=60).grid(row=0, column=0, padx=2, pady=2)
    Label(app, text="American DOLLAR", wraplength=60).grid(row=1, column=0, padx=2, pady=2)

    textbox_1 = Entry(app, textvariable=s)
    textbox_2 = Entry(app)
    textbox_1.grid(row=0, column=1, pady=2)
    textbox_2.grid(row=1, column=1, pady=2)

    textbox_1['textvariable'] = s
    s.trace_add('write', toggle_state)

    # Create buttons and other accessories
    convert = Button(app, text='CONVERT', fg='black', bg='white',
                     command=convert, height=1, width=8, state=DISABLED)
    convert.grid(row=2, column=2, pady=2)

    clear = Button(app, text='CLEAR', fg='black', bg='white',
                   command=clear, height=1, width=8)
    clear.grid(row=2, column=3, pady=2)

# start the GUI
app.mainloop()
