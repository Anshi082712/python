#------------------Listboxes and scrollbar-----------
#Listboxes are boxes where we can have list from which we can select.
#scoolbar is to scroll. We can give this too listbox in horizontal and vertical.

#Scrollbar widget is used to scroll given inside the screen used with listbox or any box. 
#Properties of scollbar:
#yscrollcommand/xscrollcommand is to put scrollbar
#if you are creating vertical scrollbar then use yscrollcommand is used that thing where you want to attach scrollbar. In below case its lixtbox so use it here otherwsie xscollcommand in horizontal case
#selectedmode set to multiple if you want to slect multiple

#later use yview/xview with listbox to scroll it veruically

#cuseselection()is used select and whereever you place your cusror select taht item

from tkinter import *
root=Tk()
root.geometry("800x800")
root.configure(bg="#000080")
f=Frame(root)
s=Scrollbar(f, orient=VERTICAL)
li1=Listbox(f, width=100, height=10, bg="pink", font=("Times Roman", 14, "bold italic"), fg="red",yscrollcommand=s.set, selectmode=MULTIPLE ) # coconnect your listbox with scrollbar using ycrollcommand. If yo want multiple things to be selected use MULTIPLE


#add items in listbox usng insert
li1.insert(END, "Samosa")
li1.insert(END, "kaju katli")
li1.insert(END, "pakori")
li1.insert(END, "gulab jamun")
li1.insert(END, "ladoo")
li1.insert(END, "rasmalaigh")
li1.insert(END, "Chum chum")
li1.insert(END, "Jalebi")

s.config(command=li1.yview)
s.pack(side=RIGHT, fill=Y) # mention side you want scrollbar to be placed
li1.pack()
f.pack()
l1=Label(root, text="hello please select")
l1.pack()

#config means to change properties of widgets later after creating
def delete():
  li1.delete(ANCHOR)
  l1.config(text="")
def selectandget():
  l1.config(text=li1.get(ANCHOR))
def deleteall():
  li1.delete(0, END)
def selectmultiple():
  result=""
  for i in li1.curselection(): # i variable gets inside liztbox and whatvere item is selected ite gets you that
    result=result+ li1.get(i) +"\n" # ite like enter \n is for new line
  l1.config(text=result)
  
def deletemultiple():
  result=""
  for i in li1.curselection(): 
    li1.delete(i) # is getting everu slected item and we give to delete fun
    l1.config(text="")
  
#delete button
b1=Button(root, text="delete", command=delete)
b1.pack()

#select item
b2=Button(root, text="select",command=selectandget)
b2.pack()

#delete all
b3=Button(root, text="deleteall",command=deleteall)
b3.pack()

#select multiple
b4=Button(root, text="select multiple",command=selectmultiple)
b4.pack()

#delete multiple
b5=Button(root, text="delete multiple",command=deletemultiple)
b5.pack()
root.mainloop()