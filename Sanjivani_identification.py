from tkinter import*

from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile

import app as ap



class Login_System:
        def __init__(self,root):
                self.root=root
                self.root.title("Sanjivani")
                self.root.geometry("1600x900+0+0")
                self.root.config(bg="lightblue")
                # self.icon_title =ImageTk.PhotoImage(file ="side1.png")
                self.icon_title=ImageTk.PhotoImage(file="side1.png")
                
                # lbl_menu=Label(LeftMenu,text="Configuration",font=("Times New Roman",20,"bold"),bg="yellow").pack(side=TOP,fill=X)
                # btn_employee=Button(LeftMenu,text="Camera",image= self.icon_title,compound=LEFT,command=self.setup,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="Pink",bd=3,cursor="hand2")
                self.bg=ImageTk.PhotoImage(file="111.jpg")
                self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

                lbl_menu=Label(self.root,text="Detection of medicinal plant | Sanjivani",bg="#{:02x}{:02x}{:02x}".format(243, 251, 228),activebackground="#00B0F0",fg="Black",activeforeground="white",font=("Times New Roman",25,"bold")).place(x=750,y=80,width=600,height=50)
         
                
                title=Label(text='Upload Files',bg="#{:02x}{:02x}{:02x}".format(243, 251, 228),font=("times",30,"bold")).place(x=850,y=130,width=400,height=50)
                

                def upload_file():
                        
                        frame = Frame(self.root,bd=0,relief=RAISED,bg="#{:02x}{:02x}{:02x}".format(243, 251, 228))
                        frame.place(x=850,y=250,width=400,height=400)
                        global img
                        f_types = [('Jpg Files', '*.jpg')]
                        
                        global filename
                        filename = filedialog.askopenfilename(filetypes=f_types)
                        print(filename)
                        print(type(filename))
                        img=Image.open(filename)
                        img_resized=img.resize((400,400)) # new width & height
                        img=ImageTk.PhotoImage(img_resized)
                        b2 =Button(frame,image=img) # using Button 
                        b2.grid(row=3,column=1)
                        # self.lab=ap.det(filename)
                        # t1=Label(self.root,text=lab,bg="#{:02x}{:02x}{:02x}".format(243, 251, 228),font=("times",30,"bold")).place(x=850,y=30,width=400,height=50)

                        if(img !=""):
                                # proceed=Label(self.root,image=self.icon_title).place(x=1150,y=655,height=45,width=40)
                                btn_login1=Button(command=lambda:proceed(self), text="Proceed",font=("Arial Rounded MT Bold",17),bg="#00CD66",activebackground="#008B45",fg="Black",activeforeground="Black",cursor="hand2").place(x=950,y=655,width=200,height=45)
                        
                def proceed(self):    
                        # self.lab=ap.det(filename)
                        
                        # t1=Label(self.root,text=self.lab,bg="#{:02x}{:02x}{:02x}".format(243, 251, 228),font=("times",15,"bold")).place(x=850,y=730,width=400,height=50)
                        # print((list(self.lab))[0])

                        global path
                        path=ap.det(filename)
                        self.root.destroy()
                       
                        import Sanjivani_dashboard

                # proceed=Label(self.root,image=self.icon_title,background="#{:02x}{:02x}{:02x}".format(255,250,250)).place(x=1150,y=200,height=45,width=40)
                btn_login=Button(command=lambda:upload_file(),text="Browse",font=("Arial Rounded MT Bold",17),bg="#00CD66",activebackground="#008B45",fg="Black",activeforeground="Black",cursor="hand2").place(x=950,y=200,width=200,height=45)
               
                
root = Tk()
obj=Login_System(root)
root.mainloop() 