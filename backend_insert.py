from datetime import date
from re import A
import time
from firebase import firebase
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import time
cred = credentials.Certificate('test-fabf4-firebase-adminsdk-qao27-af5ca4b615.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-fabf4-default-rtdb.firebaseio.com/'
})
firebase = firebase.FirebaseApplication("https://test-fabf4-default-rtdb.firebaseio.com/", None)
def insert_order_table(company_name,contact_number,related_name,order_id,order_product_id,order_product_name,order_price,order_amount,order_status,order_date):
    order_table = {
        'company_name' : company_name,
        'contact_number' : contact_number,
        'related_name' : related_name,
        'order_id' : order_id,
        'order_product_id' :order_product_id,
        'order_product_name' : order_product_name,
        'order_price' : order_price,
        'order_amount' : order_amount,
        'order_status' : order_status,
        'order_date' : order_date
    }
    result = firebase.post('/order', order_table)
    if result:
        print('success')
    else:
        print("Error")

# insert_order_table('a company','082-xxx-xxxx','Mr. A','123451','a001','test_order','99','10','ยังไม่ได้รับของ',time.ctime())
# insert_order_table('b company','082-xxx-xxxx','Mr. B','123452','a002','test_order','99','10','ยังไม่ได้รับของ',time.ctime())
# insert_order_table('c company','082-xxx-xxxx','Mr. C','123453','a003','test_order','99','10','ยังไม่ได้รับของ',time.ctime())
# insert_order_table('d company','082-xxx-xxxx','Mr. D','123454','a004','test_order','99','10','ยังไม่ได้รับของ',time.ctime())
# insert_order_table('e company','082-xxx-xxxx','Mr. E','123455','a005','test_order','99','10','ยังไม่ได้รับของ',time.ctime())
# insert_order_table('f company','082-xxx-xxxx','Mr. F','123456','a006','test_order','99','10','ยังไม่ได้รับของ',time.ctime())
# insert_order_table('g company','082-xxx-xxxx','Mr. G','123457','a007','test_order','99','10','ยังไม่ได้รับของ',time.ctime())
def insert_stock_table(company_name,contact_number,related_name,id,product_name,price,promo_price,amount,time,status,buy_price,unit):
    stock_table = {
        'company_name' : company_name,
        'contact_number' : contact_number,
        'related_name' : related_name,
        'id' : id,
        'product_name' : product_name,
        'price' : price,
        'promo_price' : promo_price,
        'amount' : amount,
        'date' : time,
        'status' : status,
        'buy_price' : buy_price,
        'unit' : unit
    }
    result = firebase.post('/stock', stock_table)
    if result:
        print('success')
    else:
        print("Error")
# insert_stock_table('comname','023421','asda','a001','test1','20','ไม่มี','2',str(time.ctime()),'ปกติ','1','ชิ้น')
# insert_stock_table('comname','023421','asda','a002','test2','20','ไม่มี','2',str(time.ctime()),'ปกติ','1','ชิ้น')
# insert_stock_table('comname','023421','asda','a003','test3','20','10บาท','2',str(time.ctime()),'โปรโมชั่น','1','ชิ้น')
# insert_stock_table('comname','023421','asda','a004','test4','20','10บาท','2',str(time.ctime()),'โปรโมชั่น','1','ชิ้น')
# insert_stock_table('comname','023421','asda','a005','test5','20','10บาท','2',str(time.ctime()),'ชำรุด','1','ชิ้น')
# insert_stock_table('comname','023421','asda','a006','test6','20','10บาท','2',str(time.ctime()),'ชำรุด','1','ชิ้น')
# insert_stock_table('comname','023421','asda','a007','test7','20','10บาท','2',str(time.ctime()),'ชำรุด','1','ชิ้น')
# insert_stock_table('comname','023421','asda','a008','test8','20','10บาท','2',str(time.ctime()),'ชำรุด','1','ชิ้น')
def insert_user(username,pwd,fname,lname,email,status,department,nametitle):
    user_table = {
        'username' : username,
        'password' : pwd,
        'fname' : fname,
        'lname' : lname,
        'email' : email,
        'status' : status,
        'department' : department,
        'name_title' : nametitle
    }
    result = firebase.post('/test', user_table)
    if result:
        print('success')
    else:
        print("Error")


