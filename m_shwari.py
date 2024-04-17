from tkinter import*
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from time import strftime
from send_mshwari import AmountSend
from withdraw_mshwari import AmountWithdraw
from lock_savings_account import LockSavingsAccount
from loan_offer import LoanOffer
from check_balance import Pin
from mini_statement_loan import MiniStatement

class Mshwari():
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



        # M-shwari on Top
        Label(self.root, text="M-Shwari", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # ===============================Main Body=======================================
        # Send To M-Shwari Button
        send_mshwari_btn = CTkButton(self.root,command=self.send_mshwari, text="Send to M-Shwari",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        send_mshwari_btn.place(x=0, y=130)

        # Withdraw from Mshwari Button
        withdraw_mshwari_btn = CTkButton(self.root,command=self.withdraw_mshwari, text="Withdraw from M-Shwari",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        withdraw_mshwari_btn.place(x=0, y=180)

        # Lock Savings Account Button
        lock_savings_btn = CTkButton(self.root,command=self.lock_savings, text="Lock Savings Account",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        lock_savings_btn.place(x=0, y=230)

        # Loan @ 9% for 30 days Button
        loan_btn = CTkButton(self.root,command=self.loan, text="Loan @ 9% for 30 days",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        loan_btn.place(x=0, y=280)

        # Check Balance Button
        check_balance_btn = CTkButton(self.root,command=self.check_balance, text="Check Balance",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        check_balance_btn.place(x=0, y=330)

        # Mini Statement Button
        mini_statement_btn = CTkButton(self.root,command=self.mini_statement, text="Mini Statement",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        mini_statement_btn.place(x=0, y=380)



        # ==================================Functions=========================================
    def send_mshwari(self):
        AmountSend(Toplevel(self.root))

    def withdraw_mshwari(self):
        AmountWithdraw(Toplevel(self.root))

    def lock_savings(self):
        LockSavingsAccount(Toplevel(self.root))

    def loan(self):
        LoanOffer(Toplevel(self.root))

    def check_balance(self):
        Pin(Toplevel(self.root))

    def mini_statement(self):
        MiniStatement(Toplevel(self.root))

    def back(self):
        self.root.destroy()
        
if __name__ == "__main__":
    root = Tk()
    Mshwari(root)
    root.mainloop()
