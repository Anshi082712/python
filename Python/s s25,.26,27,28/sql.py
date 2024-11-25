#-------------------------sqlite-------------------
#Sqlite ia a inbuilt database in python in library form whihc you can use to store data in games, website, software, apps. Sqlite is small database so only small data can be stored. Though it do not requires any installation taht is ggod thing saving time and also if anything happens while installation there will be no connection so sqlite is good as no installation requires.

#But in case if yu want to store large data databases like MYSQL, firebase, oracle are used.

#Also coding for database is pretty much the same. queries are same. so if you learm one database you can do coding in other databases by yourself.

#database also uses language called as SQL.

#Steps to to code in Sqlite
#1. import sqlite library
#2. connect with sqlite database usig connect method. syntax : variablname=sqlite3.connect("database.db"). if database is alreday there with that name it will get connect to existing db but if not there then it will create database with that name
#3. Create cusror object using cusror function . cursor() helps you to execute the query once written.
#4. Create table as data here is always stored in grid form. syntax to create table : CREATE TABLE tablename(columnname datatype, columname2 datatype, columname3 datatype, coulnname4 datatype and so on)
#5. Insert data in table using insert syntax : INSERT Into tablename VALUES (data1, data2, data3 so on)
#6. want to get data on screen : use select to select what data you want and then use fetchall. syntax : SELECT * from tablename. Use fetchall to get data afterwards
#7. To update any data syntax : UPDATE tablename set name="hamzah" where id=1.
#8. To delete the data syntax : DELETE table tablename where id=1

#To get thinsg from entry box use get and to insert use insert ()
#------------------------------------------------------------------------
import sqlite3
from tkinter import *


root=Tk()

#use connec fun
connection=sqlite3.connect("database.db")

#create cusror object0
crsr=connection.cursor()

#CREATE TABLE
#sql="""CREATE TABLE employee(
#s_no int,
#f_name text,
#l_name text,
#Gender text,
#DOJ vaechar(40)
#)"""
#use cursor
#crsr.execute(sql)


#Insert data from textboxes to database table employee

#insert manually data

crsr.execute("INSERT INTO employee VALUES(1, 'hamzah', 'iqbal', 'male', '12/12/2023')")
def add():
  crsr.execute("INSERT INTO employee VALUES(:s_no ,:f_name, :l_name, :Gender, :DOJ)", {
    's_no': e1.get(),
    'f_name': e2.get(),
    'l_name': e3.get(),    
    'Gender': e4.get(),
    'DOJ' : e5.get()
      }) #here the variables have been created and these variable will get the textbox values by creating a dictonary
  #delete as soon as data is added into table
  e1.delete(0, END),
  e2.delete(0, END),
  e3.delete(0, END),
  e4.delete(0, END),
  e5.delete(0, END)
  #use commit always at the end to save permantatly
  connection.commit()
#------------------------------------------------------------
def query():
  #use selct to slecet data want to get and use fetchall to fetch the data
  t1=e6.get()
  SQL="select * from employee where s_no =:t1"
  crsr.execute(SQL, {'t1':t1})
  ANS=crsr.fetchall() #ans is liks a list where yiu have all data. To get all data from ans we use for loop
  records=""
  for record in ANS:
    records=str(record[0]) + "\n" + record[1] + "\n" + record[2] + "\n" + record[3] + "\n" + record[4] + "\n"
  #put this in label on _ScreenUnits
  l7=Label(root, text=records)
  l7.grid(row=9, column=0)
#------------------------------------------------------------------------
#here update query is used to update the details and call this function on update button which is in update function
def edit():
  crsr.execute("""UPDATE employee SET 
  S_no =:s_no,
  f_name=:f_name,
  l_name=:l_name, 
  Gender=:gender,
  DOJ=:doj
  where oid=:Aid
  """, #In above left side is column name and right side varoable name. in the variable which is on right we will get Entry box values and variable will those values to column
   {
    "s_no" :e7.get(),
    "f_name" :e8.get(),
    "l_name" :e9.get(),
    "gender" :e10.get(),
    "doj" :e11.get(),
    "Aid" :e6.get(),
                
                
              })
  connection.commit()


#----------------------------------------------------------------------  
  #here second page is created where we have details of id needs ti be updatedand uedit function is called
def update():
  root2=Tk()
  l7=Label(root2, text = "Staff number").grid(row=0, column=0)
  global e7
  e7=Entry(root2)
  e7.grid(row=0, column=1)

  l8=Label(root2, text = "First name").grid(row=1, column=0)
  global e8
  e8=Entry(root2)
  e8.grid(row=1 ,column=1)
  l9=Label(root2, text = "Last name").grid(row=2, column=0)
  global e9
  e9=Entry(root2) 
  e9.grid(row=2 ,column=1)
  l10=Label(root2, text = "Gender").grid(row=3, column=0)
  global e10
  e10=Entry(root2)
  e10.grid(row=3 ,column=1)
  l11=Label(root2, text = "Date of joining").grid(row=4, column=0) 
  global e11
  e11=Entry(root2)
  e11.grid(row=4 ,column=1)
  e7.delete(0, END)
  e8.delete(0, END)
  e9.delete(0, END)
  e10.delete(0, END)
  e11.delete(0, END)

  #get data and insert inro entrybox
  t1=e6.get()
  SQL="select * from employee where s_no =:t1"
  crsr.execute(SQL, {'t1':t1})
  ANS=crsr.fetchall() #ans is liks a list where yiu have all data. To get all data from ans we use for loop
  records=""
  for record in ANS:
  #put this data in Entry use insert
    e7.insert(0,record[0])
    e8.insert(0,record[1])
    e9.insert(0,record[2])
    e10.insert(0,record[3])
    e11.insert(0,record[4])
    
  

  b1=Button(root2,text="update", command=edit).grid(row=6, columnspan=2)
  

#--------------------------------------------------------------------

l1=Label(root, text = "Staff number").grid(row=0, column=0)
e1=Entry(root)
e1.grid(row=0, column=1)

l2=Label(root, text = "First name").grid(row=1, column=0) 
e2=Entry(root)
e2.grid(row=1 ,column=1)
l3=Label(root, text = "Last name").grid(row=2, column=0)
e3=Entry(root)
e3.grid(row=2 ,column=1)
l4=Label(root, text = "Gender").grid(row=3, column=0) 
e4=Entry(root)
e4.grid(row=3 ,column=1)
l5=Label(root, text = "Date of joining").grid(row=4, column=0) 
l6=Label(root, text = "Enter id").grid(row=7, column=0)
e5=Entry(root)
e5.grid(row=4 ,column=1)
global e6
e6=Entry(root)
e6.grid(row=7, column=1)

b1=Button(root,text="Add record to database",command=add).grid(row=6, columnspan=2)
b2=Button(root,text="Query the database", command=query).grid(row=8, columnspan=2, pady=30)
b3=Button(root,text="edit", command=update).grid(row=10, columnspan=2, pady=30)

root.mainloop()
#create table