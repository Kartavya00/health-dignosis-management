from tkinter import *
import pymysql
from tkinter import messagebox
from welcomepage import *
import configuredb


class RegisterDoctor():

    def __init__(self):
        self.t = Tk()
        self.t.wm_title("Doctor Registration")
        self.t.geometry("400x220+300+150")
        #self.t.eval('tk::PlaceWindow . center')

        self.lbl1 = Label(self.t, text="Doctor Name", font=('Consolas', 14, 'bold'))
        self.lbl1.place(x=20, y=20, width=150, height=40)
        self.en1 = Entry(self.t, font=('Consolas', 14, 'bold'))
        self.en1.place(x=170, y=20, width=150, height=30)

        self.lbl2 = Label(self.t, text="Department",
                          font=('Consolas', 14, 'bold')) 
        self.lbl2.place(x=20, y=80, width=150, height=40)
        self.en2 = Entry(self.t, font=('Consolas', 14, 'bold'))
        self.en2.place(x=170, y=80, width=150, height=30)

        self.btn1 = Button(self.t, text="Submit", font=(
            'Consolas', 14, 'bold'), command=self.submit)
        self.t.bind('<Return>', self.submit)
        self.btn1.place(x=150, y=130, width=70, height=40)


        self.t.mainloop()
    
    
    def submit(self,event = None):
        if(self.en1.get() == "" or self.en2.get() == ""):
            messagebox.showinfo(
                "Register Error", "Docname or Dept cannot be empty")
        else:
            name = self.en1.get()
            dept = self.en2.get()

            insqry = "insert into doctor(doctorname,dept) values( '" + name + "','" + dept + "')"

            if(configuredb.connecttodb() == True):
                n=configuredb.cur.execute(insqry)
                configuredb.conn.commit()

                # checking if data has some rows or not
                if(n > 0):
                    messagebox.showinfo(
                        "Doctor Register", "Doctor Registered")
                    self.t.destroy()
                else:
                    messagebox.showerror(
                "Doctor Register Error", "Cannot Create Doctor")


if __name__ == "__main__":
    obj=RegisterDoctor()
