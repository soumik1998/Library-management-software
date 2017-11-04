#add book 
def addbook():
	fp=open("book_namesmaindata.txt","a+");
	bookid=(input('enter book id\n'))
	name=input('enter name\n')
	qty=int(input('enter no books\n'))
	sub=input('enter the subject\n')
	publisher=input('enter publisher name\n')
	price=float(input("enter the price\n"))
	#l=raw_input().split()
	#print l
	for i in range(1,qty+1):
		fp.write(str(bookid)+'.'+str(i)+'\t'+name+'\t'+sub+'\t'+publisher+'\t'+str(price)+'\n')
	fp.close()
addbook();

