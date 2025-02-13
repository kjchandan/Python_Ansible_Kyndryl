#------------------------Only Contents----------------------------------------------

# def filename(name):
#     print(name)
#     fobj=open(name,"r")
#     print(fobj.readline())
#     fobj.close()
 
# filename("print.py")



# def filename(name):
#     with open(name, "r") as fobj:
#         line_number = 1
#         for line in fobj:
#             print(line_number, line.strip())
#             line_number += 1

# filename("print.py")

#--------------------------------------COntents with line numbers(readline)-----------------------
# Comes with separate lines

# filename = input("Enter name")
# file_object = open (filename)
# ctr =1
# line = file_object.readline()
# while line :
#     print(ctr, line)
#     ctr+=1
#     line = file_object.readline()

# file_object.close()

#------------------------------------Content with line numbers(readlines)---------------------------
# It comes in single line but prints with /n.

# filename = input("Enter name")
# file_object = open (filename)
# ctr =1
# lines = file_object.readlines()
# length=len(lines)
# while ctr <= length:
#     print(ctr, lines[ctr-1], end="")
#     ctr+=1
#     # line = file_object.readlines()

# file_object.close()

# -----------------------

# wfile_object = open("python.txt", "w")
# dir(wfile_object)

# wfile_object.write("Good Afternoon")

# ------------------------Two files (1 read and another write files)
# open the second file in the write mode
# Using the read method, read from the first file &
# using the write method, write to the second file

# def filename(name,File):
#     print(name)
#     fobj=open(name,"r")
#     print(File)
#     fobj1=open(name,"w")
#     print(fobj.readline())
#     print(fobj1.readline())
#     fobj.close()
#     fobj1.close()

# filename("print.py","python1.py")


# filename = input("Chandan")
# filename1 = input("KJ")

# file_object=open(filename)
# filename1_object=open(filename1, "w")

# filename1_object.write(filename_object.read())
# file_object.close()
# file_object1.close()

# -------------------------------------Print two two lines--------------------------------


# filename = input("Enter the file name : ")
# file_object = open(filename)
# ctr = 1
# location = file_object.tell()
# line = file_object.readline()
# while line:
#     print(ctr, line, end="")
#     file_object.seek(location)
#     line = file_object.readline()
#     print(ctr, line, end="")
#     location = file_object.tell()
#     ctr += 1
#     line = file_object.readline()


# file_object.close()
 


# ____________________
# Define Function -
# def fun():
#     print("Python is fun")

#     help(fun)

# --------------------------

# def total(a=0, b=0, *c):
#     print(type(c))
#     result=a+b
#     for num in c:
#         result = result+num
#         print(result)

# total()
# total(10)
# total(10,20,30,40,50)

# ----------------------------

def total(a=0, b=0, *c, **d):
    print("a is", a)
    print("b is", b)
    print("c is", c)
    result=a+b
    for num in c:
        print(num)
        result = result+num
    for num in d.values():
        result=result+num
        print(result)

total()
total(10)
total(10,20,30,40,50, i=120, j=200, k=4000)



