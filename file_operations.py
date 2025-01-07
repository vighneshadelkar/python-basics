#  w opens file for writing, mode will always overwrite the file if it exits, if file doesnt exist it will create one
#  w+ oepns file for reading and writing, mode will always overwrite the file if it exists, if file doesnt exist it will create one
#  r oepns file for reading 
#  r+ oepns file for reading and writing
#  a mode will append text to existing file data

# f=open("C:\\Users\\ASUS\\Desktop\\vighnesh\\ML\\funny.txt","w")
f=open("C:\\Users\\ASUS\\Desktop\\vighnesh\\ML\\funny.txt","a")
# f.write("\nHello, world! by vighnesh")
f.close()
f=open("C:\\Users\\ASUS\\Desktop\\vighnesh\\ML\\funny.txt","r")
for line in f:
    tokens=line.split(' ')
    print(len(tokens))
f.close()

# when we use with we donot need to close the file using .close()
with open("C:\\Users\\ASUS\\Desktop\\vighnesh\\ML\\funny.txt","r") as f_with:
    print(f_with.read())
    # for line in f_with:
    #     print(line)
