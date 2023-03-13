#from login import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from config import *

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
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=6)
    root.rowconfigure(2,weight=4)
    root.option_add("*Font",font)
    return root

def layout(root):
    top_fm = Frame(root,bg="#FBE09A")
    top_fm.rowconfigure((0,1),weight=1)
    top_fm.columnconfigure((0,1),weight=1)
    top_fm.grid(row=0,column=0,sticky=NSEW)
    Label(top_fm,text="เช็คสินค้าที่สั่งซื้อ",fg='#000000',bg='#FBE09A',font=('Opun 30')).grid(row=0,rowspan=2,column=0)
    Button(top_fm,text='ย้อนกลับ',width=8,bg=button_color).grid(row=0,column=1,sticky=E,padx=10)

    mid_fm = Frame(root,bg="#FBE09A")
    mid_fm.columnconfigure((0,1,2,3),weight=1)
    mid_fm.rowconfigure((0,1,2,3,4,5),weight=1)
    mid_fm.grid(row=1,column=0,sticky=NSEW,pady=20,padx=20)

    buttom_fm = Frame(root)
    buttom_fm.columnconfigure((0,1,2,3,4,5),weight=1)
    buttom_fm.rowconfigure(0,weight=6)
    buttom_fm.grid(row=2,column=0,sticky=NSEW,pady=20,padx=20)

    return top_fm,mid_fm,buttom_fm




    
def layer_middle(mid_fm,buttom_fm):
    Label(mid_fm,text="ชื่อบริษัท",bg='#FBE09A').grid(row=0,column=0)
    Label(mid_fm,text="111",bg='#FBE09A').grid(row=0,column=1,sticky=W)


    Label(mid_fm,text="ชื่อผู้ติดต่อ",bg='#FBE09A').grid(row=0,column=2)
    Label(mid_fm,text="111",bg='#FBE09A').grid(row=0,column=3)

    Label(mid_fm,text="ตำแหน่ง",bg='#FBE09A').grid(row=1,column=0)
    Label(mid_fm,text="111",bg='#FBE09A').grid(row=1,column=1,sticky=W)

    Label(mid_fm,text="เบอร์โทร",bg='#FBE09A').grid(row=1,column=2)
    Label(mid_fm,text="111",bg='#FBE09A').grid(row=1,column=3)

    Label(mid_fm,text="เลขใบสั่งซื้อ",bg='#FBE09A').grid(row=2,column=0)
    Label(mid_fm,text="111",bg='#FBE09A').grid(row=2,column=1,sticky=W)

    Label(mid_fm,text="หน่วย",bg='#FBE09A').grid(row=2,column=2)
    Label(mid_fm,text="111",bg='#FBE09A').grid(row=2,column=3)
    
   

    Label(mid_fm,text=" ",bg='#FBE09A').grid(row=4,column=0,columnspan=4)


    my5=Frame(buttom_fm,bg="#FFE4B5")
    my5.grid(row=0,column=0,columnspan=5,sticky=NSEW,padx=20)
    my5.columnconfigure((0,1,2),weight=1)
    my5.rowconfigure((0,1,2,3),weight=1)

    cartbar = Scrollbar(my5)
    cartbar.grid(row=0,column=0,columnspan=5,sticky=NSEW)
    mytree = ttk.Treeview(my5,columns=("MenuId","MenuName","MenuAmount","MenuPrice"),yscrollcommand=cartbar.set)
    mytree.grid(row=0,rowspan=4,column=0,columnspan=5,sticky=NSEW)
    cartbar.config(command=mytree.yview)
    mytree.heading("#0",text="",anchor=CENTER)
    mytree.heading("MenuId",text="ไอดีสินค้า",anchor=CENTER)
    mytree.heading("MenuName",text="ชื่อสินค้า",anchor=CENTER)
    mytree.heading("MenuAmount",text="จำนวน",anchor=CENTER)
    mytree.heading("MenuPrice",text="ราคา",anchor=CENTER)

    mytree.column("#0",width=0,minwidth=0) 
    mytree.column("MenuId",anchor=CENTER,width=250)
    mytree.column("MenuName",anchor=CENTER,width=200)
    mytree.column("MenuAmount",anchor=CENTER,width=200)
    mytree.column("MenuPrice",anchor=CENTER,width=200)



root = ui_config()
top_fm,mid_fm,buttom_fm = layout(root)
layer_middle(mid_fm,buttom_fm)
root.mainloop()