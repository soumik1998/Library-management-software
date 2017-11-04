def copy(f1,f2):
	fp1=open(f1,"w")
	fp2=open(f2,"r")
	for i in fp2:
		fp1.write(i)
	fp1.close()
	fp2.close()
def removebook():
	roll=raw_input("enter book id to remove")
	fp=open("book_names.txt","r")
	fp1=open("ex1.txt","w")
	count=0
	for i in fp:
		if(roll != i.split()[0]):
			fp1.write(i)
		else:
			count+=1
	fp1.close()
	fp.close()
	if(count==0):
		print("no such book\n")
		return
	copy("book_names.txt","ex1.txt")
	print("book removed sucessfully")
removebook()