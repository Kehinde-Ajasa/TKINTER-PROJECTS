from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry('400x500')

root.config(bg='#0A0A0A')


message = messagebox.showinfo('HOW TO USE', 'Click on the gender that appears in front of you physically on the button representing such gender.')
frame = LabelFrame(root, padx=150, pady=180, bg='black', borderwidth=10)
frame.pack()

header = Label(frame, text="VISITORS' GENDER \nDATABASE SYSTEM",font=('San Franscisco', 30, 'bold'), bg='black', fg='white')
header.grid(row=0, column=0, columnspan=20)


def MALEBUTTON():
	global malenumber
	number = male.get()
	malenumber = int(number)
	male.delete(0, END)
	Total.delete(0, END)
	male.insert(0, (malenumber + 1))


def FEMALEBUTTON():
	global femalenumber
	number = female.get()
	femalenumber = int(number)
	female.delete(0, END)
	Total.delete(0, END)
	female.insert(0, (femalenumber + 1))


def TOTALBUTTON():
	global total
	total = malenumber + 1
	Total.delete(0, END)
	Total.insert(0, (int(female.get()) + int(male.get())))


def reducemale():
	number = int(male.get())
	Total.delete(0, END)
	male.delete(0, END)
	male.insert(0, (number - 1))


def reducefemale():
	number = int(female.get())
	Total.delete(0, END)
	female.delete(0, END)
	female.insert(0, (number - 1))


malebutton = Button(frame, text='MALE', padx=20, font=('San Franscisco', 8, 'bold'), width=3, command=MALEBUTTON)
malebutton.grid(row=1, column=0)
male = Entry(frame, text='0', background='#0A0A0A', fg='white', font=('San Franscisco', 12, 'bold'))
male.insert(0, '0')
male.grid(row=1, column=1)


femalebutton = Button(frame, text='FEMALE', padx=20, font=('San Franscisco', 8, 'bold'), width=3, command=FEMALEBUTTON)
femalebutton.grid(row=3, column=0)
female = Entry(frame,background='#0A0A0A', fg='white', font=('San Franscisco', 12, 'bold'))
female.insert(0, '0')
female.grid(row=3, column=1)


totalbutton = Button(frame, text='TOTAL', padx=20, font=('San Franscisco', 8, 'bold'),width=4, command=TOTALBUTTON)
totalbutton.grid(row=5, column=0)
Total = Entry(frame,background='#0A0A0A', fg='white', font=('San Franscisco', 12, 'bold'))
Total.grid(row=5, column=1)


space1 = Label(frame, text='', fg='black', background='black')
space1.grid(row=2, column=0)

space2 = Label(frame, text='', fg='black', background='black')
space2.grid(row=4, column=0)


editmale = Button(frame, text='-', padx=15, font=('San Franscisco', 8, 'bold'), bg='#0A0A0A', fg= 'white', borderwidth=3, command=reducemale)
editmale.grid(row=1, column=2)

editfemale = Button(frame, text='-', padx=15, font=('San Franscisco', 8, 'bold'), bg='#0A0A0A', fg= 'white', borderwidth=3, command= reducefemale)
editfemale.grid(row=3, column=2)


root.title('Visitors tally system')


mainloop()