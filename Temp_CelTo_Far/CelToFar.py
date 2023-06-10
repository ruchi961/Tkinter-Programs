from tkinter import *
import tkinter.messagebox
def calculate():
    try:
        lab3.configure(text='   ')
        val=int(enter.get())
        res=(val*1.8)+32
        lab3.configure(text=res)
    except ValueError:
       tkinter.messagebox.showinfo('ERROR','Please enter value in order to calculate result')
        
window=Tk()
window.configure(bg='green')
lab1=Label(window,text="Please enter temperature in celsius",font=('times','20'))
lab1.place(x=120,y=130)
lab2=Label(window,text="The temperature in fahrenheit is",font=('times','20'))
lab2.place(x=120,y=180)
cal=Button(window,text="Calculate",command=calculate,font=('times','20'))
cal.place(x=450,y=250)
enter=Entry(window,font=('times','20'))
enter.place(x=550,y=130)
lab3=Label(window,text='-----------------',font=('times','20'))
lab3.place(x=550,y=180)
window.mainloop()