def insert_oldstock(company_name,contact_number,related_name,id,product_name,price,promo_price,amount,time,status,buy_price,unit):
    stock_table = {
        'company_name' : company_name,
        'contact_number' : contact_number,
        'related_name' : related_name,
        'id' : id,
        'product_name' : product_name,
        'price' : price,
        'promo_price' : promo_price,
        'amount' : amount,
        'date' : time,
        'status' : status,
        'buy_price' : buy_price,
        'unit' : unit
    }
    result = firebase.post('/oldstock', stock_table)
    if result:
        print('success')
    else:
        print("Error")


def insert_promotion(company_name,contact_number,related_name,id,product_name,price,promo_price,amount,time,status,buy_price,unit):
    stock_table = {
        'company_name' : company_name,
        'contact_number' : contact_number,
        'related_name' : related_name,
        'id' : id,
        'product_name' : product_name,
        'price' : price,
        'promo_price' : promo_price,
        'amount' : amount,
        'date' : time,
        'status' : status,
        'buy_price' : buy_price,
        'unit' : unit
    }
    result = firebase.post('/promotion', stock_table)
    if result:
        print('success')
    else:
        print("Error")
# for i in range(20):
# insert_user('test_refresh','1234','testname','testname','testmail','0','asd','นาย')

def get_oldstock_table():
    result = firebase.get('/oldstock','')
    key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = [],[],[],[],[],[],[],[],[],[],[],[],[]
    for i in result:
        key_list.append(i)
        company_name_list.append(result[i]['company_name'])
        contact_number_list.append(result[i]['contact_number'])
        related_name_list.append(result[i]['related_name'])
        id_list.append(result[i]['id'])
        product_name_list.append(result[i]['product_name'])
        price_list.append(result[i]['price'])
        promo_price_list.append(result[i]['promo_price'])
        amount_list.append(result[i]['amount'])
        date_list.append(result[i]['date'])
        status_list.append(result[i]['status'])
        buy_price_list.append(result[i]['buy_price'])
        unit_list.append(result[i]['unit'])
    return key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list

def get_stock_table():
    result = firebase.get('/stock','')
    key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list = [],[],[],[],[],[],[],[],[],[],[],[],[]
    for i in result:
        key_list.append(i)
        company_name_list.append(result[i]['company_name'])
        contact_number_list.append(result[i]['contact_number'])
        related_name_list.append(result[i]['related_name'])
        id_list.append(result[i]['id'])
        product_name_list.append(result[i]['product_name'])
        price_list.append(result[i]['price'])
        promo_price_list.append(result[i]['promo_price'])
        amount_list.append(result[i]['amount'])
        date_list.append(result[i]['date'])
        status_list.append(result[i]['status'])
        buy_price_list.append(result[i]['buy_price'])
        unit_list.append(result[i]['unit'])
    return key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,buy_price_list,unit_list
# key_list,company_name_list,contact_number_list,related_name_list,id_list,product_name_list,price_list,promo_price_list,amount_list,date_list,status_list,unit_list = get_stock_table()
# a = 0
# for i in range(len(id_list)):
#     if status_list[i] == "โปรโมชั่น":
#         a += 1
# print(a)

def get_stock_table_v2():
    result = firebase.get('/stock','') 
    cartlist = []
    for i in result:
        listdic = []
        listdic.append([i,result[i]['company_name'],result[i]['contact_number'],result[i]['related_name'],result[i]['id'],result[i]['product_name'],result[i]['price'],result[i]['promo_price'],result[i]['amount'],result[i]['date'],result[i]['status']])
        cartlist.append(listdic)

    return cartlist

