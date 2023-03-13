from audioop import lin2adpcm
from login import root
from config import *
from tkinter import *

def re_container():
    body= Frame(root, bg = frame_color)
    body.grid(row = 0,column =0,sticky = 'news')

    body.rowconfigure(0,weight = 3)
    body.rowconfigure(1,weight = 5)
    
    body.columnconfigure(0,weight =1)
    container = Frame(body,bg=bg_color,width = 700 ,height = 500 )
    container.grid(row = 1,column = 0,sticky = 'news')
    
    Label(body,text = 'ลงทะเบียนผู้ใช้งาน',bg = frame_color,font= 'opun 18').place(x = 150,y = 20)
    
    Label(container,text = 'ชื่อผู้ใช้งาน*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 40)

    Label(container,text = 'รหัสผ่าน*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 90)
    Label(container,text = 'ยืนยันรหัสผ่าน*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 140)
    Label(container,text = 'คำนำหน้า*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 190)
    Label(container,text = 'ชื่อ*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 240)
    Label(container,text = 'นามสกุล*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 290)
    Label(container,text = 'อีเมล*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 340)
    Label(container,text = 'แผนกงาน*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 390)

    l1 = Label(container,bg = bg_color,fg = '#E44D4D',font= 'opun 13')
    l1.place(x = 810 ,y = 40)

    l2 = Label(container,bg = bg_color,fg = '#E44D4D',font= 'opun 13')
    l2.place(x = 810 ,y = 90)


    e1 = Entry(container,bg = '#EBEAEA',width = 38,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,font = 'Opun 12')
    e1.place(x = 370,y =40,height = 35)
    e2 = Entry(container,bg = '#EBEAEA',width = 38,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,font = 'Opun 12',show_=  '●')
    e2.place(x = 370,y =90,height = 35)
    e3 = Entry(container,bg = '#EBEAEA',width = 38,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,font = 'Opun 12',show_ = '●')
    e3.place(x = 370,y =140,height = 35)
    e4 = Entry(container,bg = '#EBEAEA',width = 38,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,font = 'Opun 12')
    e4.place(x = 370,y =240,height = 35)
    e5 = Entry(container,bg = '#EBEAEA',width = 38,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,font = 'Opun 12')
    e5.place(x = 370,y =290,height = 35)
    e6 = Entry(container,bg = '#EBEAEA',width = 38,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,font = 'Opun 12')
    e6.place(x = 370,y =340,height = 35)

    name = ["นาย","นาง","นางสาว"]
    section = ["ฝ่ายดูแลระบบ","ฝ่ายขาย","ฝ่ายจัดการคลังสินค้า"]
    n = 0
    s = 0
    
    for i,des in enumerate(name) :
        r1 = Radiobutton(container,text = des,bg = bg_color,font = 'Opun 13',command =onclick,variable = var,value = i+1)
        r1.place(x = 370 +n,y =180)
        n += 100

    for i,des in enumerate(section):
        r2 = Radiobutton(container,text = " " +des,bg = bg_color,font = 'Opun 13',command =onclick2,variable = var2,value = i+1)
        r2.place(x = 370 +s,y =390)
        s += 150

    b1 = Button(container,text = 'ลงทะเบียน',width =15,bg =button_color,bd = 0,cursor = 'hand2')
    b1.place(x = 460,y = 470,height = 40)
    Label(container,text = 'กลับไปหน้าเข้าสู่ระบบ',bg =bg_color,fg = 'gray',font = 'Opun 11').place(x = 430,y = 530)
    login = Label(container,text ='เข้าสู่ระบบ',bg = bg_color ,fg = '#E44D4D',font = 'Opun 11',cursor = 'hand2')
    login.place(x = 590,y = 530)
    
    return login,e1,e2,e3,e4,e5,e6,b1,r1,r2,l1,l2

def onclick():
    return var.get()
def onclick2():
    b = var.get()
    return var2.get()


def fp():
    global body
    body= Frame(root, bg = frame_color)
    body.grid(row = 0,column =0,sticky = 'news')

    body.rowconfigure(0,weight = 3)
    body.rowconfigure(1,weight = 5)
    
    body.columnconfigure(0,weight =1)
    container = Frame(body,bg=bg_color,width = 700 ,height = 500 )
    container.grid(row = 1,column = 0,sticky = 'news')

    Label(body,text = 'ลืมรหัสผ่าน',bg = frame_color,font= 'opun 18').place(x = 150,y = 20)

    
    Label(body,text = 'กรอกชื่อผู้ใช้งาน',bg = bg_color,font= 'opun 24').place(x = 420,y = 180)
    Label(container,text = 'ชื่อผู้ใช้งาน*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 220)
    l1 = Label(container,bg = bg_color,font =' Opun 13',fg = '#E44D4D')
    l1.place(x = 600 ,y = 180)
    e3 = Entry(container,bg = '#EBEAEA',width = 38,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,font = 'Opun 12')
    e3.place(x = 370,y =220,height = 35)

    b1 = Button(container,text = 'ยืนยัน',width =15,bg =button_color,bd = 0,cursor = 'hand2')
    b1.place(x = 570,y = 470,height = 40)
    
    b2 = Button(container,text = 'ยกเลิก',width =15,bg =button_color,bd = 0,cursor = 'hand2',command = button1)
    b2.place(x = 350,y = 470,height = 40)

    return b1,e3,body,l1

def fp2():
    global body2
    body2= Frame(root, bg = frame_color)
    body2.grid(row = 0,column =0,sticky = 'news')

    body2.rowconfigure(0,weight = 3)
    body2.rowconfigure(1,weight = 5)
    
    body2.columnconfigure(0,weight =1)
    container = Frame(body2,bg=bg_color,width = 700 ,height = 500 )
    container.grid(row = 1,column = 0,sticky = 'news')

    l2 = Label(container,bg = bg_color,font =' Opun 13',fg = '#E44D4D')
    l2.place(x = 600 ,y = 180)
    Label(body2,text = 'ลืมรหัสผ่าน',bg = frame_color,font= 'opun 18').place(x = 150,y = 20)
    Label(body2,text = 'กรอกรหัสผ่านใหม่',bg = bg_color,font= 'opun 24').place(x = 420,y = 180)
    Label(container,text = 'รหัสผ่าน*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 220)
    Label(container,text = 'ยืนยันรหัสผ่าน*',bg = bg_color,font =' Opun 13').place(x = 230 ,y = 290)
    
    e8 = Entry(container,bg = '#EBEAEA',width = 38,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,font = 'Opun 12',show_ =  '●')
    e8.place(x = 370,y =220,height = 35)
    e9 = Entry(container,bg = '#EBEAEA',width = 38,highlightthickness = 1,highlightbackground= '#757575',highlightcolor = 'black',bd= 0,font = 'Opun 12',show_ =  '●')
    e9.place(x = 370,y =290,height = 35)

    b3 = Button(container,text = 'ยืนยัน',width =15,bg =button_color,bd = 0,cursor = 'hand2')
    b3.place(x = 570,y = 470,height = 40)
    
    b4 = Button(container,text = 'ยกเลิก',width =15,bg =button_color,bd = 0,cursor = 'hand2',command = button1)
    b4.place(x = 350,y = 470,height = 40)

    return b3,e8,e9,body2,l2

def button1():
    body.destroy()

var = IntVar()
var2 = IntVar()
