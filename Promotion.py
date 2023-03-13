#from login import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from config import *

root = Tk()
def ui_config():
    root.title("Stock Defective Product")
    root.option_add("*Font",font)
    window_width = 1024
    window_height = 768

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2- window_width /2)
    center_y = int(screen_height / 2- window_height /2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.columnconfigure(0,weight=3)
    root.columnconfigure(1,weight=10)
    root.rowconfigure(0,weight=1)
    return root


def frameLayout(root):
    Frame_left = Label(root,bg=frame_left_color)
    Frame_left.columnconfigure((0,1,2),weight=1)
    Frame_left.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    Frame_left.grid(row=0,column=0,sticky=NSEW)

    Frame_right = Label(root,bg=bg_color)
    Frame_right.columnconfigure(0,weight=1)
    Frame_right.rowconfigure((0,1,2,4),weight=1)
    Frame_right.rowconfigure(3,weight=15)
    Frame_right.grid(row=0,column=1,sticky=NSEW)


    return Frame_left,Frame_right

def Menu_left(Frame_left):
    T1=Label(Frame_left,image=images7,text=' Stock',compound=LEFT,fg='black',bg=frame_left_color)
    T1.grid(row=0,column=0,pady=25,columnspan=2)

    T2=Label(Frame_left,text='ชื่ออ',fg='blue',bg=frame_left_color)
    T2.grid(row=1,column=1,pady=25)

    for i,des in enumerate(infolist) :
        def onclick(number=i):
            print(number)
        b1=Button(Frame_left,image=imageslist[i],text="  "+des,fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command=onclick)
        b1.grid(row=2+i,column=1,sticky=W,pady=25)  
    Button(Frame_left,image=images6,text="ออกจากระบบ  ",bg=frame_left_color,relief = "raised",compound=RIGHT).grid(row=7,column=1,sticky=W,pady=25)

def Menu_right(Frame_right):
    l1=Frame(Frame_right,bg="#FBE09A")
    l1.columnconfigure((0,1,2,3),weight=1)
    l1.rowconfigure((0,1),weight=1)
    l1.grid(row=0,column=0,sticky=NSEW)

    l2=Frame(Frame_right,bg="#FBE09A")
    l2.columnconfigure((0,1,2,3,4),weight=1)
    l2.rowconfigure((0,1,2,3,4),weight=1)
    l2.grid(row=3,column=0,sticky=NSEW,padx=20)
    return l1,l2

def layer_top(l1):
    Label(l1,text="รายการสั่งซื้อ",bg='#FBE09A').grid(row=0,column=0,rowspan=2)
    Entry(l1,width=20,textvariable=searchVar).grid(row=0,column=1,rowspan=2,sticky=W)
    Button(l1,text="ค้นหา",bg=button_color,relief = "raised",width=6).grid(row=0,column=1,rowspan=2,sticky=E)
    Button(l1,text="รีเฟรช",image=images8,compound=RIGHT,bg=bg_color,relief = "raised",width=100,height=40).grid(row=0,column=3,rowspan=2)
    

def infor2(l2):
    Label(l2,text="ไอดี",bg='#FBE09A').grid(row=0,column=0,sticky=NW,pady=20,padx=20)
    Label(l2,text="ชื่อสินค้า",bg='#FBE09A').grid(row=0,column=1,pady=20,sticky=NW)
    Label(l2,text="ราคา",bg='#FBE09A').grid(row=0,column=2,sticky=N,pady=20)
    Label(l2,text="ราคาโปรโมชั่น",bg='#FBE09A').grid(row=0,column=3,sticky=N,pady=20)
    Label(l2,text="วันที่",bg='#FBE09A').grid(row=0,column=4,sticky=N,pady=20)




#รอใส่DataDB
#lblID = Label(root, text='', font=('Tahoma', 18, 'bold'), bg='#f9f6e7')
#lblID.place(x = 300, y= 220)
#lblStock = Label(root, text='', font=('Tahoma', 18, 'bold'), bg='#f9f6e7')
#lblStock.place(x = 300, y= 320)
#lblprice = Label(root, text='', font=('Tahoma', 18, 'bold'), bg='#f9f6e7')
#lblprice.place(x = 300, y= 420)
#lblpricepromotion = Label(root, text='', font=('Tahoma', 18, 'bold'), bg='#f9f6e7')
#lblpricepromotion.place(x = 300, y= 520)
#lblDate = Label(root, text='', font=('Tahoma', 18, 'bold'), bg='#f9f6e7')
#lblDate.place(x = 300, y= 620)

root = ui_config()
infolist = ["คลังสินค้า","รายการสั่งซื้อ","รายการสั่งสินค้า","โปรโมชั่น","สินค้าชำรุด"]
frameLayout(root)
images1 = PhotoImage(file='images/dashboard.png').subsample(15,15) 
images2 = PhotoImage(file='images/box.png').subsample(15,15) 
images3 = PhotoImage(file='images/clipboard.png').subsample(15,15) 
images4 = PhotoImage(file='images/dollar.png').subsample(15,15) 
images5 = PhotoImage(file='images/tools.png').subsample(15,15) 
images6 = PhotoImage(file='images/logout.png').subsample(15,15) 
images7 = PhotoImage(file='images/boxes.png').subsample(13,13)
images8 = PhotoImage(file='images/refreshs.png').subsample(20,20)
imageslist =[images1,images2,images3,images4,images5]
spy1 = [StringVar() for i in infolist]

Frame_left,Frame_right=frameLayout(root)
Menu_left(Frame_left)
searchVar = StringVar()
l1,l2=Menu_right(Frame_right)
layer_top(l1)
infor2(l2)
root.mainloop()




