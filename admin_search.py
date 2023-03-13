#from login import *
from cProfile import label
from sqlite3 import Row
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import left
from config import *

root = Tk()
def ui_config():
    root.title("Stock main")

    window_width = 1024
    window_height = 768

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2- window_width /2)
    center_y = int(screen_height / 2- window_height /2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=10)
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=13)
    root.option_add("*Font",font)
    return root



def frameLayout(root):
    Frame_top = Label(root,bg='#FFE4B5')
    Frame_top.columnconfigure((0,1,2),weight=1)
    Frame_top.rowconfigure((0,1),weight=1)
    Frame_top.grid(row=0,column=0,columnspan=2,sticky=NSEW)

    Frame_left = Label(root,bg='white')
    Frame_left.rowconfigure(0,weight=1)
    Frame_left.rowconfigure((1,2,3,4,5,6),weight=1)
    Frame_left.columnconfigure((0,1),weight=1)
    Frame_left.grid(row=1,column=0,sticky=NSEW)
    
    Frame_right = Label(root,bg='white')
    Frame_right.rowconfigure((0,2),weight=1)
    Frame_right.rowconfigure(1,weight=9)
    Frame_right.columnconfigure((0,1),weight=1)
    Frame_right.grid(row=1,column=1,sticky=NSEW)

    return Frame_top,Frame_left,Frame_right


def layer_top(Frame_top):

    Label(Frame_top,text="แอดมิน",bg="#FFE4B5",font=('Opun 20 ')).grid(row=0,column=0,sticky=W,rowspan=2,padx=20)
    Button(Frame_top,image=refresh,text="รีเฟรส",width=100,height=40,compound=RIGHT,relief="raised",bg=button_color).grid(row=0,rowspan=2,column=1,columnspan=2) 
    Button(Frame_top,image=log_out,text="ออกจากระบบ ",width=150,height=40,compound=RIGHT,relief="raised",bg="white").grid(row=0,rowspan=2,column=2,columnspan=2,sticky=E,padx=50) 


def layer_left(Frame_left):
    Label(Frame_left,text="พนักงาน",font=('Opun 17'),bg='white').grid(row=0,column=0,sticky=W,padx=40,pady=20)
    f1 = Frame(Frame_left, width=100, height=500,bg='#FFE4B5')
    f1.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    f1.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW,rowspan=5)
    return f1

def infor(f1):
    global l1,l2,l3,l4,l5
    l1=Label(f1,image=cir_g,text="พนักงานทั้งหมด",bg='#FFE4B5',compound=LEFT)
    l1.grid(row=1,column=0,sticky=W)
    l2=Label(f1,image=cir_r,text=" รอการยืนยัน",bg='#FFE4B5',compound=LEFT)
    l2.grid(row=2,column=0,sticky=W)
    Label(f1,text="-"*30,bg='#FFE4B5').grid(row=3,column=0)
    Label(f1,text=" แผนก",bg='#FFE4B5').grid(row=4,column=0,sticky=W)
    l3=Label(f1,image=cir_g,text="ฝ่ายดูแลระบบ",bg='#FFE4B5',compound=LEFT)
    l3.grid(row=5,column=0,sticky=W)
    l4=Label(f1,image=cir_g,text="ฝ่ายจัดการคลังสินค้า",bg='#FFE4B5',compound=LEFT)
    l4.grid(row=6,column=0,sticky=W)
    l5=Label(f1,image=cir_g,text="ฝ่ายขาย",bg='#FFE4B5',compound=LEFT)
    l5.grid(row=7,column=0,sticky=W)


def layer_right(Frame_right):
    Label(Frame_right,text="รหัสพนักงาน",bg='white').grid(row=0,column=0,sticky=W,padx=40,pady=20)
    pass_item = Entry(Frame_right,width=30,textvariable=searchVar)
    pass_item.grid(row=0,column=0,columnspan=2,ipady=3)
    Button(Frame_right,text="ค้นหา",bg='#FFE4B5',relief = "raised",width=6).grid(row=0,column=1,sticky=E,padx=40)

    f2 = Frame(Frame_right,bg="#FFE4B5")
    f2.columnconfigure((0,1,2,3),weight=1)
    f2.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
    f2.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
    return f2

