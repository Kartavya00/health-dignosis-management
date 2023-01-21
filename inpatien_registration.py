from tkinter import *
from tkinter.font import ROMAN
from typing import Tuple
from pymysql import *
from tkinter import messagebox
from tkinter import ttk
import configuredb


class In_registration:
    
    def __init__(self,pid):

        self.pid = pid

        self.root = Tk()
        self.root.geometry("600x450+300+100")
        #self.root.eval('tk::PlaceWindow . center')

        #messagebox.showinfo(str(pid))

        self.title=Label(self.root,text="In Patient Registration page")
        self.title.place(x=10,y=15,width=600,height=100)

        self.lblname = Label(self.root, text="Select Room Type:")
        self.lblname.place(x = 30,y=120,width = 220,height = 30)

        #getting roomtypes from database
        self.roomtype = self.getRoomTypes()
        if(len(self.roomtype) > 0):
            pass
        else:
            messagebox.showerror(
                "In Patient Register Error", "Cannot Fetch RoomTypes during inpatient form load")
            self.root.destroy()


        self.sel_room_type = StringVar(self.root)

        # Set the default value of the variable
        self.sel_room_type.set("Select an Option")
        self.drop = OptionMenu(self.root, self.sel_room_type, *self.roomtype,command=self.setRoomPrice)
        self.drop.place(x = 240,y=120,width = 300,height = 30)

        self.lblcharge = Label(self.root, text="Charge Per Day:",font=("Times", 15, "bold"))
        self.lblcharge.place(x = 30,y=170,width = 220,height = 30)
        self.encharge = Entry(self.root, font=("Times", 15, "bold"))
        self.encharge.place(x = 240,y=170,width = 300,height = 30)

        self.lbladmitdate = Label(self.root, text="Admit Date:",font=("Times", 15, "bold"))
        self.lbladmitdate.place(x = 30,y=220,width = 220,height = 30)
        self.enadmitdate = Entry(self.root, font=("Times", 15, "bold"))
        self.enadmitdate.config(fg = 'grey')
        self.enadmitdate.insert(0,"yyyy-mm-dd")
        self.enadmitdate.bind('<FocusIn>', self.on_entry_focus)
        self.enadmitdate.bind('<FocusOut>', self.on_entry_focus_leave)
        self.enadmitdate.place(x = 240,y=220,width = 300,height = 30)
      
        


        self.lbldisdate = Label(self.root, text="Discharge Date:",font=("Times", 15, "bold"))
        self.lbldisdate.place(x = 30,y=270,width = 220,height = 30)
        self.endisdate = Entry(self.root, font=("Times", 15, "bold"))
        self.endisdate.config(fg = 'grey')
        self.endisdate.insert(0,"yyyy-mm-dd")
        self.endisdate.bind('<FocusIn>', self.on_entry_focus)
        self.endisdate.bind('<FocusOut>', self.on_entry_focus_leave)
        self.endisdate.place(x = 240,y=270,width = 300,height = 30)
        
        self.lbladvance = Label(self.root, text="Advance:",font=("Times", 15, "bold"))
        self.lbladvance.place(x = 30,y=320,width =220,height = 30)
        self.enadvance = Entry(self.root, font=("Times", 15, "bold"))
        self.enadvance.place(x = 240,y=320,width = 300,height = 30)

        self.btninsert = Button(self.root,font=("Times", 15, "bold"), text="Submit",command=self.insert_Inpatient)
        self.btninsert.place(x = 130,y=380,width = 70,height = 30)

        self.root.mainloop()


    def on_entry_focus(self,event):
        if self.enadmitdate.get() == 'yyyy-mm-dd':
            self.enadmitdate.delete(0, 'end')
            self.enadmitdate.config(fg = 'black')
        
        if self.endisdate.get() == 'yyyy-mm-dd':
            self.endisdate.delete(0, 'end')
            self.endisdate.config(fg = 'black')
  
    # call function when we leave entry box
    def on_entry_focus_leave(self,event):
        if self.enadmitdate.get() == '':
            self.enadmitdate.insert(0, 'yyyy-mm-dd')
            self.enadmitdate.config(fg = 'grey')
        
        if self.endisdate.get() == '':
            self.endisdate.insert(0, 'yyyy-mm-dd')
            self.endisdate.config(fg = 'grey')
        

    def getRoomTypes(self) -> Tuple:
        if(configuredb.connecttodb() == True):
            configuredb.cur.execute("select room_type from room")
            roomtype = configuredb.cur.fetchall()
            return roomtype

        else:
            return []


    def setRoomPrice(self,*args):
        print(self.sel_room_type.get())
        roomtype = self.sel_room_type.get()
        roomtype = roomtype.replace('(',"")
        roomtype = roomtype.replace(')',"")
        roomtype = roomtype.replace(',',"")

        getqry = "select room_id,charge_per_day from room where room_type = " + roomtype
        n = configuredb.cur.execute(getqry)

        if(n > 0):
             roomdata = configuredb.cur.fetchall()
             self.roomcharge = roomdata[0][1]
             self.roomid = roomdata[0][0]

             self.encharge.delete(0,END)
             self.encharge.insert(0,self.roomcharge)
             print(self.roomid)


        else:
            messagebox.showerror(
                "In Patient Register Error", "Cannot Fetch Room charge and id during room type change")



    def insert_Inpatient(self):
        self.admitdate = self.enadmitdate.get()
        self.disdate = self.endisdate.get()
        self.advance = self.enadvance.get()
        insqry = "insert into inpatient(pid,room_id,date_of_admit,date_of_discharge,advance) values(" + str(self.pid) + "," + str(self.roomid) + ",'" + self.admitdate + "','" + self.disdate + "'," + self.advance + ")"

        #print(insqry)
        #executing the insert query
        
        n = configuredb.cur.execute(insqry)
        configuredb.conn.commit() #to make the changes into the database permanent
        
        if(n > 0):
            #messagebox.showinfo(title="insert_inpatient",message="Data Inserted SuccessFully")
            configuredb.closeConnection()
            self.root.destroy()
        else:
            #messagebox.showinfo(title="insert_inpatient",message="Data Inserted Problem")
            pass


    


if __name__ == "__main__":
    obj = In_registration("1")
