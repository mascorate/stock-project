#from login import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from backend_insert import get_stock_table,get_stock_table_v2   
from config import *
import time
root = Tk()
def ui_config():
    root.title("Stock main")
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
    Frame_left.columnconfigure((0,1),weight=1)
    Frame_left.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    Frame_left.grid(row=0,column=0,sticky=NSEW)

    Frame_right = Label(root,bg=bg_color)
    Frame_right.columnconfigure((0,1,2,3,4,5),weight=1)
    Frame_right.rowconfigure((0,2),weight=2)
    Frame_right.rowconfigure(1,weight=1)
    Frame_right.grid(row=0,column=1,sticky=NSEW)

    return Frame_left,Frame_right

def Menu_left(Frame_left):
    T1=Label(Frame_left,image=images7,text='Stock',compound=LEFT,fg='black',bg=frame_left_color,font="Opun 20")
    T1.grid(row=0,column=1,pady=25)

    T2=Label(Frame_left,text='',fg='blue',bg=frame_left_color)
    T2.grid(row=1,column=1,pady=25)


    b1=Button(Frame_left,image=images1,text="  "+ "Dashboard",fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command = lambda:onclick())
    b1.grid(row=2,column=1,sticky=W,pady=25)

    b2=Button(Frame_left,image=images2,text="  "+ "คลังสินค้า",fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command = lambda:onclick1())
    b2.grid(row=3,column=1,sticky=W,pady=25)

    b3=Button(Frame_left,image=images3,text="  "+ "รายการสั่งซื้อ",fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command = lambda:onclick2())
    b3.grid(row=4,column=1,sticky=W,pady=25)

    b4=Button(Frame_left,image=images4,text="  "+ "โปรโมชั่น",fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command = lambda:onclick3())
    b4.grid(row=5,column=1,sticky=W,pady=25)

    b5=Button(Frame_left,image=images5,text="  "+ "สินค้าชำรุด",fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command = lambda:onclick4())
    b5.grid(row=6,column=1,sticky=W,pady=25)
    Button(Frame_left,image=images6,text="ออกจากระบบ  ",bg="white",relief = "raised",compound=RIGHT).grid(row=7,column=1,sticky=W,pady=25)

def onclick():
    Frame_right0 = Frame(Frame_right,bg=bg_color)
    f1,f2,f3,f4=Menu_right(Frame_right)
    layer1(f1)
    layer2(f2)
    layer3(f3)
    layer4(f4)
    Frame_right0.grid(row=0,rowspan=3,columnspan=7,column=0,sticky=NSEW)


