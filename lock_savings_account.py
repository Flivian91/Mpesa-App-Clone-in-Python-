from tkinter import*
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from time import strftime



class LockSavingsAccount():
    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.root.geometry("350x550+500+50")
        self.root.overrideredirect(1)
        self.root.config(background="white")

        # =========================== Upper Part====================
        def time():
            string = strftime("%H:%M:%S")
            self.time.config(text=string)
            self.time.after(1000, time)
        # time label
        self.time = Label(self.root, font=("Bookman Old Style", 15), background="white")
        self.time.place(x=5, y=17)
        time()

        # Image for thwe network And the Bettery percentage

        # icon for back ward
        back_icon = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\back arrow orignal.png")
        back_icon = back_icon.resize((40, 27))
        self.photoimg = ImageTk.PhotoImage(back_icon)

        def back():
            self.root.destroy()

        back = Button(self.root, image=self.photoimg,command=back, cursor="hand2", background="white", borderwidth=0, activebackground="white")
        back.place(x=5, y=68)

        # End session Icon
        end_session = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\end session1.png")
        end_session = end_session.resize((40, 40))
        self.end_session = ImageTk.PhotoImage(end_session)

        def end_session_command():
                close = CTkButton(self.root, text="End Session",width=100,command=self.back, cursor="hand2",corner_radius=12,text_color="black", bg_color="white",fg_color="light gray",border_width=0, hover_color="light gray")
                close.place(x=230, y=95)

        end_session = Button(self.root, image=self.end_session,command=end_session_command, cursor="hand2", background="white", borderwidth=0, activebackground="white")
        end_session.place(x=295, y=58)

        #  network icon
        network_icon = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\battery.png")
        network_icon = network_icon.resize((150, 50))
        self.photonet = ImageTk.PhotoImage(network_icon)

        f_lbl = Label(self.root, image=self.photonet,anchor=N, background="white", borderwidth=0, activebackground="white")
        f_lbl.place(x=200, y=0)



        # Lock Saving Account on Top
        Label(self.root, text="Lock Savings account", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # ===============================Main Body=======================================
        # Open Account Button
        open_account_btn = CTkButton(self.root,command=self.open_account, text="Open Account",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        open_account_btn.place(x=0, y=130)

        # Save Button
        save_btn = CTkButton(self.root,command=self.save, text="Save",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        save_btn.place(x=0, y=180)

        # Withdraw Button
        withdraw_btn = CTkButton(self.root,command=self.withdraw, text="Withdraw",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        withdraw_btn.place(x=0, y=230)

        # Check Balance Button
        check_balance_btn = CTkButton(self.root,command=self.check_balance, text="Check Balance",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        check_balance_btn.place(x=0, y=280)

        # Mini Statement Button
        mini_statement_btn = CTkButton(self.root,command=self.mini_statement, text="Mini Statement",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        mini_statement_btn.place(x=0, y=330)

        # ==================================Functions=========================================
    def open_account(self):
        # SendMoney(Toplevel(self.root))
        pass
    def save(self):
        # MainWithdraw(Toplevel(self.root))
        pass

    def withdraw(self):
        # BuyAirtime(Toplevel(self.root))
        pass

    def check_balance(self):
        pass

    def mini_statement(self):
        pass

    def back(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    LockSavingsAccount(root)
    root.mainloop()
