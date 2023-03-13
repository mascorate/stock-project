from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from backend_insert import get_stock_table, get_stock_table_v2
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
    Frame_left = Frame(root,bg=frame_left_color)
    Frame_left.columnconfigure((0,1,2),weight=1)
    Frame_left.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    Frame_left.grid(row=0,column=0,sticky=NSEW)

    Frame_right = Frame(root,bg=bg_color)
    Frame_right.columnconfigure((0,1,2,3,4),weight=1)
    Frame_right.rowconfigure((0,1,2,4),weight=1)
    Frame_right.rowconfigure(3,weight=15)
    Frame_right.grid(row=0,column=1,sticky=NSEW)
    def addtostock():
        # root.destroy()
        from addstock import layout
        # root = ui_config()
        top_fm,mid_fm=layout(root)
        # f2=menu_fm2(top_fm,mid_fm)
        # layer(f2)

    Button(Frame_right,text="เพิ่มลดรายการสินค้า",bg=button_color,width=15).grid(row=2,column=1,sticky=N,padx=10)
    Button(Frame_right,text="แก้ไขสถานะสินค้า",bg=button_color,width=15).grid(row=2,column=2,sticky=N,padx=10)
    Button(Frame_right,text="เพิ่มรายการสินค้า",bg=button_color,width=15,command=addtostock).grid(row=2,column=3,sticky=N,padx=10)


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
    l1.grid(row=0,column=0,columnspan=5,sticky=NSEW)

    l2=Frame(Frame_right,bg="#FBE09A")
    l2.columnconfigure((0,1,2,3,4),weight=1)
    l2.rowconfigure((0,1,2,3,4),weight=1)
    l2.grid(row=3,column=0,columnspan=5,sticky=NSEW,padx=20)
    return l1,l2

def refresh():
    carttree.delete(*carttree.get_children())
    result = get_stock_table_v2()
    for i,data in enumerate(result):
        carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][6],data[0][10],data[0][9]))

def search_item():
    carttree.delete(*carttree.get_children())
    id = searchVar.get()
    key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,unit_list = get_stock_table()
    if id not in id_list:
        print('not found')
    else:
        dex = id_list.index(id)
        carttree.insert('', 'end',values=(id_list[dex],product_name_list[dex],amount_list[dex],int(price_list[dex])-int(promo_price_list[dex][:-3]),status_list[dex],date_list[dex]))

def layer_top(l1):
    Label(l1,text="คลังสินค้า",bg='#FBE09A').grid(row=0,column=0,rowspan=2)
    Entry(l1,width=20,textvariable=searchVar).grid(row=0,column=1,rowspan=2,sticky=W)
    Button(l1,text="ค้นหา",bg=button_color,relief = "raised",width=6,command=search_item).grid(row=0,column=1,rowspan=2,sticky=E)
    Button(l1,text="รีเฟรช",image=images8,compound=RIGHT,bg=button_color,relief = "raised",width=100,height=40,command=refresh).grid(row=0,column=3,rowspan=2)

def refresh():
    carttree.delete(*carttree.get_children())
    result = get_stock_table_v2()
    for i,data in enumerate(result):
        if data[0][10] == "โปรโมชั่น":
            p = float(data[0][6]) - float(data[0][7][:-3])
            carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],p,data[0][10],data[0][9]))
        else:
            carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][6],data[0][10],data[0][9]))

def infor2(l2):
    global carttree
    cartbar = Scrollbar(l2)
    cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
    carttree = ttk.Treeview(l2,columns=("MenuId","MenuName","Menuquantity","Menuprice","MenuStatus","MenuUpdate"),yscrollcommand=cartbar.set)
    carttree.grid(row=0,column=0,rowspan=5,columnspan=5,sticky=NSEW)
    cartbar.config(command=carttree.yview)
    carttree.heading("#0",text="",anchor=CENTER)
    carttree.heading("MenuId",text="ไอดี",anchor=CENTER)
    carttree.heading("MenuName",text="ชื่อสินค้า",anchor=CENTER)
    carttree.heading("Menuquantity",text="จำนวน",anchor=CENTER)
    carttree.heading("Menuprice",text="ราคา",anchor=CENTER)
    carttree.heading("MenuStatus",text="สถานะ",anchor=CENTER)
    carttree.heading("MenuUpdate",text="Update",anchor=CENTER)


    carttree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    carttree.column("MenuId",anchor=CENTER,width=100)
    carttree.column("MenuName",anchor=CENTER,width=200)
    carttree.column("Menuquantity",anchor=CENTER,width=150)
    carttree.column("Menuprice",anchor=CENTER,width=120)
    carttree.column("MenuStatus",anchor=CENTER,width=125)
    carttree.column("MenuUpdate",anchor=CENTER,width=125)
    result = get_stock_table_v2()
    for i,data in enumerate(result):
        if data[0][10] == "โปรโมชั่น":
            p = float(data[0][6]) - float(data[0][7][:-3])
            carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],p,data[0][10],data[0][9]))
        else:
            carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][6],data[0][10],data[0][9]))

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