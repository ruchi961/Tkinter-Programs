from tkinter import *
import tkinter.messagebox
import webbrowser
info=[]
root=Tk()
root.configure(bg='yellow')
root.geometry("9000x900")
def openit():
    webbrowser.open("any website")
def confirm():

    val1=enter1.get()
    info.append(val1)
    val2=enter2.get()
    info.append(val2)
    val3=enter3.get()
    info.append(val3)
    if val1=="" or val2=="" or val3=="":
        tkinter.messagebox.showinfo('Error','Please fill details')
    else:
        
        var1=op1.get()
        var2=op2.get()
        var3=op3.get()
        var4=op4.get()
        fl=False
        if (var1!=" " and var2!=" ") or (var1!=" " and var3!=" "):
            fl=True
                
        elif var4!=" " and var2==" " and var3==" " and var1==" ":
            fl=True
            var2=var3=var1="-------------"
            print(fl,"dd")
        if fl:


            
            root2=Tk()
            root2.configure(bg='pink')
            root2.geometry("9000x900")
            lab1=Label(root2,text="Phone number/Email id",font=('times','20'))
            lab2=Label(root2,text="location",font=('times','20'))
            lab3=Label(root2,text="address",font=('times','20'))
            lab4=Label(root2,text='serving size',font=('times','20'))
            lab5=Label(root2,text='Veg pizza',font=('times','20'))
            lab7=Label(root2,text='Non-veg',font=('times','20'))
            lab6=Label(root2,text='Sider/Beverages',font=('times','20'))
            lab10=Label(root2,text=val1,font=('times','20'))
            lab20=Label(root2,text=val2,font=('times','20'))
            lab30=Label(root2,text=val3,font=('times','20'))
            
            lab40=Label(root2,text=var1,font=('times','20'))
            lab50=Label(root2,text=var2,font=('times','20'))
            lab70=Label(root2,text=var3,font=('times','20'))
            lab60=Label(root2,text=var4,font=('times','20'))
            label=Button(root2,text='Pay now',font=('times','20'),command=openit)
            label.place(x=400,y=700)
            lab1.place(x=100,y=100)
            lab2.place(x=100,y=160)
            lab3.place(x=100,y=220)
            lab4.place(x=100,y=280)
            lab5.place(x=100,y=320)
            lab6.place(x=100,y=360)
            lab7.place(x=100,y=400)
            lab10.place(x=400,y=100)
            lab20.place(x=400,y=160)
            lab30.place(x=400,y=220)
            lab40.place(x=400,y=280)
            lab50.place(x=400,y=320)
            lab60.place(x=400,y=360)
            lab70.place(x=400,y=400)
            root2.mainloop()
        else:
            tkinter.messagebox.showinfo('Error','Please select atleast one pizza and its serving size or atleast any side')
    
def clear():
    enter1.delete(0,END)
    enter2.delete(0,END)
    enter3.delete(0,END)
    
def exit():
    root.destroy()
op1=StringVar(value=" ")
op2=StringVar(value=" ")
op3=StringVar(value=" ")
op4=StringVar(value=" ")
lab=Label(root,text="ONLINEPIZZA DELIVERY",font=('times','20'))
lab.place(x=400,y=30)
lab1=Label(root,text="Enter Phone number/Email id",font=('times','20'))
lab2=Label(root,text="Enter location",font=('times','20'))
lab3=Label(root,text="Enter address",font=('times','20'))
lab4=Label(root,text='Please select serving size',font=('times','20'))
lab5=Label(root,text='Veg pizza',font=('times','20'))
lab7=Label(root,text='Non-veg',font=('times','20'))
lab6=Label(root,text='Sider/Beverages',font=('times','20'))
but1=Button(root,text="Confirm order",font=('times','20'),command=confirm)
but2=Button(root,text="Reorder",font=('times','20'),command=clear)
but3=Button(root,text="Exit",font=('times','20'),command=exit)

rad1=Radiobutton(root,text='serves 2',variable=op1,value='serves 2',font=('times','20'))
rad2=Radiobutton(root,text='serves 4',variable=op1,value='serves 4',font=('times','20'))
rad3=Radiobutton(root,text='serves 1',variable=op1,value='serves 1',font=('times','20'))

rad4=Radiobutton(root,text='Margerita',variable=op2,value='Margerita',font=('times','20'))
rad5=Radiobutton(root,text='Garden fest',variable=op2,value='Garden Fest',font=('times','20'))
rad6=Radiobutton(root,text='Paneer Tandoor',variable=op2,value='Paneer Tandoor',font=('times','20'))

rad7=Radiobutton(root,text='Crab',variable=op3,value='Crab',font=('times','20'))
rad8=Radiobutton(root,text='Chicken Tandoor',variable=op3,value='Chicken Tandoor',font=('times','20'))
rad9=Radiobutton(root,text='Nonveg. Exotica',variable=op3,value='Nonveg. Exotica',font=('times','20'))

radd1=Radiobutton(root,text='french fries',variable=op4,value='french fries',font=('times','20'))
radd2=Radiobutton(root,text='Coke',variable=op4,value='coke',font=('times','20'))
radd3=Radiobutton(root,text='Sprit',variable=op4,value='sprite',font=('times','20'))

radd1.place(x=1090,y=280)
radd2.place(x=1090,y=330)
radd3.place(x=1090,y=380)

rad7.place(x=1090,y=450)
rad8.place(x=1090,y=509)
rad9.place(x=1090,y=560)

rad4.place(x=500,y=450)
rad5.place(x=500,y=509)
rad6.place(x=500,y=560)

rad1.place(x=500,y=330)
rad2.place(x=500,y=380)
rad3.place(x=500,y=280)
enter1=Entry(root,font=('times','20'))
enter2=Entry(root,font=('times','20'))
enter3=Entry(root,font=('times','20'))
lab1.place(x=100,y=100)
lab2.place(x=100,y=160)
lab3.place(x=100,y=220)
lab4.place(x=100,y=280)
lab5.place(x=100,y=440)
lab6.place(x=800,y=280)
lab7.place(x=800,y=440)
but1.place(x=350,y=710)
but2.place(x=600,y=710)
but3.place(x=850,y=710)
enter1.place(x=500,y=100)
enter2.place(x=500,y=160)
enter3.place(x=500,y=220)

root.mainloop()
