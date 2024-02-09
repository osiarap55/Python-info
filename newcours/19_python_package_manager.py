# What is pip?
# PIP stands for preferred installer program. We use pip to install different python packages. packages is a python module that can contain one or more modules or other packages. A module or modules that we can install to our application is a package. In programming, we do not have to write every utility program, instead we install packages aand import them to our application.

# let use nnumpy

import numpy 
print(numpy.version.version)
lst = [1, 2, 3, 4, 5]
np_arr = numpy.array(lst)
print(np_arr)
print(len(np_arr))
print(np_arr * 2)
print(np_arr + 2)

# This section is not about numpy nor pandas, here we are trying to learn how to install packages and how to import them. If it is needed, we will talk about different packages in other sections.

# Let us import a web browser module, which can help us to open any website. We do not need to install this module, it is already installed by default with Python 3. For instance if you like to open any number of websites at any time or if you like to schedule something, this webbrowser module can be used.

import webbrowser

url_list = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in different tab 

for url in url_list:
    webbrowser.open_new_tab(url)
        

# Uninstalling Packages
# If you do not like to keep the installed packages, you can remove them using the following command.
# pip uninstall packagename

# List of Packages
# To see the installed packages on our machine. We can use pip followed by list.
# pip list

# Show Package
# To show information about a package
# pip show packagename
# If we want even more details, just add --verbose

# PIP Freeze
# Generate installed Python packages with their version and the output is suitable to use it in a requirements file. A requirements.txt file is a file that should contain all the installed Python packages in a Python project.

# Reading from URL
# By now you are familiar with how to read or write on a file located on you local machine. Sometimes, we would like to read from a website using url or from an API. API stands for Application Program Interface. It is a means to exchange structured data between servers primarily as json data. To open a network connection, we need a package called requests - it allows to open a network connection and to implement CRUD(create, read, update and delete) operations. In this section, we will cover only reading ore getting part of a CRUD.

# we will see get, status_code, headers, text and json methods requests module:

# - get(): to open a network and fetch data from url - it returns a response object
status_code: After we fetched data, we can check the status of the operation (success, error, etc)
headers: To check the header types
text: to extract the text from the fetched response object
json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

