from tkinter import *
window=Tk()
canvas=Canvas(window,bg='turquoise',height=580,width=800,relief=RAISED)
canvas.pack()
canvas.create_oval(210,100,580,480,fill='yellow',width=3)
canvas.create_oval(280,190,370,290,fill='white',width=3)
canvas.create_oval(310,230,340,270,fill='black')
canvas.create_oval(420,190,510,290,fill='white',width=3)
canvas.create_oval(450,230,480,270,fill='black')
canvas.create_arc(300,250,499,420,start=180,extent=180,fill='brown',outline='black',width=3)
canvas.create_rectangle(300,332,499,355,fill='white',width=3)
canvas.create_rectangle(370,355,435,420,fill='orange',outline='red',width=3)
canvas.create_arc(370,380,435,450,start=180,extent=180,fill='orange',outline='red',width=3)
canvas.create_rectangle(372,413,433,420,fill='orange',outline='orange')
canvas.create_rectangle(400,356,405,430,fill='red',outline='red')
window.mainloop()