def get_oldstock_table_v2():
    result = firebase.get('/oldstock','') 
    cartlist = []
    if result:
        for i in result:
            listdic = []
            listdic.append([i,result[i]['company_name'],result[i]['contact_number'],result[i]['related_name'],result[i]['id'],result[i]['product_name'],result[i]['price'],result[i]['promo_price'],result[i]['amount'],result[i]['date'],result[i]['status']])
            cartlist.append(listdic)

    return cartlist

def get_user_table():
    result = firebase.get('/test','')
    id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list = [],[],[],[],[],[],[],[],[]
    for i in result:
        id_list.append(i)
        username_list.append(result[i]['username'])
        pwd_list.append(result[i]['password'])
        fname_list.append(result[i]['fname'])
        lname_list.append(result[i]['lname'])
        email_list.append(result[i]['email'])
        status_list.append(result[i]['status'])
        department_list.append(result[i]['department'])
        nametitle_list.append(result[i]['name_title'])
    return id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,department_list,nametitle_list
# id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,access_list,department_list,nametitle_list = get_user_table()

def get_order_table():
    result = firebase.get('/order','')  
    id_list,order_id_list,company_name_list,contact_number_list,related_name_list,order_product_id_list,order_product_name_list,order_price_list,order_amount_list,order_status_list,order_date_list = [],[],[],[],[],[],[],[],[],[],[]
    for i in result:
        id_list.append(id_list.append(i))
        company_name_list.append(result[i]['company_name'])
        order_id_list.append(result[i]['order_id'])
        contact_number_list.append(result[i]['contact_number'])
        related_name_list.append(result[i]['related_name'])
        order_product_id_list.append(result[i]['order_product_id'])
        order_product_name_list.append(result[i]['order_product_name'])
        order_price_list.append(result[i]['order_price'])
        order_amount_list.append(result[i]['order_amount'])
        order_status_list.append(result[i]['order_status'])
        order_date_list.append(result[i]['order_date'])
    return id_list,order_id_list,company_name_list,contact_number_list,related_name_list,order_product_id_list,order_product_name_list,order_price_list,order_amount_list,order_status_list,order_date_list
# id_list,order_id_list,company_name_list,contact_number_list,related_name_list,order_product_id_list,order_product_name_list,order_price_list,order_amount_list,order_status_list,order_date_list = get_order_table()
# print(len(order_id_list))

def get_order_table_v2():
    result = firebase.get('/order','') 
    cartlist = []
    for i in result:
        listdic = []
        listdic.append([i,result[i]['company_name'],result[i]['contact_number'],result[i]['related_name'],result[i]['order_id'],result[i]['order_product_name'],result[i]['order_price'],result[i]['order_amount'],result[i]['order_status'],result[i]['order_date']])
        cartlist.append(listdic)

    return cartlist

def update_table(table,id,data_name,data):
    # table เช่น ที่อยู่ path ก่อนเช้าถึงตัว id
    # id คือ id ใน key_list 
    # data_name เช่น 'username' : 'admin',  data_name คือ 'username'
    # data คือ ข้อมูลที่ต้องการนำไปแทนที่
    path = '/'+table+'/'+id
    result = firebase.put(path,data_name,data)
    if result:
        print('success')

def delete_table_data(table,id):
    path = '/'+table+'/'
    result = firebase.delete(path,id)
    if result:
        print('success')

def edit_user_data(id,data_name,data): ## for admin
    path = '/test/'+id
    result = firebase.put(path,data_name,data)
    if result:
        print('success')

def confirm_user(key): ###for admin confirm account
    path = '/test/'+id
    result = firebase.put(path,'status',2)
    if result:
        print('success')


# delete_table('test',id_list[0])
# id_list,username_list,pwd_list,fname_list,lname_list,email_list,status_list,access_list = get_user_table()
# print(id_list)