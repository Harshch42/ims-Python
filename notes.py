from tkinter import *
from PIL import ImageTk,Image
from time import strftime
from tkinter import ttk
import tkinter.messagebox as messagebox
from datetime import datetime
from tkinter.messagebox import askyesno
import sqlite3

conn = sqlite3.connect('notes_data.db')
c = conn.cursor()
c.execute(
    '''CREATE TABLE IF NOT EXISTS notes(Eid INTEGER PRIMARY KEY AUTOINCREMENT,Name text, Date String, Subject text, Note text)''')
conn.commit()
conn.close()


def query_database():
    conn = sqlite3.connect('notes_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM notes")
    records = c.fetchall()
    for record in records:
        table.insert(parent='', index='end', text='', values=(
            record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))

    conn.commit()
    conn.close()


# def my_time():
#     time_string = datetime.now().strftime('%x')
#     e_date.delete(0,END)
#     e_date.insert(0,time_string)
#     e_date.after(1000,my_time)
    

def notes():
    import notes

    
def back():
    root.destroy()
    # import homepage

def reset():
    e_eid.delete(0,END)
    e_name.delete(0,END)
    e_subject.delete(0,END)
    e_date.delete(0,END)
    e_text.delete('1.0',END)
    
# def add():
#     con = sqlite3.connect(database = r'ims.db')
#     cur =   con.cursor()
#     try:
#         if e_eid.get() == '' or e_eid.get() == '' or e_date.get() == '' or e_name.get() == '' or e_subject.get() == '' or e_text.get('1.0',END) == '':
#             messagebox.showerror("Error", "Enter all the Data Correctly", parent = root)
#         else:
#             cur.execute("SELECT * FROM notes WHERE Eid = ?",(e_eid.get(),))
#             row = cur.fetchone()
#             if row != None:
#                 messagebox.showerror("Error", "This Employee Id already exists")
#             else:
#                 cur.execute('Insert into notes(Eid, Name, Date, Subject , Note) values(?,?,?,?,?)',(e_eid.get(),e_name.get(),e_date.get(),e_subject.get(),e_text.get('1.0',END)))
#                 con.commit()
#                 messagebox.showinfo("Success","Note added Successfully")
#     except Exception as ex:
#         messagebox.showerror('Error',f'Error Due to : {str(ex)}')

    
def addbutton():
    if (e_eid.get() == '') or (e_name.get() == '') or (e_date.get() == '') or (e_subject.get() == '') or (e_text.get('1.0',END) == ''):
        messagebox.showerror("Error", "Please fill all the details",parent = root)
    else:
        conn = sqlite3.connect('notes_data.db')
        c = conn.cursor()
        c.execute("SELECT * FROM notes WHERE Eid = ?",(e_eid.get(),))
        row = c.fetchone()
        if row != None:
            messagebox.showerror("Error", "This Employee Id already exists")
        else:
            c.execute('Insert into notes(Eid, Name, Date, Subject , Note) values(?,?,?,?,?)',(e_eid.get(),e_name.get(),e_date.get(),e_subject.get(),e_text.get('1.0',END)))
            conn.commit()
            e_eid.delete(0,END)
            e_name.delete(0,END)
            e_subject.delete(0,END)
            e_date.delete(0,END)
            e_text.delete('1.0',END)

            # e_eid.set("")
            # e_name.set("")
            # e_subject.set("")
            # e_date.set("")
            # e_text.set("")

            table.delete(*table.get_children())
            query_database()
            messagebox.showinfo("Success","Note added Successfully")
            conn.close()
        
        

def selectbutton(e):
    e_eid.delete(0,END)
    e_name.delete(0,END)
    e_subject.delete(0,END)
    e_date.delete(0,END)
    e_text.delete('1.0',END)

    selected = table.focus()
    values = table.item(selected, 'values')
    e_eid.insert(0, values[0])
    e_name.insert(0, values[1])
    e_date.insert(0, values[2])
    e_subject.insert(0, values[3])
    e_text.insert('1.0', values[4])
    print(values)
    
def deletebutton():
    ans = askyesno(title='Confirmation', message='Delete the selected record?')
    if ans:
        x = table.selection()[0]
        table.delete(x)
        conn = sqlite3.connect('notes_data.db')
        c = conn.cursor()
        c.execute("DELETE from notes WHERE Eid=" + e_eid.get())
        conn.commit()
        messagebox.showinfo("Success","Note Deleted Successfully")
        conn.close()
        reset()
    
def updatebutton():
        selected = table.focus()
        table.item(selected, text="", values=(e_eid.get(), e_name.get(), e_date.get(), e_subject.get(), e_text.get('1.0',END)))
        conn = sqlite3.connect('notes_data.db')
        c = conn.cursor()
        query = '''UPDATE notes SET Eid=:cusid,Name=:cn,Date=:dn,Subject=:sj,Note=:nt WHERE Eid=:cusid'''
        c.execute(query,{
                      'cusid': e_eid.get(),
                      'cn': e_name.get(),
                      'dn': e_date.get(),
                      'sj': e_subject.get(),
                      'nt': e_text.get('1.0',END),
                  })
        conn.commit()
        e_eid.delete(0,END)
        e_name.delete(0,END)
        e_subject.delete(0,END)
        e_date.delete(0,END)
        e_text.delete('1.0',END)

        # e_eid.set("")
        # e_name.set("")
        # e_subject.set("")
        # e_date.set("")
        # e_text.set("")

        table.delete(*table.get_children())
        query_database()
        messagebox.showinfo("Success","Note Updated Successfully")
        conn.close()
        

        reset()

        
root = Tk()
root.title('Inventory Management System | Notes')
root.state('zoomed')
root.resizable(False, False)

canvas = Canvas(root, width=1920, height=120)
canvas.pack()
r1 = canvas.create_rectangle(0, 0, 1920, 120, outline="cyan4", fill="cyan4")
canvas.update()

canvas2 = Canvas(root, width=1500, height=350)
canvas2.pack()
r2 = canvas2.create_rectangle(25, 10, 1500, 250, outline="Black")
canvas2.update()

canvas3 = Canvas(root, width=1500, height=400)
canvas3.pack()
r3 = canvas3.create_rectangle(25, 2, 1500, 300, outline="Black")
canvas3.update()

table = ttk.Treeview(root)
table.pack()
s = ttk.Style(root)
s.theme_use("clam")
s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))
table['columns'] = ('Eid', 'Name', 'Date', 'Subject' , 'Note')

