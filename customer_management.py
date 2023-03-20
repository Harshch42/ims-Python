from tkinter import *
from tkinter import ttk
from datetime import datetime
from time import strftime
from tkinter import messagebox
from tkinter.messagebox import askyesno
import sqlite3

conn = sqlite3.connect('cust_management.db')
c = conn.cursor()
c.execute(
    '''CREATE TABLE IF NOT EXISTS cust_management(id INTEGER PRIMARY KEY AUTOINCREMENT,date String, fname text, lname text, phno text,email text)''')
conn.commit()
conn.close()

def query_database():
    conn = sqlite3.connect('cust_management.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cust_management")
    records = c.fetchall()
    for record in records:
        table.insert(parent='', index='end', text='', values=(
            record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))

    conn.commit()
    conn.close()

def my_time():
    time_string = datetime.now().strftime('%x')
    # time_string = strftime('%H:%M:%S %p \n %x')
    # e_date.configure(text=time_string)
    e_date.delete(0, END)
    e_date.insert(0, time_string)
    e_date.after(1000, my_time)
    # temp6.set(time_string)

# def logout():
#     root.destroy()
#     import login

# def cust_management():
#     import cust_management

# def nextPage1():
#     root.destroy()
#     import inventory


def back():
    root.destroy()


def reset():
    e_cid.delete(0, END)
    e_date.delete(0, END)
    e_fname.delete(0, END)
    e_lname.delete(0, END)
    e_pno.delete(0, END)
    e_email.delete(0, END)
    


# def save():
#     # check if the entered username and password match the correct credentials
#     if (e_cid.get() == '') or (e_fname.get() == '') or (e_lname.get() == '') or (e_pno.get() == '') or (e_email.get() == '') or (e_date.get() == ''):
#         messagebox.showerror("Error", "Please fill all the details")
#     else:
#         table.insert(parent='', index='end', text='', values=(
#             e_date.get(), e_cid.get(), e_fname.get(), e_lname.get(), e_pno.get(), e_email.get()))
#         e_cid.delete(0, END)
#         e_fname.delete(0, END)
#         e_lname.delete(0, END)
#         e_pno.delete(0, END)
#         e_email.delete(0, END)
#         e_date.delete(0, END)


def addbutton():
    if (e_cid.get() == '') or (e_fname.get() == '') or (e_lname.get() == '') or (e_pno.get() == '') or (e_email.get() == '') or (e_date.get() == ''):
        messagebox.showerror("Error", "Please fill all the details",parent = root)
    else:
        conn = sqlite3.connect('cust_management.db')
        c = conn.cursor()
        c.execute("SELECT * FROM cust_management WHERE id = ?",(e_cid.get(),))
        row = c.fetchone()
        if row != None:
            messagebox.showerror("Error", "This Employee Id already exists")
        else:
            c.execute('Insert into cust_management(id, date,fname , lname , phno, email ) values(?,?,?,?,?,?)',(e_cid.get(),e_date.get(),e_fname.get(),e_lname.get(),e_pno.get(),e_email.get()))
            conn.commit()
            e_cid.delete(0, END)
            e_date.delete(0, END)
            e_fname.delete(0, END)
            e_lname.delete(0, END)
            e_pno.delete(0, END)
            e_email.delete(0, END)

            table.delete(*table.get_children())
            query_database()
            messagebox.showinfo("Success","Customer Data added Successfully")
            conn.close()
        
        

def select(e):
    e_cid.delete(0, END)
    e_date.delete(0, END)
    e_fname.delete(0, END)
    e_lname.delete(0, END)
    e_pno.delete(0, END)
    e_email.delete(0, END)

    selected = table.focus()
    values = table.item(selected, 'values')
    e_cid.insert(0, values[0])
    e_date.insert(0, values[1])    
    e_fname.insert(0, values[2])
    e_lname.insert(0, values[3])
    e_pno.insert(0, values[4])
    e_email.insert(0, values[5])
    print(values)
    
def deletebutton():
    ans = askyesno(title='Confirmation', message='Delete the selected record?')
    if ans:
        x = table.selection()[0]
        table.delete(x)
        conn = sqlite3.connect('cust_management.db')
        c = conn.cursor()
        c.execute("DELETE from cust_management WHERE id=" + e_cid.get())
        conn.commit()
        messagebox.showinfo("Success","Customer data Deleted Successfully")
        conn.close()
        reset()
    
def updatebutton():
        selected = table.focus()
        table.item(selected, text="", values=(e_cid.get() == '') or (e_fname.get() == '') or (e_lname.get() == '') or (e_pno.get() == '') or (e_email.get() == '') or (e_date.get() == ''))
        conn = sqlite3.connect('cust_management.db')
        c = conn.cursor()
        query = '''UPDATE cust_management SET id=:cusid,date=:cn,fname=:fn,lname=:ln,phno=:pn,email=:em WHERE id=:cusid'''
        c.execute(query,{
                        'cusid': e_cid.get(),
                        'cn' : e_date.get(),
                        'fn' : e_fname.get(),
                        'ln' : e_lname.get(),
                        'pn' : e_pno.get(),
                        'em' : e_email.get(),
                  })
        conn.commit()
        e_cid.delete(0, END)
        e_fname.delete(0, END)
        e_lname.delete(0, END)
        e_pno.delete(0, END)
        e_email.delete(0, END)
        e_date.delete(0, END)


        # e_cid.set("")
        # e_fname.set("")
        # e_subject.set("")
        # e_date.set("")
        # e_text.set("")

        table.delete(*table.get_children())
        # query_database()
        messagebox.showinfo("Success","Customer data Updated Successfully")
        # conn.commit()
        conn.close()
        query_database()
        reset()


# def input_record():


#     global count

#     set.insert(parent='',index='end',iid = count,text='',values=(id_entry.get(),fullname_entry.get(),award_entry.get()))
#     count += 1


#     id_entry.delete(0,END)
#     fullname_entry.delete(0,END)
#     award_entry.delete(0,END)
root = Tk()
root.state('zoomed')
root.title('Inventory Management System | Customer Management')

canvas = Canvas(root, width=1920, height=120, bg='cyan4')
canvas.pack()
canvas.update()

canvas2 = Canvas(root, width=1500, height=300)
canvas2.pack()
r2 = canvas2.create_rectangle(10, 20, 1500, 225, outline="Black")
canvas2.update()

canva3 = Canvas(root, width=1600, height=800)
canva3.pack()
r3 = canva3.create_rectangle(23, 10, 1520, 355, outline="Black")
canva3.update()

custid = StringVar()
fname = StringVar()
lname = StringVar()
ph = StringVar()
email = StringVar()
date = StringVar()


table = ttk.Treeview(root)
table.pack()

s = ttk.Style(root)
s.theme_use("clam")
s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

table['columns'] = ( 'id', 'date', 'fname', 'lname', 'phno', 'email')
table.column('#0', width=0, stretch=0)

table.column('id', anchor=CENTER, width=50)
table.column('date', anchor=CENTER, width=50)
table.column('fname', anchor=CENTER, width=80)
table.column('lname', anchor=CENTER, width=80)
table.column('phno', anchor=CENTER, width=80)
table.column('email', anchor=CENTER, width=100)

table.heading('#0', text='', anchor=CENTER)
table.heading('id', text='Customer ID', anchor=CENTER)
table.heading('date', text='Date', anchor=CENTER)
table.heading('fname', text='First Name', anchor=CENTER)
table.heading('lname', text='Last Name', anchor=CENTER)
table.heading('phno', text='Phone No.', anchor=CENTER)
table.heading('email', text='Email', anchor=CENTER)

table.place(x=40, y=450, width=1470, height=320)

vsb = ttk.Scrollbar(table, orient='vertical')
vsb.configure(command=table.yview)
table.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y, side=RIGHT)

