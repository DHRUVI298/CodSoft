import tkinter
from tkinter import *
import config


windows = tkinter.Tk()
windows.geometry("340x380+210+210")
windows.resizable(False,False)
windows.title('Calculator')


# label = Label(windows,text='Calculator',font=('Time new Roman',11,),bg="Black",fg="black").pack(side='top')


# LOGIC 
logic = ""

def show(event):
    global  logic
    logic += str(event)
    Result.delete(0,END)
    Result.insert(0,logic)
    
def clear():
    global logic
    logic=""
    Result.delete(0,END)
    

def Ans():
    global logic
    try:
        logic = str(eval(logic))
        Result.delete(0,END)
        Result.insert(0,logic)
    except:
        clear()
        Result.insert(0,"error")

label = Label(windows,text="",font=('Time new Roman',11,),fg="black",bd=5).pack(side='top')
frame = Frame(windows).pack(side='top')
Result = Entry(frame,text="",width=18,font=('Times New Roman',25,),bd=4)
Result.pack()
Result.focus()
    
    

# Making Btn
Button(windows,text="C",width=6,height=1,font=('Time new Roman',16,'bold',),fg="White",bg="#FA8128",command=lambda:clear()).place(x=13,y=90)
Button(windows,text="/",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#016064",command=lambda:show('/')).place(x=90,y=90)
Button(windows,text="%",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#016064",command=lambda:show('%')).place(x=160,y=90)
Button(windows,text="*",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#016064",command=lambda:show('*')).place(x=240,y=90)




Button(windows,text="7",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#FAF9F6",command=lambda:show('7')).place(x=13,y=130)
Button(windows,text="8",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#FAF9F6",command=lambda:show('8')).place(x=90,y=130)
Button(windows,text="9",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#FAF9F6",command=lambda:show('9')).place(x=160,y=130)
Button(windows,text="-",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#016064",command=lambda:show('-')).place(x=240,y=130)


Button(windows,text="4",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#FAF9F6",command=lambda:show('4')).place(x=13,y=170)
Button(windows,text="5",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#FAF9F6",command=lambda:show('5')).place(x=90,y=170)
Button(windows,text="6",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#FAF9F6",command=lambda:show('6')).place(x=160,y=170)
Button(windows,text="+",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#016064",command=lambda:show('+')).place(x=240,y=170)

Button(windows,text="3",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#FAF9F6",command=lambda:show('3')).place(x=13,y=210)
Button(windows,text="2",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#FAF9F6",command=lambda:show('2')).place(x=90,y=210)
Button(windows,text="1",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#FAF9F6",command=lambda:show('1')).place(x=160,y=210)
Button(windows,text="0",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#016064",command=lambda:show('0')).place(x=240,y=210)


Button(windows,text=" ^ ",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#016064",command=lambda:show('^')).place(x=13,y=250)
Button(windows,text="(",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#016064",command=lambda:show('(')).place(x=90,y=250)
Button(windows,text=")",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#016064",command=lambda:show(')')).place(x=160,y=250)
Button(windows,text=" . ",width=6,height=1,font=('Time new Roman',16,'bold',),fg="black",bg="#022D36",command=lambda:show('.')).place(x=240,y=250)


btn = tkinter.Button(text='                  =                   ',font=('Times New Roman',21),bg="#0A1172",fg="white",command=lambda:Ans())
btn.pack(side='bottom')
windows.mainloop()
