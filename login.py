from tkinter import *
from tkinter import ttk
from config import *

def ui_config():
    root = Tk()
    root.title("Stock Login")
    root.resizable(False,False)
    window_width = 1024
    window_height = 768

    root.columnconfigure(0,weight = 1)
    root.rowconfigure(0,weight = 1)
    root.option_add('*Font',font)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2- window_width /2)
    center_y = int(screen_height / 2- window_height /2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    return root

def lo_container():
    body= Frame(root, bg = bg_color)
    body.grid(row = 0,column =0,sticky = 'news')

    body.columnconfigure ((0,2),weight = 2)
    body.columnconfigure (1,weight = 1)
   
    body.rowconfigure(0,weight = 2)
    body.rowconfigure(1,weight = 6)
    body.rowconfigure (2,weight =1)

    container = Frame(body,bg=frame_color,width = 512 ,height = 500 )
    container.grid(row = 1,column = 1,sticky = 'news')

    container.rowconfigure(0,weight=1)
    container.rowconfigure(1,weight=1)
    container.rowconfigure(2,weight=6)
    container.columnconfigure(0,weight=1)


    Label(container,image= user_logo,bg = frame_color,width =450).grid(column = 0,row = 0)

    Label(container,text = 'เข้าสู่ระบบ',bg = frame_color,font= 'Opun 20').grid(column = 0,row = 1,sticky = 'n')
    Label(container,text = 'ชื่อผู้ใช้งาน',bg = frame_color).place(x = 70 ,y = 250)
    user = Entry(container,bg = '#FFFADE',width = 38,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,font = 'Opun 12')
    user.place(x = 70,y =300,height = 40)
    Label(container,text = 'รหัสผ่าน',bg = frame_color).place(x = 70 ,y = 350)
    password = Entry(container,bg = '#FFFADE',width = 46,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,show_ = '●',font = 'Opun 10')
    password.place(x = 70,y =400,height = 40 )
    lr = Label(container,bg = frame_color,fg = '#E44D4D',font = 'Opun 12')
    lr.place(x = 210 ,y = 255)
    fg = Label(container,text = '*ลืมรหัสผ่าน?',bg = frame_color,font='Opun 10',cursor = 'hand2')
    fg.place(x = 70 ,y = 450)
    
    b1 = Button(container,text = 'เข้าสู่ระบบ',width =34,bg =button_color,bd = 0,cursor = 'hand2')
    b1.place(x = 70,y = 490,height = 40)
    Label(container,text = 'ยังไม่มีบัญชีผู้ใช้งานใช่หรือไม่ ?',bg =frame_color,fg = 'gray',font = 'Opun 11').place(x = 120,y = 540)
    register = Label(container,text ='ลงทะเบียน',bg = frame_color ,fg = '#E44D4D',font = 'Opun 11',cursor = 'hand2')
    register.place(x = 350,y = 540)

    return register,user,password,b1,fg,lr


root = ui_config()
user_logo = PhotoImage(file = 'images/login_icon.png')
#lo_container()
#root.mainloop()