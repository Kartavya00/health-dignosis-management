import sys
from tkinter import *
from pymysql import *
from tkinter import ttk
import configuredb
from CheckTreeView import CbTreeview
from generatebill import *





class ViewAll:
    def __init__(self):
        self.r=Tk()
        self.r.title("Patient details")
        #self.r.geometry("900x500+300+150")
      
     
        #self.tree=ttk.Treeview(self.r)
        self.tree= CbTreeview(self.r)
        
        self.tree["columns"]=("patientId","name","age","weight","gender","address","phoneno","disease","bloodGroup","Discharge")
        self.tree.column('#0',width=0,stretch=NO)
        self.tree.column("patientId", width=100,minwidth=80,anchor=CENTER)
        self.tree.column("name", width=100,minwidth=50,anchor=CENTER)
        self.tree.column("age", width=50,minwidth=50,anchor=CENTER)
        self.tree.column("weight", width=50,minwidth=50,anchor=CENTER)
        self.tree.column("gender", width=50,minwidth=100,anchor=CENTER)
        self.tree.column("address", width=100,minwidth=100,anchor=CENTER)
        self.tree.column("phoneno", width=100,minwidth=100,anchor=CENTER)
        self.tree.column("disease", width=100,minwidth=100,anchor=CENTER)
        self.tree.column("bloodGroup", width=100,minwidth=100,anchor=CENTER)  
        self.tree.column("Discharge", width=100,minwidth=100,anchor=CENTER)  

        self.tree.heading('#0',text='',anchor=CENTER)
        self.tree.heading("patientId",text="Id",anchor=CENTER)
        self.tree.heading("name",text="Name",anchor=CENTER)
        self.tree.heading("age",text="Age",anchor=CENTER)
        self.tree.heading("weight",text="Weight",anchor=CENTER)
        self.tree.heading("gender",text="Gender",anchor=CENTER)
        self.tree.heading("address",text="Address",anchor=CENTER)
        self.tree.heading("phoneno",text="Phoneno",anchor=CENTER)
        self.tree.heading("disease",text="Disease",anchor=CENTER)
        self.tree.heading("bloodGroup",text="BloodGroup",anchor=CENTER)
        self.tree.heading("Discharge",text="Discharge",anchor=CENTER)


       

        #getting all patient details
        self.getAllPatientDetail()

        #showing all patient details
        i=0
        for ro in configuredb.cur:
            self.tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8]))
            i=i+1
        self.tree.pack()


        configuredb.closeConnection()


        
        self.btninsert = Button(self.r,text="Generate Bill for selected patient",command=self.showGenerateBill)
        self.btninsert.place(x = 40,y=250,width = 300,height = 30)

        self.r.mainloop()


    def getAllPatientDetail(self):
        configuredb.connecttodb()
        configuredb.cur.execute("select * from patient")

    def showGenerateBill(self):
        self.r.destroy()
        obj = Bill(configuredb.selectedpid)
       



if __name__ == "__main__":
    obj = ViewAll()
