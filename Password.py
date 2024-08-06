from tkinter import *
import string
import random


def generator():
    uppercase_letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters= uppercase_letters.lower()
    digits= "0123456789"
    symbols= "!@#$%^&*()_-[]{}/\',"
    all=uppercase_letters+lowercase_letters+digits+symbols

    pw_len=int(len_Box.get())
    pwField.insert(0,random.sample(all,pw_len))


root=Tk()
root.config(bg='blue4')
choice=IntVar()
Font=('arial',13,'bold')
pwLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='black',fg='white')
pwLabel.grid(pady=10)

lenLabel=Label(root,text='Password Length',font=Font,bg='black',fg='white')
lenLabel.grid(pady=5)

len_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
len_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5)

pwField=Entry(root,width=25,bd=2,font=Font)
pwField.grid()

root.mainloop()