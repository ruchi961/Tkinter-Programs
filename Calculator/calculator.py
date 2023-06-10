from tkinter import *
import tkinter.messagebox


root=Tk()
root.configure(bg='orange')
#calculation functions
def add():
    try:
        val1=int(enter1.get())
        val2=int(enter2.get())
    except ValueError:
        tkinter.messagebox.showinfo('Error','Please enter an integer and not a string')
    cal=val1+val2
    label.configure(text=cal)
    
def sub():
    try:
        val1=int(enter1.get())
        val2=int(enter2.get())
    except ValueError:
        tkinter.messagebox.showinfo('Error','Please enter an integer and not a string')
    cal=val1-val2
    label.configure(text=cal)
    
def multi():
    try:
        val1=int(enter1.get())
        val2=int(enter2.get())
    except ValueError:
        tkinter.messagebox.showinfo('Error','Please enter an integer and not a string')
    cal=val1*val2
    label.configure(text=cal)
    
def divide():
    try:
        val1=int(enter1.get())
        val2=int(enter2.get())
    except ValueError:
        tkinter.messagebox.showinfo('Error','Please enter an integer and not a string')     
    cal=val1/val2
    label.configure(text=cal)
    
def mod():
    try:
        val1=int(enter1.get())
        val2=int(enter2.get())
    except ValueError:
        tkinter.messagebox.showinfo('Error','Please enter an integer and not a string') 
    cal=val1%val2
    label.configure(text=cal)
    
def clear_it():
    enter1.delete(0,END)
    enter2.delete(0,END)
    label.configure(text='---------')
    
def exit_it():
    root.destroy()

#placing widgets
lab=Label(root,text='CALCULATOR',font=('times','20'))
lab.place(x=650,y=30)
plus=Button(root,text="ADDITION",font=('times','20'),command=add)
minus=Button(root,text='SUBTRACT',font=('times','20'),command=sub)
mul=Button(root,text="MULTIPLY",font=('times','20'),command=multi)
divi=Button(root,text="DIVISION",font=('times','20'),command=divide)
modulo=Button(root,text="MODULUS",font=('times','20'),command=mod)
clear=Button(root,text='CLEAR',font=('times','20'),command=clear_it)
exit=Button(root,text="EXIT",font=('times','20'),command=exit_it)
res=Label(root,text="RESULT",font=('times','20'))
first=Label(root,text="FIRST NUMBER",font=('times','20'))
sec=Label(root,text="SECOND NUMBER",font=('times','20'))
label=Label(root,text='---------',font=('times','20'))
enter1=Entry(root,font=('times','20'))
enter2=Entry(root,font=('times','20'))
enter1.place(x=800,y=100)
enter2.place(x=800,y=200)
label.place(x=800,y=300)
plus.place(x=500,y=400)
minus.place(x=500,y=490)
mul.place(x=700,y=430)
divi.place(x=900,y=400)
modulo.place(x=900,y=490)
clear.place(x=590,y=610)
exit.place(x=760,y=610)
res.place(x=500,y=300)
first.place(x=500,y=100)
sec.place(x=500,y=200)

root.mainloop()
