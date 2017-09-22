from tkinter import *

root=Tk()
x,y=65,30
canv = Canvas(root,width = x*4,height=y*5,bg="white" )
font="Verdana 12"
i=0
for text in ["X","Y","X and Y","X or Y"]:
    canv.create_text(x / 2 + x * i, y / 2, text=text, font=font, justify=CENTER)
    i+=1
for i in range(1,4):
    canv.create_line(x*i, 0, x*i, y*5)
for i in range(1,5):
    canv.create_line(0, y*i, x*4, y*i)
for i in range(4):
    canv.create_text(x/2+x*i,y/2+y,text="0",font=font,justify=CENTER)
i=0
for text in "0101":
    canv.create_text(x / 2+x*i, y / 2 + y * 2, text=text, font=font, justify=CENTER)
    i+=1
i=0
for text in "1001":
    canv.create_text(x / 2+x*i, y / 2 + y * 3, text="1", font=font, justify=CENTER)
    i+=1

for i in range(4):
    canv.create_text(x/2+x*i,y/2+y*4,text="1",font=font,justify=CENTER)

canv.pack()

root.mainloop()
