import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime
import socket
import random

top = tkinter.Tk()
var_time = time.time()
code = ''

def data_entry():
    global conn, cursor
    cap_db = sqlite3.connect('Access.db')
    cursor = cap_db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Entry(Registration_no int, Time text, IP_Address text)')
    cursor.execute('INSERT INTO Entry VALUES(?,?,?)', (Reg_ent.get(), str(datetime.datetime.fromtimestamp(var_time).strftime('%Y-%m-%d %H:%M:%S')), socket.gethostbyname(socket.gethostname())))
    cap_db.commit()
    cursor.close()

def gen_cap():
    n = ''
    for i in range(6):
        cap = random.randint(1, 3)
        if cap == 1:
            value = random.randint(97, 122)
            n += chr(value)
        elif cap == 2:
            value = random.randint(65, 90)
            n += chr(value)
        else:
            value = random.randint(48, 57)
            n += chr(value)
    return n

def check():
    global code
    ck = ent_cap.get()
    ent_cap.delete(0, END)
    r = Reg_ent.get()
    if r.isdigit() and (len(r) == 8 or len(r) == 5):
        if ck == code:
            messagebox.showinfo("ACCESS", "Registration no. : %s \n Accessed Successfully" % r)
            data_entry()
        else:
            messagebox.showinfo("ERROR", "Wrong captcha")
            reset1()
    else:
        messagebox.showinfo("ERROR", "Reg no. Not valid")
        Reg_ent.delete(0, END)

def display():
    c.create_rectangle(80, 10, 240, 70, fill='white')

# Initialize UI components
Reg = tkinter.Label(top, text='Registration Number : ', font='Times 13')
Reg.grid(row=1, column=10)
Reg_ent = Entry(top)
Reg_ent.grid(row=1, column=11)

c = Canvas(top, height=80, width=240)
c.grid(row=3, column=10)

code = gen_cap()
display()
c.create_text(160, 40, text=code, font='Calibri 28 bold')

see = tkinter.Label(top, text='Type the code you see above : ', font='Times 10')
see.grid(row=4, column=10)
ent_cap = Entry(top)
ent_cap.grid(row=5, column=10)

# Submit button to validate input
submit = tkinter.Button(top, text='Submit', relief=GROOVE, command=check, height=2, width=15, bg='lightblue')
submit.grid(row=7, column=10)

def reset1():
    ent_cap.delete(0, END)
    global code
    code = gen_cap()
    display()
    c.create_text(160, 40, text=code, font='Calibri 28 bold')

reset = tkinter.Button(top, text='Reload', relief=GROOVE, height=2, width=15, bg='blue', command=reset1)
reset.grid(row=6, column=10)

top.geometry('450x220')
top.title("PASSWORD REMINDER")
top.mainloop()
