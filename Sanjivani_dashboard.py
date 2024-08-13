# from tkinter import*
# from PIL import Image,ImageTk
from tkinter import*
from PIL import Image,ImageTk
from tkinter import font
import mysql.connector
from Sanjivani_identification import filename,path
print(path)



global col 
col="#{:02x}{:02x}{:02x}".format(243, 251, 228)

class IMS():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x800")
        self.root.title("Sanjivani | Identifiction of medicinal plant")
        self.root.config(bg=col)
        # self.bg=ImageTk.PhotoImage(file="111.jpg")
        # self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # self.pic = ImageTk.PhotoImage(file="spring.jpg")
        # l1 = Label(image=self.pic)
        # l1.pack()
        # LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="grey")
        # LeftMenu.place(x=0,y=37,width=360,height=900)

        
        custom_font = font.Font(family="Times New Roman", size=18, weight="bold", slant="italic")
        print(path)
        self.lab=path
        res=list(self.lab)
        con=str(res[-1])
        con=con[0:5]
        plant_name=res[0]
        print(plant_name)

        def back():

            self.root.destroy()
            import Sanjivani_iditification
            print("hi")

        def exit1():
            self.root.destroy()
            import Sanjivani_main
    
        # lbl_menu=Label(LeftMenu,text="Use Cases",font=("Times New Roman",20,"bold"),bg="Grey").pack(side=TOP)
        lbl_menu=Label(self.root,text="Detection of medicinal plant | Sanjivani",bg="#{:02x}{:02x}{:02x}".format(37,150,190),activebackground="#00B0F0",fg="white",activeforeground="white",font=("Times New Roman",25,"bold")).pack(side=TOP,fill=X)
               
        btn_6=Label(self.root,text="Biological Info",bg="#00FA9A",activeforeground="#4EEE94",font=("Times New Roman",20,"bold")).place(x=300,y=42,width=500,height=50)
        btn_7=Label(self.root,text="Description",bg="#00FA9A",activeforeground="#4EEE94",font=("Times New Roman",20,"bold")).place(x=810,y=42,width=780,height=50)
        frame7= Frame(self.root,bd=0,relief=RAISED,bg="#{:02x}{:02x}{:02x}".format(37,150,190))
        frame7.place(x=0,y=700,width=1600,height=100)
        btn_8=Button(frame7,text="Back",command=back,bg="#FFD700",activebackground="light blue",fg="black",activeforeground="white",font=("Times New Roman",20,"bold")).place(x=10,y=10,width=150,height=50)
        btn_9=Button(frame7,text="Exit",command=exit1,bg="#EE0000",activebackground="#CD0000",fg="black",activeforeground="white",font=("Times New Roman",20,"bold")).place(x=1350,y=10,width=150,height=50)

        

        # border frames
        frame2= Frame(self.root,bd=0,relief=RAISED,bg="black")
        frame2.place(x=800,y=42,width=10,height=300)
        
        frame3= Frame(self.root,bd=0,relief=RAISED,bg="black")
        frame3.place(x=310,y=342,width=10,height=358)
        
        frame4= Frame(self.root,bd=0,relief=RAISED,bg="black")
        frame4.place(x=630,y=342,width=10,height=358)

        frame5= Frame(self.root,bd=0,relief=RAISED,bg="black")
        frame5.place(x=950,y=342,width=10,height=358)

        frame6= Frame(self.root,bd=0,relief=RAISED,bg="black")
        frame6.place(x=1270,y=342,width=10,height=358)

         # image frame
        frame = Frame(self.root,bd=0,relief=RAISED,bg="white")
        frame.place(x=0,y=42,width=300,height=300)
        
        global img


        filename1= filename
        # blank frame
        fram1 = Frame(self.root,bd=0,relief=RAISED,bg=col)
        fram1.place(x=300,y=90,width=500,height=240)
        # filename1="images/brahmi.png"
        img=Image.open(filename1)
        img_resized=img.resize((300,300)) # new width & height
        img=ImageTk.PhotoImage(img_resized)
        b2 =Button(frame,image=img) # using Button 
        b2.grid(row=3,column=1)

        txt_ip41=Label(self.root,text=con,font=custom_font,bg=col).place(x=200,y=50,width=80,height=30)

        ## Bio_info
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.d=StringVar()
        self.advice=StringVar()
        self.loc=StringVar()
        self.classs=StringVar()
        self.uses=StringVar()
        # v-name 
        self.eng=StringVar()
        self.hin=StringVar()
        self.mar=StringVar()
        self.ass=StringVar()
        self.kan=StringVar()
        self.tel=StringVar()
        # classify
        self.classs=StringVar()
        #  M-use
        self.uses=StringVar()
        #  Advice
        self.advice=StringVar()
        # loc
        self.loc=StringVar()

        
        
        # custom_font = font.Font(family="Times New Roman", size=18, weight="bold", slant="italic")
        # self.lab=ap.det(filename)
        # res=list(self.lab)
        # plant_name=res[0]
        # print(plant_name)


        #   D BIOLOGICAL_INFO
        print("hi ",plant_name)
        mydb = mysql.connector.connect( host="localhost",user="root",password="Indra#123",database="sanjivani")
        mycursor = mydb.cursor()
        sql=("SELECT * FROM biological_info WHERE plant_name=%s")    
        val=("Ashoka",)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()

        # conn=mysql.connector.connect( host="localhost",user="root",passwd="Indra#123",database="Sanjivani")
        # mycur=conn.cursor()
        # sql=("SELECT * FROM biological_info WHERE plant_name=%s") 
        # val=(plant_name,)
        # mycur.execute(sql,val)
        # myres=mycur.fetchall()
        # print(myres)
        
        # print(myresult)
        myresult=list(myresult[0])
        # print(myresult)
        
        # D VARIABLE BIO
        self.s_name=myresult[1]
        self.cls=myresult[2]
        self.family=myresult[3]
        self.des=myresult[4]
        
        txt_ip41=Label(self.root,text=con,font=custom_font,bg=col).place(x=200,y=50,width=80,height=30)

        lbl_ip1=Label(self.root,text="Common Name :-",font=custom_font,bg=col).place(x=320,y=100)
        txt_ip1=Label(self.root,text=plant_name,font=custom_font,bg=col).place(x=500,y=105,width=250,height=30)

        lbl_ip2=Label(self.root,text="Scientific Name :-",font=custom_font,bg=col).place(x=320,y=165)
        txt_ip2=Label(self.root,text=self.s_name,font=custom_font,bg=col).place(x=500,y=170,width=250,height=30)

        lbl_ip3=Label(self.root,text="Class :-",font=custom_font,bg=col).place(x=390,y=230)
        txt_ip3=Label(self.root,text=self.cls,font=custom_font,bg=col).place(x=500,y=235,width=250,height=30)

        lbl_ip4=Label(self.root,text="Family :-",font=custom_font,bg=col).place(x=390,y=295)
        txt_ip4=Label(self.root,text=self.family,font=custom_font,bg=col).place(x=500,y=300,width=250,height=30)


        custom_font = font.Font(family="Times New Roman", size=15, weight="bold", slant="italic")
        
        #description

        text_widget1 = Text(root, wrap=WORD,bg=col, width=100, height=100)
        text_widget1.place(x=810,y=90,width=720,height=250)
        text_widget1.config(font=custom_font)
        text_widget1.insert(END, self.des)


        def classif():
                    mydb = mysql.connector.connect( host="localhost",user="root",password="Indra#123",database="sanjivani")
                    mycursor = mydb.cursor()
                    sql=("SELECT * FROM med_plant_info WHERE plant_name=%s") 
                    val=(plant_name,)   
                    mycursor.execute(sql,val)
                    myresult = mycursor.fetchall()
                    myresult=list(myresult[0])
                    self.advice =myresult[-2]
                    self.classs =myresult[-2]
                    text_widget5 = Text(root, wrap=WORD,bg=col, width=100, height=100)
                    text_widget5.place(x=960,y=390,width=310,height=307)
                    text_widget5.config(font=custom_font)
                    text_widget5.insert(END,self.classs)
        

        def v_name():
            mydb = mysql.connector.connect( host="localhost",user="root",password="Indra#123",database="sanjivani")
            mycursor = mydb.cursor()
            sql=("SELECT * FROM vernacular_names WHERE plant_name=%s")    
            plant=plant_name
            val=(plant,)
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()
            myresult=list(myresult[0])
            
            #D V-NAME VARIBALE
            self.eng=myresult[1]
            self.hin=myresult[2]
            self.mar=myresult[3]
            self.ass=myresult[4]
            self.kan=myresult[5]
            self.tel=myresult[6]

            custom_font1 = font.Font(family="Times New Roman", size=17, weight="bold", slant="italic")

            lbl_ip1=Label(self.root,text="English :-",font=custom_font1,bg=col).place(x=340,y=400)
            txt_ip1=Label(self.root,text=self.eng,font=custom_font1,bg=col).place(x=440,y=400,width=150,height=30)

            lbl_ip2=Label(self.root,text="Hindi :-",font=custom_font1,bg=col).place(x=340,y=445)
            txt_ip2=Label(self.root,text=self.hin,font=custom_font1,bg=col).place(x=440,y=445,width=150,height=30)

            lbl_ip3=Label(self.root,text="Marathi:-",font=custom_font1,bg=col).place(x=340,y=490)
            txt_ip3=Label(self.root,text=self.mar,font=custom_font1,bg=col).place(x=440,y=490,width=150,height=30)

            lbl_ip4=Label(self.root,text="Assamese:-",font=custom_font1,bg=col).place(x=340,y=535)
            txt_ip4=Label(self.root,text=self.ass,font=custom_font1,bg=col).place(x=440,y=535,width=150,height=30)

            lbl_ip5=Label(self.root,text="Kannada :-",font=custom_font1,bg=col).place(x=340,y=580)
            txt_ip5=Label(self.root,text=self.kan,font=custom_font1,bg=col).place(x=440,y=580,width=150,height=30)

            lbl_ip6=Label(self.root,text="Telugu :-",font=custom_font1,bg=col).place(x=340,y=625)
            txt_ip6=Label(self.root,text=self.tel,font=custom_font1,bg=col).place(x=440,y=625,width=150,height=30)

            # lbl_ip7=Label(self.root,text="Bengali :-",font=custom_font1,bg=col).place(x=340,y=670)
            # txt_ip7=Label(self.root,text=self.b,font=custom_font1,bg=col).place(x=440,y=670,width=1500,height=30)

        


        def medical():
            
            
            mydb = mysql.connector.connect( host="localhost",user="root",password="Indra#123",database="sanjivani")
            mycursor = mydb.cursor()
            sql=("SELECT * FROM medicinal_use WHERE plant_name=%s")    
            val=(plant_name,)
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()
            myresult=list(myresult[0])
            self.uses =myresult[-1]
            text_widget4 = Text(root, wrap=WORD,bg=col, width=100, height=100)
            text_widget4.place(x=640,y=390,width=310,height=307)
            text_widget4.config(font=custom_font)
            text_widget4.insert(END, self.uses)
            

        # def con_advice():

            # mydb = mysql.connector.connect( host="localhost",user="root",password="Indra#123",database="sih")
            # mycursor = mydb.cursor()
            # sql=("SELECT * FROM med_plant_info WHERE plant_name=%s")  
             
            # val=(plant_name,)
            # mycursor.execute(sql,val)
            # myresult = mycursor.fetchall()
            # myresult=list(myresult[0])
            # self.advice =myresult[-2]
            
            # text_widget5 = Text(root, wrap=WORD,bg=col, width=100, height=100)
            # text_widget5.place(x=960,y=390,width=310,height=307)
            # text_widget5.config(font=custom_font)
            # text_widget5.insert(END,self.advice)

        def location():

            mydb = mysql.connector.connect( host="localhost",user="root",password="Indra#123",database="sanjivani")
            mycursor = mydb.cursor()
            sql=("SELECT * FROM med_plant_info WHERE plant_name=%s")    
            val=(plant_name,)
            mycursor.execute(sql,val)
            myresult = mycursor.fetchall()
            myresult=list(myresult[0])
            # print(myresult)
            self.loc =myresult[-1]
            text_widget6 = Text(root, wrap=WORD,bg=col, width=100, height=100)
            text_widget6.place(x=1280,y=390,width=238,height=307)
            text_widget6.config(font=custom_font)
            text_widget6.insert(END,self.loc)


        #bio_info
        btn_1=Button(self.root,text="Medicinal Classification",command=classif,bg="#00FA9A",activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",20,"bold")).place(x=0,y=342,width=310,height=50)
        btn_2=Button(self.root,text="Vernacular Names",command=v_name,bg="#00FA9A",activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",20,"bold")).place(x=320,y=342,width=310,height=50)
        btn_3=Button(self.root,text="Medical Use",command=medical,bg="#00FA9A",activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",20,"bold")).place(x=640,y=342,width=310,height=50)

        btn_4=Button(self.root,text="Conservative Advices",command=classif,bg="#00FA9A",activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",20,"bold")).place(x=960,y=342,width=310,height=50)
        btn_5=Button(self.root,text="Location",command=location,bg="#00FA9A",activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",20,"bold")).place(x=1280,y=342,width=310,height=50)

        self.frame8= Frame(self.root,bd=0,relief=RAISED,bg=col)
        self.frame8.place(x=0,y=342,width=310,height=360)
        def back2():
            self.frame9.destroy()

        def flower():
            self.frame9= Frame(self.root,bd=0,relief=RAISED,bg=col)
            self.frame9.place(x=320,y=92,width=650,height=605)
            btn_14=Button(self.frame9,text="Back",bg="#00FA9A",command=back2,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",15,"bold")).place(x=5,y=560,width=60,height=30)
        
            self.icon_btn_supplier = PhotoImage(file="images/AF1.png")
            self.btn_supplier=Label(self.frame9,image=self.icon_btn_supplier).place(x=0,y=0)
    
            self.icon_btn_supplier1 = PhotoImage(file="images/AF2.png")
            self.btn_supplier1=Label(self.frame9,image=self.icon_btn_supplier1).place(x=320,y=0)

            self.icon_btn_supplier2 = PhotoImage(file="images/AF3.png")
            self.btn_supplier2=Label(self.frame9,image=self.icon_btn_supplier2).place(x=0,y=270)
            
            self.icon_btn_supplier3 = PhotoImage(file="images/AF4.png")
            self.btn_supplier3=Label(self.frame9,image=self.icon_btn_supplier3).place(x=320,y=270)
            btn_14=Button(self.frame9,text="Next",bg="#00FA9A",command=back2,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",15,"bold")).place(x=550,y=560,width=60,height=30)


        def result():
            self.frame9= Frame(self.root,bd=0,relief=RAISED,bg=col)
            self.frame9.place(x=320,y=92,width=650,height=605)
            btn_14=Button(self.frame9,text="Back",bg="#00FA9A",command=back2,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",15,"bold")).place(x=5,y=560,width=60,height=30)

            self.icon_btn_supplier = PhotoImage(file="images/AA1.png")
            self.btn_supplier=Label(self.frame9,image=self.icon_btn_supplier).place(x=0,y=0)
    
            self.icon_btn_supplier1 = PhotoImage(file="images/AA2.png")
            self.btn_supplier1=Label(self.frame9,image=self.icon_btn_supplier1).place(x=320,y=0)

            self.icon_btn_supplier2 = PhotoImage(file="images/AA3.png")
            self.btn_supplier2=Label(self.frame9,image=self.icon_btn_supplier2).place(x=0,y=270)
            
            self.icon_btn_supplier3 = PhotoImage(file="images/AA4.png")
            self.btn_supplier3=Label(self.frame9,image=self.icon_btn_supplier3).place(x=320,y=270)

            btn_14=Button(self.frame9,text="Next",bg="#00FA9A",command=back2,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",15,"bold")).place(x=550,y=560,width=60,height=30)

    
        def result1():
            
            pass
           
            # self.frame9= Frame(self.root,bd=0,relief=RAISED,bg=col)
            # self.frame9.place(x=320,y=92,width=650,height=605)
            # btn_14=Button(self.frame9,text="Back",bg="#00FA9A",command=back2,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",15,"bold")).place(x=5,y=560,width=60,height=30)
            
            
            # self.icon_btn_supplier = PhotoImage(file="images/AF1.png")
            # self.btn_supplier=Label(self.frame9,image=self.icon_btn_supplier).place(x=0,y=0)
    
            # self.icon_btn_supplier1 = PhotoImage(file="images/AF2.png")
            # self.btn_supplier1=Label(self.frame9,image=self.icon_btn_supplier1).place(x=320,y=0)

            # self.icon_btn_supplier2 = PhotoImage(file="images/AF3.png")
            # self.btn_supplier2=Label(self.frame9,image=self.icon_btn_supplier2).place(x=0,y=270)
            
            # self.icon_btn_supplier3 = PhotoImage(file="images/AF4.png")
            # self.btn_supplier3=Label(self.frame9,image=self.icon_btn_supplier3).place(x=320,y=270)
            # btn_14=Button(self.frame9,text="Next",bg="#00FA9A",command=back2,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",15,"bold")).place(x=550,y=560,width=60,height=30)

        def fruits():
            
            pass
            
            # self.frame9= Frame(self.root,bd=0,relief=RAISED,bg=col)
            # self.frame9.place(x=320,y=92,width=650,height=605)
            # btn_14=Button(self.frame9,text="Back",bg="#00FA9A",command=back2,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",15,"bold")).place(x=5,y=560,width=60,height=30)
            # self.icon_btn_supplier = PhotoImage(file="images/AF1.png")
            # self.btn_supplier=Label(self.frame9,image=self.icon_btn_supplier).place(x=0,y=0)
    
            # self.icon_btn_supplier1 = PhotoImage(file="images/AF2.png")
            # self.btn_supplier1=Label(self.frame9,image=self.icon_btn_supplier1).place(x=320,y=0)

            # self.icon_btn_supplier2 = PhotoImage(file="images/AF3.png")
            # self.btn_supplier2=Label(self.frame9,image=self.icon_btn_supplier2).place(x=0,y=270)
            
            # self.icon_btn_supplier3 = PhotoImage(file="images/AF4.png")
            # self.btn_supplier3=Label(self.frame9,image=self.icon_btn_supplier3).place(x=320,y=270)
            # btn_14=Button(self.frame9,text="Next",bg="#00FA9A",command=back2,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",15,"bold")).place(x=550,y=560,width=60,height=30)



        btn_10=Button(self.frame8,text="Similar Results",bg="#00FA9A",command=result,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",20,"bold")).place(x=10,y=30,width=250,height=50)
        btn_11=Button(self.frame8,text="Roots",bg="#00FA9A",command=result1,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",20,"bold")).place(x=10,y=100,width=250,height=50)
        btn_12=Button(self.frame8,text="Fruit",bg="#00FA9A",command=fruits,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",20,"bold")).place(x=10,y=170,width=250,height=50)
        btn_13=Button(self.frame8,text="Flower",bg="#00FA9A",command=flower,activebackground="#4EEE94",fg="Black",activeforeground="Black",font=("Times New Roman",20,"bold")).place(x=10,y=250,width=250,height=50)
        
        
        
root=Tk()
obj=IMS(root)
root.mainloop()







