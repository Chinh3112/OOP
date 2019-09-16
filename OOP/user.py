import json
import os
import math

class Database():
    table_name=None
    id=None
    name=None
    phone=None
    danhsach=[]
    def __init__(self,us):
        self.id=us.id
        self.table_name=us.table_name
        self.name=us.name
        self.phone=us.phone
    def load(self):
        with open(self.table_name+'/'+self.table_name+'.csv','r') as f:
            line=f.readline()
            while line:
                line=line[0:len(line)-1]
                with open(self.table_name+'/'+line+'.json','r') as files:
                    str_to_read=json.load(files)
                    self.danhsach.append(str_to_read)
                line=f.readline()
    def check_id(self):
        self.load()
        for ds in self.danhsach:
            if self.id==ds["id"]:
                return ds["id"]
    def save(self):
        number=int(self.id)
        number=str(format(number,'03d'))
        str_to_save=self.table_name+'_'+number
        if self.check_id() is None:
            with open(self.table_name+'/'+self.table_name+'.csv','a') as f:
                f.write(str_to_save+'\n')
        save={}
        save["id"]=self.id
        save["ten"]=self.name
        save["phone"]=self.phone
        with open(self.table_name+'/'+str_to_save+'.json','w') as files:
            json.dump(save,files)
    def delete(self):
        danh_sach=[]
        with open(self.table_name+'/'+self.table_name+'.csv','r') as f:
            line=f.readline()
            while line:
                line=line[0:len(line)-1]
                danh_sach.append(line.lstrip(self.table_name+'_'))
                line=f.readline()
        for ds_id in danh_sach:
            if int(ds_id)==int(self.id):
                link=self.table_name+'/'+self.table_name+'_'+ds_id+'.json'
                os.remove(link)
                danh_sach.remove(ds_id)
                with open(self.table_name+'/'+self.table_name+'.csv','r+') as f1:
                    f1.truncate()
                for ds in danh_sach:
                    with open(self.table_name+'/'+self.table_name+'.csv','a') as f2:
                        f2.write(self.table_name+'_'+ds+'\n')
                return
    def get(self):
        return 0
class User(Database):
    table_name="user"
    id=None
    name=None
    # password=None
    phone=None
    def __init__(self,id_user,name,phone):
        self.id=id_user
        self.name=name
        # self.password=password
        self.phone=phone
class Customer(Database):
    table_name="customer"
    id=None
    name=None
    phone=None
    def __init__(self,id,name,phone):
        self.id=id
        self.name=name
        self.phone=phone

while True:
    print("+=================================+")
    print("|Nhap T de tao tai khoan          |")
    print("|Nhap S de sua tai khoan user     |")
    print("|Nhap X de xoa tai khoan          |")
    print("|Nhap E de thoat                  |")
    print("+=================================+")
    x=input("Chon chuc nang:")
    print("Ban da cho chuc nang "+x)
    if x.upper()=="T":
        # chuc nang tao tk moi:
        y=input("Ban muon tao user(nhap 0) hay customer(nhap 1):")
        id=input("Nhap id user cua ban:")
        if y=="0":
            check=User(id,None,None).check_id()
        if y=="1":
            check=Customer(id,None,None).check_id()
        while check is not None:
            id=input("ID da ton tai.Xin moi nhap ID khac:")
            if y=="0":
                check=User(id,None,None).check_id()
            if y=="1":
                check=Customer(id,None,None).check_id()
        ten=input("Xin moi nhap ten cua user:")
        phone=input("Xin moi nhap so dien thoai cua ban:")
        if y=="0":
           User(id,ten,phone).save()
        if y=="1":
            Customer(id,ten,phone).save()
# def check():
    if x.upper()=="S":
        y=input("Ban muon tao user(nhap 0) hay customer(nhap 1):")
        id=input("Nhap id  cua ban:")
        if y=="0":
            check=User(id,None,None).check_id()
        if y=="1":
            check=Customer(id,None,None).check_id()
        while check is None:
            id=input("ID chua ton tai.Xin moi nhap ID khac:")
            if y=="0":
                check=User(id,None,None).check_id()
            if y=="1":
                check=Customer(id,None,None).check_id()
        ten=input("Xin moi nhap ten cua ban:")
        phone=input("Xin moi nhap so dien thoai cua ban:")
        if y=="0":
           User(id,ten,phone).save()
        if y=="1":
            Customer(id,ten,phone).save()
    if x.upper()=='X':
        y=input("Ban muon tao user(nhap 0) hay customer(nhap 1):")
        id=input("Nhap id ban muon xoa:")
        if y=="0":
            check=User(id,None,None).check_id()
        if y=="1":
            check=Customer(id,None,None).check_id()
        while check is not None:
            id=input("ID chua ton tai.Xin moi nhap ID khac:")
            if y=="0":
                check=User(id,None,None).check_id()
            if y=="1":
                check=Customer(id,None,None).check_id()
        if y=="0":
           User(id,None,None).save()
        if y=="1":
            Customer(id,None,None).save()