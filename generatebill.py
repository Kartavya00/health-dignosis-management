from tkinter import *
from datetime import date, datetime
from tkinter import messagebox

import configuredb

class Bill:
    
    def __init__(self,pid):
        self.pid = pid
        print(self.pid)
        self.root = Tk()
        self.root.geometry("600x650+300+50")

        self.lblname1 = Label(self.root, text="Bill Generation:-",fg="Blue")
        self.lblname1.place(x = 10,y=1,width = 200,height = 70)

        self.lblbillno = Label(self.root, text="Bill_No:",font=("Times", 15, "bold"))
        self.lblbillno.place(x = 30,y=70,width = 100,height = 30)
        self.enbillno = Entry(self.root, font=("Times", 15, "bold"))
        self.enbillno.place(x = 180,y=70,width = 300,height = 30)

        self.lblpid = Label(self.root, text="Patient_Id:",font=("Times", 15, "bold"))
        self.lblpid.place(x = 30,y=120,width = 100,height = 30)
        self.enpid = Entry(self.root, font=("Times", 15, "bold"))
        self.enpid.place(x = 180,y=120,width = 300,height = 30)

        
        self.lbladmitdate = Label(self.root, text="Admit Date:",font=("Times", 15, "bold"))
        self.lbladmitdate.place(x = 30,y=170,width = 100,height = 30)
        self.enadmitdate = Entry(self.root, font=("Times", 15, "bold"))
        self.enadmitdate.place(x = 180,y=170,width = 300,height = 30)

        self.lbldisdate= Label(self.root, text="Dis Date:",font=("Times", 15, "bold"))
        self.lbldisdate.place(x = 30,y=220,width = 100,height = 30)
        self.endisdate = Entry(self.root, font=("Times", 15, "bold"))
        self.endisdate.place(x = 180,y=220,width = 300,height = 30)
        

        self.lbldcharge = Label(self.root, text="Doctor Fees",font=("Times", 15, "bold"))
        self.lbldcharge.place(x = 30,y=270,width = 100,height = 30)
        self.endcharge = Entry(self.root, font=("Times", 15, "bold"))
        self.endcharge.place(x = 180,y=270,width = 300,height = 30)

        self.lblmedcharge = Label(self.root, text="Medicine Charge:",font=("Times", 15, "bold"))
        self.lblmedcharge.place(x = 30,y=320,width = 150,height = 30)
        self.enmedcharge = Entry(self.root, font=("Times", 15, "bold"))
        self.enmedcharge.place(x = 180,y=320,width = 300,height = 30)
        
        self.lblroomcharge = Label(self.root, text="Room_Charge:",font=("Times", 15, "bold"))
        self.lblroomcharge.place(x = 30,y=370,width = 150,height = 30)
        self.enroomcharge = Entry(self.root, font=("Times", 15, "bold"))
        self.enroomcharge.place(x = 180,y=370,width = 300,height = 30)

        self.lblopcharge = Label(self.root, text="Operation Charge:",font=("Times", 13, "bold"))
        self.lblopcharge.place(x = 30,y=420,width = 150,height = 30)
        self.enopcharge = Entry(self.root, font=("Times", 15, "bold"))
        self.enopcharge.place(x = 180,y=420,width = 300,height = 30)

        self.lblnoday = Label(self.root, text="No. Of Days:",font=("Times", 15, "bold"))
        self.lblnoday.place(x = 30,y=470,width = 150,height = 30)
        self.ennoday = Entry(self.root, font=("Times", 15, "bold"))
        self.ennoday.place(x = 180,y=470,width = 300,height = 30)

        self.lblnurse = Label(self.root, text="Nursing Charge:",font=("Times", 15, "bold"))
        self.lblnurse.place(x = 30,y=520,width = 150,height = 30)
        self.ennurse = Entry(self.root, font=("Times", 15, "bold"))
        self.ennurse.place(x = 180,y=520,width = 300,height = 30)

        self.lbladvance = Label(self.root, text="advanced:",font=("Times", 15, "bold"))
        self.lbladvance.place(x = 30,y=570,width = 100,height = 30)
        self.enadvance = Entry(self.root, font=("Times", 15, "bold"))
        self.enadvance.place(x = 180,y=570,width = 300,height = 30)

        self.lbltotal = Label(self.root, text="Total Bill:",font=("Times", 15, "bold"))
        self.lbltotal.place(x = 30,y=620,width = 100,height = 30)
        self.entotal = Entry(self.root, font=("Times", 15, "bold"))
        self.entotal.place(x = 180,y=620,width = 300,height = 30)

        self.btn=Button(self.root,text="OK",font=("Times", 15, "bold"))
        self.btn.place(x=40,y=670,width=60,height=25)

        #self.updateDischargeDate()
        self.getinpatientDetails()

        self.root.mainloop()



    def updateDischargeDate(self):
        configuredb.connecttodb()
        
        #getting todays date from system
        dischargedate = str(datetime.today()).split()[0]

        n = configuredb.cur.execute("update inpatient set date_of_discharge = '" + dischargedate + "' where pid = " + str(self.pid))
        configuredb.conn.commit()
        print("OK")


    def getinpatientDetails(self):
        configuredb.connecttodb()
        configuredb.cur.execute("select * from inpatient where pid = " + str(self.pid))
        indata = configuredb.cur.fetchall()

        self.roomid = indata[0][1]
        self.admitdate = str(indata[0][2])
        self.disdate =  str(indata[0][3])
        self.advance =  indata[0][4]

        d1 = str.split(self.admitdate,'-')
        d2 = str.split(self.disdate,'-')

        d1 = date(int(d1[0]), int(d1[1]), int(d1[2]))
        d2 = date(int(d2[0]), int(d2[1]), int(d2[2]))
        delta = d2 - d1
        
        self.noofdays = delta.days

        self.getperdaycharge()


    def getperdaycharge(self):
        configuredb.cur.execute("select charge_per_day from room where room_id = " + str(self.roomid))
        data = configuredb.cur.fetchall()

        self.perdaycharge = data[0][0]

        self.totalroomcharge = self.perdaycharge * self.noofdays

        self.showbill()


    def showbill(self):
        
        #getting total no of rows in bill table
        configuredb.cur.execute("select * from bill")
        data = configuredb.cur.fetchall()

        self.billno = len(data) + 1001
        self.doccharge = 1000 * self.noofdays
        self.medcharge = 500 * self.noofdays
        self.opcharge = 0 * self.noofdays
        self.nurcharge = 300 * self.noofdays

        self.totalbill = (self.doccharge + self.medcharge + self.opcharge + self.nurcharge + self.totalroomcharge ) - self.advance


        self.enbillno.insert(0,self.billno)
        self.enpid.insert(0,self.pid)
        self.endcharge.insert(0,self.doccharge)
        self.enmedcharge.insert(0,self.medcharge)
        self.enroomcharge.insert(0,self.totalroomcharge)
        self.enopcharge.insert(0,self.opcharge)
        self.ennoday.insert(0,self.noofdays)
        self.ennurse.insert(0,self.nurcharge)
        self.enadvance.insert(0,self.advance)
        self.entotal.insert(0,self.totalbill)
        self.enadmitdate.insert(0,self.admitdate)
        self.endisdate.insert(0,self.disdate)


        insbillqry = "insert into bill values(" + self.enbillno.get() + "," + self.enpid.get() + "," +  self.endcharge.get() + "," + self.enmedcharge.get() + "," + self.enroomcharge.get() + "," + self.enopcharge.get() + ","  + self.ennoday.get() + "," + self.ennurse.get() + "," + self.enadvance.get() + "," + self.entotal.get() + ")"
      
        n = configuredb.cur.execute(insbillqry)
        configuredb.conn.commit()

        if(n > 0):
            messagebox.showinfo("Bill generated successfully")
            configuredb.closeConnection()



        


     
        
        






if __name__ == '__main__':
    obj = Bill(15)
