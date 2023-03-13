from tkinter import *
from tkinter.font import Font
from backend_insert import *
from config import *

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
        register,user,password,b1,fg = lo_container()
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
                    
                    
                    main_function(name,root)
            


                else:
                   print("Username or password incorrect")
                
            
        return bind_function()
      
    def regis():
        login,e1,e2,e3,e4,e5,e6,b1,r1,r2 = re_container()
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
            elif e2.get() != e3.get():
                print('Password not match')
            else:
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
                    y == "ฝ่ายดูแลระบบ"
                elif t2 == 2 :
                    y == "ฝ่ายขาย"
                elif t2 == 3 :
                    y = "ฝ่ายจัดการคลังสินค้า"

                id_list, username_list, pwd_list,fname_list,lname_list,email_list,status_list,access_list,department_list,nametitle_list = get_user_table()
                username=e1.get()
                if username not in username_list:
                    insert_user(username,e2.get(),e4.get(),e5.get(),e6.get(),'0','???',y,x)
                    return
                print("user name already excist")


        return bind_function()
    
    def forgot_pass():
        
        b2,e3,body = fp()
        def validcheck():
            if e3.get() == "":
                e3['highlightbackground'] = '#E44D4D'
            else:
                body.destroy()
                f2()
    
        b2.configure(command = validcheck)
  
    def f2():
        b3,e8,e9,body2 = fp2()
        def validcheck():
            if e8.get() == "" or e9.get() == "":
                e8['highlightbackground'] = '#E44D4D'
                e9['highlightbackground'] = '#E44D4D'
            else:
                #นำรหัสผ่านใหม่มาอัพขึน database ตรงนี้



                body2.destroy()
        b3.configure(command = validcheck)
    register = login()
    root.mainloop()

def main_function(name,root):
    from ff import menu_left
    root.destroy()
    name = name
    print(name)
    
    menu_left(name)

#main_function('a')

login_register()