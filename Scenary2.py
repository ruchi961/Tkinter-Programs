from tkinter import *
window=Tk()
canvas=Canvas(window,bg='skyblue',height=580,width=800,relief=RAISED)
canvas.pack()
canvas.create_oval(70,60,170,150,fill='gold')
canvas.create_polygon(200,300,400,200,300,150,fill='brown')
canvas.create_polygon(180,300,530,300,300,150,fill='white')
canvas.create_polygon(400,300,600,300,500,150,fill='white')
canvas.create_polygon(200,300,500,300,300,150,fill='brown')
canvas.create_polygon(600,400,700,100,800,350,fill='brown')
canvas.create_polygon(620,400,720,100,810,350,fill='white')
canvas.create_polygon(200,300,500,300,300,150,fill='brown')
canvas.create_polygon(500,340,600,50,700,350,fill='brown')


canvas.create_rectangle(0,300,800,1000,fill='dodger blue')
canvas.create_arc(400,400,1000,900,start=0,extent=180,fill='lime')
canvas.create_rectangle(450,450,470,530,fill='brown')
canvas.create_rectangle(520,370,539,510,fill='brown')
canvas.create_oval(420,300,500,500,fill='lawn green')
canvas.create_oval(480,150,580,400,fill='green')

window.mainloop()
