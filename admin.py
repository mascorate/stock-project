#from login import *
import enum
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from backend_insert import get_user_table,edit_user_data,delete_table_data
from config import *
import time


def ui_config():
    root = Tk()
    root.title("Stock Admin")

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
def adminpp():
    
    def frameLayout(root):
        Frame_top = Label(root,bg='#FFE4B5')
        Frame_top.columnconfigure((0,1,2),weight=1)
        Frame_top.rowconfigure((0,1),weight=1)
        Frame_top.grid(row=0,column=0,columnspan=2,sticky=NSEW)

        Frame_left = Label(root,bg=bg_color)
        Frame_left.rowconfigure(0,weight=1)
        Frame_left.rowconfigure((1,2,3,4,5,6),weight=1)
        Frame_left.columnconfigure((0,1),weight=1)
        Frame_left.grid(row=1,column=0,sticky=NSEW)
        
        Frame_right = Label(root,bg=bg_color)
        Frame_right.rowconfigure((0,2),weight=1)
        Frame_right.rowconfigure(1,weight=9)
        Frame_right.columnconfigure((0,1),weight=1)
        Frame_right.grid(row=1,column=1,sticky=NSEW)

        return Frame_top,Frame_left,Frame_right


    def layer_top(Frame_top):
        Label(Frame_top,text="แอดมิน",bg="#FFE4B5",font=('Opun 20 ')).grid(row=0,column=0,sticky=W,rowspan=2,padx=20)
        Button(Frame_top,image=refresh,text="รีเฟรส",width=100,height=40,compound=RIGHT,relief="raised",bg=button_color,command=refresh_click).grid(row=0,rowspan=2,column=1,columnspan=2) 
        Button(Frame_top,image=log_out,text="ออกจากระบบ ",width=150,height=40,compound=RIGHT,relief="raised",bg="white",command=root.destroy).grid(row=0,rowspan=2,column=2,columnspan=2,sticky=E,padx=50) 


    def layer_left(Frame_left):
        Label(Frame_left,text="พนักงาน",font=('Opun 17'),bg=bg_color).grid(row=0,column=0,sticky=W,padx=40,pady=20)
        f1 = Frame(Frame_left, width=100, height=500,bg='#FFE4B5')
        f1.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
        f1.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW,rowspan=5)
        return f1

    def infor(f1):
        global l1,l2,l3,l4,l5
        l1=Label(f1,image=cir_g,text="พนักงานทั้งหมด", cursor= "hand2",bg='#FFE4B5',compound=LEFT)
        l1.grid(row=1,column=0,sticky=W)
        l2=Label(f1,image=cir_r,text=" รอการยืนยัน", cursor= "hand2",bg='#FFE4B5',compound=LEFT)
        l2.grid(row=2,column=0,sticky=W)
        Label(f1,text="-"*30,bg='#FFE4B5').grid(row=3,column=0)
        Label(f1,text=" แผนก",bg='#FFE4B5').grid(row=4,column=0,sticky=W)
        l3=Label(f1,image=cir_g,text="ฝ่ายดูแลระบบ", cursor= "hand2",bg='#FFE4B5',compound=LEFT)
        l3.grid(row=5,column=0,sticky=W)
        l4=Label(f1,image=cir_g,text="ฝ่ายจัดการคลังสินค้า", cursor= "hand2",bg='#FFE4B5',compound=LEFT)
        l4.grid(row=6,column=0,sticky=W)
        l5=Label(f1,image=cir_g,text="ฝ่ายขาย", cursor= "hand2",bg='#FFE4B5',compound=LEFT)
        l5.grid(row=7,column=0,sticky=W)

    def refresh_click():
        if fun == 1:
            id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
            mytree.delete(*mytree.get_children())
            for i in range(len(id_list)):
                if status_list[i] != '0':
                    username = username_list[i]
                    name = fname_list[i] + ' ' + lname_list[i]
                    department = department_list[i]
                    status = email_list[i]
                    mytree.insert('', 'end',values=(username,name,department,status))
            mytree.bind('<Double-1>',treeviewclick)
        elif fun == 2:
            id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
            mytree.delete(*mytree.get_children())
            for i in range(len(id_list)):
                if status_list[i] == '0':
                    username = username_list[i]
                    name = fname_list[i] + ' ' + lname_list[i]
                    department = department_list[i]
                    status = email_list[i]
                    mytree.insert('', 'end',values=(username,name,department,status))
            mytree.bind('<Double-1>',treeviewclick)
        elif fun == 3:
            id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
            mytree.delete(*mytree.get_children())
            for i in range(len(id_list)):
                if status_list[i] == '2':
                    username = username_list[i]
                    name = fname_list[i] + ' ' + lname_list[i]
                    department = department_list[i]
                    status = email_list[i]
                    mytree.insert('', 'end',values=(username,name,department,status))
            mytree.bind('<Double-1>',treeviewclick)
        elif fun == 4:
            id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
            mytree.delete(*mytree.get_children())
            for i in range(len(id_list)):
                if department_list[i] == 'ฝ่ายจัดการคลังสินค้า':
                    username = username_list[i]
                    name = fname_list[i] + ' ' + lname_list[i]
                    department = department_list[i]
                    status = email_list[i]
                    mytree.insert('', 'end',values=(username,name,department,status))
            mytree.bind('<Double-1>',treeviewclick)
        elif fun == 5:
            id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
            mytree.delete(*mytree.get_children())
            for i in range(len(id_list)):
                if department_list[i] == 'ฝ่ายขาย':
                    username = username_list[i]
                    name = fname_list[i] + ' ' + lname_list[i]
                    department = department_list[i]
                    status = email_list[i]
                    mytree.insert('', 'end',values=(username,name,department,status))
            mytree.bind('<Double-1>',treeviewclick)
        else:
            id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
            mytree.delete(*mytree.get_children())
            for i in range(len(id_list)):
                if username_list[i] == searchVar.get():
                    username = username_list[i]
                    name = fname_list[i] + ' ' + lname_list[i]
                    department = department_list[i]
                    status = email_list[i]
                    mytree.insert('', 'end',values=(username,name,department,status))
            mytree.bind('<Double-1>',treeviewclick)

    def search_click():
        id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
        mytree.delete(*mytree.get_children())
        a = searchVar.get()

        for i,data in enumerate(username_list):
            if data == a:
                username = username_list[i]
                name = fname_list[i] + ' ' + lname_list[i]
                department = department_list[i]
                status = email_list[i]
                mytree.insert('', 'end',values=(username,name,department,status))
                return
        mytree.bind('<Double-1>',treeviewclick)

    def layer_right(Frame_right):
        global f2
        Label(Frame_right,text="ไอดีผู้ใช้งาน",bg=bg_color).grid(row=0,column=0,sticky=W,padx=40,pady=20)
        pass_item = Entry(Frame_right,width=30,textvariable=searchVar)
        pass_item.grid(row=0,column=0,columnspan=2,ipady=3)
        Button(Frame_right,text="ค้นหา",bg='#FFE4B5',relief = "raised",width=6,command=search_click).grid(row=0,column=1,sticky=E,padx=40)
        f2 = Frame(Frame_right,bg="#FFE4B5")
        f2.columnconfigure((0,1,2,3),weight=1)
        f2.rowconfigure((0,1,2,3),weight=1)
        f2.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
        return f2

    def infor2(f2):
        Label(f2,text="ไอดีผู้ใช้งาน",bg='#FFE4B5').grid(row=0,column=0,sticky=N,pady=20)
        Label(f2,text="ชื่อ-นามสกุล",bg='#FFE4B5').grid(row=0,column=1,sticky=N,pady=20)
        Label(f2,text="แผนก",bg='#FFE4B5').grid(row=0,column=2,sticky=N,pady=20)
        Label(f2,text="สถานะ",bg='#FFE4B5').grid(row=0,column=3,sticky=N,pady=20)
        Label(f2,text="-"*80,bg='#FFE4B5').grid(row=0,columnspan=4,column=0)

    def confirm_user(key):
        s = ''
        if statusVar.get() == 'ยืนยัน':
            if lbldepartmentVar.get() != 'ฝ่ายดูแลระบบ':
                s = '1'
                edit_user_data(key,'status',s)
            else:
                s = '2'
                edit_user_data(key,'status',s)
        else:
            pass
        if fun == 1:
            my_fun1()
        elif fun == 2:
            my_fun2()
        elif fun == 3:
            my_fun3()
        elif fun == 4:
            my_fun4()
        else:
            my_fun5()

    def delete_user(key,f2):
        ans = messagebox.askyesno(title='Confirmation',message='ต้องการลบบัญชีใช่หรือไม่')
        if ans:
            delete_table_data('test',key)
        refresh_click()

    def infor3(key):
        f2 = Frame(Frame_right,bg="#FFE4B5")
        f2.columnconfigure((0,1,2,3),weight=1)   
        f2.rowconfigure((0,1,2,3),weight=1)
        f2.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
        Label(f2,text="ข้อมูลพนักงาน",bg='#FFE4B5',font=('Opun 17')).grid(row=0,column=1,columnspan=2)
        Label(f2,text="ไอดีผู้ใช้งาน",bg='#FFE4B5').grid(row=1,column=1,sticky=NW,columnspan=2)
        Label(f2,text="ชื่อ",bg='#FFE4B5').grid(row=2,column=1,sticky=NW,columnspan=2)
        Label(f2,text="นามสกุล",bg='#FFE4B5').grid(row=3,column=1,sticky=NW,columnspan=2)
        Label(f2,text="อีเมล",bg='#FFE4B5').grid(row=4,column=1,sticky=NW,columnspan=2)
        Label(f2,text="แผนก",bg='#FFE4B5').grid(row=5,column=1,sticky=NW,columnspan=2)
        Label(f2,text="สถานะ",bg='#FFE4B5').grid(row=6,column=1,sticky=NW,columnspan=2)

        lblPass=Label(f2,text=lblPassVar.get(),bg='#FFE4B5').grid(row=1,column=2,sticky=NE)
        lblName=Label(f2,text=lblNameVar.get(),bg='#FFE4B5').grid(row=2,column=2,sticky=NE)
        lblLastName=Label(f2,text=lblLastNameVar.get(),bg='#FFE4B5').grid(row=3,column=2,sticky=NE)
        lblEmail=Label(f2,text=lblEmailVar.get(),bg='#FFE4B5').grid(row=4,column=2,sticky=NE)
        lbldepartment=Label(f2,text=lbldepartmentVar.get(),bg='#FFE4B5').grid(row=5,column=2,sticky=NE)
        
        sp = ttk.Combobox(f2,width=5,textvariable=statusVar,background="white")
        sp['values'] = ('ไม่ยืนยัน','ยืนยัน')
        sp.grid(row=6,column=2,sticky=NE)

        Button(f2,text="ลบบัญชี",width=8,bg=button_color,command=lambda:delete_user(key,f2)).grid(row=8,column=0)
        Button(f2,text="ยกเลิก",width=8,bg=button_color,command=f2.destroy).grid(row=8,column=2)
        Button(f2,text="บันทึก",width=8,bg=button_color,command=lambda:confirm_user(key)).grid(row=8,column=3)

    def infor4(key):
        f2 = Frame(Frame_right,bg="#FFE4B5")
        f2.columnconfigure((0,1,2,3),weight=1)
        f2.rowconfigure((0,1,2,3),weight=1)
        f2.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
        Label(f2,text="ข้อมูลพนักงาน",bg='#FFE4B5',font=('Opun 17')).grid(row=0,column=1,columnspan=2)
        Label(f2,text="ไอดีผู้ใช้งาน",bg='#FFE4B5').grid(row=1,column=1,sticky=NW,columnspan=2)
        Label(f2,text="ชื่อ",bg='#FFE4B5').grid(row=2,column=1,sticky=NW,columnspan=2)
        Label(f2,text="นามสกุล",bg='#FFE4B5').grid(row=3,column=1,sticky=NW,columnspan=2)
        Label(f2,text="อีเมล",bg='#FFE4B5').grid(row=4,column=1,sticky=NW,columnspan=2)
        Label(f2,text="แผนก",bg='#FFE4B5').grid(row=5,column=1,sticky=NW,columnspan=2)

        lblPass=Label(f2,text=lblPassVar.get(),bg='#FFE4B5').grid(row=1,column=2,sticky=NE)
        lblName=Label(f2,text=lblNameVar.get(),bg='#FFE4B5').grid(row=2,column=2,sticky=NE)
        lblLastName=Label(f2,text=lblLastNameVar.get(),bg='#FFE4B5').grid(row=3,column=2,sticky=NE)
        lblEmail=Label(f2,text=lblEmailVar.get(),bg='#FFE4B5').grid(row=4,column=2,sticky=NE)
        lbldepartment=Label(f2,text=lbldepartmentVar.get(),bg='#FFE4B5').grid(row=5,column=2,sticky=NE)

        Button(f2,text="ยกเลิก",width=8,bg=button_color,command=f2.destroy).grid(row=8,column=0)
        Button(f2,text="ลบบัญชี",width=8,bg=button_color,command=lambda:delete_user(key,f2)).grid(row=8,column=3)

    def treeviewclick(event) :
        values = mytree.item(mytree.focus(),'values')
        print(values)
        a = values[0]
        id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
        for i, data in enumerate(username_list):
            if data == a:
                key = id_list[i]
                lblPassVar.set(username_list[i]) 
                lblNameVar.set(fname_list[i])
                lblLastNameVar.set(lname_list[i])
                lblEmailVar.set(email_list[i])
                lbldepartmentVar.set(department_list[i])
                break
        if fun == 2:
            infor3(key)
        else:
            infor4(key)
        

    def my_fun1(*args):
        global mytree,fun
        fun = 1
        layer_top(Frame_top)
        layer_right(Frame_right)
        my1=Frame(Frame_right,bg="#FFE4B5")
        my1.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
        my1.columnconfigure((0,1,2,3),weight=1)
        my1.rowconfigure((0,1,2,3),weight=1)

        cartbar = Scrollbar(my1)
        cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        mytree = ttk.Treeview(my1,columns=("MenuId","MenuName","MenuDepartment","MenuStatus"),yscrollcommand=cartbar.set)
        mytree.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        cartbar.config(command=mytree.yview)
        mytree.heading("#0",text="",anchor=CENTER)
        mytree.heading("MenuId",text="ไอดีผู้ใช้งาน",anchor=CENTER)
        mytree.heading("MenuName",text="ชื่อ-นามสกุล",anchor=CENTER)
        mytree.heading("MenuDepartment",text="แผนก",anchor=CENTER)
        mytree.heading("MenuStatus",text="อีเมล",anchor=CENTER)

        mytree.column("#0",width=0,minwidth=0) 
        mytree.column("MenuId",anchor=CENTER,width=150)
        mytree.column("MenuName",anchor=CENTER,width=150)
        mytree.column("MenuDepartment",anchor=CENTER,width=150)
        mytree.column("MenuStatus",anchor=CENTER,width=125)
        id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
        mytree.delete(*mytree.get_children())
        for i in range(len(id_list)):
            if status_list[i] != '0':
                username = username_list[i]
                name = fname_list[i] + ' ' + lname_list[i]
                department = department_list[i]
                status = email_list[i]
                mytree.insert('', 'end',values=(username,name,department,status))
        mytree.bind('<Double-1>',treeviewclick)

    def my_fun2(*args):
        global mytree,fun
        fun = 2
        layer_top(Frame_top)
        layer_right(Frame_right)
        my2=Frame(Frame_right,bg="#FFE4B5")
        my2.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
        my2.columnconfigure((0,1,2,3),weight=1)
        my2.rowconfigure((0,1,2,3),weight=1)


        cartbar = Scrollbar(my2)
        cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        mytree = ttk.Treeview(my2,columns=("MenuId","MenuName","MenuDepartment","MenuStatus"),yscrollcommand=cartbar.set)
        mytree.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        cartbar.config(command=mytree.yview)
        mytree.heading("#0",text="",anchor=CENTER)
        mytree.heading("MenuId",text="ไอดีผู้ใช้งาน",anchor=CENTER)
        mytree.heading("MenuName",text="ชื่อ-นามสกุล",anchor=CENTER)
        mytree.heading("MenuDepartment",text="แผนก",anchor=CENTER)
        mytree.heading("MenuStatus",text="อีเมล",anchor=CENTER)

        mytree.column("#0",width=0,minwidth=0) 
        mytree.column("MenuId",anchor=CENTER,width=150)
        mytree.column("MenuName",anchor=CENTER,width=150)
        mytree.column("MenuDepartment",anchor=CENTER,width=150)
        mytree.column("MenuStatus",anchor=CENTER,width=125)
        id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
        mytree.delete(*mytree.get_children())
        for i in range(len(id_list)):
            if status_list[i] == '0':
                username = username_list[i]
                name = fname_list[i] + ' ' + lname_list[i]
                department = department_list[i]
                status = email_list[i]
                mytree.insert('', 'end',values=(username,name,department,status))
        mytree.bind('<Double-1>',treeviewclick)

    def my_fun3(*args):
        global mytree, fun
        fun =3
        layer_top(Frame_top)
        layer_right(Frame_right)
        my3=Frame(Frame_right,bg="#FFE4B5")
        my3.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
        my3.columnconfigure((0,1,2),weight=1)
        my3.rowconfigure((0,1,2,3),weight=1)

        cartbar = Scrollbar(my3)
        cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        mytree = ttk.Treeview(my3,columns=("MenuId","MenuName","MenuDepartment","MenuStatus"),yscrollcommand=cartbar.set)
        mytree.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        cartbar.config(command=mytree.yview)
        mytree.heading("#0",text="",anchor=CENTER)
        mytree.heading("MenuId",text="ไอดีผู้ใช้งาน",anchor=CENTER)
        mytree.heading("MenuName",text="ชื่อ-นามสกุล",anchor=CENTER)
        mytree.heading("MenuDepartment",text="แผนก",anchor=CENTER)
        mytree.heading("MenuStatus",text="อีเมล",anchor=CENTER)

        mytree.column("#0",width=0,minwidth=0) 
        mytree.column("MenuId",anchor=CENTER,width=150)
        mytree.column("MenuName",anchor=CENTER,width=150)
        mytree.column("MenuDepartment",anchor=CENTER,width=150)
        mytree.column("MenuStatus",anchor=CENTER,width=125)
        id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
        mytree.delete(*mytree.get_children())
        for i in range(len(id_list)):
            if status_list[i] == '2':
                username = username_list[i]
                name = fname_list[i] + ' ' + lname_list[i]
                department = department_list[i]
                status = email_list[i]
                mytree.insert('', 'end',values=(username,name,department,status))
        mytree.bind('<Double-1>',treeviewclick)

    def my_fun4(*args):
        global mytree, fun,id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list
        fun = 4
        layer_top(Frame_top)
        layer_right(Frame_right)
        my4=Frame(Frame_right,bg="#FFE4B5")
        my4.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
        my4.columnconfigure((0,1,2),weight=1)
        my4.rowconfigure((0,1,2,3),weight=1)

        cartbar = Scrollbar(my4)
        cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        mytree = ttk.Treeview(my4,columns=("MenuId","MenuName","MenuDepartment","MenuStatus"),yscrollcommand=cartbar.set)
        mytree.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        cartbar.config(command=mytree.yview)
        mytree.heading("#0",text="",anchor=CENTER)
        mytree.heading("MenuId",text="ไอดีผู้ใช้งาน",anchor=CENTER)
        mytree.heading("MenuName",text="ชื่อ-นามสกุล",anchor=CENTER)
        mytree.heading("MenuDepartment",text="แผนก",anchor=CENTER)
        mytree.heading("MenuStatus",text="อีเมล",anchor=CENTER)

        mytree.column("#0",width=0,minwidth=0) 
        mytree.column("MenuId",anchor=CENTER,width=150)
        mytree.column("MenuName",anchor=CENTER,width=150)
        mytree.column("MenuDepartment",anchor=CENTER,width=150)
        mytree.column("MenuStatus",anchor=CENTER,width=125)
        id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
        mytree.delete(*mytree.get_children())
        for i in range(len(id_list)):
            if department_list[i] == 'ฝ่ายจัดการคลังสินค้า':
                username = username_list[i]
                name = fname_list[i] + ' ' + lname_list[i]
                department = department_list[i]
                status = email_list[i]
                mytree.insert('', 'end',values=(username,name,department,status))
        mytree.bind('<Double-1>',treeviewclick)


    def my_fun5(*args):
        global mytree, fun
        fun = 5
        layer_top(Frame_top)
        layer_right(Frame_right)
        my5=Frame(Frame_right,bg="#FFE4B5")
        my5.grid(row=1,column=0,columnspan=2,padx=20,sticky=NSEW)
        my5.columnconfigure((0,1,2),weight=1)
        my5.rowconfigure((0,1,2,3),weight=1)

        cartbar = Scrollbar(my5)
        cartbar.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        mytree = ttk.Treeview(my5,columns=("MenuId","MenuName","MenuDepartment","MenuStatus"),yscrollcommand=cartbar.set)
        mytree.grid(row=0,rowspan=4,column=0,columnspan=4,sticky=NSEW)
        cartbar.config(command=mytree.yview)
        mytree.heading("#0",text="",anchor=CENTER)
        mytree.heading("MenuId",text="ไอดีผู้ใช้งาน",anchor=CENTER)
        mytree.heading("MenuName",text="ชื่อ-นามสกุล",anchor=CENTER)
        mytree.heading("MenuDepartment",text="แผนก",anchor=CENTER)
        mytree.heading("MenuStatus",text="อีเมล",anchor=CENTER)

        mytree.column("#0",width=0,minwidth=0) 
        mytree.column("MenuId",anchor=CENTER,width=150)
        mytree.column("MenuName",anchor=CENTER,width=150)
        mytree.column("MenuDepartment",anchor=CENTER,width=150)
        mytree.column("MenuStatus",anchor=CENTER,width=125)
        id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = get_user_table()
        mytree.delete(*mytree.get_children())
        for i in range(len(id_list)):
            if department_list[i] == 'ฝ่ายขาย':
                username = username_list[i]
                name = fname_list[i] + ' ' + lname_list[i]
                department = department_list[i]
                status = email_list[i]
                mytree.insert('', 'end',values=(username,name,department,status))
        mytree.bind('<Double-1>',treeviewclick)

    root = ui_config()
    # fun = 0
    cir_g=PhotoImage(file='images/circle_green.png',master=root).subsample(15,15)  
    cir_r=PhotoImage(file='images/circle_red.png',master=root).subsample(20,20)  
    log_out=PhotoImage(file='images/log-out.png',master=root).subsample(15,15)  
    refresh=PhotoImage(file='images/refreshs.png',master=root).subsample(20,20)  
    Frame_top,Frame_left,Frame_right=frameLayout(root)
    
    layer_top(Frame_top)
    searchVar = StringVar()
    statusVar = StringVar()
    lblPassVar = StringVar()
    lblNameVar = StringVar()
    lblLastNameVar = StringVar()
    lblEmailVar = StringVar()
    lbldepartmentVar = StringVar()
    f1=layer_left(Frame_left)
    infor(f1)

    f2=layer_right(Frame_right)
    infor2(f2)
    my_fun1()

    l1.bind("<Button>",my_fun1)
    l2.bind("<Button>",my_fun2)
    l3.bind("<Button>",my_fun3)
    l4.bind("<Button>",my_fun4)
    l5.bind("<Button>",my_fun5)

    root.mainloop()