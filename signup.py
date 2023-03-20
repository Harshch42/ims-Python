from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title("SignUp")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

img = PhotoImage(file='signup.png')
Label(root, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(root, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white',
                font=('Microsoft Yahaei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


# def on_enter(e):
#     user.delete(0, 'end')


# def on_leave(e):
#     if user.get() == '':
#         user.insert(0, 'Username')


# user = Entry(frame, width=25, fg='black', border=0, bg='white',
#              font=('Microsoft Yahaei UI Light', 11))
# user.place(x=30, y=80)
# user.insert(0, 'Username')
# user.bind("<FocusIn>", on_enter)
# user.bind("<FocusOut>", on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


# def on_enter(e):
#     code.delete(0, 'end')


# def on_leave(e):
#     if code.get() == '':
#         code.insert(0, 'Password')


# code = Entry(frame, width=25, fg='black', border=0, bg='white',
#              font=('Microsoft Yahaei UI Light', 11))
# code.place(x=30, y=150)
# code.insert(0, 'Password')
# code.bind("<FocusIn>", on_enter)
# code.bind("<FocusOut>", on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


# def on_enter(e):
#     confirm_code.delete(0, 'end')


# def on_leave(e):
#     if confirm_code.get() == '':
#         confirm_code.insert(0, 'Confirm Password')


# confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white',
#                      font=('Microsoft Yahaei UI Light', 11))
# confirm_code.place(x=30, y=220)
# confirm_code.insert(0, 'Confirm Password')
# confirm_code.bind("<FocusIn>", on_enter)
# confirm_code.bind("<FocusOut>", on_leave)

# Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)
def signin():
    root.destroy()
    import login

def signup():
    username = e1.get()
    password = e2.get()
    confirmpassword = e3.get()
    if password == confirmpassword:
        try:
            file = open('datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)
            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('datasheet.txt', 'w')
            w = file.write(str(r))
            messagebox.showinfo('Signip', 'Successfully Sign Up')
        except:
            file = open('datasheet.txt', 'w')
            pp = str({'Username: Password'})
            file.write(pp)
            file.close()
        root.destroy()
        import login
    else:
        messagebox.showerror('Invalid', 'Both Password should match')


# Button(frame, width=39, pady=7, text='Sign up',
#        bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
# label = Label(frame, text='I have an account', fg='black',
#               bg='white', font=('Microsoft YaHei UI Light', 9))
# label.place(x=90, y=340)

# signin = Button(frame, width=6, text='Sign in', border=0,
#                 bg='white', cursor='hand2', fg='#57a1f8')
# signin.place(x=200, y=340)

#############################################################################################

frame1 = Frame(root,bg = 'white')
frame1.place(x = 480 , y = 20 , width = 400 , height = 500)






sign_in = Label(frame1, text='Sign up ',background='white',foreground = 'DeepSkyBlue2',activebackground = 'Light Blue' ,font=('Microsoft YaHei UI light', 30, 'bold'))
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


def on_enter(e):
    e3.delete(0,'end')

def on_leave(e):
    name = e3.get()
    if name == '':
        e2.insert(0,'Password')

l3 = Label(frame1, text='Confirm Password',background='white',foreground = 'Black',activebackground = 'Light Blue' ,font=('Microsoft YaHei UI light', 11, 'bold'))
l3.place(x = 6,y = 260)
# temp2 = StringVar()
e3 = Entry(frame1,bd = 3,font = ('Microsoft YaHei UI light',12))
e3.place(x = 10,y = 290,width = 400,height = 35 )
e3.insert(0,'Re-Enter Your Password')
e3.bind("<FocusIn>", on_enter)
e3.bind("<FocusOut>", on_leave)



signup_button = Button(frame1, text='Sign Up',command=signup,fg = 'Black',background = "DeepSkyBlue2",border = 0,font=('Microsoft YaHei UI light', 15))
signup_button.place(x = 10,y =360,width = 400,height = 35 )

l3 = Label(frame1, text="I have an account",background='white',foreground = 'Black',activebackground = 'Light Blue' ,font=('Microsoft YaHei UI light', 12))
l3.place(x = 70,y = 410)

b2 = Button(frame1, text="Sign in!",background='white',foreground = 'Black',command = signin,border = 0,cursor = 'hand2',font=('Microsoft YaHei UI light', 12,'bold'))
b2.place(x = 220,y = 406)










#########################################################
root.mainloop()