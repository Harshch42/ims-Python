from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as messagebox
import ast

def nextPage():
    root.destroy()
    import homepage
    
def sign_up():
    import signup
    
    
# def check_credentials():
#     # check if the entered username and password match the correct credentials
#     if (e1.get() == 'Harsh' or e1.get() == 'harshchaudhari150@gmail.com') and e2.get() == 'hmc':
#         nextPage()
#     else:
#         messagebox.showerror("Error", "Invalid Username or password")
#         e1.set('')
#         e2.set('')

def signin():
    file = open('datasheet.txt','r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()
    
    # print(r.keys())
    # print(r.values())
    if e1.get() in r.keys() and e2.get() == r[e1.get()]:
        root.destroy()
        import homepage
    else:
        messagebox.showerror('Invalid' , 'invalid username or password')

        
# create a new Tkinter window
root = Tk()
root.geometry('925x500+300+200')
root.title('Inventory Management System Login')
root.configure(background='white')
root.resizable(False, False)
# root.state('zoomed')

img1 = PhotoImage(file='login_theme.png')
Label(root, image = img1,bg = 'white').place(x = 50,y = 50)
# image = image.zoom(1, 1)
# label = Label(root, image=image).place(x=0, y=0)
# img = Image.open("inventory.png")
# img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
# img = ImageTk.PhotoImage(img)

# canvas = Canvas(root, height=root.winfo_screenheight(), width=root.winfo_screenwidth(), bg="white")
# canvas.pack()

# canvas.create_image(0, 0, anchor=NW, image=img)

# create a label for the username field


frame1 = Frame(root,bg = 'white')
frame1.place(x = 480 , y = 20 , width = 400 , height = 400)






sign_in = Label(frame1, text='Sign in ',background='white',foreground = 'DeepSkyBlue2',activebackground = 'Light Blue' ,font=('Microsoft YaHei UI light', 30, 'bold'))
sign_in.place(x = 120,y = 0)

def on_enter(e):
    e1.delete(0,'end')

def on_leave(e):
    name = e1.get()
    if name == '':
        e1.insert(0,'john@uxsaints.com')

l1 = Label(frame1, text='Username / Email Address',background='white',foreground = 'Black',activebackground = 'Light Blue' ,font=('Microsoft YaHei UI light', 11, 'bold'))
l1.place(x = 6,y = 100)
# temp1 = StringVar()
e1 = Entry(frame1,bd = 3,font = ('Microsoft YaHei UI light',12))
e1.place(x = 10,y = 130,width = 400,height = 35 )
e1.insert(0,'john@uxsaints.com')
e1.bind("<FocusIn>", on_enter)
e1.bind("<FocusOut>", on_leave)

# Frame(frame1, width=295, height=2, bg='black').place(x = 10, y = 165)

def on_enter(e):
    e2.delete(0,'end')

def on_leave(e):
    name = e2.get()
    if name == '':
        e2.insert(0,'Password')

l2 = Label(frame1, text='Password',background='white',foreground = 'Black',activebackground = 'Light Blue' ,font=('Microsoft YaHei UI light', 11, 'bold'))
l2.place(x = 6,y = 180)
# temp2 = StringVar()
e2 = Entry(frame1,bd = 3,font = ('Microsoft YaHei UI light',12))
e2.place(x = 10,y = 210,width = 400,height = 35 )
e2.insert(0,'Enter Your Password')
e2.bind("<FocusIn>", on_enter)
e2.bind("<FocusOut>", on_leave)



login_button = Button(frame1, text='Sign in',command=signin,fg = 'Black',background = "DeepSkyBlue2",border = 0,font=('Microsoft YaHei UI light', 15))
login_button.place(x = 10,y =280,width = 400,height = 35 )

l3 = Label(frame1, text="Don't have an account?",background='white',foreground = 'Black',activebackground = 'Light Blue' ,font=('Microsoft YaHei UI light', 12))
l3.place(x = 50,y = 350)

b2 = Button(frame1, text="Sign up!",background='white',foreground = 'Black',command = sign_up,border = 0,cursor = 'hand2',font=('Microsoft YaHei UI light', 12,'bold'))
b2.place(x = 240,y = 346)


# l2 = Label(root, text='Welcome! login to use this exciting Inventory Management System',foreground = 'Black',background='white',activebackground = 'Light Blue' ,font=('Microsoft YaHei UI light', 12)).place(x = 1000,y = 120)

# l3 = Label(root, text='Username:',background='white',foreground = 'Black',font=('Microsoft YaHei UI light', 20)).place(x = 1000,y = 200)
# temp1 = StringVar()
# e1 = Entry(root,width = 20,textvariable=temp1,font = ('Microsoft YaHei UI light',20))
# e1.place(x = 1200,y = 200 )

# Password = Label(root, text='Password:',background='white',foreground = 'Black',font=('Microsoft YaHei UI light', 20)).place(x = 1000,y = 300)
# temp2 = StringVar()
# e2 = Entry(root,show='*',width = 20,textvariable=temp2,font = ('Microsoft YaHei UI light',20))
# e2.place(x = 1200,y = 300 )

# forgot_pass = Button(root, text='Forgot Password ?',background = "white",width = 25,font=('Microsoft YaHei UI light', 12)).place(x = 1000,y = 380)

# login_button = Button(root, text='LOGIN',width = 30,command=check_credentials,background = "white",font=('Microsoft YaHei UI light', 22)).place(x = 1000,y =450)


# l5 = Label(root, text="Don't have an account ?",background='white',foreground = 'Black',font=('Microsoft YaHei UI light', 14)).place(x = 1000,y = 550)

# sign_up = Button(root, text='Sign up here',background = "white",command = signup,font=('Microsoft YaHei UI light', 10)).place(x = 1200,y = 550)



root.mainloop()
