import tkinter
from tkinter import ttk

screen=tkinter.Tk()
screen.geometry("400x500")
screen.title("FirstApp")
screen.config(bg="gold")

#tkinter.Label(text="Firstname:",bg='gold',fg='red',font='Candara 15').pack()
#tkinter.Label(text="Firstname:",bg='gold',fg='red',font='Candara 15').place(x=0,y=0)
#tkinter.Label(text="Lasstname:",bg='gold',fg='red',font='Candara 15').place(x=0,y=40)

tkinter.Label(text="Firstname:",bg='gold',fg='red',font='Candara 15').grid(row=0,column=0,sticky='W')
tkinter.Label(text="Lastname:",bg='gold',fg='red',font='Candara 15').grid(row=1,column=0,sticky='W')

tkinter.Entry().grid(row=0,column=1,sticky='W')
tkinter.Entry().grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=0, text="Male",bg='gold',fg='red',font='Candara 15').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1, text="Female",bg='gold',fg='red',font='Candara 15').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text="Programming",bg='gold',fg='red',font='Candara 15').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text="Reading",bg='gold',fg='red',font='Candara 15').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text="Travelling",bg='gold',fg='red',font='Candara 15').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text="Cooking",bg='gold',fg='red',font='Candara 15').grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Rajkot','Baroda','Surat','Jamnagar']
ttk.Combobox(values=city).grid(row=7,column=0)

tkinter.Button(text="Submit",fg='red',font='Candara 15').place(x=180,y=280)
screen.mainloop()