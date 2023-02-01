f=open("myfile.txt","r");
text=f.read()
print(text)
f.close()
f1=open("myfile.txt","a");
f1.write('i am appending something')
f.close()

