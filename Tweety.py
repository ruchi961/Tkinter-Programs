from tkinter import *
window=Tk()
canvas=Canvas(window,bg='pink',height=900,width=1000)
canvas.pack()
canvas.create_oval(300,50,640,350,width=3,outline='brown',fill='yellow')
canvas.create_arc(300,4,450,110,start=330,extent=3,fill='blue')
canvas.create_arc(240,5,490,85,start=330,extent=3,fill='blue')
canvas.create_oval(350,140,430,300,fill='white',width=3,outline='brown')
#eyes
canvas.create_oval(500,140,580,300,fill='white',width=3,outline='brown')
canvas.create_oval(390,180,430,250,width=3,outline='black',fill='blue')
canvas.create_oval(540,180,580,250,width=3,outline='black',fill='blue')
canvas.create_oval(410,210,430,240,width=3,fill='black')
canvas.create_oval(560,210,580,240,width=3,fill='black')


#body
canvas.create_arc(400,400,510,520,start=90,extent=180,width=3,fill='yellow',outline='brown')
canvas.create_arc(440,400,550,520,start=270,extent=180,width=3,fill='yellow',outline='brown')

canvas.create_arc(350,220,595,390,fill='yellow',width=3,outline='brown',start=180,extent=180)
canvas.create_rectangle(354,300,590,320,fill='yellow',outline='yellow')
canvas.create_rectangle(430,580,460,610,width=3,outline='brown',fill='yellow')
canvas.create_rectangle(490,580,520,610,width=3,outline='brown',fill='yellow')
canvas.create_rectangle(445,390,505,420,width=3,outline='brown',fill='yellow')
canvas.create_oval(420,390,530,500,width=3,outline='brown',fill='yellow')
canvas.create_oval(400,450,550,600,width=3,outline='brown',fill='yellow')
canvas.create_arc(430,430,529,468,start=180,extent=180,fill='yellow',outline='yellow')
#legs

canvas.create_oval(230,630,460,720,width=3,fill='orange',outline='red')
canvas.create_oval(490,630,710,720,width=3,fill='orange',outline='red')



canvas.create_rectangle(430,613,460,680,fill='orange',width=3,outline='red')
canvas.create_rectangle(490,613,520,680,fill='orange',width=3,outline='red')
canvas.create_arc(450,300,500,343,width=3,fill='orange',outline='red',start=160,extent=210)
canvas.create_oval(440,310,500,330,width=3,fill='orange',outline='red')

canvas.create_arc(360,280,420,340,width=3,start=0,extent=180,fill='yellow',outline='brown')
canvas.create_arc(353,286,430,350,fill='yellow',outline='yellow',start=0,extent=180)
canvas.create_arc(510,280,570,340,width=3,start=0,extent=180,fill='yellow',outline='brown')
canvas.create_arc(505,283,576,350,fill='yellow',outline='yellow',start=0,extent=180)

canvas.create_rectangle(359,650,457,684,fill='orange',outline='orange')
canvas.create_rectangle(493,650,557,684,fill='orange',outline='orange')
window.mainloop()
