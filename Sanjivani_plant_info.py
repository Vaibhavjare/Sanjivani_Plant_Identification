from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,Tk
from tkinter import PhotoImage
from tkinter import messagebox
import mysql.connector

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Team Sanjivani")
        self.root.config(bg="#E0FFFF")


    # def pr1():
    #     self.root.destroy()
    #     import dashboard3

    
        # conn=mysql.connector.connect(host="localhost",user="root",passwd="Indra#123",database="Sanjivani")
        # mycusor=conn.cursor()
        
        
        entry = Entry(self.root, width=30,font=("goudy old style",20),bg="#A2B5CD")
        entry.pack(pady=20)
        search_symbol = Button(root, text="🔍", font=("Arial",20),bg="#A2B5CD").place(x=945,y=18,width=40,height=35)

        self.ashoka=PhotoImage(file='data/ashoka.png')
        
        br_box=Label(self.root,text="Ashoka",font=("Times New Roman",20,"bold"),fg="#308014",bg="#E0FFFF").place(x=250,y=370)
        border_box = Button(self.root,image=self.ashoka,relief=SOLID,borderwidth=2).place(x=150,y=150,width=300,height=200)


    
        self.alevera=PhotoImage(file='data/aleovera.png')
       
        br_box2=Label(self.root,text="Aloevera",font=("Times New Roman",20,"bold"),fg="#308014",bg="#E0FFFF").place(x=700,y=370)
        border_bx2 = Button(self.root,image=self.alevera,relief=SOLID,borderwidth=2).place(x=600,y=150,width=300,height=200)

        self.brambi=PhotoImage(file='data/brahmi.png')
        
        br_box3=Label(self.root,text="Brahmi",font=("Times New Roman",20,"bold"),fg="#308014",bg="#E0FFFF").place(x=1150,y=370)
        border_bx3 = Button(self.root,image=self.brambi,relief=SOLID,borderwidth=2).place(x=1050,y=150,width=300,height=200)

        self.betel=PhotoImage(file='data/betel.png')
        
        br_box=Label(self.root,text="Betel",font=("Times New Roman",20,"bold"),fg="#308014",bg="#E0FFFF").place(x=250,y=670)
        border_bx4 = Button(self.root,image=self.betel,relief=SOLID,borderwidth=2).place(x=150,y=450,width=300,height=200)
    
        self.mint=PhotoImage(file='data/mint.png')
        
        br_box=Label(self.root,text="Mint",font=("Times New Roman",20,"bold"),fg="#308014",bg="#E0FFFF").place(x=700,y=670)
        border_bx5 = Button(self.root,image=self.mint,relief=SOLID,borderwidth=2).place(x=600,y=450,width=300,height=200)
    
        self.tulsi=PhotoImage(file='data/tulsi.png')
        
        br_box=Label(self.root,text="Tulsi",font=("Times New Roman",20,"bold"),fg="#308014",bg="#E0FFFF").place(x=1150,y=670)
        border_bx6 = Button(self.root,image=self.tulsi,relief=SOLID,borderwidth=2).place(x=1050,y=450,width=300,height=200)
    
        self.arrow=PhotoImage(file="arrow.png")
        arrow_im1=Button(self.root,image=self.arrow).place(x=1400,y=700,width=100,height=50)
        



   



root=Tk()
obj=IMS(root)
root.mainloop()