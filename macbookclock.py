from tkinter import *
import time


clock = Tk()

clock.title('My Own clock')
clock.config(bg='black')
clock.geometry('400x300')



def myclock():
	hour = time.strftime('%I')
	minute = time.strftime('%M')
	second = time.strftime('%S')
	meridian = time.strftime('%p')
	day = time.strftime('%a')
	month = time.strftime('%B')
	year = time.strftime('%Y')
	main_date = time.strftime('%d')

	label = Label(clock, text= ' ', bg='black')
	label.grid(row=0, column=0)

	label2 = Label(clock, text= ' ', bg='black')
	label2.grid(row=2, column=0)
	hour_button = Button(clock, text=hour, bg='#0A0A0A')
	hour_button.config(font=('San Franscisco', 213, 'bold'), fg='white', borderwidth=0)
	hour_button.grid(row=2, column=2)
	line = Canvas(width=588, height=17, bg='black', borderwidth=-9)
	line.grid(row=2, column=2)

	label1 = Label(clock, text= ' ', bg='black')
	label1.grid(row=2, column=3)

	minute_button = Button(clock, text=minute, bg='#0A0A0A',pady=82)
	minute_button.config(font=('San Franscisco', 150, 'bold'), fg='white', borderwidth=0)
	minute_button.grid(row=2, column=4)
	line2 = Canvas(width=417, height=17, bg='black', borderwidth=-9)
	line2.grid(row=2, column=4)

	meridian_button = Button(clock, text=meridian, bg='#0A0A0A')
	meridian_button.config(font=('San Franscisco', 30, 'bold'), fg='white', borderwidth=0, pady=238)
	meridian_button.grid(row=2, column=1, columnspan=1)
	line1 = Canvas(width=106, height=17, bg='black', borderwidth=-9)
	line1.grid(row=2, column=1)


	clock.after(60000, myclock)

myclock()
clock.mainloop()