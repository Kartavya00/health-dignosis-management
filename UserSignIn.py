from tkinter import *
import pymysql
from tkinter import messagebox
from welcomepage import *
import configuredb


class SignInForm():

    def __init__(self):
        self.t = Tk()
        self.t.wm_title("Sign In")
        self.t.geometry("400x220+300+150")
        #self.t.eval('tk::PlaceWindow . center')

        self.lbl1 = Label(self.t, text="User Name")
        self.lbl1.place(x=20, y=20, width=150, height=40)
        self.en1 = Entry(self.t,)
        self.en1.place(x=170, y=20, width=150, height=30)

        self.lbl2 = Label(self.t, text="Password")
        self.lbl2.place(x=20, y=80, width=150, height=40)
        self.en2 = Entry(self.t)
        self.en2.place(x=170, y=80, width=150, height=30)

        self.btn1 = Button(self.t, text="Submit", font=(
            'Consolas', 14, 'bold'), command=self.submit)
        self.t.bind('<Return>', self.submit)
        self.btn1.place(x=150, y=130, width=70, height=40)


        self.t.mainloop()


    def submit(self,event = None):

     
        if(self.en1.get() == "" or self.en2.get() == ""):
            messagebox.showinfo(
                "Sign In Error", "user name or password cannot be empty")
        else:
            name = self.en1.get()
            password = self.en2.get()

            insqry = "insert into hosp_login values( '" + name + "','" + password + "')"

            if(configuredb.connecttodb() == True):
                n=configuredb.cur.execute(insqry)
                configuredb.conn.commit()

                # checking if data has some rows or not
                if(n > 0):
                    messagebox.showinfo(
                        "Sign In", "User Created SucessFully")
                    self.t.destroy()
                    obj = WelcomePage()
                else:
                    messagebox.showerror(
                "Sign In Error", "Cannot Create User")


if __name__ == "__main__":
    obj=SignInForm()
