from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from config import *
from backend_insert import get_stock_table,get_stock_table_v2,delete_table_data, insert_stock_table,update_table,insert_oldstock,get_oldstock_table,insert_promotion
import time

def statusconfig2():
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

        mid_fm = Label(root,bg="white")
        mid_fm.columnconfigure((0,1,2,3),weight=1)
        mid_fm.rowconfigure((0,2),weight=1)
        mid_fm.rowconfigure(1,weight=3)
        mid_fm.grid(row=1,sticky=NSEW)
        return top_fm,mid_fm

    def menu_fm2(top_fm,mid_fm): ### page 15, 17
        Label(top_fm,text="แก้ไขสถาณะสินค้า",fg='#000000',bg=frame_color,font=('Opun 20 ')).grid(row=0,rowspan=2,column=0,sticky=W,padx=50)

        Label(mid_fm,text="รหัสสินค้า",bg="white").grid(row=0,column=0,sticky=E)
        en1 = Entry(mid_fm,width=30)
        en1.grid(row=0,column=1,columnspan=2)
        Button(mid_fm,text="ค้นหา",width=6,bg=button_color,command=lambda:search_click(en1.get())).grid(row=0,column=3,sticky=W)

        f2 = Frame(mid_fm,bg="#FBE09A")
        f2.grid(row=1,column=0,columnspan=12,rowspan=3,sticky=NSEW,padx=50)
        return f2

    def layer(f2):
        Label(f2,text="รหัสสินค้า",bg="#FBE09A").grid(row=1,column=0,sticky=W,padx=50)
        p1 = Label(f2,bg="#FBE09A")
        p1.grid(row=1,column=2,pady=10)

        Label(f2,text="ชื่อ",bg="#FBE09A").grid(row=2,column=0,sticky=W,padx=50,pady=10)
        p2 = Label(f2,bg="#FBE09A")
        p2.grid(row=2,column=2,pady=10)

        Label(f2,text="จำนวน",bg="#FBE09A").grid(row=3,column=0,sticky=W,padx=50,pady=10)
        p3 = Label(f2,bg="#FBE09A")
        p3.grid(row=3,column=2,pady=10)

        Label(f2,text="จำนวนที่ต้องการจะเปลี่ยน",bg="#FBE09A").grid(row=4,column=0,sticky=W,padx=50,pady=10)
        sd = Spinbox(f2,form_=0,to=9999,form="%10.0f")
        sd.grid(row=4,column=2,columnspan=2,sticky=EW,pady=10)

        Label(f2,text="สถานะ",bg="#FBE09A").grid(row=5,column=0,columnspan=2,sticky=W,padx=50,pady=10)
        sp = ttk.Combobox(f2)
        sp['values'] = ('ปกติ','ชำรุด','โปรโมชั่น')
        sp.grid(row=5,column=2,columnspan=2,sticky=EW,pady=10)


        Button(mid_fm,text='ยกเลิก',bg=button_color,width=7,command = root.destroy).grid(row=6,column=0,pady=10)
        Button(mid_fm,text='บันทึก',bg=button_color,width=7,command=update_click2).grid(row=6,column=2,columnspan=2,pady=10)
        
        return p1,p2,p3,sp,sd
    def search_click(search):
        key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = get_stock_table()
        global x,s,p,key,sta
        key = ''
        sta = ''
        x = ''
        s = 0
        p = 0
        if search in id_list:
            dex = id_list.index(search)
            p1['text'] = product_name_list[dex]
            p2['text'] = id_list[dex]
            p3['text'] = amount_list[dex]
            if status_list[dex] == 'ปกติ':
                s = 0
            elif status_list[dex] == 'ชำรุด':
                s = 1
            if status_list[dex] == "โปรโมชั่น":
                s = 2
            x = amount_list[dex]
            p = int(price_list[dex])
            key = key_list[dex]
            sta = status_list[dex]
        sp.current(int(s))
            

    def update_popup2():
        global cb,ee
        popup2=Toplevel(root)
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width / 2- window_width /2)
        center_y = int(screen_height / 2- window_height /2)
        popup2.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        popup2.config(bg=frame_color)

        Label(popup2,text="ตั้งราคาที่ต้องการจะลด",compound=CENTER,font=('Garamond 20'),bg="#FBE09A").pack(pady=50)
        ee = Entry(popup2,textvariable=n_priceVar,width=10)
        ee.pack()
        Label(popup2,text="ส่วนลด",font=('Garamond 20'),bg="#FBE09A").place(x=20,y=135)
        
        cb = ttk.Combobox(popup2,textvariable=tyVar,width=5)
        cb['values'] = ('บาท','เปอร์เซ็น')
        cb.place(x=300,y=135)
        cb.current(0)
        Button(popup2,text='ยกเลิก',width=7,bg=button_color,command=popup2.destroy).place(x=100,y=200)
        Button(popup2,text='บันทึก',width=7,bg=button_color,command = calculate).place(x=220,y=200)

    def calculate():
        global cal
        if cb.get() == "บาท":
            cal = p - int(ee.get())
        
        elif cb.get() == "เปอร์เซ็น":
            cal = p *((100-int(ee.get()))/100)

        if cal < 0 :
            messagebox.showwarning('ราคา',"ราคาของสินค้าน้อยกว่า 0 โปรดใส่ใหม่!")
           
        else:
            updatedata()

        

    def selectpopup():
        if sp.get() == 'โปรโมชั่น':
            update_popup2()
        else:
            key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = get_stock_table()
            key_list2,company_name_list2,contact_number_list2,related_name_list2,id_list2,product_name_list2,price_list2,promo_price_list2,amount_list2,date_list2,status_list2,buy_price_list2,unit_list2 = get_oldstock_table()
            dex = key_list.index(key)
            
            r = ''
            o = sd.get().strip()
            if sta == 'ปกติ':
                    
                for i in range(len(company_name_list)):
                    if id_list[i] == id_list[dex] and status_list[dex] == 'ชำรุด':
                        update_table('stock',key_list[i],'amount',amount_list[i]+sd)
                        update_table('stock',key,'amount',x-int(o))
                        
                        return

                if key in key_list2:
                    r = key_list2[dex]
                    n = int(o)
                    o = int(amount_list2[dex]) + n
                    update_table('oldstock',r,'amount',str(o))
                    update_table('stock',key,'amount',x-int(sd.get()))
                elif key not in key_list2:
                    insert_oldstock(company_name_list[dex],contact_number_list[dex],related_name_list[dex],id_list[dex],product_name_list[dex],price_list[dex],promo_price_list[dex],str(sd.get().strip()),time.ctime(),'ชำรุด',buy_price_list[dex],unit_list[dex])
                
                messagebox.showinfo("อัพเดท","อัพเดทสินค้าจำนวน " + str(o) +" ชิ้นเสร็จสิ้น")
                root.destroy()

                 


    def updatedata():
        print("A")
        # x คือ จำนวนสินค้า
        # sp.get() คือข้อมูลสถานะสินค้าใน combobox ที่ทำการเลือก
        # sd คือจำนสินค้าที่ต้องการจะเปลี่ยน

        # cal คือราคาสินค้าหลังปรับโปรโมชั่น

        # ปรับราคาและใส่ใน database

        #ins

    def update_click2():
        root2 = selectpopup()

    
    root = ui_config()
    amountVar = StringVar()
    amountVar2 = StringVar()
    statusVar = StringVar()
    n_priceVar = StringVar()
    tyVar = StringVar()
    top_fm,mid_fm=layout(root)
    f2=menu_fm2(top_fm,mid_fm)
    p1,p2,p3,sp,sd = layer(f2)


    root.mainloop()