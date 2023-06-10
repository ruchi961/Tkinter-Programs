from tkinter import *
window=Tk()
window.configure(bg='yellow')
window.configure(height=600,width=1200)
def even_odd():
    val=entry1.get()
    if int(val)%2==0:
        lab3.configure(text='Number is even')
    else:
        lab3.configure(text='Number is odd')
    
def prime():
    val=int(entry1.get())
    for i in range(2,val):
        if val%i==0:
            lab3.configure(text='Number is not prime')
            break
    else:
        lab3.configure(text='Number is prime')
   
def perfect():
    val=int(entry1.get())
    v_sum=0
    for i in range(1,val):
        if val%i==0:
            v_sum=v_sum+i
    if v_sum==val:
        lab3.configure(text='Number is perfect')
    else:
        lab3.configure(text='Number is not perfect')
    
lab1=Label(window,text='Please enter any number',bg='blue',fg='white',font=('times','24'))
lab1.place(x=80,y=40)
entry1=Entry(window,font=('times','24'))
entry1.place(x=430,y=40)

but1=Button(window,text="Check if odd/even number",command=even_odd,font=('times','22'),bg='blue',fg='white')
but2=Button(window,text="Check if prime number",command=prime,font=('times','22'),bg='blue',fg='white')
but3=Button(window,text="Check if perfect number",command=perfect,font=('times','22'),bg='blue',fg='white')
but1.place(x=80,y=100)
but2.place(x=420,y=100)
but3.place(x=720,y=100)
lab3=Label(window,text='Result',font=('times','24'),bg='blue',fg='white')
lab3.place(x=400,y=210)
lab3=Label(window,text='-------',font=('times','24'),bg='blue',fg='white')
lab3.place(x=560,y=210)
window.mainloop()
