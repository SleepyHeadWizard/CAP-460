# make a attendance tracker for a class use file handling to store the data

# attendance Tracker

f=open('attendance.txt','r')

def file_read(f):
    txt=open(f,'r')
    print(txt.read())
    txt.close()
    
def add_student(f,s=""):
    txt=open(f,'a')
    txt.write(s)
    txt.close()
    
def remove_student(f,s=""):
    txt=open(f,'r')
    r=txt.readlines()
    txt.close()
    txt=open(f,'w')
    for i in r:
        if i!=s:
            txt.write(i)
    txt.close()
    
def attendance(f,s=""):
    txt=open(f,'r')
    r=txt.readlines()
    txt.close()
    txt=open(f,'w')
    for i in r:
        if i==s:
            txt.write(i.strip()+' Present\n')
        else:
            txt.write(i)
    txt.close()