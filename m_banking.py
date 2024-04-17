from tkinter import*
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from time import strftime


class Bank():
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



        # M-banking services on Top
        Label(self.root, text="My Account", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # ===============================Main Body=======================================
        # Barclay Bank Button
        barclays_bank = CTkButton(self.root,command=self.barclays_bank, text="Barclays Bank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        barclays_bank.place(x=0, y=120)

        # co-op Bank Button
        co_op_bank_btn = CTkButton(self.root,command=self.co_op_bank, text="Co-op Bank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        co_op_bank_btn.place(x=0, y=160)

        # DTB Bank Button
        dtb_bank_btn = CTkButton(self.root,command=self.dtb_bank, text="DTB",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        dtb_bank_btn.place(x=0, y=200)

        # Ecobank Button
        ecobank_btn = CTkButton(self.root,command=self.ecobank, text="Ecobank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        ecobank_btn.place(x=0, y=240)

        #  Equity bank Button
        equity_bank_btn = CTkButton(self.root,command=self.equity_bank, text="Equity Bank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        equity_bank_btn.place(x=0, y=280)

        #  Equity bank Button
        family_bank = CTkButton(self.root,command=self.family_bank, text="Family Bank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        family_bank.place(x=0, y=320)
        
        #  Faulu DTM Button
        faulu_dtm_btn = CTkButton(self.root,command=self.faulu_dtm, text="Faulu DTM",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        faulu_dtm_btn.place(x=0, y=360)

        #  First Community Button
        first_community = CTkButton(self.root,command=self.first_community, text="First Community",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        first_community.place(x=0, y=400)

        #  I_m Bank Button
        i_m_bank_btn = CTkButton(self.root,command=self.i_m_bank, text="I&M Bank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        i_m_bank_btn.place(x=0, y=440)
        
        #  More  Button
        more_btn = CTkButton(self.root,command=self.more, text="More ,,,",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        more_btn.place(x=0, y=480)

        # ==================================Functions=========================================
    def barclays_bank(self):
        pass

    def co_op_bank(self):
        pass

    def dtb_bank(self):
        pass

    def ecobank(self):
        pass

    def equity_bank(self):
        pass

    def family_bank(self):
        pass

    def faulu_dtm(self):
        pass

    def first_community(self):
        pass

    def i_m_bank(self):
        pass

    def more(self):
        More(Toplevel(self.root))


    def back(self):
        self.root.destroy()


# New Window to display More
class More():
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



        # M-banking services on Top
        Label(self.root, text="More ,,,", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================

        # ===============================Main Body=======================================
        # KCB Bank Button
        kcb_bank_btn = CTkButton(self.root,command=self.kcb_bank, text="KCB",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        kcb_bank_btn.place(x=0, y=120)

        # KWFT Bank Button
        kwft_btn = CTkButton(self.root,command=self.kwft, text="KWFT",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        kwft_btn.place(x=0, y=160)

        # m-sacco Button
        m_sacco_btn = CTkButton(self.root,command=self.m_sacco, text="M-SACCO",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        m_sacco_btn.place(x=0, y=200)

        # National Bank Button
        national_bank_btn = CTkButton(self.root,command=self.national_bank, text="National Bank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        national_bank_btn.place(x=0, y=240)

        #  NIC bank Button
        nic_bank_btn = CTkButton(self.root,command=self.nic_bank, text="NIC Bank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        nic_bank_btn.place(x=0, y=280)

        #  Post bank Button
        post_bank_btn = CTkButton(self.root,command=self.post_bank, text="Post Bank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        post_bank_btn.place(x=0, y=320)
        
        #  SBM Button
        sbm_bank_btn = CTkButton(self.root,command=self.sbm_bank, text="SBM Bank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        sbm_bank_btn.place(x=0, y=360)

        #  Sidian Bank Button
        sidian_bank_btn = CTkButton(self.root,command=self.sidian_bank, text="Sidian Bank",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        sidian_bank_btn.place(x=0, y=400)

        #  Standard Bank Button
        standard_btn = CTkButton(self.root,command=self.standard, text="Standard Chartered",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        standard_btn.place(x=0, y=440)
        
        # ==================================Functions=========================================
    def kcb_bank(self):
        pass

    def kwft(self):
        pass

    def m_sacco(self):
        pass

    def national_bank(self):
        pass

    def nic_bank(self):
        pass

    def post_bank(self):
        pass

    def sbm_bank(self):
        pass

    def sidian_bank(self):
        pass

    def standard(self):
        pass

    def back(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    Bank(root)
    root.mainloop()
