#add students
def addstudent():
	fp=open("student_names.txt","a+");
	roll=input('enter roll no. \n')
	name=input('enter name\n')
	mail=input("Enter the students mail\n")
	#l=raw_input().split()
	#print l
	fp.write(str(roll)+'\t'+name+'\t'+mail+'\n')
	fp.close()
addstudent();