def onclick1():
    Frame_right1 = Frame(Frame_right,bg=bg_color)
    Frame_right1.columnconfigure((0,1,2,3,4),weight=1)
    Frame_right1.rowconfigure((0,1,2,4),weight=1)
    Frame_right1.rowconfigure(3,weight=15)
    Frame_right1.grid(row=0,rowspan=3,columnspan=7,column=0,sticky=NSEW)

    l1=Frame(Frame_right1,bg="#FBE09A")
    l1.columnconfigure((0,1,2,3),weight=1)
    l1.rowconfigure((0,1),weight=1)
    l1.grid(row=0,column=0,columnspan=5,sticky=NSEW)

    def refresh_stock_click():
        carttree.delete(*carttree.get_children())
        result = get_stock_table_v2()
        for i,data in enumerate(result):
            if data[0][10] == "โปรโมชั่น":
                p = float(data[0][6]) - float(data[0][7][:-3])
                carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],p,data[0][10],data[0][9]))
            else:
                carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][6],data[0][10],data[0][9]))

    def search_stock_click():
        a = searchstockVar.get()
        key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list = get_stock_table()
        if a == '':
            messagebox.showwarning(title='Warning',message='กรุณากรอกไอดีสินค้า')
        elif a in id_list:
            index = id_list.index(a)
            carttree.delete(*carttree.get_children())
            if status_list[index] == 'โปรโมชั่น':
                p = float(price_list[index]) - float(promo_price_list[index][:-3])
                carttree.insert('', 'end',values=(id_list[index],product_name_list[index],amount_list[index],status_list[index],p,date_list[index]))
            else:
                carttree.insert('', 'end',values=(id_list[index],product_name_list[index],amount_list[index],status_list[index],price_list[index],date_list[index]))
        else:
            messagebox.showwarning(title='Warning',message='ไม่พบไอดีสินค้า')

    Label(l1,text="คลังสินค้า",bg='#FBE09A').grid(row=0,column=0,rowspan=2)
    Entry(l1,width=20,textvariable=searchstockVar).grid(row=0,column=1,rowspan=2,sticky=W)
    Button(l1,text="ค้นหา",bg=button_color,relief = "raised",width=6,command=search_stock_click).grid(row=0,column=1,rowspan=2,sticky=E)
    Button(l1,text="รีเฟรช",image=images8,compound=RIGHT,bg=button_color,relief = "raised",width=100,height=40,command=refresh_stock_click).grid(row=0,column=3,rowspan=2)


    my1=Frame(Frame_right1,bg="#FFE4B5")
    my1.grid(row=3,column=0,columnspan=5,padx=20,sticky=NSEW)
    my1.columnconfigure((0,1,2),weight=1)
    my1.rowconfigure((0,1,2,3),weight=1)
    Button(Frame_right1,text="เพิ่มลดรายการสินค้า",bg=button_color,width=15,command=status).grid(row=2,column=0,sticky=NE,padx=10)
    Button(Frame_right1,text="แก้ไขสถานะสินค้า",bg=button_color,width=15,command=status2).grid(row=2,column=1,sticky=N,padx=10)
    Button(Frame_right1,text="เพิ่มรายการสินค้า",bg=button_color,width=18,command=addstock).grid(row=2,column=2,sticky=N,padx=10)
    cartbar = Scrollbar(my1)
    cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
    carttree = ttk.Treeview(my1,columns=("MenuId","MenuName","Menuquantity","MenuStatus","MenuPrice","MenuUpdate"),yscrollcommand=cartbar.set)
    carttree.grid(row=0,column=0,rowspan=5,columnspan=5,sticky=NSEW)
    cartbar.config(command=carttree.yview)
    carttree.heading("#0",text="",anchor=CENTER)
    carttree.heading("MenuId",text="ไอดี",anchor=CENTER)
    carttree.heading("MenuName",text="ชื่อสินค้า",anchor=CENTER)
    carttree.heading("Menuquantity",text="จำนวน",anchor=CENTER)
    carttree.heading("MenuPrice",text="ราคา",anchor=CENTER)
    carttree.heading("MenuStatus",text="สถานะ",anchor=CENTER)
    carttree.heading("MenuUpdate",text="Update",anchor=CENTER)


    carttree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    carttree.column("MenuId",anchor=CENTER,width=100)
    carttree.column("MenuName",anchor=CENTER,width=200)
    carttree.column("Menuquantity",anchor=CENTER,width=150)
    carttree.column("MenuPrice",anchor=CENTER,width=120)
    carttree.column("MenuStatus",anchor=CENTER,width=125)
    carttree.column("MenuUpdate",anchor=CENTER,width=125)
    result = get_stock_table_v2()
    for i,data in enumerate(result):
        if data[0][10] == "โปรโมชั่น":
            p = float(data[0][6]) - float(data[0][7][:-3])
            carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],p,data[0][10],data[0][9]))
        else:
            carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][6],data[0][10],data[0][9]))

