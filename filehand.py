#open file
f=open('hello.txt','r')

#read
def file_read(f):
    txt=open(f,'r')
    print(txt.read())
    txt.close()
    
#write    
def file_write(f,s=""):
    txt=open(f,'w')
    txt.write(s)
    txt.close()
    
#append
def file_append(f,s=""):
    txt=open(f,'a')
    txt.write(s)
    txt.close()
    
# file_read('hello.txt')
file_write('hello.txt', 'Hello World')
file_append('hello.txt', '\nHello, how are you?')
file_append('hello.txt', '\nI am fine, thank you.')

#read from last
r=f.readlines()
print(r[-1])
print(r[-2])