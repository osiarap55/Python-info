# So far we have seen different Python data types. we usually store our data in different file formats. In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section. First, let us get familiar with handling files with common file format(.txt).
# File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use open() built-in function.

# Syntax
# open("filename", mode) # mode(r, a, w, x, t, b) could be to read, write, update.

#    "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
#    "a" - Append - Opens a file for appending, creates the file if it does not exist
#    "w" - Write - Opens a file for writing, creates the file if it does not exist
#    "x" - Create - Creates the specified file, returns an error if the file exists
#    "t" - Text - Default value. Text mode
#    "b" - Binary - Binary mode (e.g. images)

# OPENING FILES FOR READING

# The default mode of open is reading, so we do not have to apecify "r" or "rt". I have created and saved a file named reading_file_example.txt in the files directory. Let us see how it is done:

f = open("/home/paradiseland86/Documentos/Topicos/INFORMATICA/Python_info/newcours/18.1_example.txt")
print(f)

# As you can see in the example above, I printed the opened file and it gaves some information about it. Opened file has to be closed with close() method.

# read(): read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method.

f = open("/home/paradiseland86/Documentos/Topicos/INFORMATICA/Python_info/newcours/18.1_example.txt")
txt = f.read()
print(type(txt))
print(txt)
f.close()

# instead of printing all the text, let us print the first 10 characters of the text file.

f = open("/home/paradiseland86/Documentos/Topicos/INFORMATICA/Python_info/newcours/18.1_example.txt")
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

# readline(): read only the first line

f = open("/home/paradiseland86/Documentos/Topicos/INFORMATICA/Python_info/newcours/18.1_example.txt")
line = f.readline()
print(type(line))
print(line)
f.close()

# readlines(): read all the text line by line and returns a list of lines

f = open("/home/paradiseland86/Documentos/Topicos/INFORMATICA/Python_info/newcours/18.1_example.txt")
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open("/home/paradiseland86/Documentos/Topicos/INFORMATICA/Python_info/newcours/18.1_example.txt")
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# After we open a file, we should close it. There is a high tendency of forgettinf to close them. There is a new way of openning files using with-closes the files by itself. Let us rewrite the previous example with the with method:

with open("/home/paradiseland86/Documentos/Topicos/INFORMATICA/Python_info/newcours/18.1_example.txt") as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# OPENING FILES FOR WRITTING AND UPDATING



