l1 = Label(canvas, text='Customer Management', foreground='white', background='cyan4',activebackground='Light Blue', font=('Times New Roman', 45, 'bold'))
l1.place(x=500, y=20)

b1=Button(canvas, text='   BACK   ',width=10, bd=5, relief=RIDGE, background="white", command=back,
          font=('Times New Roman', 15,'bold'), bg='Light Grey')
b1.place(x=20, y=40)


l_cid = Label(root, text='Customer ID:', anchor='e',width=12, font=('times new roman', 18, 'bold'))
l_cid.place(x=50, y=170)
e_cid = Entry(root, textvariable=custid, highlightthickness=1,font=('times new roman', 16))
e_cid.place(x=240, y=170)

l_fname = Label(root, text='First Name:', anchor='e', width=12, font=('times new roman', 18, 'bold'))
l_fname.place(x=500, y=170)
e_fname = Entry(root, textvariable=fname, highlightthickness=1,font=('times new roman', 16))
e_fname.place(x=690, y=170)

l_lname = Label(root, text='Last Name:', anchor='e', width=12,font=('times new roman', 18, 'bold'))
l_lname.place(x=500, y=230)
e_lname = Entry(root, textvariable=lname, highlightthickness=1,font=('times new roman', 16))
e_lname.place(x=690, y=230)

