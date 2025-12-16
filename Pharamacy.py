from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        
#=============================================================================

        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("D:/pharma/logo.jpg")
        img1=img1.resize((80,80),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=20)

#============== DATA FRAME =================================
        
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        

#============ BUTTON FRAME =================================
        
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

#======================== MEDICINE ADD DATABASE ========= MEDICINE INFORMATION ===============
      
        #========= ADD MEDICINE BUTTON ============== MEDICINE INFORMATION =====
        def MedAddInfo():
                try:
                        ref=ref_combo.get()
                        cmp=txtCmp.get()
                        tmed=tom_combo.get()
                        medname=MedName_combo.get()
                        lot=txtLotNo.get()
                        issue=txtIssuDt.get()
                        exp=txtExpDt.get()
                        uses=txtUse.get()
                        side=txtSideEffect.get()
                        prec=txtPre.get()
                        dos=txtDos.get()
                        tprice=txtTbp.get()
                        proq=txtProq.get()

                        if (cmp=="" or lot==""):
                                ref_combo.focus()
                                messagebox.showinfo("Insert Status","All Fields Are Required")
                        elif (issue=="" or exp==""):
                                ref_combo.focus()
                                messagebox.showinfo("Insert Status","All Fields Are Required")
                        elif (uses=="" or side==""):
                                ref_combo.focus()
                                messagebox.showinfo("Insert Status","All Fields Are Required")
                        elif (prec=="" or dos==""):
                                ref_combo.focus()
                                messagebox.showinfo("Insert Status","All Fields Are Required")
                        elif (tprice=="" or proq==""):
                                ref_combo.focus()
                                messagebox.showinfo("Insert Status","All Fields Are Required")
                        else:
                                prompt1=messagebox.askyesno('Confirmation','Are You Confirm For INSERT Medicine ?')

                                if prompt1:
                                        con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                                        c1=con.cursor()
                                        c1.execute("insert into medinfo values('"+ ref +"','"+ cmp +"','"+ tmed +"','"+ medname +"','"+ lot +"','"+ issue +"','"+ exp +"','"+ uses +"','"+ side +"','"+ prec +"','"+ dos +"','"+ tprice +"','"+ proq +"')")

                                        vals=(ref,cmp,tmed,medname,lot,issue,exp,uses,side,prec,dos,tprice,proq)
                                        trv2.insert('',END,values=vals)

                                        ref_combo.delete(0,END)
                                        txtCmp.delete(0,END)
                                        tom_combo.delete(0,END)
                                        MedName_combo.delete(0,END)
                                        txtLotNo.delete(0,END)
                                        txtIssuDt.delete(0,END)
                                        txtExpDt.delete(0,END)
                                        txtUse.delete(0,END)
                                        txtSideEffect.delete(0,END)
                                        txtPre.delete(0,END)
                                        txtDos.delete(0,END)
                                        txtTbp.delete(0,END)
                                        txtProq.delete(0,END)

                                        c1.execute("commit")
                                        ref_combo.focus()
                                        messagebox.showinfo("Insert Status","Inserted Successfully")
                                        c1.close()
                                else:
                                        ref_combo.delete(0,END)
                                        txtCmp.delete(0,END)
                                        tom_combo.delete(0,END)
                                        MedName_combo.delete(0,END)
                                        txtLotNo.delete(0,END)
                                        txtIssuDt.delete(0,END)
                                        txtExpDt.delete(0,END)
                                        txtUse.delete(0,END)
                                        txtSideEffect.delete(0,END)
                                        txtPre.delete(0,END)
                                        txtDos.delete(0,END)
                                        txtTbp.delete(0,END)
                                        txtProq.delete(0,END)

                                        ref_combo.focus()
                                        messagebox.showerror('Cancel','Cancel Successfully')
                except Exception as e:
                        if "Duplicate entry" in str(e):
                                messagebox.showwarning("ERROR","Reference No Already Exists In The Table")
                        else:
                                print("Error Occured",e)


        #======== UPDATE MEDICINE BUTTON =========== MEDICINE INFORMATION =========
        def MedUpdInfo():
                ref=ref_combo.get()
                cmp=txtCmp.get()
                tmed=tom_combo.get()
                medname=MedName_combo.get()
                lot=txtLotNo.get()
                issue=txtIssuDt.get()
                exp=txtExpDt.get()
                uses=txtUse.get()
                side=txtSideEffect.get()
                prec=txtPre.get()
                dos=txtDos.get()
                tprice=txtTbp.get()
                proq=txtProq.get()

                if (cmp=="" or lot==""):
                        ref_combo.focus()
                        messagebox.showinfo("Insert Status","All Fields Are Required")
                elif (issue=="" or exp==""):
                        ref_combo.focus()
                        messagebox.showinfo("Insert Status","All Fields Are Required")
                elif (uses=="" or side==""):
                        ref_combo.focus()
                        messagebox.showinfo("Insert Status","All Fields Are Required")
                elif (prec=="" or dos==""):
                        ref_combo.focus()
                        messagebox.showinfo("Insert Status","All Fields Are Required")
                elif (tprice=="" or proq==""):
                        ref_combo.focus()
                        messagebox.showinfo("Insert Status","All Fields Are Required")
                else:
                        prompt2=messagebox.askyesno('Confirmtion','Are You Confirm For UPDATE Medicine ?')

                        if prompt2:
                                con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                                c1=con.cursor()
                                c1.execute("update medinfo set cmp='"+ cmp +"',tmed='"+ tmed +"',medname='"+ medname +"',lot='"+ lot +"',issue='"+ issue +"',exp='"+ exp +"',uses='"+ uses +"',side='"+ side +"',prec='"+ prec +"',dos='"+ dos +"',tprice='"+ tprice +"',proq='"+ proq +"'where ref='"+ ref +"' ")
                        
                                SelectedItem=trv2.selection()[0]
                                vals=(ref,cmp,tmed,medname,lot,issue,exp,uses,side,prec,dos,tprice,proq)
                                trv2.item(SelectedItem,values=vals)

                                ref_combo.delete(0,END)
                                txtCmp.delete(0,END)
                                tom_combo.delete(0,END)
                                MedName_combo.delete(0,END)
                                txtLotNo.delete(0,END)
                                txtIssuDt.delete(0,END)
                                txtExpDt.delete(0,END)
                                txtUse.delete(0,END)
                                txtSideEffect.delete(0,END)
                                txtPre.delete(0,END)
                                txtDos.delete(0,END)
                                txtTbp.delete(0,END)
                                txtProq.delete(0,END)

                                c1.execute("commit")
                                ref_combo.focus()
                                messagebox.showinfo("Update Status","Updated Successfully")
                                c1.close()
                        else:
                                ref_combo.delete(0,END)
                                txtCmp.delete(0,END)
                                tom_combo.delete(0,END)
                                MedName_combo.delete(0,END)
                                txtLotNo.delete(0,END)
                                txtIssuDt.delete(0,END)
                                txtExpDt.delete(0,END)
                                txtUse.delete(0,END)
                                txtSideEffect.delete(0,END)
                                txtPre.delete(0,END)
                                txtDos.delete(0,END)
                                txtTbp.delete(0,END)
                                txtProq.delete(0,END)

                                ref_combo.focus()
                                messagebox.showerror('Cancel','Cancel Successfully')

        #=========== DELETE MEDICINE BUTTON ============ MEDICINE INFORMATION ===========
        def MedDelInfo():
                ref=ref_combo.get()
                cmp=txtCmp.get()
                tmed=tom_combo.get()
                medname=MedName_combo.get()
                lot=txtLotNo.get()
                issue=txtIssuDt.get()
                exp=txtExpDt.get()
                uses=txtUse.get()
                side=txtSideEffect.get()
                prec=txtPre.get()
                dos=txtDos.get()
                tprice=txtTbp.get()
                proq=txtProq.get()

                if (cmp=="" or lot==""):
                        ref_combo.focus()
                        messagebox.showinfo("Insert Status","All Fields Are Required")
                elif (issue=="" or exp==""):
                        ref_combo.focus()
                        messagebox.showinfo("Insert Status","All Fields Are Required")
                elif (uses=="" or side==""):
                        ref_combo.focus()
                        messagebox.showinfo("Insert Status","All Fields Are Required")
                elif (prec=="" or dos==""):
                        ref_combo.focus()
                        messagebox.showinfo("Insert Status","All Fields Are Required")
                elif (tprice=="" or proq==""):
                        ref_combo.focus()
                        messagebox.showinfo("Insert Status","All Fields Are Required")
                else:
                        prompt3=messagebox.askyesno('Confirmation','Are You Confirm For DELETE Medicine')

                        if prompt3:
                                con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                                c1=con.cursor()
                                c1.execute("delete from medinfo")

                                SelectedItem=trv2.selection()[0]
                                trv2.delete(SelectedItem)
                                ref_combo.delete(0,END)
                                txtCmp.delete(0,END)
                                tom_combo.delete(0,END)
                                MedName_combo.delete(0,END)
                                txtLotNo.delete(0,END)
                                txtIssuDt.delete(0,END)
                                txtExpDt.delete(0,END)
                                txtUse.delete(0,END)
                                txtSideEffect.delete(0,END)
                                txtPre.delete(0,END)
                                txtDos.delete(0,END)
                                txtTbp.delete(0,END)
                                txtProq.delete(0,END)

                                c1.execute("commit")
                                ref_combo.focus()
                                messagebox.showinfo("Delete Status","Deleted Successfully")
                                c1.close()
                        else:
                                ref_combo.delete(0,END)
                                txtCmp.delete(0,END)
                                tom_combo.delete(0,END)
                                MedName_combo.delete(0,END)
                                txtLotNo.delete(0,END)
                                txtIssuDt.delete(0,END)
                                txtExpDt.delete(0,END)
                                txtUse.delete(0,END)
                                txtSideEffect.delete(0,END)
                                txtPre.delete(0,END)
                                txtDos.delete(0,END)
                                txtTbp.delete(0,END)
                                txtProq.delete(0,END)

                                ref_combo.focus()
                                messagebox.showerror('Cancel','Cancel Successfully')
        

        #========= RESET BUTTON =========== MEDICINE INFORMATION ==========
        def ClrMedInfo():
                ref_combo.delete(0,END)
                txtCmp.delete(0,END)
                tom_combo.delete(0,END)
                MedName_combo.delete(0,END)
                txtLotNo.delete(0,END)
                txtIssuDt.delete(0,END)
                txtExpDt.delete(0,END)
                txtUse.delete(0,END)
                txtSideEffect.delete(0,END)
                txtPre.delete(0,END)
                txtDos.delete(0,END)
                txtTbp.delete(0,END)
                txtProq.delete(0,END)
                ref_combo.focus()


        #========= SEARCH MEDICINE BUTTON =========== MEDICINE INFORMATION ============
        def search_com():
                ser=search_combo.get()
                txt1=txtSearch.get()
                if txt1=='':
                        messagebox.showerror('Error','Please Select And Enter Data')
                else:
        
                                con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                                c1=con.cursor()
                                c1.execute('select * from medinfo where ' + ser +" LIKE '%"+ txt1 +"%'")
                                rows=c1.fetchall()
                                if len(rows)!=0:
                                        for item in trv2.get_children():
                                                trv2.delete(item)
                                        for i in rows:
                                                trv2.insert("",END,values=i)
                                con.commit()
                con.close()
                        
        #=========== SHOW ALL MEDICINE BUTTON ============= MEDICINE INFORMATION ==========
        def ShowAllInfo():
                con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                c1=con.cursor()
                rows=c1.execute("select * from medinfo")
                rows=c1.fetchall()

                if len(rows)!=0:
                        for item in trv2.get_children():
                                trv2.delete(item)
                        for i in rows:
                                trv2.insert("",END,values=i)
                c1.close()


