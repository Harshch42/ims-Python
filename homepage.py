from tkinter import *
from PIL import ImageTk,Image
from time import strftime

def logout():
    root.destroy()
    import login

def notes():
    import notes


def item_management():
    import item_management
   
def import_data():
    import import_data 
    
def export_data():
    import export_data

def customer_management():
    import customer_management
    
def purchase_billing():
    import purchase_billing

root = Tk()
root.title('Inventory Management System | Homepage')
root.state('zoomed')

# canvas1 = Canvas(root,width = 1920,height = 120)
# canvas1.pack()
# canvas1.create_rectangle(0, 0, 1920, 120, outline="cyan4", fill="cyan4")
# canvas1.update()


# canvas2 = Canvas(root,width = 1920,height = 20)
# canvas2.pack()
# canvas2.create_rectangle(0, 120, 1920, 140, outline="cyan4", fill="blue")
# canvas2.update()



canvas2 = Canvas(root, width=1500, height=700)
canvas2.pack()
r2 = canvas2.create_rectangle(360, 230, 1500, 700, outline="Black")
canvas2.update()

frame1 = Frame(root,bg = 'cyan4')
frame1.place(x = 0 , y = 0 , width = 1920 , height = 120)

frame2 = Frame(root,bg = 'black')
frame2.place(x = 0 , y = 120 , width = 1920 , height = 20)



frame3 = Frame(root, bd = 3, relief=RIDGE)
frame3.place(x = 0 , y = 140 , width = 320 , height = 600)

image1 = Image.open("admin.png")

# Resize the image to the desired dimensions
# new_size = (, 4)
image1 = image1.resize((200,200), resample=Image.LANCZOS)

img_admin = ImageTk.PhotoImage(image1)
# img_admin = img_admin.subsample(4)
# img_admin = img_admin.resize((200, 200), Image.ANTIALIAS)

title = Label(frame3,text = '',image = img_admin )
# title.place(x=100,y=100)
title.place(x = 56,y = 0)

# image2 = Image.open("head_icon1.png")

# # Resize the image to the desired dimensions
# # new_size = (, 4)
# image2 = image2.resize((100,100), resample=Image.LANCZOS)

# img_inven = ImageTk.PhotoImage(image2)

l1 = Label(root, text='Inventory Management System',foreground = 'white',background='cyan4',activebackground = 'Light Blue' ,font=('Times New Roman', 45, 'bold'))
l1.place(x = 40,y = 20)

logout = Button(root, text='Logout',width = 10,bd = 5,relief = RIDGE,background = "white",command=logout,font=('Times New Roman', 18,'bold'))
logout.place(x = 1350,y = 36)




# image2 = Image.open("head_icon.png")

# # Resize the image to the desired dimensions
# # new_size = (, 4)
# image2 = image2.resize((200,200), resample=Image.LANCZOS)

# img_admin = ImageTk.PhotoImage(image2)
# img_admin = img_admin.subsample(4)
# img_admin = img_admin.resize((200, 200), Image.ANTIALIAS)

# title = Label(frame3,text = '',image = img_admin )
# # title.place(x=100,y=100)
# title.pack(side = TOP, fill = X)

l2 = Label(root, text='Total Employee\n[0]',background='DeepSkyBlue2',bd = 5,relief = RIDGE ,activebackground = 'Light Blue' ,font=('Times New Roman', 20,'bold'))
l2.place(x = 400,y = 250,width = 300,height = 150)

l3 = Label(root, text='Total Items\n[0]',background='DeepSkyBlue2',bd = 5,relief = RIDGE ,activebackground = 'Light Blue' ,font=('Times New Roman', 20,'bold'))
l3.place(x = 800,y = 250,width = 300,height = 150)

l4 = Label(root, text='Total Customers\n[0]',background='DeepSkyBlue2',bd = 5,relief = RIDGE ,activebackground = 'Light Blue' ,font=('Times New Roman', 20,'bold'))
l4.place(x = 1200,y = 250,width = 300,height = 150)

l5 = Label(root, text='Total Paid Orders\n[0]',background='DeepSkyBlue2',bd = 5,relief = RIDGE ,activebackground = 'Light Blue' ,font=('Times New Roman', 20,'bold'))
l5.place(x = 400,y = 500,width = 300,height = 150)

l6 = Label(root, text='Total Unpaid Orders\n[0]',background='DeepSkyBlue2',bd = 5,relief = RIDGE ,activebackground = 'Light Blue' ,font=('Times New Roman', 20,'bold'))
l6.place(x = 800,y = 500,width = 300,height = 150)

l7 = Label(root, text='Dashboard',font=('Times New Roman', 32, 'bold'))
l7.place(x = 370,y = 150)

l8 = Label(root, text='Admin',foreground = 'black',bd = 5,relief = RIDGE,background='RoyalBlue1',activebackground = 'Light Blue' ,font=('Times New Roman', 28, 'bold'))
l8.place(x = 0,y = 340,width = 320,height = 100)


b1 = Button(root, text='Customer Management',command = customer_management,compound=LEFT,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
b1.place(x = 0,y = 440,width = 320,height = 60)

b2 = Button(root, text='Purchase & Billing',width = 12,command= purchase_billing ,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
b2.place(x = 0,y = 500,width = 320,height = 60)

b3 = Button(root, text='Import Data',width = 12,command= import_data ,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
b3.place(x = 0,y = 560,width = 320,height = 60)

b4 = Button(root, text='Export Data',width = 12,command= export_data ,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
b4.place(x = 0,y = 620,width = 320,height = 60)

b5 = Button(root, text='Items Management',width = 12,command= item_management,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
b5.place(x = 0,y = 680,width = 320,height = 60)

b6 = Button(root, text='Notes',width = 12,command= notes,bd = 5,relief = RIDGE,background = "white",font=('Times New Roman', 22))
b6.place(x = 0,y = 740,width = 320,height = 60)

root.mainloop()