from tkinter import *
from PIL import ImageTk,Image
from time import strftime
from tkinter import ttk
import tkinter.messagebox as messagebox
from datetime import datetime


# def my_time():
#     time_string = datetime.now().strftime('%x')
#     e6.delete(0,END)
#     e6.insert(0,time_string)
#     e6.after(1000,my_time)
    

def notes():
    import notes

def nextPage1():
    root.destroy()
    import inventory
    
def back():
    import homepage
        
root = Tk()
root.title('Inventory Management System | Import Data')
root.state('zoomed')
root.resizable(False, False)

canvas1 = Canvas(root,width = 1920,height = 120)
canvas1.pack()
r1 = canvas1.create_rectangle(0, 0, 1920, 120, outline="cyan4", fill="cyan4")
canvas1.update()

canvas2 = Canvas(root, width=1550, height=160)
canvas2.pack()
r2 = canvas2.create_rectangle(23, 30, 1520, 160, outline="Black")
canvas2.update()

# canvas3 = Canvas(root, width=1500, height=100)
# canvas3.pack()
# r3 = canvas3.create_rectangle(25, 1, 1520, 145, outline="Black")
# canvas3.update()

canvas3 = Canvas(root, width=1550, height=490)
canvas3.pack()
r3 = canvas3.create_rectangle(23, 42, 1520, 480, outline="Black")
canvas3.update()





frame2 = Frame(root,bg = 'black')
frame2.place(x = 0 , y = 120 , width = 1920 , height = 20)



# frame3 = Frame(root,bg = 'white')
# frame3.place(x = 40 , y = 280 , width = 1600 , height = 540)
# canvas2 = Canvas(root,width = 1500,height = 350)
# canvas2.pack()
# r2 = canvas2.create_rectangle(50, 42, 1500, 350, outline="Black")
# canvas2.update()

table = ttk.Treeview(root)
table.pack()
s = ttk.Style(root)
s.theme_use("clam")
s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))
table['columns'] = ('ID', 'Name', 'Date & Time', 'Subject' , 'Note')

table.column('#0' , width = 0, stretch=0)
table.column('ID' , anchor = W, width = 120)
table.column('Name' , anchor = W, width = 120)
table.column('Date & Time' , anchor = W, width = 120)
table.column('Subject' , anchor = W, width = 120)
table.column('Note' , anchor = W, width = 120)

table.heading('#0' ,text = '' ,anchor = W )
table.heading('ID' ,text = 'ID' ,anchor = W )
table.heading('Name' ,text = 'Name' ,anchor = W )
table.heading('Date & Time' ,text = 'Date & Time' ,anchor = W )
table.heading('Subject' ,text = 'Subject' ,anchor = W )
table.heading('Note' ,text = 'Note' ,anchor = W )


table.insert(parent = '', index = 'end', iid = 0 , text = '' , values = (1,'Harsh' ,'03/01/23' , 'Inventory' , 'Just Got Started with tkinter' ))
table.place(x = 50, y = 350, width = 1450, height = 400)


l1 = Label(root, text='Import Data',foreground = 'white',background='cyan4',activebackground = 'Light Blue' ,font=('Times New Roman', 45, 'bold'))
l1.place(x = 550,y = 20)


b1=Button(root, text='   BACK   ',width=10, bd=5, relief=RIDGE, background="white", command=back,
          font=('Times New Roman', 15,'bold'), bg='Light Grey')
b1.place(x=20, y=40)


b_select = Button(root, cursor='hand2', text='SELECT', background="CadetBlue3", bd=7, relief=RIDGE, font=('Times New Roman', 18, 'bold'))
b_select.place(x=950, y=210, width=150, height=45)

b_update = Button(root, cursor='hand2', text='UPDATE', background="CadetBlue3", bd=7, relief=RIDGE, font=('Times New Roman', 18, 'bold'))
b_update.place(x=1150, y=210, width=150, height=45)


search = ['ID','Date','Name' , 'Subject']

search_frame = LabelFrame(root, text = 'Search Import Data',font = ('goudy old type',12, 'bold'))
search_frame.place(x = 40,y = 180,width = 840,height = 90)

combobox = ttk.Combobox(root, values = search,font = ('Times New Roman',15))
combobox.place(x = 100 , y = 220 , width = 200 , height = 30)
combobox.set('Search by')
temp8 = StringVar()
e8 = Entry(root,textvariable = temp8,highlightthickness=1,font = ('Times New Roman',15))
e8.place(x = 320,y = 220 , width = 300 , height = 35 )

b5 = Button(root, text='Search', background = "CadetBlue3",font=('Times New Roman', 22, "bold"))
b5.place(x = 650,y = 220 ,width = 200,height = 35)

root.mainloop()
