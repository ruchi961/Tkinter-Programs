from tkinter import *
window=Tk()
canvas=Canvas(window,bg='turquoise',height=580,width=800,relief=RAISED)
canvas.pack()
canvas.create_oval(210,100,580,480,fill='yellow')
canvas.create_oval(280,190,370,290,fill='black',)
canvas.create_oval(420,190,510,290,fill='black')

canvas.create_rectangle(295,370,500,380,fill='grey')
canvas.create_rectangle(299,380,330,400,fill='grey')
canvas.create_rectangle(330,350,360,370,fill='grey')
canvas.create_rectangle(360,380,390,400,fill='grey')
canvas.create_rectangle(390,350,420,370,fill='grey')
canvas.create_rectangle(420,380,450,400,fill='grey')
canvas.create_rectangle(450,350,480,370,fill='grey')
canvas.create_arc(412,260,580,480,fill='grey',start=290,extent=43)
window.mainloop()