table.column('#0' , width = 0, stretch=0)
table.column('Eid' , anchor = W, width = 120)
table.column('Name' , anchor = W, width = 120)
table.column('Date' , anchor = W, width = 120)
table.column('Subject' , anchor = W, width = 120)
table.column('Note' , anchor = W, width = 120)

table.heading('#0' ,text = '' ,anchor = W )
table.heading('Eid' ,text = 'Eid' ,anchor = W )
table.heading('Name' ,text = 'Name' ,anchor = W )
table.heading('Date' ,text = 'Date' ,anchor = W )
table.heading('Subject' ,text = 'Subject' ,anchor = W )
table.heading('Note' ,text = 'Note' ,anchor = W )

# table.insert(parent = '', index = 'end', iid = 0 , text = '' , values = (1,'Harsh' ,'03/01/23' , 'Inventory' , 'Just Got Started with tkinter' ))
table.place(x=55, y=500, width=1450, height=270)



vsb = ttk.Scrollbar(table, orient='vertical')
vsb.configure(command=table.yview)
table.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y, side=RIGHT)


# frame2 = Frame(root,bg = 'black')

# frame2.place(x = 0 , y = 120 , width = 1920 , height = 20)


l1 = Label(root, text='Notes',foreground = 'white',background='cyan4',activebackground = 'Light Blue' ,font=('Times New Roman', 45, "bold"))
l1.place(x = 500,y = 20)


b1=Button(canvas, text='   BACK   ',width=10, bd=5, relief=RIDGE, background="white", command=back,
          font=('Times New Roman', 15,'bold'), bg='Light Grey')
b1.place(x=20, y=40)

l_id = Label(root, text='ID : ',foreground = 'Black',font=('Times New Roman', 18, "bold"))
l_id.place(x = 65,y = 150,width = 200 , height = 30 )
temp3 = StringVar()
e_eid = Entry(root, width = 20 ,textvariable = temp3,font = ('Times New Roman',18, "bold"))
e_eid.place(x = 240,y = 150  )

l_date = Label(root, text='Date :',foreground = 'Black',font=('Times New Roman', 18, "bold"))
l_date.place(x = 950,y = 150,width = 200 , height = 30 )
temp6 = StringVar()
e_date = Entry(root,width = 14 ,font = ('Times New Roman',18, "bold"))
e_date.place(x = 1135,y = 150 )
# my_time()

l4 = Label(root, text='Name : ',foreground = 'Black',font=('Times New Roman', 18, "bold"))
l4.place(x = 500,y = 150,width = 200 , height = 30 )
temp4 = StringVar()
e_name = Entry(root,width = 20 ,textvariable = temp4,font = ('Times New Roman',18, "bold"))
e_name.place(x = 680,y = 150  )


