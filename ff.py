#from login import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from config import *
from tkinter.font import Font
from backend_insert import *
import time




def login_register():
    from login import root,lo_container
    from register import re_container,onclick,onclick2,fp,fp2
    def log(e):
        regis()
    def reg(e):
        login()
    def forg(e):
        forgot_pass()
    
    underline_font = Font(family= 'Opun',size= 11,underline=1)

    def login():
        register,user,password,b1,fg,lr = lo_container()
        def underline(e):
            register['font'] = underline_font
        def outline(e):
            register['font'] = 'Opun 11'
        
        def underline2(e):
            fg['font'] = underline_font
        def outline2(e):
            fg['font'] = 'Opun 10'

        def bind_function():
            register.bind('<Button-1>',log)
            register.bind('<Enter>',underline)
            register.bind('<Leave>',outline)
            b1.configure(command = validcheck)
            
            fg.bind('<Button-1>',forg)
            fg.bind('<Enter>',underline2)
            fg.bind('<Leave>',outline2)
    
            return register
        
        def validcheck(): ### may be use messagebox instead of print
            if user.get() == "" or password.get() == "":
                user['highlightbackground'] = '#E44D4D'
                password['highlightbackground'] = '#E44D4D'
                lr['text'] = 'กรุณากรอกชื่อผู้ใช้งานหรือรหัสผ่าน*'
            
            else:
                username = user.get()
                pass_ = password.get()
                id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
                if username in username_list and pass_ in pwd_list:
                    print("login")
                    name = ""
                    for i in range(len(username_list)):
                        if username == username_list[i]:
                            name = fname_list[i] + " " + lname_list[i]
                            status = status_list[i]
                    if status == "0":
                        lr['text'] = 'ไอดีนี้ยังไม่ได้รับการยืนยัน*'
                    elif status == "1":
                        main_function(name,root)
                    elif status == "2":
                        from admin import adminpp
                        root.destroy()
                        adminpp()
                        return



                else:
                   lr['text'] = 'ชื่อผู้ใช้งานและรหัสผ่านไม่ตรงกัน*'

            
        return bind_function()
      

    def regis():
        login,e1,e2,e3,e4,e5,e6,b1,r1,r2,l1,l2 = re_container()
        def underline(e):
            login['font'] = underline_font
        def outline(e):
            login['font'] = 'Opun 11'

      
        def bind_function():
            login.bind('<Button-1>',reg)
            login.bind('<Enter>',underline)
            login.bind('<Leave>',outline)
            b1.configure(command = validcheck)
            r1.configure(command = onclick)
            

            return login
    
        def validcheck():
            if e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == "" or e6.get() == "" or onclick() == 0 or onclick2() == 0 : 
                e1['highlightbackground'] = '#E44D4D'
                e2['highlightbackground'] = '#E44D4D'
                e3['highlightbackground'] = '#E44D4D'
                e4['highlightbackground'] = '#E44D4D'
                e5['highlightbackground'] = '#E44D4D'
                e6['highlightbackground'] = '#E44D4D'
                l1['text'] = 'กรุณากรอกข้อมูล*'
                
                

            elif e2.get() != e3.get():
                l1['text'] = ''
                l2['text'] = 'รหัสผ่านไม่ตรงกัน*'
            else:
                l1['text'] = ''
                l2['text'] = ''
                # e1 = e6 ไว้เก็บ entry ข้อมูลเรียงตามหน้าลงทะเบียน อย่าลืม .get() ก่อนเพื่ิอดึงข้อมูล
                x = "" #เก็บข้อมูล คำนำหน้า
                y = "" #เก็บข้อมูล แผนก
                t1 = onclick() #คำนำหน้า
                t2 = onclick2() #แผนก
                
                if t1 == 1 :
                    x = "นาย"
                elif t1 == 2 :
                    x = "นาง"
                elif t1 == 3 :
                    x = 'นางสาว'

                if t2 == 1:
                    y = "ฝ่ายดูแลระบบ"
                elif t2 == 2 :
                    y = "ฝ่ายขาย"
                elif t2 == 3 :
                    y = "ฝ่ายจัดการคลังสินค้า"

                id_list, username_list, pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
                username=e1.get()
                if username not in username_list:
                    insert_user(username,e2.get(),e4.get(),e5.get(),e6.get(),'0',y,x)
                    return
                
                l1['text'] = 'ชื่อผู้ใช้งานถูกใช้แล้ว*'
                e1['highlightbackground'] = '#E44D4D'

        return bind_function()
    
    def forgot_pass():
        
        b2,e3,body,l1 = fp()
        def validcheck():
            if e3.get() == "":
                e3['highlightbackground'] = '#E44D4D'
                l1['text'] = 'กรุณากรอกชื่อผู้ใช้งาน*'
            else:
                id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
                username = e3.get()
                print(username_list)
                if username in username_list:
                    index = username_list.index(username)
                    key = id_list[index]
                    f2(username_list,key)
                    body.destroy()
                    return 
    

                l1['text'] = 'ไม่พบชื่อผู้ใช้งานนี้*'

       
        b2.configure(command = validcheck)
  
    def f2(username_list,key):
        b3,e8,e9,body2,e2 = fp2()
        def validcheck():
            if e8.get() == "" or e9.get() == "":
                e8['highlightbackground'] = '#E44D4D'
                e9['highlightbackground'] = '#E44D4D'
                e2['text'] = 'กรอกรหัสผ่าน*'
            else:
                if e8.get() == e9.get():
                    update_table('test',key,'password',e8.get())
                    messagebox.showinfo("เปลี่ยนรหัสผ่าน","เปลี่ยนรหัสผ่านเสร็จสิ้น")
                    login_register()
                    body2.destroy()
                else:
                     e2['text'] = 'รหัสผ่านไม่ตรงกัน*'



                
        b3.configure(command = validcheck)
    register = login()
    root.mainloop()


