from tkinter import *
from patient_register import * 
from viewall_patient import *
from DoctorRegister import *

class WelcomePage:

    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry("300x300+300+150")
        self.root.title("Welcome ")
        #self.root.eval('tk::PlaceWindow . center')


        # Creating Menubar
        menubar = Menu(self.root)
        
        # Adding File Menu and commands
        file = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='View',menu = file)
        
        file.add_command(label ='Register a new patient', command = self.showRegisterPage)
        file.add_separator()
        file.add_command(label ='Register a new Doctor', command = self.showDocRegisterPage)
        file.add_separator()
        file.add_command(label ='View Patient and Generate Bill',
                                    command = self.showVViewAllPatient)
        file.add_separator()
        file.add_command(label ='Exit', command = self.root.destroy)

        # display Menu
        self.root.config(menu = menubar)
        self.root.mainloop()


    def showVViewAllPatient(self):
        self.root.iconify()
        obj = ViewAll()

    def showRegisterPage(self):
        self.root.iconify()
        obj = Register()

    def showDocRegisterPage(self):
        self.root.iconify()
        obj = RegisterDoctor()


if __name__ == "__main__":
    WP =WelcomePage()