def infor2(f2):
    Label(f2,text="ข้อมูลพนักงาน",bg='#FFE4B5',font=('Opun 17')).grid(row=0,column=1,columnspan=2)
    Label(f2,text="รหัสพนักงาน",bg='#FFE4B5').grid(row=1,column=1,sticky=NW,columnspan=2)
    Label(f2,text="ชื่อ",bg='#FFE4B5').grid(row=2,column=1,sticky=NW,columnspan=2)
    Label(f2,text="นามสกุล",bg='#FFE4B5').grid(row=3,column=1,sticky=NW,columnspan=2)
    Label(f2,text="อีเมล",bg='#FFE4B5').grid(row=4,column=1,sticky=NW,columnspan=2)
    Label(f2,text="แผนก",bg='#FFE4B5').grid(row=5,column=1,sticky=NW,columnspan=2)
    Label(f2,text="สถานะ",bg='#FFE4B5').grid(row=6,column=1,sticky=NW,columnspan=2)


    lblPass=Label(f2,text="11111",bg='#FFE4B5').grid(row=1,column=2,sticky=NE)
    lblName=Label(f2,text="11111",bg='#FFE4B5').grid(row=2,column=2,sticky=NE)
    lblLastName=Label(f2,text="11111",bg='#FFE4B5').grid(row=3,column=2,sticky=NE)
    lblEmail=Label(f2,text="11111",bg='#FFE4B5').grid(row=4,column=2,sticky=NE)
    lbldepartment=Label(f2,text="11111",bg='#FFE4B5').grid(row=5,column=2,sticky=NE)
    
    sp = ttk.Combobox(f2,width=5,textvariable=statusVar,background="white")
    sp['values'] = ('ไม่ยืนยัน','ยืนยัน')
    sp.grid(row=6,column=2,sticky=NE)

    Button(f2,text="ลบบัญชี",width=8,bg=button_color).grid(row=8,column=0)
    Button(f2,text="ยกเลิก",width=8,bg=button_color).grid(row=8,column=2)
    Button(f2,text="บันทึก",width=8,bg=button_color,command=update_click).grid(row=8,column=3)

    


def update_popup():
    popup=Toplevel(root)
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2- window_width /2)
    center_y = int(screen_height / 2- window_height /2)
    popup.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    popup.config(bg=bg_color)

    Label(popup,text="ต้องการบันทึกใช่หรือไม่",font=('Garamond 20'),bg=bg_color).pack(pady=50)
    Button(popup,text='ยกเลิก',width=8,bg=button_color,command=popup.destroy).pack(side=LEFT,padx=50)
    Button(popup,text='บันทึก',width=8,bg=button_color).pack(side=RIGHT,padx=50,pady=50)

def update_click():
    root2 = update_popup()


def my_fun1(*args):
    layer_top(Frame_top)
    layer_right(Frame_right)
    my1=Frame(Frame_right,bg="#FFE4B5")
    my1.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
    my1.columnconfigure((0,1,2,3),weight=1)

    Label(my1,text="รหัสพนักงาน",bg='#FFE4B5').grid(row=0,column=0,sticky=N,pady=20)
    Label(my1,text="ชื่อ-นามสกุล",bg='#FFE4B5').grid(row=0,column=1,sticky=N,pady=20)
    Label(my1,text="แผนก",bg='#FFE4B5').grid(row=0,column=2,sticky=N,pady=20)
    Label(my1,text="สถานะ",bg='#FFE4B5').grid(row=0,column=3,sticky=N,pady=20)
    Label(my1,text="-"*80,bg='#FFE4B5').grid(row=1,columnspan=4,column=0)


