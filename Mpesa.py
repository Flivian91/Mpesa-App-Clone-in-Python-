from tkinter import*
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from time import strftime
from send_money import SendMoney
from withdraw_cash import MainWithdraw
from buy_airtime import BuyAirtime
from loan_savings import LoanSavings
from lipa_na_mpesa import LipaNaMpesa


class Mpesa():
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



        # Mpesa Word on Top
        Label(self.root, text="M-PESA", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # ===============================Main Body=======================================
        # Send Money Button
        send_money_btn = CTkButton(self.root,command=self.send_money, text="Send Money",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        send_money_btn.place(x=0, y=130)

        # Withdraw Cash Button
        withdraw_cash_btn = CTkButton(self.root,command=self.withdraw_cash, text="Withdraw Cash",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        withdraw_cash_btn.place(x=0, y=180)

        # Buy Airtime Button
        buy_airtime_btn = CTkButton(self.root,command=self.buy_airtime, text="Buy Airtime",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        buy_airtime_btn.place(x=0, y=230)

        # Loan And Saving Button
        loan_and_saving_btn = CTkButton(self.root,command=self.loan_and_saving, text="Loan And Savings",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        loan_and_saving_btn.place(x=0, y=280)

        # Lipa na Mpesa Button
        lipa_na_mpesa_btn = CTkButton(self.root,command=self.lipa_na_mpesa, text="Lipa na M-PESA",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        lipa_na_mpesa_btn.place(x=0, y=330)

        # My Account Button
        account_btn = CTkButton(self.root,command=self.account, text="My Account",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        account_btn.place(x=0, y=380)

        # ==================================Functions=========================================
    def send_money(self):
        SendMoney(Toplevel(self.root))

    def withdraw_cash(self):
       MainWithdraw(Toplevel(self.root))

    def buy_airtime(self):
      BuyAirtime(Toplevel(self.root))

    def loan_and_saving(self):
        LoanSavings(Toplevel(self.root))

    def lipa_na_mpesa(self):
        LipaNaMpesa(Toplevel(self.root))

    def account(self):
        pass

    def back(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    Mpesa(root)
    root.mainloop()
