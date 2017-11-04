from tkinter import *
import tkinter.messagebox
#-----------------------------------------------------------------------------------------------------------
def addbookinfile():
    fp=open("book_namesmaindata.txt","a+");
    try:
        bid=float(bookid.get())
        name=bookname.get()
        qty=int(quantity.get())
        sub=subject.get()
        publish=publisher.get()
        cost=float(price.get())
        toprint=''
        for i in range(1,qty+1):
            substr=str(bid)+'.'+str(i)+'\t'+name+'\t'+sub+'\t'+publish+'\t'+str(cost)+'\n'
            toprint=toprint+substr
        ans=tkinter.messagebox.askquestion("Add Book",toprint)
        if ans=="yes":
            fp.write(toprint)
        fp.close()
    except:
        tkinter.messagebox.showinfo("Add Book","The values entered do not match the format")
def copy(f1,f2):
    fp1=open(f1,"w")
    fp2=open(f2,"r")
    for i in fp2:
        fp1.write(i)
    fp1.close()
    fp2.close()
def removebookfromfile():
	#only one book with a particular bookid will be removed
    #print(bookid.get())
    bid=bookid.get()#(input("enter book id to remove"))
    fp=open("book_namesmaindata.txt","r")
    fp1=open("ex1.txt","w")
    count=0
    for i in fp:
        if(bid != i.split()[0]):
            fp1.write(i)
        else:
            count+=1
            break
    fp1.close()
    fp.close()
    if(count==0):
        tkinter.messagebox.showinfo("Remove Book","No such book in library.")
        #print("no such book\n")
        return
    ans=tkinter.messagebox.askquestion("Remove Book","Book Details:\n"+i)
    if ans=="yes":
        copy("book_namesmaindata.txt","ex1.txt")
        tkinter.messagebox.showinfo("Remove Book","Book removed sucessfully")
    #print("book removed sucessfully")
def addbook():
    global frame3
    global bookid
    global quantity
    global bookname
    global subject
    global publisher
    global price
    frame3.destroy()
    frame3=Frame(root)
    frame3.pack(side=BOTTOM)
    label1=Label(frame3,text="book name").grid(row=0,column=0)
    label2=Label(frame3,text="quantity").grid(row=1,column=0)
    label3=Label(frame3,text="book id").grid(row=2)
    label4=Label(frame3,text="subject").grid(row=3)
    label5=Label(frame3,text="publisher").grid(row=4)
    label6=Label(frame3,text="price").grid(row=5)
    bookname=Entry(frame3)
    quantity=Entry(frame3)
    bookid=Entry(frame3)
    subject=Entry(frame3)
    publisher=Entry(frame3)
    price=Entry(frame3)
    bookname.grid(row=0,column=1)
    quantity.grid(row=1,column=1)
    bookid.grid(row=2,column=1)
    subject.grid(row=3,column=1)
    publisher.grid(row=4,column=1)
    price.grid(row=5,column=1)
    add=Button(frame3,text="ADD BOOK IN DATABASE",command=addbookinfile).grid(row=7,column=1)
def removebook():
    global frame3
    global bookid
    global reason
    frame3.destroy()
    frame3=Frame(root)
    frame3.pack(side=BOTTOM)
    label1=Label(frame3,text="enter book id").grid(row=0,column=0)
    bookid=Entry(frame3)
    bookid.grid(row=0,column=1)
    remove=Button(frame3,text="REMOVE BOOK FROM LIBRARY",command=removebookfromfile).grid(row=1,column=1)
def book():
    global frame2
    frame2.destroy()
    frame2=Frame(root)
    frame2.pack()
    add=Button(frame2,text="ADD BOOK",command=addbook).grid(row=0,column=0)
    remove=Button(frame2,text="REMOVE BOOK",command=removebook).grid(row=0,column=1)
#-------------------------------------------------------------------------------------------------------------
def addstudnetinfile():
    print(studentname.get())
    print(rollno.get())
    print(emailid.get())
    print(contact.get())
