from tkinter import *
from pymysql import *
from tkinter import messagebox
from tkinter import ttk
import configuredb
from inpatien_registration import *


class Register:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("490x600+300+100")
        #self.root.eval('tk::PlaceWindow . center')

        self.lblname = Label(self.root, text="Name:")
        self.lblname.place(x=30, y=20, width=70, height=30)
        self.enname = Entry(self.root)
        self.enname.place(x=120, y=20, width=300, height=30)

        self.lblage = Label(self.root, text="Age:")
        self.lblage.place(x=30, y=70, width=70, height=30)
        self.enage = Entry(self.root)
        self.enage.place(x=120, y=70, width=300, height=30)

        self.lblweight = Label(self.root, text="Weight")
        self.lblweight.place(x=30, y=120, width=70, height=30)
        self.enweight = Entry(self.root)
        self.enweight.place(x=120, y=120, width=300, height=30)

        self.lblgender = Label(self.root, text="Gender:")
        self.lblgender.place(x=30, y=170, width=70, height=30)
        self.engender = Entry(self.root)
        self.engender.place(x=120, y=170, width=300, height=30)

        self.lbladdress = Label(
            self.root, text="Address:")
        self.lbladdress.place(x=30, y=220, width=70, height=30)
        self.enaddress = Entry(self.root)
        self.enaddress.place(x=120, y=220, width=300, height=30)

        self.lblmobile = Label(
            self.root, text="Phone NO.:")
        self.lblmobile.place(x=30, y=270, width=90, height=30)
        self.enmobile = Entry(self.root)
        self.enmobile.place(x=120, y=270, width=300, height=30)

        self.lbldisease = Label(
            self.root, text="Disease:")
        self.lbldisease.place(x=30, y=320, width=70, height=30)
        self.endisease = Entry(self.root)
        self.endisease.place(x=120, y=320, width=300, height=30)

        self.lblboodgrp = Label(
            self.root, text="B Grp:")
        self.lblboodgrp.place(x=30, y=370, width=70, height=30)
        self.enboodgrp = Entry(self.root)
        self.enboodgrp.place(x=120, y=370, width=300, height=30)



        self.lbldrname = Label(self.root, text="Dr. Name:"
                               )
        self.lbldrname.place(x=30, y=420, width=90, height=30)

        # getting docnames from database
        self.docnames = self.getDoctorNames()
        if(len(self.docnames) > 0):
            pass
        else:
            messagebox.showerror(
                "Patient Register Error", "module:Patient_register\nclass:Register\nMethod:__init__\nErr Msg:Cannot fetch DoctorNames")

        self.sel_doc_name = StringVar(self.root)
        # Set the default value of the variable
        self.sel_doc_name.set("Select an Option")
        self.drop = OptionMenu(self.root, self.sel_doc_name, *self.docnames)
        self.drop.place(x=120, y=420, width=300, height=30)

        self.var = IntVar(self.root)
        self.var.set(0)
        self.radio = Radiobutton(self.root, text="In Patient", variable=self.var,
                                 font=("Times", 15, "bold"), value=1)
        self.radio.place(x=60, y=470, width=150, height=50)

        self.radio = Radiobutton(self.root, text="Out Patient", variable=self.var,
                                 font=("Times", 15, "bold"), value=2)
        self.radio.place(x=310, y=470, width=150, height=50)

        self.btninsert = Button(self.root, font=("Times", 15, "bold"), text="Submit",
                                command=self.insertpatient)
        self.btninsert.place(x=220, y=540, width=70, height=30)

        self.root.mainloop()

    def getDoctorNames(self) -> tuple:

        if(configuredb.connecttodb() == True):
            configuredb.cur.execute("select doctorname from doctor")
            docname = configuredb.cur.fetchall()
            return docname

        else:

            return []

    def insertpatient(self):
        if(self.var.get() == 1 or self.var.get() == 2):    
            docid = self.getDocid()
            #print(docid)
            if(docid != 0):
                # collecting the data from text boxes
                name = self.enname.get()
                age = self.enage.get()
                weight = self.enweight.get()
                gender = self.engender.get()
                address = self.enaddress.get()
                mob = self.enmobile.get()
                dis = self.endisease.get()
                bgrp = self.enboodgrp.get()

                insqry = "insert into patient(name,age,weight,gender,address,phoneno,disease,blood_grp,doctorid) values('" + name + "'," + age + "," + weight + ",'" + gender + "','" + address + "',"+mob+",'"+dis+"','" + bgrp + "'," + str(docid)+")"

                print(insqry)

                #executing the insert query
                n = configuredb.cur.execute(insqry)
                configuredb.conn.commit() #to make the changes into the database permanent
                if(n > 0):
                    messagebox.showinfo(title="patient_register",message="Data Inserted SuccessFully")

                    if(self.var.get() == 1):
                        #get patient id of current inserted patient
                        pid = self.getpatient_id()
                        if(pid != 0):
                            self.root.destroy()
                            configuredb.conn.close()
                            #show inpatient form
                            obj = In_registration(pid)
                        else:
                             messagebox.showerror(title="patient_register",message="Unable to fetch pid after insert")

                else:
                    messagebox.showerror(title="patient_register",message="Data Insertion Problem")
        else:
            messagebox.showerror("patient_register","Please Select Inpatient or Outpatient")
                   

    
    def getpatient_id(self)->str:
        getqry = "select * from patient"
        n = configuredb.cur.execute(getqry)
        if(n > 0):
             data = configuredb.cur.fetchall()

             #getting pid of the latest inserted patient
             pid = data[len(data) - 1][0]
             return pid
        else:
            return 0

    def getDocid(self) -> int:

        # print(self.value_inside.get())
        docname = self.sel_doc_name.get()
        docname = docname.replace('(',"")
        docname = docname.replace(')',"")
        docname = docname.replace(',',"")

        print(docname)

        
        getqry = "select doctorid from doctor where doctorname = " + docname

        print(getqry)
        n = configuredb.cur.execute(getqry)

        if(n > 0):
             id = configuredb.cur.fetchall()
             return id[0][0]
        else:
             return 0


if __name__ == "__main__":
    obj = Register()
