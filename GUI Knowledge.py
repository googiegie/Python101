from tkinter import *
from tkinter import ttk #theme of Tk
from tkinter import messagebox


GUI = Tk() #นี่คือหน้าจอหลัก
GUI.title('Saving Program') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400')#นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='Food Program',font=('Angsana New',30),fg='blue')
L1.place(x=30,y=20)
############################
def Button2():
    text = 'Bonchon'
    messagebox.showwarning('Googie is hungry',text)
    
FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='Course Menu',command=Button2)
B2.pack(ipadx=20,ipady=20)
############################
############################
def Button3():
    text = 'ตอนนี้กี้มีเงินในบัญชีอยู่ 20 บาท'
    messagebox.showwarning('เงินในบัญชี',text)
    
FB2 = Frame(GUI)#คล้ายกระดาน
FB2.place(x=100,y=100)
B3 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button3)
B3.pack(ipadx=20,ipady=20)
############################


GUI.mainloop()
