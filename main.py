from tkinter import*
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from time import strftime
from safaricom import Safaricom
from Mpesa import Mpesa


class Main():
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

        f_lbl = Button(self.root, image=self.photoimg,command=back, cursor="hand2", background="white", borderwidth=0, activebackground="white")
        f_lbl.place(x=5, y=70)

        #  network icon
        network_icon = Image.open(r"C:\Users\Flivian\PROJECTS\MPESA APPLICATION\images\battery.png")
        network_icon = network_icon.resize((150, 50))
        self.photonet = ImageTk.PhotoImage(network_icon)

        f_lbl = Label(self.root, image=self.photonet,anchor=N, background="white", borderwidth=0, activebackground="white")
        f_lbl.place(x=200, y=0)


        # Safaricon Name on Top
        Label(self.root, text="Safaricom", font=("Times New Roman", 16), background="white").place(x=60, y=68)
        
        # ================================end upper==========================================


        # Safaricom Button
        safaricom_btn = CTkButton(self.root,command=self.safaricom, text="Safaricom+",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        safaricom_btn.place(x=0, y=120)

        # Mpesa Button
        mpesa_btn = CTkButton(self.root,command=self.mpesa, text="M-PESA",text_color="black",width=360,border_width=0,corner_radius=0,
         fg_color="white", bg_color="white", font=("Bookman old Style", 17), hover_color="light gray", anchor=W, height=42)
        mpesa_btn.place(x=0, y=170)


    # ============================Function=================================================
    def safaricom(self):
        self.new = Toplevel(self.root)
        self.app = Safaricom(self.new)

    def mpesa(self):
        self.new = Toplevel(self.root)
        self.app = Mpesa(self.new)



if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()
