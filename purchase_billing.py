from tkinter import *
import tkinter.messagebox
from tkinter.messagebox import askyesno
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Inventory Management System')
root.state('zoomed')

conn = sqlite3.connect('tree_crm.db')
c = conn.cursor()
c.execute(
    '''CREATE TABLE if not exists customers (cname text,cid integer,bno integer,invoice integer,pname text,quant integer,price integer,tax integer,disc integer,tprice integer) ''')
conn.commit()
conn.close()


def query_database():
    conn = sqlite3.connect('tree_crm.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    records = c.fetchall()
    for record in records:
        table.insert(parent='', index='end', text='', values=(
            record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=('evenrow',))

    conn.commit()
    conn.close()


def back():
    root.destroy()
    import homepage

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

l1 = Label(root, text='Billing and Purchase', foreground='white',
           background='cyan4', activebackground='Light Blue', font=('Times New Roman', 45, 'bold'))
l1.place(x=500, y=20)

b1=Button(canvas, text='   BACK   ',width=10, bd=5, relief=RIDGE, background="white", command=back,
          font=('Times New Roman', 15,'bold'), bg='Light Grey')
b1.place(x=20, y=40)


cname = StringVar()
cid = StringVar()
bno = StringVar()
pname = StringVar()
pri = StringVar()
quant = StringVar()
invoice = StringVar()
taxxx = StringVar()
disc = StringVar()
total = StringVar()

custname = Label(root, text='Customer Name :', font=(
    'Times New Roman', 18, 'bold')).place(x=50, y=150)
e1 = Entry(root, width=20, textvariable=cname, font=(
    'Times New Roman', 18))
e1.place(x=250, y=150)

custid = Label(root, text='Customer ID :', font=(
    'Times New Roman', 18, 'bold')).place(x=510, y=150)
e2 = Entry(root, width=20, textvariable=cid, font=(
    'Times New Roman', 18))
e2.place(x=680, y=150)

billno = Label(root, text='Bill No :', font=(
    'Times New Roman', 18, 'bold')).place(x=980, y=150)
e3 = Entry(root, width=20, textvariable=bno, font=(
    'Times New Roman', 18))
e3.place(x=1080, y=150)

itemname = Label(root, text='Product Name :', font=(
    'Times New Roman', 18, 'bold')).place(x=65, y=200)
e4 = Entry(root, width=20, textvariable=pname, font=(
    'Times New Roman', 18))
e4.place(x=250, y=200)

price = Label(root, text='Price :', font=(
    'Times New Roman', 18, 'bold')).place(x=585, y=200)
e5 = Entry(root, width=20, textvariable=pri, font=(
    'Times New Roman', 18))
e5.place(x=680, y=200)

quantity = Label(root, text='Quantity :', font=(
    'Times New Roman', 18, 'bold')).place(x=960, y=200)
e6 = Entry(root, width=20, textvariable=quant, font=(
    'Times New Roman', 18))
e6.place(x=1080, y=200)

invoiceno = Label(root, text='Invoice No :', font=(
    'Times New Roman', 18, 'bold')).place(x=103, y=250)
e7 = Entry(root, width=20, textvariable=invoice, font=(
    'Times New Roman', 18))
e7.place(x=250, y=250)

tax = Label(root, text='Tax(%) :', font=(
    'Times New Roman', 18, 'bold')).place(x=560, y=250)
e8 = Entry(root, width=20, textvariable=taxxx, font=(
    'Times New Roman', 18))
e8.place(x=680, y=250)

discount = Label(root, text='Discount :', font=(
    'Times New Roman', 18, 'bold')).place(x=962, y=250)
e9 = Entry(root, width=20, textvariable=disc, font=(
    'Times New Roman', 18))
e9.place(x=1080, y=250)


def totalcal():
    cusname = (cname.get())
    proname = (pname.get())
    item1 = (pri.get())
    item2 = (quant.get())
    taxper = (taxxx.get())
    discitem = (disc.get())
    if (cname.get() == '') or (cid.get() == '') or (bno.get() == '') or (pname.get() == '') or (pri.get() == '') or (quant.get() == '') or (invoice.get() == '') or (taxxx.get() == '') or (disc.get() == ''):
        tkinter.messagebox.showerror("Error", "Please fill all the details")

    elif (cusname.isdigit() or proname.isdigit()):
        tkinter.messagebox.showwarning("Invalid Data", "Enter Proper Data")
        return True

    elif (item1.isdigit() and item2.isdigit() and taxper.isdigit() and discitem.isdigit()):
        item3 = (float(item1) * float(item2)) + \
            float(float(taxper)*0.01*(float(item1) * float(item2)))
        total.set(item3)
        return True

    else:
        tkinter.messagebox.showwarning("Invalid Data", "Enter Numbers Only")
        return True


calculatebutton = Button(root, cursor='hand2', text='CALCULATE',
                         background="CadetBlue3", bd=7, relief=RIDGE, command=totalcal, font=(
                             'Times New Roman', 18, 'bold')).place(x=600, y=310, width=180, height=45)


def Reset():
    cname.set("")
    cid.set("")
    bno.set("")
    pname.set("")
    pri.set("")
    quant.set("")
    invoice.set("")
    taxxx.set("")
    disc.set("")
    total.set("")
    return


reset = Button(root, cursor='hand2', text='RESET',
               background="CadetBlue3", bd=7, relief=RIDGE, font=(
                   'Times New Roman', 18, 'bold'), command=Reset).place(x=800, y=310, width=150, height=45)


totalcost = Label(root, text='Total Cost :', font=(
    'Times New Roman', 25, 'bold')).place(x=50, y=400)
e10 = Entry(root, width=20, textvariable=total, font=(
    'Times New Roman', 18, 'bold'), state=DISABLED)
e10.place(x=240, y=400, width=300, height=45)


table = ttk.Treeview(root)
table.pack()

s = ttk.Style(root)
s.theme_use("clam")
s.configure("Treeview.Heading", font=('Helvetica', 10, "bold"))

table['columns'] = ('cname', 'cid', 'bno', 'ino',
                    'pname', 'quan', 'price', 'tax', 'disc', 'tprice')
table.column('#0', width=0, stretch=NO)
table.column('cname', anchor=CENTER, width=100)
table.column('cid', anchor=CENTER, width=50)
table.column('bno', anchor=CENTER, width=50)
table.column('ino', anchor=CENTER, width=50)
table.column('pname', anchor=CENTER, width=70)
table.column('quan', anchor=CENTER, width=10)
table.column('price', anchor=CENTER, width=20)
table.column('tax', anchor=CENTER, width=1)
table.column('disc', anchor=CENTER, width=1)
table.column('tprice', anchor=CENTER, width=50)

table.heading('#0', text='', anchor=W)
table.heading('cname', text='Customer Name', anchor=CENTER)
table.heading('cid', text='Customer ID', anchor=CENTER)
table.heading('bno', text='Bill No', anchor=CENTER)
table.heading('ino', text='Invoice No', anchor=CENTER)
table.heading('pname', text='Product Name', anchor=CENTER)
table.heading('quan', text='Quantity', anchor=CENTER)
table.heading('price', text='Price', anchor=CENTER)
table.heading('tax', text='Tax(%)', anchor=CENTER)
table.heading('disc', text='Discount(%)', anchor=CENTER)
table.heading('tprice', text='Total Price', anchor=CENTER)

table.place(x=55, y=500, width=1450, height=270)

# hsb = ttk.Scrollbar(table, orient='horizontal')
# hsb.configure(command=table.xview)
# table.configure(xscrollcommand=hsb.set)
# hsb.pack(fill=X, side=BOTTOM)

vsb = ttk.Scrollbar(table, orient='vertical')
vsb.configure(command=table.yview)
table.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y, side=RIGHT)


def addbutton():
    if (cname.get() == '') or (cid.get() == '') or (bno.get() == '') or (pname.get() == '') or (pri.get() == '') or (quant.get() == '') or (invoice.get() == '') or (taxxx.get() == '') or (disc.get() == ''):
        tkinter.messagebox.showerror("Error", "Please fill all the details")
    elif (total.get() == ''):
        tkinter.messagebox.showerror("Error", "Please Calculate the Total")

    else:
        conn = sqlite3.connect('tree_crm.db')
        c = conn.cursor()
        c.execute("INSERT INTO customers VALUES (:cname,:cid,:bno,:invoice,:pname,:quant,:price,:tax,:disc,:tprice)",
                  {
                      'cname': cname.get(),
                      'cid': cid.get(),
                      'bno': bno.get(),
                      'invoice': invoice.get(),
                      'pname': pname.get(),
                      'quant': quant.get(),
                      'price': pri.get(),
                      'tax': taxxx.get(),
                      'disc': disc.get(),
                      'tprice': total.get(),
                  })
        conn.commit()
        conn.close()

        cname.set("")
        cid.set("")
        bno.set("")
        pname.set("")
        pri.set("")
        quant.set("")
        invoice.set("")
        taxxx.set("")
        disc.set("")
        total.set("")

        table.delete(*table.get_children())
        query_database()




add = Button(root, cursor='hand2', text='ADD',
             background="CadetBlue3", bd=7, relief=RIDGE, font=(
                 'Times New Roman', 18, 'bold'), command=addbutton).place(x=700, y=400, width=150, height=45)


def deletebutton():
    ans = askyesno(title='Confirmation', message='Delete the selected record?')
    if ans:
        x = table.selection()[0]
        table.delete(x)
        conn = sqlite3.connect('tree_crm.db')
        c = conn.cursor()
        c.execute("DELETE from customers WHERE cid=" + cid.get())
        conn.commit()
        conn.close()
        Reset()


delete = Button(root, cursor='hand2', text='DELETE',
                background="CadetBlue3", bd=7, relief=RIDGE, font=(
                    'Times New Roman', 18, 'bold'), command=deletebutton).place(x=1100, y=400, width=150, height=45)


def selectbutton(e):
    cname.set("")
    cid.set("")
    bno.set("")
    pname.set("")
    pri.set("")
    quant.set("")
    invoice.set("")
    taxxx.set("")
    disc.set("")
    total.set("")

    # selected = table.selection()[0]
#
    # e1.insert(0, table.item(selected)['values'][0])
    # e2.insert(0, table.item(selected)['values'][1])
    # e3.insert(0, table.item(selected)['values'][2])
    # e4.insert(0, table.item(selected)['values'][3])
    # e5.insert(0, table.item(selected)['values'][4])
    # e6.insert(0, table.item(selected)['values'][5])
    # e7.insert(0, table.item(selected)['values'][6])
    # e8.insert(0, table.item(selected)['values'][7])
    # e9.insert(0, table.item(selected)['values'][8])
    # e10.insert(0, table.item(selected)['values'][9])
# table.bind("<<TreeviewSelect>>", selectrow)

    selected = table.focus()
    values = table.item(selected, 'values')
    e1.insert(0, values[0])
    e2.insert(0, values[1])
    e3.insert(0, values[2])
    e7.insert(0, values[3])
    e4.insert(0, values[4])
    e6.insert(0, values[5])
    e5.insert(0, values[6])
    e8.insert(0, values[7])
    e9.insert(0, values[8])
    e10.insert(0, values[9])


# select = Button(root, cursor='hand2', text='SELECT',
#                background="CadetBlue3", bd=7, relief=RIDGE, font=(
#                    'Times New Roman', 18, 'bold'), command=selectbutton).place(x=1300, y=400, width=150, height=45)

table.bind("<ButtonRelease-1>", selectbutton)


def updatebutton():
    if (total.get() == ''):
        tkinter.messagebox.showerror("Error", "Please Calculate the Total")
    else:
        selected = table.focus()
        table.item(selected, text="", values=(cname.get(), cid.get(), bno.get(), invoice.get(
        ), pname.get(), quant.get(), pri.get(), taxxx.get(), disc.get(), total.get()))
        conn = sqlite3.connect('tree_crm.db')
        c = conn.cursor()
        c.execute('''UPDATE customers SET cname=:cn,cid=:cusid,bno=:bn,invoice=:in,pname=:pn,quant=:qn,price=:pr,tax=:tx,disc=:dsc,tprice=:tp WHERE cid=:cusid''',
                  {
                      'cn': cname.get(),
                      'cusid': cid.get(),
                      'bn': bno.get(),
                      'in': invoice.get(),
                      'pn': pname.get(),
                      'qn': quant.get(),
                      'pr': pri.get(),
                      'tx': taxxx.get(),
                      'dsc': disc.get(),
                      'tp': total.get(),
                  })
        conn.commit()
        conn.close()

        Reset()


update = Button(root, cursor='hand2', text='UPDATE',
                background="CadetBlue3", bd=7, relief=RIDGE, font=(
                    'Times New Roman', 18, 'bold'), command=updatebutton).place(x=900, y=400, width=150, height=45)

query_database()
root.mainloop()