def onclick2():
    Frame_right2 = Label(root,bg=bg_color)
    Frame_right2.columnconfigure(0,weight=1)
    Frame_right2.rowconfigure((0,1,2,4),weight=1)
    Frame_right2.rowconfigure(3,weight=15)
    Frame_right2.grid(row=0,column=1,sticky=NSEW)

    l2=Frame(Frame_right2,bg="#FBE09A")
    l2.columnconfigure((0,1,2,3,3,4,5,6,7),weight=1)
    l2.rowconfigure((0,1,2,3,4),weight=1)
    l2.grid(row=0,column=0,columnspan=8,sticky=NSEW)

    def refresh_stock_click():
        carttree.delete(*carttree.get_children())
        result = get_stock_table_v2()
        for i,data in enumerate(result):
            # MenuId","MenuName","Menuquantity","MenuStatus","MenuPrice","MenuUpdate"
            if data[0][6] == 'ชำรุด':
                carttree.insert('', 'end',values=(data[0][1],data[0][2],data[0][3],data[0][6]))

    def search_stock_click():
        a = searchstockVar.get()
        key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list = get_stock_table()
        if a == '':
            messagebox.showwarning(title='Warning',message='กรุณากรอกไอดีสินค้า')
        elif a in id_list:
            index = id_list.index(a)
            carttree.delete(*carttree.get_children())
            carttree.insert('', 'end',values=(id_list[index],product_name_list[index],amount_list[index],status_list[index]))
        else:
            messagebox.showwarning(title='Warning',message='ไม่พบไอดีสินค้า')

    Label(l2,text="รายการสั่งซื้อ",bg='#FBE09A').grid(row=0,column=0,rowspan=2)
    Entry(l2,width=30,textvariable=searchstockVar).grid(row=0,column=1,rowspan=2,sticky=W)
    Button(l2,text="ค้นหา",bg=button_color,relief = "raised",width=6).grid(row=0,column=2,rowspan=2,sticky=E)
    Button(l2,image=images8,text="รีเฟรช",compound=RIGHT,bg=button_color,relief = "raised",width=100,height=40).grid(row=0,column=6,rowspan=2)
    Button(Frame_right2,text="+ เปิดใบสั่งซื้อใหม่",bg=button_color,width=18,command=neworder).grid(row=2,column=2,sticky=N,padx=10)
    my2=Frame(Frame_right2,bg="#FFE4B5")
    my2.columnconfigure((0,1,2),weight=1)
    my2.rowconfigure((0,1,2,3),weight=1)
    my2.grid(row=3,column=0,columnspan=3,padx=20,sticky=NSEW)

    cartbar = Scrollbar(my2)
    cartbar.grid(row=0,rowspan=4,column=0,columnspan=5,sticky=NSEW)
    carttree = ttk.Treeview(my2,columns=("MenuName","MenuNumber","MenuPhone","MenuSum","MenuPrice","MenuStatus","MenuDate"),yscrollcommand=cartbar.set)
    carttree.grid(row=0,column=0,rowspan=5,columnspan=5,sticky=NSEW)
    cartbar.config(command=carttree.yview)
    carttree.heading("#0",text="",anchor=CENTER)
    carttree.heading("MenuName",text="ชื่อบริษัท",anchor=CENTER)
    carttree.heading("MenuNumber",text="เลขใบสั่งซื้อ",anchor=CENTER)
    carttree.heading("MenuPhone",text="เบอร์ติดต่อ",anchor=CENTER)
    carttree.heading("MenuSum",text="ยอดสั่งซื้อ",anchor=CENTER)
    carttree.heading("MenuPrice",text="ราคา",anchor=CENTER)
    carttree.heading("MenuStatus",text="สถานะ",anchor=CENTER)
    carttree.heading("MenuDate",text="วันที่",anchor=CENTER)


    carttree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    carttree.column("MenuName",anchor=CENTER,width=130)
    carttree.column("MenuNumber",anchor=CENTER,width=130)
    carttree.column("MenuPhone",anchor=CENTER,width=125)
    carttree.column("MenuSum",anchor=CENTER,width=100)
    carttree.column("MenuPrice",anchor=CENTER,width=100)
    carttree.column("MenuStatus",anchor=CENTER,width=100)
    carttree.column("MenuDate",anchor=CENTER,width=120)


def status():
    from status_config import ui_config
    
def status2():
    from status2_config import ui_config
    
def addstock():
    from addstock import ui_config

def neworder():
    from new_Order_old import ui_config



