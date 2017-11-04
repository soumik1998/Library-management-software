def copy(f1,f2):
	fp1=open(f1,"w")
	fp2=open(f2,"r")
	for i in fp2:
		fp1.write(i)
	fp1.close()
	fp2.close()
def remove():
	roll=raw_input("enter roll no. to remove")
	fp=open("student_names.txt","r")
	fp1=open("ex1.txt","w")
	for i in fp:
		if(roll != i.split()[0]):
			fp1.write(i)
	fp1.close()
	fp.close()
	copy("student_names.txt","ex1.txt")
remove()