def my_fun2(*args):
    layer_top(Frame_top)
    layer_right(Frame_right)
    my2=Frame(Frame_right,bg="#FFE4B5")
    my2.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
    my2.columnconfigure((0,1,2,3),weight=1)

    Label(my2,text="รหัสพนักงาน",bg='#FFE4B5').grid(row=0,column=0,sticky=N,pady=20)
    Label(my2,text="ชื่อ-นามสกุล",bg='#FFE4B5').grid(row=0,column=1,sticky=N,pady=20)
    Label(my2,text="แผนก",bg='#FFE4B5').grid(row=0,column=2,sticky=N,pady=20)
    Label(my2,text="สถานะ",bg='#FFE4B5').grid(row=0,column=3,sticky=N,pady=20)
    Label(my2,text="-"*80,bg='#FFE4B5').grid(row=1,columnspan=4,column=0)

def my_fun3(*args):
    layer_top(Frame_top)
    layer_right(Frame_right)
    my3=Frame(Frame_right,bg="#FFE4B5")
    my3.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
    my3.columnconfigure((0,1,2),weight=1)

    Label(my3,text="รหัสพนักงาน",bg='#FFE4B5').grid(row=0,column=0,sticky=N,pady=20)
    Label(my3,text="ชื่อ-นามสกุล",bg='#FFE4B5').grid(row=0,column=1,sticky=N,pady=20)
    Label(my3,text="แผนก",bg='#FFE4B5').grid(row=0,column=2,sticky=N,pady=20)
    Label(my3,text="-"*80,bg='#FFE4B5').grid(row=1,columnspan=4,column=0)


def my_fun4(*args):
    layer_top(Frame_top)
    layer_right(Frame_right)
    my4=Frame(Frame_right,bg="#FFE4B5")
    my4.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
    my4.columnconfigure((0,1,2),weight=1)

    Label(my4,text="รหัสพนักงาน",bg='#FFE4B5').grid(row=0,column=0,sticky=N,pady=20)
    Label(my4,text="ชื่อ-นามสกุล",bg='#FFE4B5').grid(row=0,column=1,sticky=N,pady=20)
    Label(my4,text="แผนก",bg='#FFE4B5').grid(row=0,column=2,sticky=N,pady=20)
    Label(my4,text="-"*80,bg='#FFE4B5').grid(row=1,columnspan=4,column=0)



def my_fun5(*args):
    layer_top(Frame_top)
    layer_right(Frame_right)
    my5=Frame(Frame_right,bg="#FFE4B5")
    my5.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
    my5.columnconfigure((0,1,2),weight=1)

    Label(my5,text="รหัสพนักงาน",bg='#FFE4B5').grid(row=0,column=0,sticky=N,pady=20)
    Label(my5,text="ชื่อ-นามสกุล",bg='#FFE4B5').grid(row=0,column=1,sticky=N,pady=20)
    Label(my5,text="แผนก",bg='#FFE4B5').grid(row=0,column=2,sticky=N,pady=20)
    Label(my5,text="-"*80,bg='#FFE4B5').grid(row=1,columnspan=4,column=0)
   
root = ui_config()  
statusVar = StringVar()
cir_g=PhotoImage(file='images/circle_green.png').subsample(15,15)  
cir_r=PhotoImage(file='images/circle_red.png').subsample(20,20)  
log_out=PhotoImage(file='images/log-out.png').subsample(15,15)  
refresh=PhotoImage(file='images/refreshs.png').subsample(20,20)  
Frame_top,Frame_left,Frame_right=frameLayout(root)
layer_top(Frame_top)
searchVar = StringVar()
f1=layer_left(Frame_left)
infor(f1)

f2=layer_right(Frame_right)
infor2(f2)



l1.bind("<Button>",my_fun1)
l2.bind("<Button>",my_fun2)
l3.bind("<Button>",my_fun3)
l4.bind("<Button>",my_fun4)
l5.bind("<Button>",my_fun5)

root.mainloop()