from tkinter import *
window = Tk()
window.title("MILE TO KM CONVERTER")
window.minsize(width=500, height=300)
window.config(padx=20,  pady=20)
on = True



def calculate():
    miles = float(miles_to_input.get())
    km = miles * 1.609
    kilometer_label.config(text=f"{km}")

miles_to_input = Entry(width=7)
miles_to_input.grid(column=1, row=0)

miles_to_label = Label(text="MILE")
miles_to_label.grid(column=2, row=0)
equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)
km = Label(text="km")
km.grid(column=2,row=1)
kilometer_label = Label(text="0")
kilometer_label.grid(column=1, row=1)



button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



window.mainloop()