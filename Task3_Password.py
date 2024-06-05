import random
import tkinter
from tkinter import *
import tkinter.messagebox

window = tkinter.Tk()
window.title("Password Generator")
window.geometry("410x550+510+130")
window.resizable(False,False)

#label 
label = Label(window,text='Password Generator',font=('Times New Roman',21),bg="black",fg='lightgreen').pack(side='top')

# Result = tkinter.Entry().pack()
frame = Frame(window,width=420,height=45,bg="white").place(x=0,y=50)
Result = Entry(frame,width=18,font=('Times New Roman',),bd=0)
Result.place(x=77,y=55)
Result.focus()


clen1 = IntVar()
clen2 = IntVar()
clen3 = IntVar()
clen4 = IntVar()

# main logic
# validchar ="qwertyuiopasdfghjklzxcvbnm1234567890ASDFGHJKLPOIUYTREWQZXCVBNM@#$"

def password_click(lenth):
    try:
        validchar ="(qwertyui!&_-/opasdfghjklzxcvbnm1234567890ASDFGHJKLPOIUYTREWQZXCVBNM@#$)"
        password = "".join(random.sample(validchar,lenth))
        Result.delete(0,tkinter.END)
        Result.insert(0,password)
    except:
        pass

def checkbox_click():
    if clen1.get()==6:
        password_click(6)
    elif clen2.get()==8:
       password_click(8)
    elif clen3.get()==10:
       password_click(10)
    elif clen4.get()==12:
       password_click(12)
    else:
        password_click(15)
     
def copy_text():
    password = Result.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)  
        tkinter.messagebox.showinfo(f"Password Copy{password}")
    else:
        tkinter.messagebox.showwarning(f"Oops Password is Not Copy{password}")
        


Clenone = tkinter.Checkbutton(text='6 character',font=('Times New Roman',),onvalue=6,offvalue=0,variable=clen1)
Clenone.place(x=77,y=98)
Clentwo = tkinter.Checkbutton(text='8 character',font=('Times New Roman',),onvalue=8,offvalue=0,variable=clen2)
Clentwo.place(x=79,y=150)
Clenthree = tkinter.Checkbutton(text='10 character',font=('Times New Roman',),onvalue=10,offvalue=0,variable=clen3)
Clenthree.place(x=81,y=200)
Clenfour = tkinter.Checkbutton(text='12 character',font=('Times New Roman',),onvalue=12,offvalue=False,variable=clen4)
Clenfour.place(x=85,y=250)


password = tkinter.Button(text='Generate password:)',font=('Times New Roman',21),bg="black",fg="white",command=checkbox_click)
password.pack(side='bottom')
label = Label(window,text='Without clicked checkbox then 15 letter strong password generate',fg="red",font=('times new roman',10,))
label.pack(side='bottom')
btn = Button(frame,text='Copy',font=('Times New Roman',),width=5,bg="blue",fg="white",bd=0,command=copy_text)
btn.place(x=340,y=55)

window.mainloop()