def onclick3():
    Frame_right3 = Frame(Frame_right,bg=bg_color)
    Frame_right3.columnconfigure((0,1,2,3,4),weight=1)
    Frame_right3.rowconfigure((0,1,2,4),weight=1)
    Frame_right3.rowconfigure(3,weight=15)
    Frame_right3.grid(row=0,rowspan=3,columnspan=7,column=0,sticky=NSEW)

    l1=Frame(Frame_right3,bg="#FBE09A")
    l1.columnconfigure((0,1,2,3),weight=1)
    l1.rowconfigure((0,1),weight=1)
    l1.grid(row=0,column=0,columnspan=5,sticky=NSEW)

    l2=Frame(Frame_right3,bg="#FBE09A")
    l2.columnconfigure((0,1,2,3,4),weight=1)
    l2.rowconfigure((0,1,2,3,4),weight=1)
    l2.grid(row=3,column=0,columnspan=5,sticky=NSEW,padx=20)

    def refresh_stock_click():
        carttree.delete(*carttree.get_children())
        result = get_stock_table_v2()
        for i,data in enumerate(result):
            # MenuId","MenuName","Menuquantity","MenuStatus","MenuPrice","MenuUpdate"
            if data[0][6] == 'ชำรุด':
                carttree.insert('', 'end',values=(data[0][1],data[0][2],data[0][3],data[0][6]))

    def search_stock_click():
        a = searchstockVar.get()
        key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list = get_stock_table()
        if a == '':
            messagebox.showwarning(title='Warning',message='กรุณากรอกไอดีสินค้า')
        elif a in id_list:
            index = id_list.index(a)
            carttree.delete(*carttree.get_children())
            carttree.insert('', 'end',values=(id_list[index],product_name_list[index],amount_list[index],status_list[index]))
        else:
            messagebox.showwarning(title='Warning',message='ไม่พบไอดีสินค้า')

    Label(l1,text="โปรโมชั่น",bg='#FBE09A').grid(row=0,column=0,rowspan=2)
    Entry(l1,width=20,textvariable=searchstockVar).grid(row=0,column=1,rowspan=2,sticky=W)
    Button(l1,text="ค้นหา",bg=button_color,relief = "raised",width=6).grid(row=0,column=1,rowspan=2,sticky=E)
    Button(l1,text="รีเฟรช",image=images8,compound=RIGHT,bg=bg_color,relief = "raised",width=100,height=40).grid(row=0,column=3,rowspan=2)

    cartbar = Scrollbar(l2)
    cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
    carttree = ttk.Treeview(l2,columns=("MenuId","MenuName","MenuPrice","MenuPromotion","MenuDate"),yscrollcommand=cartbar.set)
    carttree.grid(row=0,column=0,rowspan=5,columnspan=5,sticky=NSEW)
    cartbar.config(command=carttree.yview)
    carttree.heading("#0",text="",anchor=CENTER)
    carttree.heading("MenuId",text="ไอดี",anchor=CENTER)
    carttree.heading("MenuName",text="ชื่อสินค้า",anchor=CENTER)
    carttree.heading("MenuPrice",text="ราคา",anchor=CENTER)
    carttree.heading("MenuPromotion",text="ราคาโปรโมชั่น",anchor=CENTER)
    carttree.heading("MenuDate",text="วันที่",anchor=CENTER)


    carttree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    carttree.column("MenuId",anchor=CENTER,width=100)
    carttree.column("MenuName",anchor=CENTER,width=200)
    carttree.column("MenuPrice",anchor=CENTER,width=150)
    carttree.column("MenuPromotion",anchor=CENTER,width=125)
    carttree.column("MenuDate",anchor=CENTER,width=125)

