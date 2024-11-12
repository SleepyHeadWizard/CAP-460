f=open('hello.txt','r')
def file_read(f):
    txt=open(f,'r')
    print(txt.read())
    txt.close()
    
def file_write(f,s=""):
    txt=open(f,'w')
    txt.write(s)
    txt.close()
    
def file_append(f,s=""):
    txt=open(f,'a')
    txt.write(s)
    txt.close()
    
# file_read('hello.txt')
file_write('hello.txt', 'Hello World')
file_append('hello.txt', '\nHello, how are you?')

#read from last
