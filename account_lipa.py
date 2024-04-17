from tkinter import*
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from time import strftime
import random as re
import string
from datetime import datetime



class AccountNoLipa():
    def __init__(self, root):
        self.root1 = root
        self.root1.title("")
        self.root1.geometry("350x550+500+50")
        self.root1.overrideredirect(1)
        self.root1.config(background="white")

        # =========================== Upper Part====================
        def time():
            string = strftime("%H:%M:%S")
            self.time.config(text=string)
            self.time.after(1000, time)
        # time label
        self.time = Label(self.root1, font=("Bookman Old Style", 15), background="white")
        self.time.place(x=5, y=17)
        time()

        # Image for thwe network And the Bettery percentage

        # icon for back ward
        back_icon = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\back arrow orignal.png")
        back_icon = back_icon.resize((40, 27))
        self.photoimg = ImageTk.PhotoImage(back_icon)

        def back():
            self.root1.destroy()

        back = Button(self.root1, image=self.photoimg,command=back, cursor="hand2", background="white", borderwidth=0, activebackground="white")
        back.place(x=5, y=68)

        # End session Icon
        end_session = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\end session1.png")
        end_session = end_session.resize((40, 40))
        self.end_session = ImageTk.PhotoImage(end_session)

        def end_session_command():
                close = CTkButton(self.root1, text="End Session",width=100,command=self.back, cursor="hand2",corner_radius=12,text_color="black", bg_color="white",fg_color="light gray",border_width=0, hover_color="light gray")
                close.place(x=230, y=95)

        end_session = Button(self.root1, image=self.end_session,command=end_session_command, cursor="hand2", background="white", borderwidth=0, activebackground="white")
        end_session.place(x=295, y=58)

        #  network icon
        network_icon = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\battery.png")
        network_icon = network_icon.resize((150, 50))
        self.photonet = ImageTk.PhotoImage(network_icon)

        f_lbl = Label(self.root1, image=self.photonet,anchor=N, background="white", borderwidth=0, activebackground="white")
        f_lbl.place(x=200, y=0)



        # Lipa na Mpesa For account Number on Top
        Label(self.root1, text="Lipa na M-PESA", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # Label to show user what to enter
        Label(self.root1, text="Enter Account No.", font=("Times New Roman", 16), background="white").place(x=80, y=148)

        # Entry Field for Phone number

        self.account_no_var = StringVar() #String variable to store Phone Number Entered by the user

        account_no = CTkEntry(self.root1, width=300, height=40,font=("Bookman Old Style", 20),textvariable=self.account_no_var, 
        border_width=0, fg_color="white", corner_radius=0, text_color="black")
        account_no.place(x=20, y=188)
        account_no.focus()
        # Label Iaccount_nodicator
        self.indicator_label = Label(self.root1, text="", font=("Times New Roman", 16), background="green")
        self.indicator_label.place(x=20, y=224, height=4, width=300)

        # Label to show instruction for the input
        Label(self.root1, text="Digits (0-9,*,#,+) 0 - 20", font=("Times New Roman", 12), background="white").place(x=20, y=234)

        # Cancel button
        cancel = CTkButton(self.root1, text="Cancel",width=130,command=self.cancel,height=35,font=("Bookman Old Style", 20),
         cursor="hand2",corner_radius=22,text_color="white", fg_color="black", hover_color="gray")
        cancel.place(x=20, y=310)

        # Ok button
        cancel = CTkButton(self.root1, text="OK",width=130,command=self.ok,height=35,font=("Bookman Old Style", 20),
         cursor="hand2",corner_radius=22,text_color="black", fg_color="green", hover_color="light green")
        cancel.place(x=190, y=310)



    def cancel(self):
        time.sleep(1)
        self.back()

    def ok(self):
        if self.account_no_var.get() ==  "":
            self.indicator_label.config(background="red")
        elif len(self.account_no_var.get()) > 20:
            self.indicator_label.config(background="red")
        elif len(self.account_no_var.get()) < 0:
            self.indicator_label.config(background="red")
        elif self.account_no_var.get().isdecimal() == False:
            self.indicator_label.config(background="red")
        else:
            account_no = self.account_no_var.get()
            Amount(Toplevel(self.root1), account_no)

    def back(self):
        self.root1.destroy()

# Enter Amount Class

class Amount():
    def __init__(self, root, account_no):
        self.root1 = root
        self.root1.title("")
        self.root1.geometry("350x550+500+50")
        self.root1.overrideredirect(1)
        self.root1.config(background="white")
        self.account_no = account_no

        # =========================== Upper Part====================
        def time():
            string = strftime("%H:%M:%S")
            self.time.config(text=string)
            self.time.after(1000, time)
        # time label
        self.time = Label(self.root1, font=("Bookman Old Style", 15), background="white")
        self.time.place(x=5, y=17)
        time()

        # Image for thwe network And the Bettery percentage

        # icon for back ward
        back_icon = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\back arrow orignal.png")
        back_icon = back_icon.resize((40, 27))
        self.photoimg = ImageTk.PhotoImage(back_icon)

        def back():
            self.root1.destroy()

        back = Button(self.root1, image=self.photoimg,command=back, cursor="hand2", background="white", borderwidth=0, activebackground="white")
        back.place(x=5, y=68)

        # End session Icon
        end_session = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\end session1.png")
        end_session = end_session.resize((40, 40))
        self.end_session = ImageTk.PhotoImage(end_session)

        def end_session_command():
                close = CTkButton(self.root1, text="End Session",width=100,command=self.back, cursor="hand2",corner_radius=12,text_color="black", bg_color="white",fg_color="light gray",border_width=0, hover_color="light gray")
                close.place(x=230, y=95)

        end_session = Button(self.root1, image=self.end_session,command=end_session_command, cursor="hand2", background="white", borderwidth=0, activebackground="white")
        end_session.place(x=295, y=58)

        #  network icon
        network_icon = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\battery.png")
        network_icon = network_icon.resize((150, 50))
        self.photonet = ImageTk.PhotoImage(network_icon)

        f_lbl = Label(self.root1, image=self.photonet,anchor=N, background="white", borderwidth=0, activebackground="white")
        f_lbl.place(x=200, y=0)



        # Safaricon Name on Top
        Label(self.root1, text="Lipa na M-PESA", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # Label to show user what to enter
        Label(self.root1, text="Enter Amount", font=("Times New Roman", 16), background="white").place(x=80, y=148)

        # Entry Field for AMount

        self.amount_var = StringVar()
        amount = CTkEntry(self.root1, width=300, height=40,font=("Bookman Old Style", 20), textvariable=self.amount_var, 
        border_width=0, fg_color="white", corner_radius=0, text_color="black")
        amount.place(x=20, y=188)
        amount.focus()
        # Label Indicator
        self.indicator_label = Label(self.root1, text="", font=("Times New Roman", 16), background="green")
        self.indicator_label.place(x=20, y=224, height=4, width=300)

        # Label to show instruction for the input
        Label(self.root1, text="Digits (0-9,*,#,+) 1 - 10", font=("Times New Roman", 12), background="white").place(x=20, y=234)

        # Cancel button
        cancel = CTkButton(self.root1, text="Cancel",width=130,command=self.cancel,height=35,font=("Bookman Old Style", 20),
         cursor="hand2",corner_radius=22,text_color="white", fg_color="black", hover_color="gray")
        cancel.place(x=20, y=310)

        # Ok button
        cancel = CTkButton(self.root1, text="OK",width=130,command=self.ok,height=35,font=("Bookman Old Style", 20),
         cursor="hand2",corner_radius=22,text_color="black", fg_color="green", hover_color="light green")
        cancel.place(x=190, y=310)



    def cancel(self):
        time.sleep(1)
        self.back()

    def ok(self):
        if self.amount_var.get() == "":
            self.indicator_label.config(background="red")
        elif len(self.amount_var.get()) > 10:
            self.indicator_label.config(background="red")
        elif int(self.amount_var.get()) < 5:
            self.indicator_label.config(background="red")
        elif self.amount_var.get().isdecimal() == False:
            self.indicator_label.config(background="red")
        else:
            account_no = self.account_no
            amount = self.amount_var.get()
            Pin(Toplevel(self.root1), account_no, amount)

    def back(self):
        self.root1.destroy()

# Mpesa Pin Class

class Pin():
    def __init__(self, root, account_no, amount):
        self.root1 = root
        self.root1.title("")
        self.root1.geometry("350x550+500+50")
        self.root1.overrideredirect(1)
        self.root1.config(background="white")
        self.account_no = account_no
        self.amount = amount
        self.actual_pin = 1234
        self.balance = 30000
        self.date = datetime.now()
        self.now = self.date.strftime("%Y-%m-%d at %H:%M:%S %p")

        # =========================== Upper Part====================
        def time():
            string = strftime("%H:%M:%S")
            self.time.config(text=string)
            self.time.after(1000, time)
        # time label
        self.time = Label(self.root1, font=("Bookman Old Style", 15), background="white")
        self.time.place(x=5, y=17)
        time()

        # Image for thwe network And the Bettery percentage

        # icon for back ward
        back_icon = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\back arrow orignal.png")
        back_icon = back_icon.resize((40, 27))
        self.photoimg = ImageTk.PhotoImage(back_icon)

        def back():
            self.root1.destroy()

        back = Button(self.root1, image=self.photoimg,command=back, cursor="hand2", background="white", borderwidth=0, activebackground="white")
        back.place(x=5, y=68)

        # End session Icon
        end_session = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\end session1.png")
        end_session = end_session.resize((40, 40))
        self.end_session = ImageTk.PhotoImage(end_session)

        def end_session_command():
                close = CTkButton(self.root1, text="End Session",width=100,command=self.back, cursor="hand2",corner_radius=12,text_color="black", bg_color="white",fg_color="light gray",border_width=0, hover_color="light gray")
                close.place(x=230, y=95)

        end_session = Button(self.root1, image=self.end_session,command=end_session_command, cursor="hand2", background="white", borderwidth=0, activebackground="white")
        end_session.place(x=295, y=58)

        #  network icon
        network_icon = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\battery.png")
        network_icon = network_icon.resize((150, 50))
        self.photonet = ImageTk.PhotoImage(network_icon)

        f_lbl = Label(self.root1, image=self.photonet,anchor=N, background="white", borderwidth=0, activebackground="white")
        f_lbl.place(x=200, y=0)



        # Safaricon Name on Top
        Label(self.root1, text="M-PESA", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # Label to show user what to enter
        Label(self.root1, text="Enter M-PESA PIN", font=("Times New Roman", 16), background="white").place(x=80, y=148)

        # Entry Field for Pin

        self.pin_var = StringVar()
        pin = CTkEntry(self.root1, width=300, height=40,font=("Bookman Old Style", 20), textvariable=self.pin_var,
        border_width=0, fg_color="white", corner_radius=0, text_color="black", show="*")
        pin.place(x=20, y=188)
        pin.focus()
        # Label Indicator
        self.indicator_label = Label(self.root1, text="", font=("Times New Roman", 16), background="green")
        self.indicator_label.place(x=20, y=224, height=4, width=300)

        # Label to show instruction for the input
        Label(self.root1, text="Digits (0-9,*,#,+) 4", font=("Times New Roman", 12), background="white").place(x=20, y=234)

        # Cancel button
        cancel = CTkButton(self.root1, text="Cancel",width=130,command=self.cancel,height=35,font=("Bookman Old Style", 20),
         cursor="hand2",corner_radius=22,text_color="white", fg_color="black", hover_color="gray")
        cancel.place(x=20, y=310)

        # Ok button
        cancel = CTkButton(self.root1, text="OK",width=130,command=self.ok,height=35,font=("Bookman Old Style", 20),
         cursor="hand2",corner_radius=22,text_color="black", fg_color="green", hover_color="light green")
        cancel.place(x=190, y=310)

        self.code = CTkLabel(self.root1, text="", font=("Bookman Old Style", 16),fg_color="white", anchor=W)
        self.code.place(x=10, y=380)


    def cancel(self):
        time.sleep(1)
        self.back()

    def ok(self):
        if self.pin_var.get() ==  "":
            self.indicator_label.config(background="red")
        elif len(self.pin_var.get()) > 4:
            self.indicator_label.config(background="red")
        elif self.pin_var.get().isdecimal() == False:
            self.indicator_label.config(background="red")
        else:
            if int(self.pin_var.get()) == self.actual_pin:
                self.code.configure(text="Processing....")
                time.sleep(2)
                accept = messagebox.askyesno(title="", message=f"    Send Money \n\n Send Money to {str(self.account_no)} kSH {self.amount}", parent=self.root1)
                if accept == False:
                    self.root1.destroy()
                else:
                    time.sleep(2)
                    mess = messagebox.askyesno(title="", message=f"    Send Money \n\nSent\nWait for M-PESA to reply", parent=self.root1)
                    if mess == False:
                        self.root1.quit
                    else:
                        time.sleep(2)
                        def generate_random(length):
                            characters = "R" + string.digits + string.ascii_uppercase

                            create_random = ''.join(re.choices(characters, k=length))
                            return create_random
                        length_str = 8
                        random = generate_random(length_str)
                        self.response = f"""RH{random} Confirmed, Ksh{self.amount}.00\n sent to Equity Paybill Account to Account {self.account_no} on
                        {self.now}.\nNew Mpesa balance is Ksh {self.balance - int(self.amount)}. 
                        Transaction cost, Ksh{0.003 * int(self.amount)}.\nThank you for chosing Mpesa"""
                        self.code.configure(text=f"{self.response}")
            else:
                messagebox.showerror(title="", message="Wrong M-PESA PIN Try Again!!", parent=self.root1)                
    def back(self):
        self.root1.destroy()


if __name__ == "__main__":
    root = Tk()
    AccountNoLipa(root)
    root.mainloop()