l_pno = Label(root, text='Phone Number:', anchor='e',width=12, font=('times new roman', 18, 'bold'))
l_pno.place(x=1000, y=170)
e_pno = Entry(root, textvariable=ph, highlightthickness=1,font=('times new roman', 16))
e_pno.place(x=1180, y=170)

l_email = Label(root, text='Email:', anchor='e', width=12,font=('times new roman', 18, 'bold'))
l_email.place(x=1000, y=230)
e_email = Entry(root, textvariable=email, highlightthickness=1,font=('times new roman', 16))
e_email.place(x=1180, y=230)

l_date = Label(root, text='Date:', anchor='e', width=12,font=('times new roman', 18, 'bold'))
l_date.place(x=50, y=230)
e_date = Entry(root, textvariable=date, highlightthickness=1,font=('times new roman', 16))
e_date.place(x=240, y=230)
my_time()

# l8=Label(root,text='Total orders:\n[0]',relief=RIDGE,background='DarkSlategray3',font=('times new roman',20)).place(x=500,y=660,width=250,height=120)
# l9=Label(root,text='Total amount:\n[0]',relief=RIDGE,background='DarkSlategray3',font=('times new roman',20)).place(x=780,y=660,width=250,height=120)
# l10=Label(root,text='Last order date:',relief=RIDGE,background='DarkSlategray3',font=('times new roman',20)).place(x=1080,y=660,width=300,height=120)


search = ['ID', 'Date', 'Name']

search_frame = LabelFrame(root, text='Search customer',font=('goudy old type', 12, 'bold'))
search_frame.place(x=45, y=350, width=840, height=80)

e_search = Entry(root, highlightthickness=1, font=('times new roman', 16))
e_search.place(x=380, y=380)

combobox = ttk.Combobox(root, values=search,state="readonly", font=('Times New Roman', 16))
combobox.place(x=100, y=380)
combobox.set('Search by')

search = Button(root, text='SEARCH', width=10, relief=RIDGE, bd=7,background='CadetBlue3', font=('times new roman', 16, 'bold'))
search.place(x=640, y=370, width=150, height=45)

# selectb = Button(root, text='SELECT', width=10, bd=7, relief=RIDGE,
#                 background='CadetBlue3', command=select, font=('times new roman', 18, 'bold'))
# selectb.place(x=1000, y=370, width=150, height=48)


update = Button(root, text='UPDATE', width=10, bd=7, relief=RIDGE,command=updatebutton,background='CadetBlue3', font=('times new roman', 18, 'bold'))
update.place(x=1200, y=370, width=150, height=48)

insert = Button(root, text='ADD', width=10, bd=7, relief=RIDGE,command=addbutton,background='CadetBlue3', font=('times new roman', 18, 'bold'))
insert.place(x=500, y=290, width=150, height=48)


# def deletebutton():
#     ans = messagebox.askyesno("Confirmation", "Delete the selected record?")
#     if ans:
#         x = table.selection()[0]
#         table.delete(x)


delete = Button(root, text='DELETE', width=10, bd=7, relief=RIDGE, command=deletebutton,
                background='CadetBlue3', font=('times new roman', 18, 'bold'))
delete.place(x=700, y=290, width=150, height=48)

resetb = Button(root, text='RESET', width=10, bd=7, relief=RIDGE,
               background='CadetBlue3', command=reset, font=('times new roman', 18, 'bold'))
resetb.place(x=900, y=290, width=150, height=48)




table.bind("<ButtonRelease-1>", select)
query_database()

root.mainloop()