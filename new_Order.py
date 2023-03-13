#from login import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from config import *
from backend_insert import get_stock_table

def ui_config():
    root = Tk()
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
    root.rowconfigure(1,weight=10)
    root.option_add("*Font",font)
    return root


    
def neworder():
    def layout(root):
        top_fm = Frame(root,bg="#FBE09A")
        top_fm.rowconfigure((0,1),weight=1)
        top_fm.grid(row=0,column=0,sticky=NSEW)
        Label(top_fm,text="เปิดใบสั่งซื้อใหม่",fg='#000000',bg='#FBE09A',font=('Opun 30')).grid(row=0,rowspan=2,column=0,padx=50,stick=NSEW)

        mid_fm = Frame(root,bg="#FBE09A")
        mid_fm.columnconfigure((0,1,2,3),weight=1)
        mid_fm.rowconfigure((0,1,2,3,4,5),weight=1)
        mid_fm.grid(row=1,column=0,sticky=NSEW,pady=20,padx=20)

        buttom_fm = Frame(root)
        buttom_fm.columnconfigure((0,1,2,3,4,5),weight=1)
        buttom_fm.rowconfigure(0,weight=6)
        buttom_fm.grid(row=2,column=0,sticky=NSEW,pady=20,padx=20)

        return top_fm,mid_fm,buttom_fm


    def insert():
        if l1.get()== '':
            lr1['text'] = 'กรุณากรอกข้อมูล'
        if l2.get()== '':
            lr2['text'] = 'กรุณากรอกข้อมูล'
        if l3.get()== '':
            lr3['text'] = 'กรุณากรอกข้อมูล'
        if l4.get()== '':
            lr4['text'] = 'กรุณากรอกข้อมูล'
        if l5.get()== '':
            lr5['text'] = 'กรุณากรอกข้อมูล'
        if l6.get()== '':
            lr6['text'] = 'กรุณากรอกข้อมูล'
            #if l6.get() == ใส่data base:
            #   messagebox.showerror("ID ของสินค้าไม่ถูกต้อง","ID ของสินค้ายังไม่ถูกใช้งาน กรุณาใช้งานฟังก์ชันเพิ่มรายการสินค้า)  

        if l7.get()== '':
            lr7['text'] = 'กรุณากรอกข้อมูล'
        if l8.get()== '':
            lr8['text'] = 'กรุณากรอกข้อมูล'

        
    def layer_middle(mid_fm,buttom_fm):
        global lr1,lr2,lr3,lr4,lr5,lr6,lr7,lr8,l1,l2,l3,l4,l5,l6,l7,l8
        Label(mid_fm,text="ชื่อบริษัท",bg='#FBE09A').grid(row=0,column=0)
        l1=Entry(mid_fm,width=18)
        l1.grid(row=0,column=1,sticky=W)
        lr1 = Label(mid_fm,text='',bg = frame_color,fg = '#E44D4D',font = 'Opun 8')
        lr1.grid(row=0,column=0,columnspan=2,sticky=E)

        Label(mid_fm,text="ชื่อผู้ติดต่อ",bg='#FBE09A').grid(row=0,column=2)
        l2=Entry(mid_fm,width=18)
        l2.grid(row=0,column=3)
        lr2 = Label(mid_fm,text='',bg = frame_color,fg = '#E44D4D',font = 'Opun 8')
        lr2.grid(row=0,column=3,columnspan=2,sticky=E,padx=30)

        Label(mid_fm,text="ตำแหน่ง",bg='#FBE09A').grid(row=1,column=0)
        l3=Entry(mid_fm,width=18)
        l3.grid(row=1,column=1,sticky=W)
        lr3 = Label(mid_fm,text='',bg = frame_color,fg = '#E44D4D',font = 'Opun 8')
        lr3.grid(row=1,column=0,columnspan=2,sticky=E)

        Label(mid_fm,text="เบอร์โทร",bg='#FBE09A').grid(row=1,column=2)
        l4=Entry(mid_fm,width=18)
        l4.grid(row=1,column=3)
        lr4 = Label(mid_fm,text='',bg = frame_color,fg = '#E44D4D',font = 'Opun 8')
        lr4.grid(row=1,column=3,columnspan=2,sticky=E,padx=30)

        Label(mid_fm,text="เลขใบสั่งซื้อ",bg='#FBE09A').grid(row=2,column=0)
        l5=Entry(mid_fm,width=18)
        l5.grid(row=2,column=1,sticky=W)
        lr5 = Label(mid_fm,text='',bg = frame_color,fg = '#E44D4D',font = 'Opun 8')
        lr5.grid(row=2,column=0,columnspan=2,sticky=E)

        Label(mid_fm,text="ไอดีสินค้า",bg='#FBE09A').grid(row=2,column=2)
        l6=Entry(mid_fm,width=18)
        l6.grid(row=2,column=3)
        lr6 = Label(mid_fm,text='',bg = frame_color,fg = '#E44D4D',font = 'Opun 8')
        lr6.grid(row=2,column=3,columnspan=2,sticky=E,padx=30)

        Label(mid_fm,text="หน่วย",bg='#FBE09A').grid(row=3,column=0)
        sp = ttk.Combobox(mid_fm,width=18,textvariable=statusVar,background="white")
        sp['values'] = ('ชิ้น','โหล','เครื่อง','รีม','แพ็ก')
        sp.grid(row=3,column=1,sticky=W)

        Label(mid_fm,text="ราคาต่อหน่วย",bg='#FBE09A').grid(row=3,column=2)
        l7=Entry(mid_fm,width=18)
        l7.grid(row=3,column=3)
        lr7 = Label(mid_fm,text='',bg = frame_color,fg = '#E44D4D',font = 'Opun 8')
        lr7.grid(row=3,column=3,columnspan=2,sticky=E,padx=30)


        Label(mid_fm,text="จำนวน",bg='#FBE09A').grid(row=4,column=0)
        l8=Entry(mid_fm,width=18)
        l8.grid(row=4,column=1,sticky=W)
        lr8 = Label(mid_fm,text='',bg = frame_color,fg = '#E44D4D',font = 'Opun 8')
        lr8.grid(row=4,column=0,columnspan=2,sticky=E)

        Button(mid_fm,text='Reset',bg=button_color,width=8).grid(row=5,column=0)
        Button(mid_fm,text='ยกเลิก',width=8,bg=button_color).grid(row=5,column=2)
        Button(mid_fm,text='บันทึก',bg=button_color,width=8,command=insert).grid(row=5,column=4,padx=10)

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

    l1=StringVar()
    l2=StringVar()
    l3=StringVar()
    l4=StringVar()
    l5=StringVar()
    l6=StringVar()
    l7=StringVar()
    l8=StringVar()
    statusVar = StringVar()
    root = ui_config()
    top_fm,mid_fm,buttom_fm = layout(root)
    layer_middle(mid_fm,buttom_fm)
    root.mainloop()