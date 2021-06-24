from tkinter import *
import os
from tkinter import messagebox
from tkinter.ttk import Combobox
#import mysql.connector as mycon
import random
import time;
import datetime

'''db=mycon.connect(host='localhost',user='root',passwd='1234',database='project')
cur=db.cursor()'''

root=Tk()

can=PhotoImage(file='image.png')
pas=Canvas(root,width=350,height=300)
pas.create_image(0,0,image=can,anchor=NW)
pas.place(x=0,y=0)

#-------------------------------------FUNTIONS-------------------------------------------------------
#-------------------------------------LOGIN----------------------------------------------------------
def login():
    def sub():
        cur.execute('select * from login')
        for x in cur:
            a=x[0]
            b=x[1]
        if (ent1.get()==a and ent2.get()==b):
            login.destroy()
            messagebox.showinfo("Success",'Login Completed')
            book()        
        else:
            messagebox.showerror("OOPS",'Invalid Username or Password')
    def data():
        os.system('data.txt')

    root.iconify()
    login=Toplevel()
    login.title('LOGIN')
    login.geometry('350x300+500+120')
    login.resizable(False,False)
    
    fr=Frame(login ,bd=7,background='black', relief='raise')
    wel=Label(fr,text='Login',font=('arial',25,'bold'),fg='blue')
    wel.grid(row=0,columnspan=2)
    fr.pack(side=TOP)
    
    fr2=Frame(login)
    note=Label(fr2,text='*Entering Wrong Data Will Lead Returning Home Page',font=('arial',10,'bold')).pack()
    fr2.pack(side=BOTTOM)
    
    fr1=Frame(login)
    user=Label(fr1,text='User Name',font=('arial',15,'bold'),fg='black')
    password=Label(fr1,text='Password',font=('arial',15,'bold'))
    
    ent1=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=15, bg='#ffffff', justify='right')
    ent2=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=15, bg='#ffffff', justify='right')
    
    user.grid(row=1,sticky=E)
    ent1.grid(row=1,column=1)
    password.grid(row=2,sticky=E)
    ent2.grid(row=2,column=1)
    
    b=Button(fr1,text='Submit', width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
    b.grid(row=3,column=1,sticky=W)
    
    da=Label(fr1,text='Forgot data?',font=('arial',15,'bold'),fg='black')
    bt=Button(fr1,text='Click Here',command=data, width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
    da.grid(row=4,column=1,sticky=E)
    bt.grid(row=4,column=2)
    fr1.place(x=10,y=90)
#--------------------------------------------BOOKING--------------------------------------------------------   
def book():
    def nextt():
        tno=random.randint(100,999)
        source=b1.get()
        des=b2.get()
        date=b3.get()
        month=b4.get()
        year=sp.get()
        code='MH'
        did=1
        
        sql="insert into booking(pickup,dropoff,date,month,year,code,did,ticket) values('{}','{}',{},{},{},'{}',{},{})".format(source,des,date,month,year,code,did,tno) 
        cur.execute(sql)
        db.commit()

        messagebox.showinfo("Success",'Your Ticket No. Is:228')

        nxtt()                
        bot.destroy()
        
    bot=Toplevel()
    bot.title('Booking')
    bot.geometry('350x300+500+120')
    bot.resizable(False,False)
    
    fr=Frame(bot,bd=7,background='black', relief='raise')
    wel=Label(fr,text='Select Journey',font=('arial',25,'bold'),fg='blue')
    wel.grid(row=0,columnspan=2)
    fr.pack(side=TOP)
    
    fr1=Frame(bot)
    fr1.place(x=35,y=70)
    
    sor=Label(fr1,text='Pick-Up ',font=('arial',15,'bold'))
    c=['Devlali','Nasik']
    b1=Combobox(fr1,values=c,width=19,font=('arial', 9, 'bold') )
    b1.set('--------Select---------')
    sor.grid(row=1,sticky=E)
    b1.grid(row=1,column=1)
    
    des=Label(fr1,text='Drop-Off ',font=('arial',15,'bold'))
    d=['Mumbai','Chennai','Delhi','Kolkata','Ahemdabad','Lucknow','Patna','Chandigarh']
    b2=Combobox(fr1,values=d,width=19,font=('arial', 9, 'bold') )
    b2.set('--------Select---------')
    des.grid(row=2,sticky=E)
    b2.grid(row=2,column=1)
    
    dat=Label(fr1,text='Date',font=('arial',15,'bold'))
    e=list(range(1,32))
    b3=Combobox(fr1,values=e,width=19,font=('arial', 9, 'bold'))
    b3.set('--------Select---------')
    dat.grid(row=3,sticky=E)
    b3.grid(row=3,column=1)
    
    mon=Label(fr1,text='Month',font=('arial',15,'bold'))
    k=[1,2,3,4,5,6,7,8,9,10,11,12]
    b4=Combobox(fr1,values=k,width=19,font=('arial', 9, 'bold'))
    b4.set('--------Select---------')
    mon.grid(row=4,sticky=E)
    b4.grid(row=4,column=1)
    
    pe=Label(fr1,text='Year',font=('arial',15,'bold'))
    sp=Spinbox(fr1,from_=2019,to=2020,width=20,font=('arial', 9, 'bold'))
    pe.grid(row=5,sticky=E)
    sp.grid(row=5,column=1)
   
    sub=Button(fr1,text='Next',command=nextt, width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
    sub.grid(row=6,column=1,sticky=W)  
        
    fr2=Frame(bot)
    note=Label(fr2,text='*Please Store the Ticket No. Provided For Further',font=('arial',10,'bold')).pack()
    fr2.pack(side=BOTTOM)

def nxtt():
    def con():
        tno=t1.get()
        bclass=b11.get()
        btype=b12.get()
        stype=b13.get()
        if stype=='Window':
            st='w'
        elif stype=='Non-Window':
            st='s'
        sno=random.randint(1,9)
        kc=str(sno)
        seat=st+kc
        
        sql="select pickup,dropoff from booking where ticket={}".format(tno) 
        cur.execute(sql)
        for x in cur:
            pick=x[0]
            drop=x[1]
        if pick=='Devlali':
            sql1="select Price from devlali where Destination='{}' and category='{}'".format(drop,bclass)
            cur.execute(sql1)
            for x in cur:
                price=x[0]
        elif pick=='Nasik':
            sql2="select Price from nasik where Destination='{}' and category='{}'".format(drop,bclass)
            cur.execute(sql2)
            for y in cur:
                price=y[0]                   
                                          
        sql="update booking set class='{}',type2='{}',stype='{}',price={},seat='{}' where ticket={}".format(bclass,btype,stype,price,seat,tno)
        cur.execute(sql)
        db.commit()
                
        tp.destroy()
        details()
                   
    tp=Toplevel()
    tp.title('Select Type')
    tp.geometry('350x300+500+120')
    tp.resizable(False,False)
    
    fr=Frame(tp,bd=7,background='black', relief='raise')
    wel=Label(fr,text='Select Type',font=('arial',25,'bold'),fg='blue')
    wel.grid(row=0,columnspan=2)
    fr.pack(side=TOP)
    
    fr1=Frame(tp)
    fr1.place(x=35,y=80)
    
    wek=Label(fr1,text='Ticket No.',font=('arial',15,'bold'))
    wek.grid(row=1,sticky=E)
    t1=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=16, bg='#ffffff', justify='right')
    t1.grid(row=1,column=1)
    
    Bt1=Label(fr1,text=' Bus Class',font=('arial',15,'bold'))
    ck=['AC','Non-AC']
    b11=Combobox(fr1,values=ck,width=19,font=('arial', 9, 'bold'))
    b11.set('--------Select---------')
    Bt1.grid(row=2,sticky=E)
    b11.grid(row=2,column=1)
    
    Bt2=Label(fr1,text=' Bus Type ',font=('arial',15,'bold'))
    ck2=['Seater','Semi-Sleeper','Sleeper']
    b12=Combobox(fr1,values=ck2,width=19,font=('arial', 9, 'bold'))
    b12.set('--------Select---------')
    Bt2.grid(row=3,sticky=E)
    b12.grid(row=3,column=1)
    
    Bt3=Label(fr1,text=' Seat Type',font=('arial',15,'bold'))
    ck3=['Window','Non-Window']
    b13=Combobox(fr1,values=ck3,width=19,font=('arial', 9, 'bold'))
    b13.set('--------Select---------')
    Bt3.grid(row=4,sticky=E)
    b13.grid(row=4,column=1)      
        
    sub=Button(fr1,text='Continue',command=con, width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
    sub.grid(row=5,column=1,sticky=W)

    fr2=Frame(tp)
    note=Label(fr2,text='*Price varies on class',font=('arial',10,'bold')).pack()
    fr2.pack(side=BOTTOM)

def details():
    def done():
        def ok():
            cat.destroy()
            root.deiconify()
            
        tno=t1.get()
        name=ent1.get()
        age=ent2.get()
        gender=bbb.get()
        mobile=ent3.get()

        sql="update booking set name='{}',gender='{}',age={},mobile={} where ticket={}".format(name,gender,age,mobile,tno)
        cur.execute(sql)
        db.commit()
        
        tic.destroy()
        
        cat=Toplevel()
        cat.title('SUCCESS')
        cat.geometry('240x200+550+200')
        cat.resizable(False,False)
        
        fr=Frame(cat ,bd=7,background='black', relief='raise')
        wel=Label(fr,text='Booking Successful',font=('arial',15,'bold'),fg='blue')
        wel.grid(row=0,columnspan=2)
        fr.pack(side=TOP)

        fr1=Frame(cat)
        fr1.place(x=5,y=70)

        no=Label(fr1,text='Ticket No.  :-',font=('arial',12,'bold'),fg='red').pack()
        cod=Label(fr1,text='Journey Code  :-',font=('arial',12,'bold'),fg='red').pack()

        fr2=Frame(cat)
        fr2.place(x=200,y=70)
        
        no=Label(fr2,text=tno,font=('arial',12,'bold'),fg='green').pack()
        cod=Label(fr2,text='MH',font=('arial',12,'bold'),fg='green').pack()
        
        fr3=Frame(cat)
        note=Label(fr3,text='*Store This Data For Further Uses.',font=('arial',10,'bold'))
        note.grid(row=1,columnspan=2)
        fr3.pack(side=BOTTOM)

        ok=Button(fr3,text='OK' ,command=ok ,width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
        ok.grid(row=0,column=1,sticky=W)        
            
    tic=Toplevel()
    tic.title('ENTER DETAILS')
    tic.geometry('350x300+500+120')
    tic.resizable(False,False)
    
    fr=Frame(tic ,bd=7,background='black', relief='raise')
    wel=Label(fr,text='Enter Details',font=('arial',25,'bold'),fg='blue')
    wel.grid(row=0,columnspan=2)
    fr.pack(side=TOP)
    
    fr1=Frame(tic)
    fr1.place(x=25,y=80)

    wek=Label(fr1,text='Ticket No.',font=('arial',15,'bold'))
    wek.grid(row=1,sticky=E)
    t1=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=15, bg='#ffffff', justify='right')
    t1.grid(row=1,column=1)
    
    name=Label(fr1,text='Enter Name',font=('arial',15,'bold'))
    ent1=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=15, bg='#ffffff', justify='right')
    name.grid(row=2,sticky=E)
    ent1.grid(row=2,column=1)
    
    age=Label(fr1,text='Enter Age',font=('arial',15,'bold'))
    ent2=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=15, bg='#ffffff', justify='right')   
    age.grid(row=3,sticky=E)
    ent2.grid(row=3,column=1)

    gender=Label(fr1,text='Select Gender',font=('arial',15,'bold'))
    ckk=['Male','Female','Others']
    bbb=Combobox(fr1,values=ckk,width=17,font=('arial', 9, 'bold'))
    gender.grid(row=4,sticky=E)
    bbb.grid(row=4,column=1)
    bbb.set('------Select------')

    mobile=Label(fr1,text=' Mobile No.',font=('arial',15,'bold'))
    ent3=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=15, bg='#ffffff', justify='right')   
    mobile.grid(row=5,sticky=E)
    ent3.grid(row=5,column=1)

    sub=Button(fr1,text='Book',command=done, width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
    sub.grid(row=6,column=1,sticky=W)
#----------------------------------------------------TICKET-------------------------------------------
def ticket():
    root.iconify()
    def tiket():        
        tno=ent1.get()
        code=ent2.get()
        if code=='MH':
            def ck():
                det.destroy()
                root.deiconify()
            tick.destroy()
            
            sql="select pickup,dropoff,date,month,year,name,class,type2,stype,seat,price,gender,mobile,age from booking where ticket={}".format(tno)
            cur.execute(sql)
            for x in cur:
                pick=x[0]
                drop=x[1]
                date=x[2]
                month=x[3]
                year=x[4]
                name=x[5]
                bclass=x[6]
                btype=x[7]
                stype=x[8]
                sno=x[9]
                price=x[10]
                gender=x[11]
                mno=x[12]
                age=x[13]
            
            det=Toplevel()
            det.title('SUCCESS')
            det.geometry('350x570+480+30')
            det.resizable(False,False)
            
            fr=Frame(det ,bd=7,background='black', relief='raise')
            wel=Label(fr,text='Your Details',font=('arial',25,'bold'),fg='blue')
            wel.grid(row=0,columnspan=2)
            fr.pack(side=TOP)
            
            fr1=Frame(det)
            fr1.place(x=5,y=80)

            a=int(date)
            b=int(month)
            c=int(year)
            jdate=datetime.date(c,b,a)
            tim='8:00 Hrs'

            no=Label(fr1,text='Ticket No.  :-',font=('arial',15,'bold'),fg='red').grid(row=0,sticky=W)
            cod=Label(fr1,text='Pickup  :-',font=('arial',15,'bold'),fg='red').grid(row=1,sticky=W)
            codq=Label(fr1,text='Dropoff  :-',font=('arial',15,'bold'),fg='red').grid(row=2,sticky=W)
            codw=Label(fr1,text='Date  :-',font=('arial',15,'bold'),fg='red').grid(row=3,sticky=W)
            code=Label(fr1,text='Name :-',font=('arial',15,'bold'),fg='red').grid(row=4,sticky=W)
            codr=Label(fr1,text='Age  :-',font=('arial',15,'bold'),fg='red').grid(row=5,sticky=W)
            codt=Label(fr1,text='Gender  :-',font=('arial',15,'bold'),fg='red').grid(row=6,sticky=W)
            cody=Label(fr1,text='Mobile No.  :-',font=('arial',15,'bold'),fg='red').grid(row=7,sticky=W)
            codu=Label(fr1,text='Bus Class :-',font=('arial',15,'bold'),fg='red').grid(row=8,sticky=W)
            codi=Label(fr1,text='Bus Type  :-',font=('arial',15,'bold'),fg='red').grid(row=9,sticky=W)
            coda=Label(fr1,text='Seat Type  :-',font=('arial',15,'bold'),fg='red').grid(row=10,sticky=W)
            codo=Label(fr1,text='Seat No.  :-',font=('arial',15,'bold'),fg='red').grid(row=11,sticky=W)
            codp=Label(fr1,text='Price  :-',font=('arial',15,'bold'),fg='red').grid(row=12,sticky=W)
            cods=Label(fr1,text='Time  :-',font=('arial',15,'bold'),fg='red').grid(row=13,sticky=W)

            fr2=Frame(det)
            fr2.place(x=210,y=80)

            no=Label(fr2,text=tno,font=('arial',15,'bold'),fg='green').grid(row=0,sticky=E)
            cod=Label(fr2,text=pick,font=('arial',15,'bold'),fg='green').grid(row=1,sticky=E)
            codq=Label(fr2,text=drop,font=('arial',15,'bold'),fg='green').grid(row=2,sticky=E)
            codw=Label(fr2,text=jdate,font=('arial',15,'bold'),fg='green').grid(row=3,sticky=E)
            code=Label(fr2,text=name,font=('arial',15,'bold'),fg='green').grid(row=4,sticky=E)
            codr=Label(fr2,text=age,font=('arial',15,'bold'),fg='green').grid(row=5,sticky=E)
            codt=Label(fr2,text=gender,font=('arial',15,'bold'),fg='green').grid(row=6,sticky=E)
            cody=Label(fr2,text=mno,font=('arial',15,'bold'),fg='green').grid(row=7,sticky=E)
            codu=Label(fr2,text=bclass,font=('arial',15,'bold'),fg='green').grid(row=8,sticky=E)
            codi=Label(fr2,text=btype,font=('arial',15,'bold'),fg='green').grid(row=9,sticky=E)
            codo=Label(fr2,text=stype,font=('arial',15,'bold'),fg='green').grid(row=10,sticky=E)
            codp=Label(fr2,text=sno,font=('arial',15,'bold'),fg='green').grid(row=11,sticky=E)
            codp=Label(fr2,text=price,font=('arial',15,'bold'),fg='green').grid(row=12,sticky=E)
            cods=Label(fr2,text=tim,font=('arial',15,'bold'),fg='green').grid(row=13,sticky=E)

            fr3=Frame(det)
            note=Label(fr3,text='*Give Feedback About Your Experience',font=('arial',13,'bold'))
            note.grid(row=1,columnspan=2)
            fr3.pack(side=BOTTOM)

            ok=Button(fr3,text='OK' ,command=ck ,width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
            ok.grid(row=0,column=1,sticky=W)               

        else:
            messagebox.showerror("OOPS",'Invalid Journey code')                     
        
    tick=Toplevel()
    tick.title('ENTER DETAILS')
    tick.geometry('350x300+500+120')
    tick.resizable(False,False)

    fr=Frame(tick ,bd=7,background='black', relief='raise')
    wel=Label(fr,text='Enter Details',font=('arial',25,'bold'),fg='blue')
    wel.grid(row=0,columnspan=2)
    fr.pack(side=TOP)

    fr1=Frame(tick)
    fr1.place(x=15,y=100)

    Tno=Label(fr1,text=' Ticket No.',font=('arial',15,'bold'))
    
    Tno.grid(row=1,sticky=E)
    ent1=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=15, bg='#ffffff', justify='right')
    ent1.grid(row=1,column=1)

    jc=Label(fr1,text=' Journey code',font=('arial',15,'bold'))
    ent2=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=15, bg='#ffffff', justify='right')
    jc.grid(row=2,sticky=E)
    ent2.grid(row=2,column=1)

    ub=Button(fr1,text='Submit',command=tiket, width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
    ub.grid(row=3,column=1,sticky=W)

    fr2=Frame(tick)
    note=Label(fr2,text='*Provided When Booking Was finished',font=('arial',10,'bold')).pack()
    fr2.pack(side=BOTTOM)
#----------------------------------------------CANCELLATION----------------------------------------------------    
def cancel():
    root.iconify()
    def canc():
        
        tno=ent1.get()
        code=ent2.get()
        if code=='MH':
            def kk():
                deta.destroy()
                root.deiconify() 
            can.destroy()
            
            sql="delete from booking where ticket={}".format(tno)
            cur.execute(sql)
            db.commit()

            deta=Toplevel()
            deta.title('SUCCESS')
            deta.geometry('330x180+550+200')
            deta.resizable(False,False)

            fr=Frame(deta ,bd=7,background='black', relief='raise')
            wel=Label(fr,text='Cancellation Successful',font=('arial',15,'bold'),fg='blue')
            wel.grid(row=0,columnspan=2)
            fr.pack(side=TOP)

            fr1=Frame(deta)
            fr1.place(x=5,y=70)

            no=Label(fr1,text='Your Ticket Has Been Cancelled.',font=('arial',15,'bold'),fg='red').grid(row=0,column=1,sticky=W)

            ok=Button(fr1,text='OK' ,command=kk ,width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
            ok.grid(row=5,columnspan=2)
                       
        else:
            messagebox.showerror("OOPS",'Invalid Journey code')
        
    can=Toplevel()
    can.title('Cancellation')
    can.geometry('350x300+500+120')
    can.resizable(False,False)
   
    fr=Frame(can,bd=7,background='black', relief='raise')
    wel=Label(fr,text='Enter Details',font=('arial',25,'bold'),fg='blue')
    wel.grid(row=0,columnspan=2)
    fr.pack(side=TOP)

    fr1=Frame(can)
    fr1.place(x=15,y=100)

    tno=Label(fr1,text=' Ticket No.',font=('arial',15,'bold'))
    ent1=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=15, bg='#ffffff', justify='right')
    tno.grid(row=1,sticky=E)
    ent1.grid(row=1,column=1)

    jc=Label(fr1,text=' Journey code',font=('arial',15,'bold'))
    ent2=Entry(fr1,font=('arial', 12, 'bold'), bd=4, width=15, bg='#ffffff', justify='right')
    jc.grid(row=2,sticky=E)
    ent2.grid(row=2,column=1)

    ub=Button(fr1,text='Submit',command=canc, width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
    ub.grid(row=3,column=1,sticky=W)

    fr2=Frame(can)
    note=Label(fr2,text='*Provided When Booking Was finished',font=('arial',10,'bold')).pack()
    fr2.pack(side=BOTTOM)
#--------------------------------------CHECK PRICE-------------------------------------------------------
def price():
    root.iconify()
    def pcheck():
        def dk():
            cata.destroy()
            root.deiconify()
        
        pick=b1.get()
        drop=b2.get()
        bclass=b11.get()
        if pick=='Devlali':
            sql1="select Price from devlali where Destination='{}' and category='{}'".format(drop,bclass)
            cur.execute(sql1)
            for x in cur:
                price=x[0]
        elif pick=='Nasik':
            sql2="select Price from nasik where Destination='{}' and category='{}'".format(drop,bclass)
            cur.execute(sql2)
            for y in cur:
                price=y[0]

        pot.destroy()
        cata=Toplevel()
        cata.title('Price')
        cata.geometry('300x260+550+200')
        cata.resizable(False,False)
        
        fr=Frame(cata ,bd=7,background='black', relief='raise')
        wel=Label(fr,text='Journey Price',font=('arial',15,'bold'),fg='blue')
        wel.grid(row=0,columnspan=2)
        fr.pack(side=TOP)

        fr1=Frame(cata)
        fr1.place(x=5,y=70)

        no=Label(fr1,text='Pickup  :-',font=('arial',12,'bold'),fg='red').pack()
        cod=Label(fr1,text='Dropoff  :-',font=('arial',12,'bold'),fg='red').pack()
        no1=Label(fr1,text='Bus Class  :-',font=('arial',12,'bold'),fg='red').pack()
        no2=Label(fr1,text='Price  :-',font=('arial',12,'bold'),fg='red').pack()

        fr2=Frame(cata)
        fr2.place(x=200,y=70)
        
        no=Label(fr2,text=pick,font=('arial',12,'bold'),fg='green').pack()
        cod=Label(fr2,text=drop,font=('arial',12,'bold'),fg='green').pack()
        no1=Label(fr2,text=bclass,font=('arial',12,'bold'),fg='green').pack()
        no2=Label(fr2,text=price,font=('arial',12,'bold'),fg='green').pack()
        
        fr3=Frame(cata)
        note=Label(fr3,text='*Cash Payment To Be Made While Boarding.',font=('arial',10,'bold'))
        note.grid(row=1,columnspan=2)
        fr3.pack(side=BOTTOM)

        ok=Button(fr3,text='OK' ,command=dk ,width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
        ok.grid(row=0,column=1,sticky=W)   
            
    pot=Toplevel()
    pot.title('See Price')
    pot.geometry('350x300+500+120')
    pot.resizable(False,False)
    
    fr=Frame(pot,bd=7,background='black', relief='raise')
    wel=Label(fr,text='Select Journey',font=('arial',25,'bold'),fg='blue')
    wel.grid(row=0,columnspan=2)
    fr.pack(side=TOP)
    
    fr1=Frame(pot)
    fr1.place(x=25,y=85)
    
    sor=Label(fr1,text='Pick-Up ',font=('arial',15,'bold'))
    c=['Devlali','Nasik']
    b1=Combobox(fr1,values=c,width=19,font=('arial', 9, 'bold') )
    b1.set('--------Select---------')
    sor.grid(row=1,sticky=E)
    b1.grid(row=1,column=1)
    
    des=Label(fr1,text='Drop-Off ',font=('arial',15,'bold'))
    d=['Mumbai','Chennai','Delhi','Kolkata','Ahemdabad','Lucknow','Patna','Chandigarh']
    b2=Combobox(fr1,values=d,width=19,font=('arial', 9, 'bold') )
    b2.set('--------Select---------')
    des.grid(row=2,sticky=E)
    b2.grid(row=2,column=1)

    Bt1=Label(fr1,text=' Bus Class',font=('arial',15,'bold'))
    ck=['AC','Non-AC']
    b11=Combobox(fr1,values=ck,width=19,font=('arial', 9, 'bold'))
    b11.set('--------Select---------')
    Bt1.grid(row=3,sticky=E)
    b11.grid(row=3,column=1)
    
    ub=Button(fr1,text='Check',command=pcheck, width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
    ub.grid(row=4,column=1,sticky=W)

    fr2=Frame(pot)
    note=Label(fr2,text='*Inclusive All Taxes',font=('arial',10,'bold')).pack()
    fr2.pack(side=BOTTOM)
#--------------------------------------FEEDBACK-----------------------------------------------------------------------    
def feedback():
    root.iconify()
    def subb():
        messagebox.showinfo("Submitted",'Feedback Submitted')
        
        feed.destroy()
        root.deiconify()
    feed=Toplevel()
    feed.title('Feedback')
    feed.resizable(False,False)
    
    fr=Frame(feed)
    fr.place(x=15,y=80)
    feed.geometry('450x430+500+120')

    fr1=Frame(feed,bd=7,background='black', relief='raise')
    wel=Label(fr1,text='Feedback',font=('arial',25,'bold'),fg='blue')
    wel.grid(row=0,columnspan=2)
    fr1.pack(side=TOP)

    i=StringVar()
    u1=Label(fr,text='How would you rate your first impression of us?',font=('arial',12,'bold'))
    r1=Radiobutton(fr,text='Excellent',value='Excellent',variable=i)
    r2=Radiobutton(fr,text='Good',value='Good',variable=i)
    r3=Radiobutton(fr,text='Satisfactory',value='Satisfactory',variable=i)
    r4=Radiobutton(fr,text='Poor',value='Poor',variable=i)
    u1.grid(row=2,columnspan=4)
    r1.grid(row=3,column=0,sticky=W)
    r2.grid(row=3,column=1,sticky=W)
    r3.grid(row=3,column=2)
    r4.grid(row=3,column=3,sticky=E)

    l=StringVar()
    u2=Label(fr,text='Did you feel safe and comfortable?',font=('arial',12,'bold'))
    c1=Radiobutton(fr,text='Yes',value='Y',variable=l)
    c2=Radiobutton(fr,text='No',value='N',variable=l)
    u2.grid(row=4,columnspan=3)
    c1.grid(row=5,column=0,sticky=W)
    c2.grid(row=5,column=1,sticky=W)
    
    j=StringVar()
    u3=Label(fr,text='Would you travel with us in the future?',font=('arial',12,'bold'))
    a1=Radiobutton(fr,text='Yes',value='Yes',variable=j)
    a2=Radiobutton(fr,text='No',value='No',variable=j)
    u3.grid(row=6,columnspan=3)
    a1.grid(row=7,column=0,sticky=W)
    a2.grid(row=7,column=1,sticky=W)

    k=StringVar()
    u4=Label(fr,text='Would you recommend us to others?',font=('arial',12,'bold'))
    b1=Radiobutton(fr,text='Yes',value='Yes',variable=k)
    b2=Radiobutton(fr,text='No',value='No',variable=k)
    u4.grid(row=8,columnspan=3)
    b1.grid(row=9,column=0,sticky=W)
    b2.grid(row=9,column=1,sticky=W)

    u6=Label(fr,text='Anything More?',font=('arial',12,'bold'))
    fdk = StringVar()
    fd = Entry(fr, font=('arial', 16), textvariable = fdk, width = 30)
    u6.grid(row=10,columnspan=2)
    fd.grid(row=11,columnspan=4,sticky='s',rowspan=3,ipady=20)

    ub=Button(fr,text='Submit',command=subb, width=8, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
    ub.grid(row=18,column=1,sticky=E)


    
#------------------------------------------EXIT------------------------------------------------------------------------   
def iexit():
    qExit = messagebox.askyesno("Quit","Do  you want to quit")
    if qExit > 0:
        root.destroy()
        return     
#------------------------------------------HOMEPAGE--------------------------------------------------------------------------------------------
root.title('Bus Booking')
fr=Frame(root, bd=7,background='black', relief='raise')
fr.pack(side=TOP)
fr1=Frame(root)
w=Label(fr,font=('arial',25,'bold'),text='HAPPY TRAVELS',fg='blue')
w.grid(row=0,columnspan=2)
fr1.place(x=110,y=70)

b=Button(fr1,text='BOOK BUS', command=login, width=15, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
b1=Button(fr1,text='VIEW TICKET', command=ticket, width=15, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
b2=Button(fr1,text='CANCEL TICKET', command=cancel, width=15, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
b3=Button(fr1,text='CHECK PRICE', command=price, width=15, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
b4=Button(fr1,text='FEEDBACK', command=feedback, width=15, bd=5,bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)
b5=Button(fr1,text='EXIT', command=iexit, width=15,bd=5, bg='antiquewhite1',font=('arial',10,'bold'),fg='green', padx=2, pady=1)

b.grid(columnspan=2)
b1.grid(columnspan=2)
b2.grid(columnspan=2)
b3.grid(columnspan=2)
b4.grid(columnspan=2)
b5.grid(columnspan=2)

root.resizable(False,False)
root.geometry('350x300+500+120')
root.mainloop() 
