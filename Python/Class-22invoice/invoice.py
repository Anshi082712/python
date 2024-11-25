
from tkinter import*
from reportlab.pdfgen import canvas
root = Tk()
screen= Tk()
root.geometry("800x800")
global e1,e2,e3,ea,eb,ec,ed,ee,ef,e4
L1= Label(root,text="name")
L1.grid(row=0, column=0)
e1= Entry(root)
e1.grid(row=0, column=1)

L2=Label(root, text="email")
L2.grid(row=1, column=0)
e2= Entry(root)
e2.grid(row=1, column=1)

L3= Label(root, text="phonenumber")
L3.grid(row=2, column=0)
e3= Entry(root)
e3.grid(row=2, column=1)

L4= Label(root, text="coffee")
L4.grid(row=3, column=0)

L5= Label(root, text="quantity")
L5.grid(row=3, column=1)

L6= Label(root, text="price")
L6.grid(row=3, column=2)

L7= Label(root, text="Expresso")
L7.grid(row=4, column=0)
ea= Entry(root)
ea.grid(row=4, column=1)
eb= Entry(root)
eb.grid(row=4, column=2)



L8= Label(root, text="Cappachino")
L8.grid(row=5, column=0)
ec= Entry(root)
ec.grid(row=5, column=1)
ed= Entry(root)
ed.grid(row=5, column=2)

L9= Label(root, text="Americano")
L9.grid(row=6, column=0)
ee= Entry(root)
ee.grid(row=6, column=1)
ef= Entry(root)
ef.grid(row=6, column=2)

L10= Label(root, text="total")
L10.grid(row=7, column=1)
v= IntVar()
e4= Entry(root, textvariable=v)
e4.grid(row=7, column=2)


def total():
    r= int(ea.get())*int(eb.get())+int(ec.get())*int(ed.get())+int(ee.get())*int(ef.get())
    v.set(r)

#We are using canvas to generate a pdf bill and for that we have to do the following steps are
#1. import reportlab at the top, then use canvas.Canvas to give the name of the pdf
#2. Draw a string function with position
#3. Then we use save to save itfrom tkinter import*




#We are using canvas to generate a pdf bill and for that we have to do the following steps are
#1. import reportlab at the top, then use canvas.Canvas to give the name of the pdf
#2. Draw a string function with position
#3. Then we use save to save it
def bill():
    c=canvas.Canvas("invoice.pdf", pagesize=(400,1100))
    c.drawString(200,50,"Name:"+e1.get())
    #200 abd 50 are the x and y axis
    c.drawString(200,100,"Email:"+e2.get())
    c.drawString(200,150,"Phonenumber:"+e3.get())
    c.drawString(200,200,"Expresso"+ea.get())
    c.drawString(200,250,"Cappachino"+ec.get())
    c.drawString(200,300,"Americano"+ee.get())
    c.drawString(200,300,"Total:"+e4.get())
    c.save()
    
    
    
    
B= Button(root, text="Generate bill", command=bill)
B.grid(row=8, column=1)

C= Button(root, text= "Total", command=total)
C.grid(row=8, column=2)
root.mainloop()