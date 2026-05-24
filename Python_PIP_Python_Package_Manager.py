What is PIP ?
PIP stands for Preferred installer program. We use pip to install different Python packages. 
Package is a Python module that can contain one or more modules or other packages. 
A module or modules that we can install to our application is a package. 

In programming, we do not have to write every utility program, instead we install packages and import them to our applications.


Installing PIP
If you did not install pip, let us install it now. Go to your terminal or command prompt and copy and paste this:


#In terminal line by line
exit()
py -m ensurepip --upgrade
py -m pip --version



Installing packages using pip
Let us try to install numpy, called numeric python.
 It is one of the most popular packages in machine learning and data science community.

NumPy is the fundamental package for scientific computing with Python. It contains among other things:
a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities



# Now to go back to python editor type python in terminal


import numpy

print(numpy.version.version)

lst = [1, 2, 3, 4, 5]

np_arr = numpy.array(lst)

print(np_arr)
print(len(np_arr))
print(np_arr * 2)
print(np_arr + 2)




Let us import a web browser module, which can help us to open any website. We do not need to install this module, 
it is already installed by default with Python 3. For instance if 
you like to open any number of websites at any time or if you like to schedule something, this webbrowser module can be used.


import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)



Uninstalling Packages
If you do not like to keep the installed packages, you can remove them using the following command.

pip uninstall packagename




List of Packages
To see the installed packages on our machine. We can use pip followed by list.
exit()
pip list



Show Package
To show information about a package

pip show packagename

#pip show numpy



or more info  # pip show --verbose pandas



PIP Freeze
Generate installed Python packages with their version and the output is suitable to use it in a requirements file. 
A requirements.txt file is a file that should contain all the installed Python packages in a Python project.


pip freeze



Reading from URL

By now you are familiar with how to read or write on a file located on you local machine. 
Sometimes, we would like to read from a website using url or from an API. API stands for Application Program Interface. 
It is a means to exchange structured data between servers primarily as json data. 
To open a network connection, we need a package called requests - it allows to open a network connection and 
to implement CRUD(create, read, update and delete) operations. In this section, we will cover only reading 
ore getting part of a CRUD.

Let us install requests:


# in terminal

pip install requests



We will see get, status_code, headers, text and json methods in requests module:

get(): to open a network and fetch data from url - it returns a response object
status_code: After we fetched data, we can check the status of the operation (success, error, etc)
headers: To check the header types
text: to extract the text from the fetched response object
json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.



import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page





Let us read from an API. API stands for Application Program Interface. It is a means to exchange structure 
data between servers primarily a json data. 
An example of an API:https://restcountries.eu/rest/v2/all. Let us read this API using requests module.


import requests

url = 'https://api.worldbank.org/v2/incomeLevel/LIC/country?format=json'

response = requests.get(url)

print(response)
print(response.status_code)

countries = response.json()

# metadata
print(countries[0])

# actual country data
print(countries[1][:1])


# code changes dependig on what data type the API has, forexample JSON or XML 


#Checking URL opens 

import webbrowser # web browser module to open websites
# list of urls: python
url_lists = ['https://api.worldbank.org/V2/incomeLevel/LIC/country']

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)




We use json() method from response object, 
if the we are fetching JSON data. For txt, html, xml and other file formats we can use text.




Creating a Package
We organize a large number of files in different folders and sub-folders based on some criteria, 
so that we can find and manage them easily. As you know, a module can contain multiple objects, 
such as classes, functions, etc. A package can contain one or more relevant modules. 
A package is actually a folder containing one or more module files. 
Let us create a package named mypackage, using the following steps:

Create a new folder named mypackage inside 30DaysOfPython folder Create an empty init.py file in the mypackage folder. 
Create modules arithmetic.py and greet.py with following code:



Data Analysis, Data Science and Machine learning

Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.

Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures 
of high-level and a wide variety of tools for analysis.

SciPy: SciPy is a machine learning library for application developers and engineers. 
SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
   
Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
TensorFlow: is a machine learning library built by Google.

Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides 
some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
   







