from tkinter import *
window=Tk()
canvas=Canvas(window,bg='black',height=580,width=800,relief=RAISED)
canvas.pack()
#moon star
canvas.create_oval(50,30,150,120,fill='white')

canvas.create_text(18,310,text='*',font=('arial','30'),fill='white')
canvas.create_text(400,60,text='*',font=('arial','30'),fill='white')

canvas.create_text(700,30,text='*',font=('arial','30'),fill='white')
canvas.create_text(240,90,text='*',font=('arial','30'),fill='white')
canvas.create_text(360,160,text='*',font=('arial','30'),fill='white')
canvas.create_text(500,40,text='*',font=('arial','30'),fill='white')
canvas.create_text(40,160,text='*',font=('arial','30'),fill='white')

#building
canvas.create_rectangle(700,100,780,280,fill='pink')
canvas.create_line(700,150,780,150,width=4,fill='white')
canvas.create_line(700,210,780,210,width=4,fill='white')

canvas.create_rectangle(500,50,700,280,fill='crimson')
canvas.create_line(500,90,700,90,width=4,fill='white')
canvas.create_line(500,140,700,140,width=4,fill='white')
canvas.create_line(500,200,700,200,width=4,fill='white')
canvas.create_rectangle(400,130,490,270,fill='white')
canvas.create_rectangle(300,80,410,299,fill='plum')
canvas.create_rectangle(400,130,490,270,fill='white')
#tree
canvas.create_rectangle(270,250,290,400,fill='brown')
canvas.create_rectangle(230,250,250,400,fill='brown')
canvas.create_oval(250,210,320,270,fill='lime')
canvas.create_oval(200,190,280,270,fill='lime')
#water
canvas.create_arc(0,220,1300,1000,start=0,extent=180,fill='grey')
canvas.create_arc(180,230,1300,1000,start=0,extent=180,fill='gold')
canvas.create_arc(240,240,1300,1000,start=0,extent=180,fill='brown')
canvas.create_arc(300,250,1300,1000,start=0,extent=180,fill='deep sky blue')
window.mainloop()
