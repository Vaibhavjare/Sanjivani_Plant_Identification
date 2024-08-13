from tkinter import*
from PIL import Image,ImageTk

from tkinter import messagebox

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.config(bg="#BDFCC9")
        self.root.title("Sanjivani | Identifiction of medicinal plant")
        # self.bg=ImageTk.PhotoImage(file="111.jpg")
        # self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)



        
        def identification():
            self.root.destroy()
            import Sanjivani_dashboard

        def medicinal_plant():
            self.root.destroy()
            import Sanjivani_plant_info

        
       
        label_1=Label(text="IDENTIFICATION OF MEDICINAL PLANTS | SANJIVANI",font=("Times New Roman",25,"bold"),fg="black",bg="#BDFCC9").place(x=310,y=90)
        f1=Button(self.root,text="Identification of Plant",command=identification,font=("Arial",20,"bold"),fg="#DC143C",bg="#98F5FF",relief=SOLID,borderwidth=2).place(x=300,y=300,width=300,height=200)
        f2=Button(self.root,text="Medicinal Plant",command=medicinal_plant,font=("Arial",20,"bold"),fg="#DC143C",bg="#98F5FF",relief=SOLID,borderwidth=2).place(x=900,y=300,width=300,height=200)
        
    

root=Tk()
obj=IMS(root)
root.mainloop()