#=========================== MEDICINE INFORMATION ===================================================
        
        BtnAdd=Button(ButtonFrame,text="Medicine Add",font=("arial",13,"bold"),bg="darkgreen",fg="white",command=MedAddInfo)
        BtnAdd.grid(row=0,column=0)
        
        BtnUpd=Button(ButtonFrame,text="UPDATE",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white",command=MedUpdInfo)
        BtnUpd.grid(row=0,column=1)
        
        BtnDel=Button(ButtonFrame,text="DELETE",font=("arial",13,"bold"),width=14,bg="red",fg="white",command=MedDelInfo)
        BtnDel.grid(row=0,column=2)
        
        BtnRes=Button(ButtonFrame,text="RESET",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white",command=ClrMedInfo)
        BtnRes.grid(row=0,column=3)
        
        BtnExit=Button(ButtonFrame,text="EXIT",font=("arial",13,"bold"),width=14,bg="darkgreen",fg="white")
        BtnExit.grid(row=0,column=4)

#=========================== SEARCH BY ======================================
        
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        search_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",17,"bold"),state="readonly")
        search_combo['values']=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        txtSearch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)

        BtnSearch=Button(ButtonFrame,text="SEARCH",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white",command=search_com)
        BtnSearch.grid(row=0,column=8)

        BtnShow=Button(ButtonFrame,text="SHOW ALL",font=("arial",13,"bold"),width=13,bg="darkgreen",fg="white",command=ShowAllInfo)
        BtnShow.grid(row=0,column=9)

#===================== LABELS AND ENTRY ==============================
        
        lblRefNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No",padx=2,pady=6)
        lblRefNo.grid(row=0,column=0,sticky=W)

        #============Fetch Reference Value From Database==================
        #============Fetch Medicine Name From Database====================
        #============Auto Update Combobox Every 2 Seconds=================
        
        def refresh():
                con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                c1=con.cursor()
                c1.execute("select ref1 from meddep")
                data=[row[0] for row in c1.fetchall()]

                c1.execute("select med1 from meddep")
                data2=[row[0] for row in c1.fetchall()]

                ref_combo['values']=data
                if data:
                        ref_combo.current()

                MedName_combo['values']=data2
                if data2:
                        MedName_combo.current()

                root.after(2000,refresh)

        #====================================================================

        ref_combo=ttk.Combobox(DataFrameLeft,width=27,font=("arial",12,"bold"),state="readonly")
        ref_combo.grid(row=0,column=1)

        lblCmp=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name :",padx=2,pady=6)
        lblCmp.grid(row=1,column=0,sticky=W)
        txtCmp=Entry(DataFrameLeft,bd=2,bg="white",width=29,relief=RIDGE,font=("arial",13,"bold"))
        txtCmp.grid(row=1,column=1)

        lblTom=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type Of Medicine :",padx=2,pady=6)
        lblTom.grid(row=2,column=0,sticky=W)
        tom_combo=ttk.Combobox(DataFrameLeft,width=27,font=("arial",12,"bold"),state="readonly")
        tom_combo['values']=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection")
        tom_combo.grid(row=2,column=1)
        tom_combo.current(0)

#===================== ADD MEDICINE ===========================
        
        lblMedName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name :",padx=2,pady=6)
        lblMedName.grid(row=3,column=0,sticky=W)

        MedName_combo=ttk.Combobox(DataFrameLeft,width=27,font=("arial",12,"bold"),state="readonly")
        MedName_combo.grid(row=3,column=1)
        refresh()
        #================================================================

        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No :",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,bd=2,bg="white",width=29,relief=RIDGE,font=("arial",13,"bold"))
        txtLotNo.grid(row=4,column=1)

        lblIssuDt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date :",padx=2,pady=6)
        lblIssuDt.grid(row=5,column=0,sticky=W)
        txtIssuDt=Entry(DataFrameLeft,bd=2,bg="white",width=29,relief=RIDGE,font=("arial",13,"bold"))
        txtIssuDt.grid(row=5,column=1)

        lblExpDt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date :",padx=2,pady=6)
        lblExpDt.grid(row=6,column=0,sticky=W)
        txtExpDt=Entry(DataFrameLeft,bd=2,bg="white",width=29,relief=RIDGE,font=("arial",13,"bold"))
        txtExpDt.grid(row=6,column=1)

        lblUse=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses :",padx=2,pady=6)
        lblUse.grid(row=7,column=0,sticky=W)
        txtUse=Entry(DataFrameLeft,bd=2,bg="white",width=29,relief=RIDGE,font=("arial",13,"bold"))
        txtUse.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect :",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,bd=2,bg="white",width=29,relief=RIDGE,font=("arial",13,"bold"))
        txtSideEffect.grid(row=8,column=1)

        lblPre=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning :",padx=15,pady=6)
        lblPre.grid(row=0,column=2,sticky=W)
        txtPre=Entry(DataFrameLeft,bd=2,bg="white",width=29,relief=RIDGE,font=("arial",13,"bold"))
        txtPre.grid(row=0,column=3)

        lblDos=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage :",padx=15,pady=6)
        lblDos.grid(row=1,column=2,sticky=W)
        txtDos=Entry(DataFrameLeft,bd=2,bg="white",width=29,relief=RIDGE,font=("arial",13,"bold"))
        txtDos.grid(row=1,column=3)

        lblTbp=Label(DataFrameLeft,font=("arial",12,"bold"),text="Tablet Price :",padx=15,pady=6)
        lblTbp.grid(row=2,column=2,sticky=W)
        txtTbp=Entry(DataFrameLeft,bd=2,bg="white",width=29,relief=RIDGE,font=("arial",13,"bold"))
        txtTbp.grid(row=2,column=3)

        lblProq=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT :",padx=15,pady=6)
        lblProq.grid(row=3,column=2,sticky=W)
        txtProq=Entry(DataFrameLeft,bd=2,bg="white",width=29,relief=RIDGE,font=("arial",13,"bold"))
        txtProq.grid(row=3,column=3)

#======================= IMAGES =========================     

        lblHome=Label(DataFrameLeft,font=("arial",15,"bold"),text="Stay Home Stay Safe",padx=2,pady=6,bg="white",fg="red",width=36)
        lblHome.place(x=425,y=140)

        img2=Image.open("D:/pharma/tab.jpg")
        img2=img2.resize((150,135),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=770,y=340)

        img3=Image.open("D:/pharma/p2.jpg")
        img3=img3.resize((150,135),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=620,y=340)

        img4=Image.open("D:/pharma/p1.jpeg")
        img4=img4.resize((150,135),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=490,y=340)

#================ DATA FRAME RIGHT ========================  

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=550,height=350)

        #============== IMAGES ========== MEDICINE ADD DEPARTMENT ================
        img5=Image.open("D:/pharma/tab2.jpg")
        img5=img5.resize((200,75),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=960,y=160)

        img6=Image.open("D:/pharma/tab2.jpg")
        img6=img6.resize((200,75),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.photoimg6,borderwidth=0)
        b1.place(x=1160,y=160)

        img7=Image.open("D:/pharma/tab.jpg")
        img7=img7.resize((200,145),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(self.root,image=self.photoimg7,borderwidth=0)
        b1.place(x=1280,y=160)

        #======================= ADD MEDICINE ============================

        lblRefNo=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference No :")
        lblRefNo.place(x=0,y=80)
        txtRefNo=Entry(DataFrameRight,bd=2,bg="white",width=14,relief=RIDGE,font=("arial",15,"bold"))
        txtRefNo.place(x=135,y=80)

        lblMedN=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name :")
        lblMedN.place(x=0,y=110)
        txtMedN=Entry(DataFrameRight,bd=2,bg="white",width=14,relief=RIDGE,font=("arial",15,"bold"))
        txtMedN.place(x=135,y=110)

#====================== SIDE FRAME ==========================================================
        

        Down_Frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        Down_Frame.place(x=330,y=150,width=135,height=160)


#==================================== SIDE FARME TREEVIEW ======================================
        Side_Frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        Side_Frame.place(x=0,y=150,width=290,height=160)

        Sc_x=ttk.Scrollbar(Side_Frame,orient=HORIZONTAL)
        Sc_x.pack(side=BOTTOM,fill=X)
        Sc_y=ttk.Scrollbar(Side_Frame,orient=VERTICAL)
        Sc_y.pack(side=RIGHT,fill=Y)

        trv1=ttk.Treeview(Side_Frame,columns=(1,2),show='headings',xscrollcommand=Sc_x.set, yscrollcommand=Sc_y.set)
        trv1.column(1,anchor='center',width=100)
        trv1.column(2,anchor='center',width=100)

        Sc_x.config(command=trv1.xview)
        Sc_y.config(command=trv1.yview)

        trv1.heading(1,text='Ref')
        trv1.heading(2,text='MedName')

        trv1.pack(fill=BOTH,expand=1)


#================== MEDICINE ADD DEPARTMENT DATABASE =========================================

        #======== ADD MEDICINE BUTTON =========== MEDICINE ADD DEPARTMENT =========
        def AddMed():
                try:
                        ref1=txtRefNo.get()
                        med1=txtMedN.get()

                        if (ref1=="" or med1==""):
                                txtRefNo.focus()
                                messagebox.showinfo("Insert Status","All Fields Are Required")
                        else:
                                prompt4=messagebox.askyesno('Confirmation','Are You Confirm For INSERT ?')

                                if prompt4:
                                        con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                                        c1=con.cursor()
                                        c1.execute("insert into meddep values('"+ ref1 +"','"+ med1 +"')")

                                        vals=(ref1,med1)
                                        trv1.insert('',END,values=vals)

                                        c1.execute("commit")

                                        txtRefNo.delete(0, 'end')
                                        txtMedN.delete(0, 'end')
                                        txtRefNo.focus()
                                        refresh()
                                        messagebox.showinfo("Insert Status","Inserted Successfully")
                                        c1.close()
                                else:
                                        txtRefNo.delete(0, 'end')
                                        txtMedN.delete(0, 'end')

                                        txtRefNo.focus()
                                        messagebox.showerror("Cancel","Cancel Successfully")
                except Exception as e:
                        if "Duplicate entry" in str(e):
                                messagebox.showwarning("ERROR","Reference No Already Exists In The Table")
                        else:
                                print("Error Occured",e)


        #============= DELETE MEDICINE BUTTON ========== MEDICINE ADD DEPARTMENT ========
        def DelMed():
                
                if(txtRefNo.get()==""):
                        txtRefNo.focus()
                        messagebox.showinfo("Delete Status", "Id Is Required For Delete")
                else:
                        prompt5=messagebox.askyesno('Confirmation','Are You Confirm For DELETE ?')

                        if prompt5:
                                con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                                c1=con.cursor()
                                c1.execute("delete from meddep where ref1='"+ txtRefNo.get() +"' ")

                                SelectedItem=trv1.selection()[0]
                                trv1.delete(SelectedItem)

                                c1.execute("commit")

                                txtRefNo.delete(0, 'end')
                                txtMedN.delete(0, 'end')
                                txtRefNo.focus()
                            
                                messagebox.showinfo("Delete Status","Deleted Successfully")
                                c1.close()
                        else:
                                txtRefNo.delete(0, 'end')
                                txtMedN.delete(0, 'end')

                                txtRefNo.focus()
                                messagebox.showerror('Cancel','Cencel Successfully')

        #============= UPDATE MEDICINE BUTTON ========== MEDICINE ADD DEPARTMENT ======
        def UpdMed():
                ref1=txtRefNo.get()
                med1=txtMedN.get()

                if (ref1=="" or med1==""):
                        txtRefNo.focus()
                        messagebox.showinfo("Update Status","All Fields Are Required")
                else:
                        prompt6=messagebox.askyesno('Confirmation','Are You Confirm For UPDATE ?')

                        if prompt6:
                                con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                                c1=con.cursor()
                                c1.execute("update meddep set med1='"+ med1 +"' where ref1='"+ ref1 +"' ")

                                SelectedItem=trv1.selection()[0]
                                vals=(ref1,med1)
                                trv1.item(SelectedItem,values=vals)

                                

                                txtRefNo.delete(0, 'end')
                                txtMedN.delete(0, 'end')
                                txtRefNo.focus()
                               
                                messagebox.showinfo("Update Status","Updated Successfully")
                                con.commit()
                                c1.close()
                        else:
                                txtRefNo.delete(0, 'end')
                                txtMedN.delete(0, 'end')

                                txtRefNo.focus()
                                messagebox.showerror('Cancel','Cancel Successfully')
        
        #============= CLEAR MEDICINE BUTTON ========= MEDICINE ADD DEPARTMENT ============
        def ClrMed():
                txtRefNo.delete(0, 'end')
                txtMedN.delete(0, 'end')
                txtRefNo.focus()

        #============= SHOW ALL MEDICINE IN TREEVIEW ============== MEDICINE ADD DEPARTMENT ===========
        def ShowMed():
                con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                c1=con.cursor()
                rows=c1.execute("select * from meddep")
                rows=c1.fetchall()

                for row in rows:
                        trv1.insert('',END,values=row)

                c1.close()
        ShowMed()


        #================= SELECT MEDICINE ============= MEDICINE ADD DEPARTMENT ===========
        def DisplaySelectedItem(a):
                txtRefNo.delete(0,END)
                txtMedN.delete(0,END)
                SelectedItem=trv1.selection()[0]
                txtRefNo.insert(0,trv1.item(SelectedItem)['values'][0])
                txtMedN.insert(0,trv1.item(SelectedItem)['values'][1])

        trv1.bind("<<TreeviewSelect>>",DisplaySelectedItem)




#=====================MEDICINE ADD BUTTON================MEDICINE ADD DEPARTMENT========================

        
        BtnAddMed=Button(Down_Frame,text="ADD",font=("arial",12,"bold"),width=12,bg="lime", fg="white", pady=4, command=AddMed)
        BtnAddMed.grid(row=0,column=0)

        BtnUpdMed=Button(Down_Frame,text="UPDATE",font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=4, command=UpdMed)
        BtnUpdMed.grid(row=1,column=0)

        BtnDelMed=Button(Down_Frame,text="DELETE",font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=4, command=DelMed)
        BtnDelMed.grid(row=2,column=0)

        BtnClrMed=Button(Down_Frame,text="CLEAR",font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=4, command=ClrMed)
        BtnClrMed.grid(row=3,column=0)

#==================== FRAME DETAILS =========================================

        FrameDet=Frame(self.root,bd=15,relief=RIDGE)
        FrameDet.place(x=0,y=580,width=1530,height=210)

#=============== MEDICINE INFORMATION TREEVIEW ==================================

        Table_Frame=Frame(FrameDet,bd=15,relief=RIDGE)
        Table_Frame.place(x=0,y=1,width=1500,height=180)

        Scr_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scr_x.pack(side=BOTTOM,fill=X)
        Scr_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        Scr_y.pack(side=RIGHT,fill=Y)

        trv2=ttk.Treeview(Table_Frame,column=(1,2,3,4,5,6,7,8,9,10,11,12,13),show='headings',xscrollcommand=Scr_x.set,yscrollcommand=Scr_y.set)
        trv2.column(1,anchor='center',width=100)
        trv2.column(2,anchor='center',width=100)
        trv2.column(3,anchor='center',width=100)
        trv2.column(4,anchor='center',width=100)
        trv2.column(5,anchor='center',width=100)
        trv2.column(6,anchor='center',width=100)
        trv2.column(7,anchor='center',width=100)
        trv2.column(8,anchor='center',width=100)
        trv2.column(9,anchor='center',width=100)
        trv2.column(10,anchor='center',width=100)
        trv2.column(11,anchor='center',width=100)
        trv2.column(12,anchor='center',width=100)
        trv2.column(13,anchor='center',width=100)

        Scr_x.config(command=trv2.xview)
        Scr_y.config(command=trv2.yview)

        trv2.heading(1,text="Reference No")
        trv2.heading(2,text="Company Name")
        trv2.heading(3,text="Type Of Medicine")
        trv2.heading(4,text="Tablet Name")
        trv2.heading(5,text="Lot No")
        trv2.heading(6,text="Issue date")
        trv2.heading(7,text="Exp date")
        trv2.heading(8,text="Uses")
        trv2.heading(9,text="Side Effect")
        trv2.heading(10,text="Warning")
        trv2.heading(11,text="Dosage")
        trv2.heading(12,text="Price")
        trv2.heading(13,text="Product QT")
        
        trv2.pack(fill=BOTH,expand=1)

        #============= SHOW ALL MEDICINE IN TREEVIEW ============ MEDICINE INFORMATION ============
        def ShowMedInfo():
                con = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='pharmacy')
                c1=con.cursor()
                rows=c1.execute("select * from medinfo")
                rows=c1.fetchall()

                for row in rows:
                        trv2.insert('',END,values=row)

                c1.close()
        ShowMedInfo()

        #============= SELECT MEDICINE ======== MEDICINE INFORMATION ========
        def DisplaySelectedItemInfo(a):
                ref_combo.delete(0,END)
                txtCmp.delete(0,END)
                tom_combo.delete(0,END)
                MedName_combo.delete(0,END)
                txtLotNo.delete(0,END)
                txtIssuDt.delete(0,END)
                txtExpDt.delete(0,END)
                txtUse.delete(0,END)
                txtSideEffect.delete(0,END)
                txtPre.delete(0,END)
                txtDos.delete(0,END)
                txtTbp.delete(0,END)
                txtProq.delete(0,END)


                SelectedItem=trv2.selection()[0]
                ref_combo.set(trv2.item(SelectedItem)['values'][0])
                txtCmp.insert(0,trv2.item(SelectedItem)['values'][1])
                tom_combo.set(trv2.item(SelectedItem)['values'][2])
                MedName_combo.set(trv2.item(SelectedItem)['values'][3])
                txtLotNo.insert(0,trv2.item(SelectedItem)['values'][4])
                txtIssuDt.insert(0,trv2.item(SelectedItem)['values'][5])
                txtExpDt.insert(0,trv2.item(SelectedItem)['values'][6])
                txtUse.insert(0,trv2.item(SelectedItem)['values'][7])
                txtSideEffect.insert(0,trv2.item(SelectedItem)['values'][8])
                txtPre.insert(0,trv2.item(SelectedItem)['values'][9])
                txtDos.insert(0,trv2.item(SelectedItem)['values'][10])
                txtTbp.insert(0,trv2.item(SelectedItem)['values'][11])
                txtProq.insert(0,trv2.item(SelectedItem)['values'][12])

        trv2.bind("<<TreeviewSelect>>",DisplaySelectedItemInfo)
            
                        
if __name__ == "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
