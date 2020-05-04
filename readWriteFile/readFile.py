#File Object
f= open("file.txt","r")

#Read a line of file
content = f.readline()

#Print using content
print("Hello " + content + "!")

#Close the File Object
f.close()