l5 = Label(root, text='Subject : ',foreground = 'Black',font=('Times New Roman', 18, "bold"))
l5.place(x = 50,y = 200,width = 200 , height = 30 )
temp5 = StringVar()
e_subject = Entry(root,width = 20 ,textvariable = temp5,font = ('Times New Roman',18, "bold"))
e_subject.place(x = 240,y = 200 )



l7 = Label(root, text='Note : ',foreground = 'Black',font=('Times New Roman', 18, "bold"))
l7.place(x = 500,y = 200,width = 200 , height = 30 )
temp7 = StringVar()
e_text = Text(root,  height = 3,width=52, font = ('Times New Roman',18))
e_text.place(x = 680,y = 200)
# e7 = Entry(root,width = 60,textvariable = temp7, font = ('Times New Roman',18))
# e7.place(x = 680,y = 200)

b_add = Button(root, cursor='hand2', text='ADD', background="CadetBlue3", bd=7, relief=RIDGE, font=('Times New Roman', 18, 'bold'), command = addbutton)
b_add.place(x=680, y=310, width=150, height=45)

b_reset = Button(root, cursor='hand2', text='RESET', background="CadetBlue3", bd=7, relief=RIDGE, font=('Times New Roman', 18, 'bold'), command = reset)
b_reset.place(x=850, y=310, width=150, height=45)

# b_delete = Button(root, cursor='hand2', text='DELETE', background="CadetBlue3", bd=7, relief=RIDGE, font=('Times New Roman', 18, 'bold'), command = save)
# b_delete.place(x=400, y=310, width=150, height=45)

# b_reset = Button(root, cursor='hand2', text='RESET', background="CadetBlue3", bd=7, relief=RIDGE, font=('Times New Roman', 18, 'bold'), command = save)
# b_reset.place(x=600, y=310, width=150, height=45)

b_delete = Button(root, cursor='hand2', text='DELETE', background="CadetBlue3", bd=7, relief=RIDGE, font=('Times New Roman', 18, 'bold'), command = deletebutton)
b_delete.place(x=950, y=410, width=150, height=45)

b_update = Button(root, cursor='hand2', text='UPDATE', background="CadetBlue3", bd=7, relief=RIDGE, font=('Times New Roman', 18, 'bold'), command = updatebutton)
b_update.place(x=1150, y=410, width=150, height=45)


# b1 = Button(root, text='SAVE', command = save,  background = "CadetBlue3",font=('Times New Roman', 22,"bold"))
# b1.place(x = 1300,y = 200,width = 200,height = 40)

# b2 = Button(root, text='UPDATE', background = "CadetBlue3",font=('Times New Roman', 22,"bold"))
# b2.place(x = 1300,y = 270,width = 200,height = 40)

# b3 = Button(root, text='DELETE', background = "CadetBlue3",font=('Times New Roman', 22,"bold"))
# b3.place(x = 1300,y = 340,width = 200,height = 40)

# b4 = Button(root, text='RESET', command = clear, background = "CadetBlue3",font=('Times New Roman', 22,"bold"))
# b4.place(x = 1300,y = 410,width = 200,height = 40)


search = ['ID','Date','Name' , 'Subject']

search_frame = LabelFrame(root, text = 'Search Note',font = ('goudy old type',12, 'bold'))
search_frame.place(x = 40,y = 380,width = 840,height = 90)
combobox = ttk.Combobox(root, values = search,font = ('Times New Roman',18, "bold"))
combobox.place(x = 100 , y = 420 , width = 200 , height = 30)
combobox.set('Search by')
e8 = Entry(root,textvariable = temp5,font = ('Times New Roman',18, "bold"))
e8.place(x = 320,y = 416 , width = 300 , height = 35 )

b5 = Button(root, text='Search', command = reset, background = "CadetBlue3",font=('Times New Roman', 22, "bold"))
b5.place(x = 650,y = 416,width = 200,height = 35)


# def add():
#     con = sqlite3.connect(database = r'ims.db')
#     cur =   con.cursor()
#     try:
#         if e_eid.get() == '' or e_eid.get() == '' or e_date.get() == '' or e_name.get() == '' or e_subject.get() == '' or e_text.get('1.0',END) == '':
#             messagebox.showerror("Error", "Enter all the Data Correctly", parent = root)
#     except Exception as ex:
#         messagebox.showerror('Error',f'Error Due to : {str(ex)}')




table.bind("<ButtonRelease-1>", selectbutton)


query_database()

root.mainloop()