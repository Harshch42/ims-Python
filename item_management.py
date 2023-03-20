from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

root=Tk()
root.state('zoomed')
root.title('Items Management')

canvas=Canvas(root, width=1920, height=120)
canvas.pack()
r1=canvas.create_rectangle(0, 0, 1920, 150, outline='cyan4', fill='cyan4')
canvas.update()

canvas2=Canvas(root, width=1500, height=290)
canvas2.pack()
r2=canvas2.create_rectangle(25,10,1500,290,outline='Black')
canvas2.update()

def back():
    root.destroy()
    import homepage

def clear():
    e1.delete(0, END)
    e3.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)

def save():
    if (e1.get() == '') or (e3.get() == '') or (e5.get() == '') or (e6.get() == '') or (e8.get() == '') or (
            e9.get() == '' or e11.get()==''):
        messagebox.showerror("Error", "Please fill all the details")
    else:
        table.insert(parent='', index='end', text='',
                     values=(e1.get(), e3.get(), e5.get(), e6.get(), e8.get(), e9.get(), e11.get()))

def my_time():
    time_string = datetime.now().strftime('         %x ')
    e14.delete(0,END)
    e14.insert(0,time_string)
    e14.after(1000,my_time)

def updatebutton():
        selected = table.focus()
        table.item(selected, text="", values=(l14.get(), l3.get(), l1.get(), l6.get(
        ), l8.get(), l9.get(), l11.get()))
        l14.set("")
        l3.set("")
        l1.set("")
        l6.set("")
        l8.set("")
        l9.set("")
        l11.set("")



table = ttk.Treeview(root)
table.pack()

s = ttk.Style(root)
s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

table['columns'] = ('date', 'itemname', 'itemid', 'totalqty', 'price', 'supplier', 'label')
table.column('#0', width=0, stretch=0)
table.column('date', anchor=W, width=50)
table.column('itemname', anchor=W, width=50)
table.column('itemid', anchor=W, width=80)
table.column('totalqty', anchor=W, width=80)
table.column('price', anchor=W, width=80)
table.column('supplier', anchor=W, width=50)
table.column('label', anchor=W, width=100)

table.heading('#0', text='', anchor=CENTER)
table.heading('date', text='Date', anchor=CENTER)
table.heading('itemname', text='Item Name', anchor=CENTER)
table.heading('itemid', text='Item Id', anchor=CENTER)
table.heading('totalqty', text='Quantity', anchor=CENTER)
table.heading('price', text='Price', anchor=CENTER)
table.heading('supplier', text='Supplier', anchor=CENTER)
table.heading('label', text='Label', anchor=CENTER)
table.place(x=40, y=490, width=1480, height=300)

vsb = ttk.Scrollbar(table, orient='vertical')
vsb.configure(command=table.yview)
table.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y, side=RIGHT)

s = ttk.Style(root)
s.theme_use("clam")
s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

l4 = Label(root, text='Items Management ',foreground = 'white',background='cyan4',
           activebackground = 'Light Blue' ,font=('Times New Roman', 45, 'bold'))
l4.place(x = 500,y = 20)

l1=Label(root, text='Item Id: ', font=('Times new Roman',18))
l1.place(x=100, y=170)
temp1=StringVar()
e1=Entry(root, textvariable=temp1,font=('Times', 17))
e1.place(x=280, y=170)

l3=Label(root,text='Item Type: ',font=('Times new Roman',18))
l3.place(x=530,y=170)
temp2=StringVar()
e3=Entry(root,textvariable=temp2, font=('Times new Roman', 17))
e3.place(x=780, y=170)

l5=Label(root, text='Company Brand ', font=('Times new Roman', 18))
l5.place(x=100, y=230)
temp3=StringVar()
e5=Entry(root, textvariable=temp3,font=('Times new Roman', 17))
e5.place(x=280, y=230)

l6=Label(root, text='Quantity: ', font=('Times new Roman', 18))
l6.place(x=530, y=230)
temp4=StringVar()
e6=Entry(root, textvariable=temp4,font=('Times new Roman', 17))
e6.place(x=780, y=230)

l8=Label(root, text='Price: ', font=('Times new Roman', 18))
l8.place(x=1050, y=230)
temp5=StringVar()
e8=Entry(root,textvariable=temp5, font=('Times new Roman', 17))
e8.place(x=1150, y=230)

l9=Label(root, text='Label: ', font=('Times', 18))
l9.place(x=100, y=290)
temp6=StringVar()
e9=Entry(root, textvariable=temp6, font=('Times', 17))
e9.place(x=280, y=290)

l10=Label(root, text='Calculate Total Quantity: ', font=('Times', 18))
l10.place(x=530, y=290)
temp7=StringVar()
e10=Entry(root, textvariable=temp7, font=('Times New Roman', 17))
e10.place(x=780, y=290)

l11=Label(root, text='Supplier: ', font=('Times New Roman', 18))
l11.place(x=1050, y=290)
temp8=StringVar()
e11=Entry(root,textvariable=temp8, font=('Times New Roman', 17))
e11.place(x=1150, y=290)

l14=Label(root, text='Date: ', font=('Times New Roman', 18))
l14.place(x=1050, y=170)
e14=Entry(root,width=20, font=('Times New Roman', 17))
e14.place(x=1150, y=170)
my_time()

#l15=Label(root, text='Calculate Total Cost: ', font=('Times', 18))
#l15.place(x=100, y=360)
#e15=Entry(root, textvariable=temp7, font=('Times New Roman', 17))
#e15.place(x=380, y=360)

b1=Button(canvas, text='   BACK   ',width=10, bd=5, relief=RIDGE, background="white", command=back,
          font=('Times New Roman', 15,'bold'), bg='Light Grey')
b1.place(x=20, y=40)

b2=Button(root, text='  UPDATE  ', relief=RIDGE,width=10, font=('Times New Roman', 15, 'bold'), bg='cadetblue3', bd=5,
          command=updatebutton)
b2.place(x=900, y=430)

b3=Button(root, text='    SEARCH  ', relief=RIDGE, font=('Times New Roman', 15 ,'bold'), bg='cadetblue3', bd=5)
b3.place(x=700, y=430)

b4=Button(root, text='     ADD    ',relief=RIDGE,width=10, font=('Times New Roman', 15,'bold'), bg='cadetblue3',command=save, bd=5)
b4.place(x=500, y=350)

#b5=Button(root, text='CALCULATE' ,relief=RIDGE,width=10, font=('Times New Roman', 15,'bold'), bg='cadetblue3', bd=5)
#b5.place(x=650, y=350)

b6=Button(root, text='  DELETE  ', relief=RIDGE, width=10, bd=5,font=('Times New Roman', 15,'bold'), bg='cadetblue3')
b6.place(x=1100, y=430)

b7=Button(root, text='   CLEAR   ', relief=RIDGE, width=10, bd=5,font=('Times New Roman', 15,'bold'), bg='cadetblue3', command=clear)
b7.place(x=700, y=350)

e13 = ['ID','Date','Name' , 'Subject']
combobox = ttk.Combobox(root, values = e13,font = ('Times New Roman',18, "bold"))
combobox.place(x = 100 , y = 430 , width = 200 , height = 35)
combobox.set('Search by')

root.mainloop()