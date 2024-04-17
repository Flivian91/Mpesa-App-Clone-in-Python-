from tkinter import*
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from time import strftime
from business_no_lipa import BusinessNo
from buy_goods import BuyGoods
from pochi_la_biashara import PochiBiashara


class LipaNaMpesa():
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



        # Lipa Na Mpesa on Top
        Label(self.root, text="Lipa Na M-PESA", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # ===============================Main Body=======================================
        # pay bill Button
        pay_bill_btn = CTkButton(self.root,command=self.pay_bill, text="Pay Bill",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        pay_bill_btn.place(x=0, y=130)

        # Buy Goods and Services Button
        buy_good_btn = CTkButton(self.root,command=self.buy_good, text="Buy Goods and Services",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        buy_good_btn.place(x=0, y=180)

        # Pochi La biashara Button
        pochi_biashara_btn = CTkButton(self.root,command=self.pochi_biashara, text="Pochi La Biashara",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        pochi_biashara_btn.place(x=0, y=230)


        # ==================================Functions=========================================
    def pay_bill(self):
        PayBill(Toplevel(self.root))
        pass

    def buy_good(self):
        BuyGoods(Toplevel(self.root))

    def pochi_biashara(self):
        PochiBiashara(Toplevel(self.root))
        
    def back(self):
        self.root.destroy()


# !class to open New window Of paying Bill
class PayBill():
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



        # Lipa na Mpesa Option on Top
        Label(self.root, text="Lipa na M-PESA", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # ===============================Main Body=======================================
        # Search SIM Contacts Button
        search_contact_btn = CTkButton(self.root,command=self.search_contact, text="Search SIM Contacts",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        search_contact_btn.place(x=0, y=130)

        # Enter Business Numbers  Button
        business_no_btn = CTkButton(self.root,command=self.business_no, text="Business No",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        business_no_btn.place(x=0, y=180)


        # ==================================Functions=========================================
    def search_contact(self):
        SearchContact(Toplevel(self.root))
        
    def business_no(self):
        BusinessNo(Toplevel(self.root))
        pass

    def back(self):
        self.root.destroy()

# Class Seach Phone Number
class SearchContact():
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



        # Search Phone By Existing Contact on Top
        Label(self.root1, text="Lipa na M-PESA", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # Label to show user what to enter
        Label(self.root1, text="Enter name", font=("Times New Roman", 16), background="white").place(x=80, y=148)

        # Entry Field for Name

        self.name_var = StringVar()
        name = CTkEntry(self.root1, width=300, height=40,font=("Bookman Old Style", 20), textvariable=self.name_var, 
        border_width=0, fg_color="white", corner_radius=0, text_color="black")
        name.place(x=20, y=188)
        name.focus()
        # Label Indicator
        self.indicator_label = Label(self.root1, text="", font=("Times New Roman", 16), background="green")
        self.indicator_label.place(x=20, y=224, height=4, width=300)

        # Label to show instruction for the input
        Label(self.root1, text="Alphabets 0 - 10", font=("Times New Roman", 12), background="white").place(x=20, y=234)

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
        if self.name_var.get() ==  "":
            self.indicator_label.config(background="red")
        elif len(self.name_var.get()) > 20:
            self.indicator_label.config(background="red")
        elif len(self.name_var.get()) < 1:
            self.indicator_label.config(background="red")
        else:
            amount = self.name_var.get()
            # Pin(Toplevel(self.root1), amount)
            res = messagebox.askokcancel(title="", message="     Search SIM Contacts\n\n       No match ", parent=self.root1)
            if res == True:
                pass
            else:
                pass
    def back(self):
        self.root1.destroy()

if __name__ == "__main__":
    root = Tk()
    LipaNaMpesa(root)
    root.mainloop()
