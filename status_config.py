from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from typing import Literal
from config import *
from backend_insert import get_stock_table,get_stock_table_v2,delete_table_data,update_table


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

def statusconfig():
    def layout(root):
        top_fm = Frame(root,bg="#FBE09A")
        top_fm.columnconfigure(0,weight=1)
        top_fm.rowconfigure((0,1),weight=1)
        top_fm.grid(row=0,column=0,sticky=NSEW)

        mid_fm = Label(root,bg="white")
        mid_fm.columnconfigure((0,1,2,3),weight=1)
        mid_fm.rowconfigure((0,2),weight=1)
        mid_fm.rowconfigure(1,weight=3)
        mid_fm.grid(row=1,sticky=NSEW)
        return top_fm,mid_fm

    def search_click(search):
        global x,p
        key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = get_stock_table()
        x = ''
        p = ''
        if search == '':
            messagebox.showwarning(title='Warning',message='กรุณากรอกไอดีสินค้า')
        elif search in id_list:
            dex = id_list.index(search)
            p = id_list[dex]
            p1['text'] = product_name_list[dex]
            p2['text'] = id_list[dex]
            p3['text'] = amount_list[dex]
            x  = amount_list[dex]


    def delete_product_click(search):
        key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = get_stock_table()
      
        if search in id_list:
            dex = id_list.index(search)
            key = key_list[dex]
            delete_table_data('stock',key)
            root.destroy()


    def menu_fm(top_fm,mid_fm): ### page 8, 13
        Label(top_fm,text="เพิ่ม/ลด สินค้า",fg='#000000',bg=frame_color,font=('Opun 20')).grid(row=0,rowspan=2,column=0,sticky=W,padx=50)
        
        Label(mid_fm,text="รหัสสินค้า",bg="white").grid(row=0,column=0,sticky=E)
        e1 = Entry(mid_fm,width=30)
        e1.grid(row=0,column=1,columnspan=2)
        Button(mid_fm,text="ค้นหา",width=8,bg=button_color,command=lambda:search_click(e1.get())).grid(row=0,column=3,sticky=W)


        f1 = Frame(mid_fm,bg="#FBE09A")
        f1.grid(row=1,column=0,columnspan=12,rowspan=3,sticky=NSEW,padx=50)
        return f1,e1

    def set_zero():
        amountVar.set(0)
    def increase():
        global new_a
        print(x)
        new_a = int(x)+int(s1.get())
        print(x,new_a)
    def decrease():
        global new_a
        new_a = int(x)-int(s1.get()) 

    def update_click():
        root2 = update_popup()
        
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

        
        def update_amount():
            key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = get_stock_table()
            if p in id_list:
                dex = id_list.index(p)
                key = key_list[dex]
    
            update_table('stock',key,'amount',new_a)  
            messagebox.showinfo(title='Warning',message='ดำเนินการเสร็จสิ้น')
            popup.destroy()

       
        Label(popup,text="ต้องการบันทึกใช่หรือไม่",font=('Garamond 20'),bg=bg_color).pack(pady=50)
        Button(popup,text='ยกเลิก',width=8,bg=button_color,command=popup.destroy).pack(side=LEFT,padx=50)
        Button(popup,text='บันทึก',width=8,bg=button_color,command=update_amount).pack(side=RIGHT,padx=50,pady=50)

    def layer(f1):
        Label(f1,text="ชื่อสินค้า",bg="#FBE09A").grid(row=1,column=0,sticky=W,padx=50)
        p1 = Label(f1,bg=frame_color)
        p1.grid(row=1,column=2,pady=10,sticky=NSEW)
        Label(f1,text="รหัสสินค้า",bg="#FBE09A").grid(row=2,column=0,sticky=W,padx=50,pady=10)
        p2 = Label(f1,bg=frame_color)
        p2.grid(row=2,column=2,pady=10,sticky=NSEW)
        Label(f1,text="จำนวนสินค้า",bg="#FBE09A").grid(row=3,column=0,sticky=W,padx=50,pady=10)
        p3 = Label(f1,bg=frame_color)
        p3.grid(row=3,column=2,pady=10,sticky=NSEW)
        Label(f1,text="เพิ่ม/ลด จำนวนสินค้า",bg="#FBE09A").grid(row=4,column=0,columnspan=2,sticky=W,padx=50)
        s1 = Spinbox(f1,form_=0,to=9999,textvariable=amountVar,form="%10.0f")
        s1.grid(row=4,column=2,columnspan=3,sticky=EW,pady=10,padx=10)
        Button(f1,width=6,text="เพิ่ม",bg=button_color,command=increase).grid(row=5,column=2)
        Button(f1,width=6,text="ลด",bg=button_color,command=decrease).grid(row=5,column=3)
        Button(f1,width=6,text="ตั้งใหม่",bg="#FBE09A",command=set_zero).grid(row=5,column=4)
        
        Button(mid_fm,text='ลบสินค้า',width=8,bg=button_color,border=2,command=lambda:delete_product_click(e1.get())).grid(row=6,column=0,pady=10)
        Button(mid_fm,text='ยกเลิก',width=8,bg=button_color,border=2,command=root.destroy).grid(row=6,column=2,pady=10,sticky=E)
        Button(mid_fm,text='บันทึก',width=8,bg=button_color,border=2,command=update_click).grid(row=6,column=3,pady=10)
        return p1,p2,p3,s1

    root = ui_config()
    amountVar = StringVar()
    statusVar = StringVar()
    n_priceVar = StringVar()
    tyVar = StringVar()
    p_name = StringVar()

    top_fm,mid_fm=layout(root)
    f1,e1 =menu_fm(top_fm,mid_fm)
    p1,p2,p3,s1 = layer(f1)
    #menu_fm2(top_fm,mid_fm)
    root.mainloop()
