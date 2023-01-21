from tkinter import *
import pymysql
from tkinter import messagebox
from welcomepage import *
import configuredb


class userGUI():

    def __init__(self):
        self.t = Tk()
        self.t.wm_title("Login")
        self.t.geometry("400x220+300+150")
        #self.t.eval('tk::PlaceWindow . center')

        self.lbl1 = Label(self.t, text="UserID", font=('Consolas', 14, 'bold'))
        self.lbl1.place(x=20, y=20, width=150, height=40)
        self.en1 = Entry(self.t)
        self.en1.place(x=170, y=20, width=150, height=30)

        self.lbl2 = Label(self.t, text="Password")
        self.lbl2.place(x=20, y=80, width=150, height=40)
        self.en2 = Entry(self.t, show="*")
        self.en2.place(x=170, y=80, width=150, height=30)

        self.btn1 = Button(self.t, text="LOGIN", font=(
            'Consolas', 14, 'bold'), command=self.log)
        self.t.bind('<Return>', self.log)
        self.btn1.place(x=150, y=130, width=70, height=40)


        self.link = Label(self.t, text="Sign In",font=('Helvetica bold', 10,'bold'), fg="blue", cursor="hand2")
        self.link.bind("<Button-1>",self.SignIn)
        self.link.place(x=300, y=160, width=70, height=40)

        self.t.mainloop()

    def SignIn(self,event = None):
        import UserSignIn
        self.t.destroy()
        obj = UserSignIn.SignInForm()
      

    def log(self,event = None):

        global conn
        global cur

        if(self.en1.get() == "" or self.en2.get() == ""):
            messagebox.showinfo(
                "Login Error", "userid or password cannot be empty")
        else:
            name = self.en1.get()
            password = self.en2.get()

            getqry = "select * from hosp_login where user_id = '" + \
                    name + "' and password = '" + password + "'"

            if(configuredb.connecttodb() == True):
                n=configuredb.cur.execute(getqry)

                # checking if data has some rows or not
                if(n == 0):
                    messagebox.showerror(
                        "Login Error", "Invlalid name or password")
                else:
                    self.t.destroy()
                    configuredb.closeConnection()
                    obj = WelcomePage()

            else:
                messagebox.showerror(
                "Login Error", "module:Login\nclass:UserGui\nMethod:connectToDb\nErr Msg:Cannot connect to DB")



if __name__ == "__main__":
        obj=userGUI()
