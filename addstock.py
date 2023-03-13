from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from typing import Literal
from config import *

def add_stock():
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
        root.rowconfigure(1,weight=6)
        root.option_add("*Font",font)
        return root

    def layout(root):
        top_fm = Frame(root,bg="#FBE09A")
        top_fm.columnconfigure(0,weight=1)
        top_fm.rowconfigure((0,1),weight=1)
        top_fm.grid(row=0,column=0,sticky=NSEW)

        mid_fm = Label(root,bg="#FFF7EB")
        mid_fm.columnconfigure((0,1,2,3),weight=1)
        mid_fm.rowconfigure((0,2),weight=1)
        mid_fm.rowconfigure(1,weight=3)
        mid_fm.grid(row=1,sticky=NSEW)
        return top_fm,mid_fm

    def menu_fm2(top_fm,mid_fm): ### page 15, 17
        Label(top_fm,text="เพิ่มรายการสินค้า",fg='#000000',bg=frame_color,font=('Opun 20 ')).grid(row=0,rowspan=2,column=0,sticky=W,padx=50)

        f2 = Frame(mid_fm,bg="#FFF7EB")
        f2.columnconfigure((0,1,2),weight=1)
        f2.rowconfigure((0,1,2,3,4,5,6),weight=1)
        f2.grid(row=1,column=0,columnspan=12,rowspan=3,sticky=NSEW,padx=50)
        return f2

    def layer(f2):
        Label(f2,text="ชื่อสินค้า",bg="#FFF7EB").grid(row=1,column=0,sticky=E,padx=50)
        Entry(f2,width=30,bg="white").grid(row=1,column=1,sticky=E,pady=10)

        Label(f2,text="ไอดีสินค้า",bg="#FFF7EB").grid(row=2,column=0,sticky=E,padx=50)
        Entry(f2,width=30,bg="white").grid(row=2,column=1,sticky=E,pady=10)

        Label(f2,text="หน่วย",bg="#FFF7EB").grid(row=3,column=0,padx=50,pady=10,sticky=E)
        sp = ttk.Combobox(f2,width=28,textvariable=statusVar,background="white")
        sp['values'] = ('ชิ้น','โหล','เครื่อง','รีม','แพ็ก')
        sp.grid(row=3,column=1,pady=10,sticky=E)

        Label(f2,text="จำนวน",bg="#FFF7EB").grid(row=4,column=0,padx=50,pady=10,sticky=E)
        Entry(f2,width=30,bg="white").grid(row=4,column=1,sticky=E,pady=10)

        Label(f2,text="ราคาซื้อ",bg="#FFF7EB").grid(row=5,column=0,padx=50,pady=10,sticky=E)
        Entry(f2,width=30,bg="white").grid(row=5,column=1,sticky=E,pady=10)

        
        Label(f2,text="ราคาขาย",bg="#FFF7EB").grid(row=6,column=0,padx=50,pady=10,sticky=E)
        Entry(f2,width=30,bg="white").grid(row=6,column=1,sticky=E,pady=10)
    
        Button(mid_fm,text='ยกเลิก',bg=button_color,width=7).grid(row=5,column=1,pady=10)
        Button(mid_fm,text='บันทึก',bg=button_color,width=7,command=update_click).grid(row=5,column=2,columnspan=2,pady=30)

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

    root = ui_config()


    searchVar = StringVar()
    amountVar = StringVar()
    amountVar2 = StringVar()
    statusVar = StringVar()
    n_priceVar = StringVar()
    tyVar = StringVar()
    top_fm,mid_fm=layout(root)
    f2=menu_fm2(top_fm,mid_fm)
    layer(f2)


    root.mainloop()