def main_function(name,root):
    root.destroy()

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
        root.columnconfigure(0,weight=3)
        root.columnconfigure(1,weight=10)
        root.rowconfigure(0,weight=1)
    
        return root

    def frameLayout():
        frame_left = Frame(root,bg=frame_left_color)
        frame_left.columnconfigure((0,1),weight=1)
        frame_left.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
        frame_left.grid(row=0,column=0,sticky=NSEW)

        frame_right = Frame(root,bg=bg_color)
        frame_right.columnconfigure((0,2,4,6),weight=1)
        frame_right.columnconfigure((1,3,5),weight=3)
        frame_right.rowconfigure((0,2),weight=2)
        frame_right.rowconfigure(1,weight=1)
        frame_right.grid(row=0,column=1,sticky=NSEW)

        return frame_left,frame_right

    def menu_right():
        frame_right1 = Frame(frame_right,bg=bg_color)
        frame_right1.columnconfigure((0,2,4,6),weight=1)
        frame_right1.columnconfigure((1,3,5),weight=3)
        frame_right1.rowconfigure((0,2),weight=2)
        frame_right1.rowconfigure(1,weight=1)
        frame_right1.grid(row=0,column=0,columnspan=7,rowspan=3,sticky=NSEW)
        
        f1=Frame(frame_right1,bg=frame_left_color)
        f1.rowconfigure(0,weight=1)
        f1.rowconfigure(1,weight=1)
        f1.columnconfigure((0,1),weight=1)
        f1.grid(row=0,column=0,columnspan=6,sticky=NSEW,pady=60,padx=50)
        Label(f1,text="คลังสินค้า",font="Opun 45",bg=frame_left_color).grid(row=0,column=0,columnspan=2)
        st1 = Label(f1,text="0",font="Opun 45",bg=frame_left_color)
        st1.grid(row=1,column=0,columnspan=2)

        f2=Frame(frame_right1,bg=frame_color)
        f2.rowconfigure(0,weight=1)
        f2.rowconfigure(1,weight=1)
        f2.columnconfigure((0,1),weight=1)
        f2.grid(row=1,column=1,sticky=NSEW,)
        Label(f2,text="รายการสั่งซื้อ",font="Opun 20",bg=frame_color).grid(row=0,column=0,columnspan=2,sticky=N)
        st2 = Label(f2,text="0",font="Opun 20",bg=frame_color)
        st2.grid(row=1,column=0,columnspan=2,sticky=N)

        f3=Frame(frame_right1,bg=frame_color)
        f3.rowconfigure(0,weight=1)
        f3.rowconfigure(1,weight=1)
        f3.columnconfigure((0,1),weight=1)
        f3.grid(row=1,column=3,sticky=NSEW)
        Label(f3,text="โปรโมชั่น",font="Opun 20",bg=frame_color).grid(row=0,column=0,columnspan=2,sticky=N)
        st3 = Label(f3,text="0",font="Opun 20",bg=frame_color)
        st3.grid(row=1,column=0,columnspan=2,sticky=N)


        f4=Frame(frame_right1,bg=frame_color)
        f4.rowconfigure(0,weight=1)
        f4.rowconfigure(1,weight=1)
        f4.columnconfigure((0,1),weight=1)
        f4.grid(row=1,column=5,sticky=NSEW)
        Label(f4,text="สินค้าชำรุด",font="Opun 20",bg=frame_color).grid(row=0,column=0,columnspan=2,sticky=N)
        st4 = Label(f4,text="0",font="Opun 20",bg=frame_color)
        st4.grid(row=1,column=0,columnspan=2,sticky=N)


        key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = get_stock_table()
  
        x = 0
        y = 0

        for i in range(len(id_list)):
            if status_list[i] == "โปรโมชั่น":
                x += 1
            elif status_list[i] == "ชำรุด":
                y += 1

        st1['text'] = str(len(product_name_list)) + " ชิ้น"
        st3['text'] = str(x) + " ชิ้น"
        st2['text'] = str(len(company_name_list)) + " รายการ"
        st4['text'] = str(y) + " ชิ้น"

    def menu_left():
        t1=Label(frame_left,image=images7,text='Stock',compound=LEFT,fg='black',bg=frame_left_color,font="Opun 20")
        t1.grid(row=0,column=1,pady=25)

        t2=Label(frame_left,text= name,fg='black',bg=frame_left_color)
        t2.grid(row=1,column=1,pady=25)


        b1=Button(frame_left,image=images1,text="  "+ "Dashboard",fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command = lambda:menu_right())
        b1.grid(row=2,column=1,sticky=W,pady=25)

        b2=Button(frame_left,image=images2,text="  "+ "คลังสินค้า",fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command = lambda:onclick1())
        b2.grid(row=3,column=1,sticky=W,pady=25)

        b3=Button(frame_left,image=images3,text="  "+ "รายการสั่งซื้อ",fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command = lambda:onclick2())
        b3.grid(row=4,column=1,sticky=W,pady=25)

        b4=Button(frame_left,image=images4,text="  "+ "โปรโมชั่น",fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command = lambda:onclick3())
        b4.grid(row=5,column=1,sticky=W,pady=25)

        b5=Button(frame_left,image=images5,text="  "+ "สินค้าชำรุด",fg='black',bg=frame_left_color,relief="flat",compound=LEFT,command = lambda:onclick4())
        b5.grid(row=6,column=1,sticky=W,pady=25)
        Button(frame_left,image=images6,text="ออก  ",bg="white",relief = "raised",compound=RIGHT,command = root.destroy).grid(row=7,column=1,sticky=W,pady=25)


    def onclick1():
        frame_right1 = Frame(frame_right,bg=bg_color)
        frame_right1.columnconfigure((0,1,2,3,4),weight=1)
        frame_right1.rowconfigure((0,1,2,4),weight=1)
        frame_right1.rowconfigure(3,weight=15)
        frame_right1.grid(row=0,rowspan=3,columnspan=7,column=0,sticky=NSEW)

        l1=Frame(frame_right1,bg="#FBE09A")
        l1.columnconfigure((0,1,2,3),weight=1)
        l1.rowconfigure((0,1),weight=1)
        l1.grid(row=0,column=0,columnspan=5,sticky=NSEW)

        def refresh_stock_click1():
            carttree.delete(*carttree.get_children())
            result = get_stock_table_v2()
            for i,data in enumerate(result):
                if data[0][10] == "โปรโมชั่น":
                    p = float(data[0][6]) - float(data[0][7][:-3])
                    carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][10],p,data[0][9]))
                else:
                    carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][10],data[0][6],data[0][9]))

        def search_stock_click1():
            a = searchstockVar.get()
            key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = get_stock_table()
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

        Label(l1,text="คลังสินค้า",bg='#FBE09A',font="Opun 45").grid(row=0,column=0,columnspan=4)
        Label(l1,text="ค้นหาไอดีสินค้า",bg='#FBE09A').grid(row=1,column=1)
        Entry(l1,width=35,textvariable=searchstockVar).grid(row=1,column=2,sticky=W)

        Button(l1,text="ค้นหา",bg=button_color,relief = "raised",width=6,command=search_stock_click1).grid(row=1,column=3,sticky=NW)
        Button(l1,text="รีเฟรช",image=images8,compound=RIGHT,bg=button_color,relief = "raised",width=100,height=40,command=refresh_stock_click1).grid(row=0,column=3)


        my1=Frame(frame_right1,bg="#FFE4B5")
        my1.grid(row=3,column=0,columnspan=5,padx=20,sticky=NSEW)
        my1.columnconfigure((0,1,2),weight=1)
        my1.rowconfigure((0,1,2,3),weight=1)
        Button(frame_right1,text="เพิ่มลดรายการสินค้า",bg=button_color,width=15,command=status).grid(row=2,column=1,sticky=N,padx=10)
        Button(frame_right1,text="แก้ไขสถานะสินค้า",bg=button_color,width=15,command=status2).grid(row=2,column=2,sticky=N,padx=10)
        Button(frame_right1,text="เพิ่มรายการสินค้า",bg=button_color,width=18,command=addstock).grid(row=2,column=3,sticky=N,padx=10)
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
        array = []
        ssl = []
   

        for i,data in enumerate(result):
            #if data[0][4] not in array:
               # array.append(data[0][4])
            if data[0][10] == "โปรโมชั่น":
                p = float(data[0][6]) - float(data[0][7][:-3])
                carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][10],p,data[0][9]))
            else:
                carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][10],data[0][6],data[0][9]))


    def onclick2():
        frame_right2 = Frame(frame_right,bg=bg_color)
        frame_right2.columnconfigure((0,1,2,3,4),weight=1)
        frame_right2.rowconfigure((0,1,2,4),weight=1)
        frame_right2.rowconfigure(3,weight=15)
        frame_right2.grid(row=0,rowspan=3,columnspan=7,column=0,sticky=NSEW)

        l2=Frame(frame_right2,bg="#FBE09A")
        l2.columnconfigure((0,1,2,3),weight=1)
        l2.rowconfigure((0,1),weight=1)
        l2.grid(row=0,column=0,columnspan=5,sticky=NSEW)

        def refresh_stock_click2():
            carttree.delete(*carttree.get_children())
            result = get_order_table_v2()
            for i,data in enumerate(result):
                carttree.insert('', 'end',values=(data[0][1],data[0][4],data[0][2],int(data[0][7])*int(data[0][6]),data[0][6],data[0][8],data[0][9]))
        def search_stock_click2():
            a = searchstockVar.get()
            id_list,order_id_list,company_name_list,contact_number_list,related_name_list,order_product_id_list,order_product_name_list,order_price_list,order_amount_list,order_status_list,order_date_list = get_order_table()
            if a == '':
                messagebox.showwarning(title='Warning',message='กรุณากรอกเลขใบสั่งซื้อ')
            elif a in order_id_list:
                index = order_id_list.index(a)
                carttree.delete(*carttree.get_children())
                carttree.insert('', 'end',values=(company_name_list[index],order_id_list[index],contact_number_list[index],int(order_amount_list[index])*int(order_price_list[index]),order_price_list[index],order_status_list[index],order_date_list[index]))
            else:
                messagebox.showwarning(title='Warning',message='ไม่พบเลขใบสั่งซื้อ')

        Label(l2,text="รายการสั่งซื้อ",bg='#FBE09A',font="Opun 45").grid(row=0,column=0,columnspan=4)
        Label(l2,text="ค้นหาเลขใบสั่งซื้อ",bg='#FBE09A').grid(row=1,column=1)
        Entry(l2,width=35,textvariable=searchstockVar).grid(row=1,column=2,sticky=W)

        Button(l2,text="ค้นหา",bg=button_color,relief = "raised",width=6,command=search_stock_click2).grid(row=1,column=3,sticky=NW)
        Button(l2,text="รีเฟรช",image=images8,compound=RIGHT,bg=button_color,relief = "raised",width=100,height=40,command=refresh_stock_click2).grid(row=0,column=3)
        Button(frame_right2,text="+ เปิดใบสั่งซื้อใหม่",bg=button_color,width=15,command=neworder).grid(row=2,column=4,sticky=NE,padx=10)

        my2=Frame(frame_right2,bg="#FFE4B5")
        my2.grid(row=3,column=0,columnspan=5,padx=20,sticky=NSEW)
        my2.columnconfigure((0,1,2),weight=1)
        my2.rowconfigure((0,1,2,3),weight=1)
        cartbar = Scrollbar(my2)
        cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
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
        result = get_order_table_v2()
        for i,data in enumerate(result):
            carttree.insert('', 'end',values=(data[0][1],data[0][4],data[0][2],int(data[0][7])*int(data[0][6]),data[0][6],data[0][8],data[0][9]))

    def status():
        from status_config import statusconfig
        statusconfig()
        
    def status2():
        from status2_config import statusconfig2
        statusconfig2()
        
    def addstock():
        from addstock import add_stock
        add_stock()

    def neworder():
        from new_Order import neworder
        neworder()
    


    def onclick3():
        frame_right3 = Frame(frame_right,bg=bg_color)
        frame_right3.columnconfigure((0,1,2,3,4),weight=1)
        frame_right3.rowconfigure((0,1,2,4),weight=1)
        frame_right3.rowconfigure(3,weight=15)
        frame_right3.grid(row=0,rowspan=3,columnspan=7,column=0,sticky=NSEW)

        l3=Frame(frame_right3,bg="#FBE09A")
        l3.columnconfigure((0,1,2,3),weight=1)
        l3.rowconfigure((0,1),weight=1)
        l3.grid(row=0,column=0,columnspan=5,sticky=NSEW)

        def refresh_stock_click3():
            carttree.delete(*carttree.get_children())
            result = get_stock_table_v2()
            for i,data in enumerate(result):
                if data[0][10] == "โปรโมชั่น":
                    p = float(data[0][6]) - float(data[0][7][:-3])
                    carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][10],p,data[0][9]))
        
        def search_stock_click3():
            a = searchstockVar.get()
            key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = get_stock_table()
            if a == '':
                messagebox.showwarning(title='Warning',message='กรุณากรอกไอดีสินค้า')
            elif a in id_list:
                index = id_list.index(a)
                carttree.delete(*carttree.get_children())
                if status_list[index] == 'โปรโมชั่น':
                    p = float(price_list[index]) - float(promo_price_list[index][:-3])
                    carttree.insert('', 'end',values=(id_list[index],product_name_list[index],amount_list[index],status_list[index],p,date_list[index]))
                else:
                    messagebox.showwarning(title='Warning',message='ไม่พบไอดีสินค้า')


        Label(l3,text="โปรโมชั่น",bg='#FBE09A',font="Opun 45").grid(row=0,column=0,columnspan=4)
        Label(l3,text="ค้นหาไอดีสินค้า",bg='#FBE09A').grid(row=1,column=1)
        Entry(l3,width=35,textvariable=searchstockVar).grid(row=1,column=2,sticky=W)

        Button(l3,text="ค้นหา",bg=button_color,relief = "raised",width=6,command=search_stock_click3).grid(row=1,column=3,sticky=NW)
        Button(l3,text="รีเฟรช",image=images8,compound=RIGHT,bg=button_color,relief = "raised",width=100,height=40,command=refresh_stock_click3).grid(row=0,column=3)
        my3=Frame(frame_right3,bg="#FBE09A")
        my3.grid(row=3,column=0,columnspan=5,padx=20,sticky=NSEW)
        my3.columnconfigure((0,1,2),weight=1)
        my3.rowconfigure((0,1,2,3),weight=1)
        cartbar = Scrollbar(my3)
        cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        carttree = ttk.Treeview(my3,columns=("MenuId","MenuName","MenuPrice","MenuPromotion","MenuDate"),yscrollcommand=cartbar.set)
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
        result = get_stock_table_v2()
        for i,data in enumerate(result):    
            if data[0][10] == "โปรโมชั่น":
                p = float(data[0][6]) - float(data[0][7][:-3])
                carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][10],p,data[0][9]))
          
    def onclick4():
        frame_right4 = Frame(frame_right,bg=bg_color)
        frame_right4.columnconfigure((0,1,2,3,4),weight=1)
        frame_right4.rowconfigure((0,1,2,4),weight=1)
        frame_right4.rowconfigure(3,weight=15)
        frame_right4.grid(row=0,rowspan=3,columnspan=7,column=0,sticky=NSEW)

        l4=Frame(frame_right4,bg="#FBE09A")
        l4.columnconfigure((0,1,2,3),weight=1)
        l4.rowconfigure((0,1),weight=1)
        l4.grid(row=0,column=0,columnspan=5,sticky=NSEW)

        my4=Frame(frame_right4,bg="#FBE09A")
        my4.columnconfigure((0,1,2,3,4),weight=1)
        my4.rowconfigure((0,1,2,3,4),weight=1)
        my4.grid(row=3,column=0,columnspan=5,sticky=NSEW,padx=20)

        def refresh_stock_click4():
            carttree.delete(*carttree.get_children())
            result = get_stock_table_v2()
            for i,data in enumerate(result):  
                if data[0][10] == "ชำรุด":
                    p = float(data[0][6]) - float(data[0][7][:-3])
                    carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][10],p,data[0][9]))

        def search_stock_click4():
            a = searchstockVar.get()
            key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = get_stock_table()
            if a == '':
                messagebox.showwarning(title='Warning',message='กรุณากรอกไอดีสินค้า')
            elif a in id_list:
                index = id_list.index(a)
                carttree.delete(*carttree.get_children())
                if status_list[index] == 'ชำรุด':
                    p = float(price_list[index]) - float(promo_price_list[index][:-3])
                    carttree.insert('', 'end',values=(id_list[index],product_name_list[index],amount_list[index],status_list[index],p,date_list[index]))
            else:
                messagebox.showwarning(title='Warning',message='ไม่พบไอดีสินค้า')

        Label(l4,text="สินค้าชำรุด",bg='#FBE09A',font="Opun 45").grid(row=0,column=0,columnspan=4)
        Label(l4,text="ค้นหาไอดีสินค้า",bg='#FBE09A').grid(row=1,column=1)
        Entry(l4,width=35,textvariable=searchstockVar).grid(row=1,column=2,sticky=W)

        Button(l4,text="ค้นหา",bg=button_color,relief = "raised",width=6,command=search_stock_click4).grid(row=1,column=3,sticky=NW)
        Button(l4,text="รีเฟรช",image=images8,compound=RIGHT,bg=button_color,relief = "raised",width=100,height=40,command=refresh_stock_click4).grid(row=0,column=3)
        cartbar = Scrollbar(my4)
        cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        carttree = ttk.Treeview(my4,columns=("MenuId","MenuName","Menuquantity","MenuStatus"),yscrollcommand=cartbar.set)
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
        result = get_oldstock_table_v2()

        for i,data in enumerate(result):   
            print(data[0][4],data[0][5],data[0][10])
            print(data[0][6])
            if data[0][10] == "ชำรุด":

                p = float(data[0][6]) - float(data[0][7][:-3])
                carttree.insert('', 'end',values=(data[0][4],data[0][5],data[0][8],data[0][10],p,data[0][9]))

    def layer1(f1):
        Label(f1,text="คลังสินค้า",font="Opun 30 ",bg=frame_left_color).grid(row=0,column=0,columnspan=2)

    def layer2(f2):
        Label(f2,text="รายการสั่งซื้อ",bg=frame_color).grid(row=0,column=0,columnspan=2)

    def layer3(f3):
        Label(f3,text=" โปรโมชั่น ",bg=frame_color).grid(row=0,column=0,columnspan=2)

    def layer4(f4):
        Label(f4,text="สินค้าชำรุด",bg=frame_color).grid(row=0,column=0,columnspan=2)


    root = ui_config()
    frame_left,frame_right =frameLayout()
    nameVar = StringVar()
    nameVar.set('asd')
    searchstockVar = StringVar()
    infolist = ["คลังสินค้า","รายการสั่งซื้อ","รายการสั่งสินค้า","โปรโมชั่น","สินค้าชำรุด"]
    images1 = PhotoImage(file='images/dashboard.png').subsample(15,15) 
    images2 = PhotoImage(file='images/box.png').subsample(15,15) 
    images3 = PhotoImage(file='images/clipboard.png').subsample(15,15) 
    images4 = PhotoImage(file='images/dollar.png').subsample(15,15) 
    images5 = PhotoImage(file='images/tools.png').subsample(15,15) 
    images6 = PhotoImage(file='images/logout.png').subsample(15,15) 
    images7 = PhotoImage(file='images/boxes.png').subsample(13,13) 
    images8 = PhotoImage(file='images/refreshs.png').subsample(20,20)
    imageslist =[images1,images2,images3,images4,images5]
    
    menu_left()
    menu_right()
    root.mainloop()

login_register()
