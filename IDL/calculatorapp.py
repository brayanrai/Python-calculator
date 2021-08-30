from tkinter import *
root= Tk()
root.title("Calculator")
root.geometry("250x450")
e=Entry(root,width=35,borderwidth=5,bg="yellow")
e.grid(row=0,column=0,columnspan=3)
def buttons(number):
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def addition():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num= int(first_number)
    e.delete(0, END)
def subtraction():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num= int(first_number)
    e.delete(0, END)
def multiplication():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num= int(first_number)
    e.delete(0, END)
def division():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num= int(first_number)
    e.delete(0, END)
def equals():
    
    second_number=e.get()
    e.delete(0, END)
    if math== "addition":
        e.insert(0, f_num+int(second_number))
    if math== "subtraction":
        e.insert(0, f_num - int(second_number))
    if math== "multiplication":
        e.insert(0, f_num * int(second_number))
    if math== "division":
        e.insert(0, f_num/int(second_number))

no1=Button(root, text=1,padx=32,pady=20,bg="pink",command=lambda:buttons(1)).grid(row=1,column=0)
no2=Button(root, text=2,padx=31,pady=20,bg="pink",command=lambda:buttons(2)).grid(row=1,column=1)
no3=Button(root, text=3,padx=32,pady=20,bg="pink",command=lambda:buttons(3)).grid(row=1,column=2)
           
no4=Button(root, text=4,padx=32,pady=20,bg="pink",command=lambda:buttons(4)).grid(row=2,column=0)
no5=Button(root, text=5,padx=31,pady=20,bg="pink",command=lambda:buttons(5)).grid(row=2,column=1)
no6=Button(root, text=6,padx=32,pady=20,bg="pink",command=lambda:buttons(6)).grid(row=2,column=2)

no7=Button(root, text=7,padx=32,pady=20,bg="pink",command=lambda:buttons(7)).grid(row=3,column=0)
no8=Button(root, text=8,padx=31,pady=20,bg="pink",command=lambda:buttons(8)).grid(row=3,column=1)
no9=Button(root, text=9,padx=32,pady=20,bg="pink",command=lambda:buttons(9)).grid(row=3,column=2)
no0=Button(root, text=0,padx=32,pady=20,bg="pink",command=lambda:buttons(0)).grid(row=4,column=0)

add=Button(root,text="+",padx=31,pady=20,bg="pink",command=addition).grid(row=5,column=0)
equals=Button(root,text="=",padx=70,pady=20,bg="pink",command=equals).grid(row=6,column=1,columnspan=2)
clear=Button(root,text="C",padx=70,pady=20,bg="pink",command=button_clear).grid(row=5,column=1,columnspan=2)
minus=Button(root,text="-",padx=33,pady=20,bg="pink",command=subtraction).grid(row=6,column=0)
division=Button(root,text="/",padx=32,pady=20,bg="pink",command=division).grid(row=4,column=1)
multiply=Button(root,text="*",padx=32,pady=20,bg="pink",command=multiplication).grid(row=4,column=2)
#allclear=Button(root,text="/",padx=30,pady=30).grid(row=0,column=3)


#minus=Button(root,text="*",padx=30,pady=30).grid(row=0,column=4)
#minus=Button(root,text="-",padx=30,pady=30).grid(row=1,column=4)
#minus=Button(root,text="+-",padx=30,pady=30).grid(row=3,column=4)


#cal=Button(root,text="cal",padx=20,pady=20,state="disable").grid(row=4,column=1)

                                                     