def removestudentfromfile():
    print(rollno.get())
def addstudent():
    global frame3
    global studentname
    global rollno
    global emailid
    global contact
    frame3.destroy()
    frame3=Frame(root)
    frame3.pack(side=BOTTOM)
    label1=Label(frame3,text="student name").grid(row=0,column=0)
    label3=Label(frame3,text="roll no.").grid(row=1)
    label4=Label(frame3,text="email id").grid(row=2)
    label5=Label(frame3,text="contact no.").grid(row=3)
    studentname=Entry(frame3)
    rollno=Entry(frame3)
    emailid=Entry(frame3)
    contact=Entry(frame3)
    studentname.grid(row=0,column=1)
    rollno.grid(row=1,column=1)
    emailid.grid(row=2,column=1)
    contact.grid(row=3,column=1)
    add=Button(frame3,text="Submit",command=addstudnetinfile).grid(row=4,column=1)
def removestudent():
    global frame3
    global studentid
    frame3.destroy()
    frame3=Frame(root)
    frame3.pack(side=BOTTOM)
    label1=Label(frame3,text="enter student id").grid(row=0,column=0)
    studentid=Entry(frame3)
    studentid.grid(row=0,column=1)
    remove=Button(frame3,text="Submit",command=removestudentfromfile).grid(row=2,column=1)
def student():
    global frame2
    global frame3
    frame2.destroy()
    frame3.destroy()
    frame2=Frame(root)
    frame2.pack()
    add=Button(frame2,text="ADD STUDENT",command=addstudent).grid(row=0,column=0)
    remove=Button(frame2,text="REMOVE STUDENT",command=removestudent).grid(row=0,column=1)
#------------------------------------------------------------------------------------------------------------
def check():
    print(studentid.get())
    print(bookid.get())
def issue():
    global frame2
    global frame3
    global studentid
    global bookid
    frame2.destroy()
    frame3.destroy()
    frame2=Frame(root)
    frame2.pack()
    label1=Label(frame2,text="student id").grid(row=0)
    label2=Label(frame2,text="book id").grid(row=1)
    studentid=Entry(frame2)
    bookid=Entry(frame2)
    studentid.grid(row=0,column=1)
    bookid.grid(row=1,column=1)
    issue=Button(frame2,text="ISSUE",command=check).grid()

#------------------------------------------------------------------------------------------------------------
def returnbook():
    global frame2
    global frame3
    frame2.destroy()
    frame3.destroy()
    frame2=Frame(root)
    frame2.pack()
    label1=Label(frame2,text="book id").grid(row=0)
    bookid=Entry(frame2)
    bookid.grid(row=0,column=1)
    returnbk=Button(frame2,text="RETURN BOOK").grid(row=1)
#---------------------------------------------------------------------------------------------------------
def makenew():
        global frame
        frame.destroy()
        global frame1
        global frame2
        global frame3
        global book
        global student
        global issuebook
        global returnbook
        frame1=Frame(root)
        frame1.pack()
        frame2=Frame(root)
        frame2.pack()
        frame3=Frame(root)
        frame3.pack()
        book=Button(frame1,text="BOOK DETAILS",command=book).grid(row=0,column=0)
        student=Button(frame1,text="STUDENT DETAILS",command=student).grid(row=0,column=1)
        issuebook=Button(frame1,text="ISSUE BOOK",command=issue).grid(row=0,column=2)
        returnbook=Button(frame1,text="RETURN BOOK",command=returnbook).grid(row=0,column=3)
        root.mainloop()
def checkpass():
    if password.get()=="abc":
        makenew()
    else:
        print("no")
global frame
root=Tk()
frame=Frame(root)
frame.pack()
label2=Label(frame,text="Password").pack()
password=Entry(frame,show="*")
password.pack()
submit=Button(frame,text="SUBMIT",command=checkpass).pack()
root.mainloop()
