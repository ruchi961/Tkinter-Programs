from tkinter import *
window=Tk()
canvas=Canvas(window,bg='turquoise',height=580,width=800,relief=RAISED)
canvas.pack()
canvas.create_oval(210,100,580,480,fill='yellow')
canvas.create_oval(280,170,370,270,fill='black',)
canvas.create_oval(420,170,510,270,fill='black')
canvas.create_arc(300,280,499,430,start=180,extent=180,fill='black')
canvas.create_arc(295,280,503,390,start=180,extent=180,fill='yellow',outline='yellow')
canvas.create_oval(250,280,300,340,fill='red',width=3,outline='red')
canvas.create_oval(490,280,540,340,fill='red',width=3,outline='red')
canvas.create_oval(200,95,590,130,width=12,outline='blue')
window.mainloop()