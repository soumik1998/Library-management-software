import datetime
from datetime import timedelta
now=datetime.datetime.now()
issue_date=now.strftime("%d-%m-%Y")
EndDate = str(now + timedelta(days=14))
ls=EndDate[:10].split('-')
return_date=ls[2]+"-"+ls[1]+"-"+ls[0]

def issuebook():
        flag=0
        while flag==0:
                roll=(input("enter student roll no.\n"))
                fp=open("student_names.txt","r")
                for i in fp:
                        #print(i)
                        if(i.split()[0] == roll):
                                #i=i.strip
                                print(i.strip())
                                student=i.strip()
                                flag=1
                                break;
                
                fp.close()
        if flag==0:
                print("no such student in data")
                exit(0)
        flag=0
        bid=input("enter book id to issue\n")
        fp=open("book_namesmaindata.txt","r")
        for i in fp:
                if i.split()[0]==bid:
                        print(i.strip())
                        book=i.strip()
                        flag=1
                        break;
        if(flag==0):
                print("no book with this id\n")
                exit(1)
        fp.close()
        fp=open("books_studentsissued.txt","a+");
        a=student+'\t'+book+'\t'+issue_date+"\t"+return_date+'\n'
        fp.write(a)
        fp.close()

issuebook()        