def onclick4():
    Frame_right4 = Frame(Frame_right,bg="pink")
    Frame_right4 = Frame(Frame_right,bg="black")
    Frame_right4 = Frame(Frame_right,bg=bg_color)
    Frame_right4.columnconfigure((0,1,2,3,4),weight=1)
    Frame_right4.rowconfigure((0,1,2,4),weight=1)
    Frame_right4.rowconfigure(3,weight=15)
    Frame_right4.grid(row=0,rowspan=3,columnspan=7,column=0,sticky=NSEW)

    l1=Frame(Frame_right4,bg="#FBE09A")
    l1.columnconfigure((0,1,2,3),weight=1)
    l1.rowconfigure((0,1),weight=1)
    l1.grid(row=0,column=0,columnspan=5,sticky=NSEW)

    l2=Frame(Frame_right4,bg="#FBE09A")
    l2.columnconfigure((0,1,2,3,4),weight=1)
    l2.rowconfigure((0,1,2,3,4),weight=1)
    l2.grid(row=3,column=0,columnspan=5,sticky=NSEW,padx=20)

    def refresh_stock_click():
        carttree.delete(*carttree.get_children())
        result = get_stock_table_v2()
        for i,data in enumerate(result):
            # MenuId","MenuName","Menuquantity","MenuStatus","MenuPrice","MenuUpdate"
            if data[0][6] == 'ชำรุด':
                carttree.insert('', 'end',values=(data[0][1],data[0][2],data[0][3],data[0][6]))

    def search_stock_click():
        a = searchstockVar.get()
        key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list = get_stock_table()
        if a == '':
            messagebox.showwarning(title='Warning',message='กรุณากรอกไอดีสินค้า')
        elif a in id_list:
            index = id_list.index(a)
            carttree.delete(*carttree.get_children())
            carttree.insert('', 'end',values=(id_list[index],product_name_list[index],amount_list[index],status_list[index]))
        else:
            messagebox.showwarning(title='Warning',message='ไม่พบไอดีสินค้า')

    Label(l1,text="สินค้าชำรุด",bg='#FBE09A').grid(row=0,column=0,rowspan=2)
    Entry(l1,width=20,textvariable=searchstockVar).grid(row=0,column=1,rowspan=2,sticky=W)
    Button(l1,text="ค้นหา",bg=button_color,relief = "raised",width=6,command=search_stock_click).grid(row=0,column=1,rowspan=2,sticky=E)
    Button(l1,text="รีเฟรช",image=images8,compound=RIGHT,bg=bg_color,relief = "raised",width=100,height=40,command=refresh_stock_click).grid(row=0,column=3,rowspan=2)
    Frame_right4.grid(row=0,rowspan=3,columnspan=7,column=0,sticky=NSEW)

    cartbar = Scrollbar(l2)
    cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
    carttree = ttk.Treeview(l2,columns=("MenuId","MenuName","Menuquantity","MenuStatus"),yscrollcommand=cartbar.set)
    carttree.grid(row=0,column=0,rowspan=5,columnspan=5,sticky=NSEW)
    cartbar.config(command=carttree.yview)
    carttree.heading("#0",text="",anchor=CENTER)
    carttree.heading("MenuId",text="ไอดี",anchor=CENTER)
    carttree.heading("MenuName",text="ชื่อสินค้า",anchor=CENTER)
    carttree.heading("Menuquantity",text="จำนวน",anchor=CENTER)
    carttree.heading("MenuStatus",text="สถานะ",anchor=CENTER)


    carttree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    carttree.column("MenuId",anchor=CENTER,width=100)
    carttree.column("MenuName",anchor=CENTER,width=200)
    carttree.column("Menuquantity",anchor=CENTER,width=150)
    carttree.column("MenuStatus",anchor=CENTER,width=125)
    result = get_stock_table_v2()
    for i,data in enumerate(result):
        # MenuId","MenuName","Menuquantity","MenuStatus","MenuPrice","MenuUpdate"
        if data[0][6] == 'ชำรุด':
            carttree.insert('', 'end',values=(data[0][1],data[0][2],data[0][3],data[0][6]))






def Menu_right(Frame_right):
    f1=Frame(Frame_right,bg=frame_left_color)
    f1.rowconfigure((0,1),weight=1)
    f1.columnconfigure((0,1),weight=1)
    f1.grid(row=0,column=0,columnspan=6,sticky=NSEW,pady=60,padx=50)

    f2=Frame(Frame_right,bg=frame_color,height=50,width=50)
    f2.rowconfigure((0,1),weight=1)
    f2.columnconfigure((0,1),weight=1)
    f2.grid(row=1,column=0,columnspan=2,sticky=NSEW,padx=20)

    f3=Frame(Frame_right,bg=frame_color,height=50,width=50)
    f3.rowconfigure((0,1),weight=1)
    f3.columnconfigure((0,1),weight=1)
    f3.grid(row=1,column=2,columnspan=2,sticky=NSEW,padx=60)
    
    f4=Frame(Frame_right,bg=frame_color)
    f4.rowconfigure((0,1),weight=1)
    f4.columnconfigure((0,1),weight=1)
    f4.grid(row=1,column=4,columnspan=2,sticky=NSEW,padx=20)
    return f1,f2,f3,f4

def layer1(f1):
    Label(f1,text="คลังสินค้า",font="Opun 30 ",bg=frame_left_color).grid(row=0,column=0,columnspan=2)


def layer2(f2):
    Label(f2,text="รายการสั่งซื้อ",bg=frame_color).grid(row=0,column=0,columnspan=2)

def layer3(f3):
    Label(f3,text=" โปรโมชั่น ",bg=frame_color).grid(row=0,column=0,columnspan=2)

def layer4(f4):
    Label(f4,text="สินค้าชำรุด",bg=frame_color).grid(row=0,column=0,columnspan=2)


root = ui_config()
nameVar = StringVar()
searchstockVar = StringVar()
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
f1,f2,f3,f4=Menu_right(Frame_right)
layer1(f1)
layer2(f2)
layer3(f3)
layer4(f4)

root.mainloop()