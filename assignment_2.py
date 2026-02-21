# EXPLAINING TO A BODA BODA GUY

# 1. Declaring
'''This refers to writing the name of a variable
just like l can the word name on a piece of paper.
It is introducing something to a computer without
giving it a value
'''
# name
# In Python you cannot declare a variable without giving it a value

# 2. Initializing
'''This refers to giving a variable its first value just like l can
say the word name is egual to Oscar where Oscar is the 
value of name'''

name='Oscar'

#3. Data types in Python
# A data type tells Python what type of data something is
# They help allocate memory space to data
# There are various data types in Python for example:

# a. String
'''This is text just like your name or the place 
where you live '''

name="Oscar"
# Where oscar is a string and it should be enclosed in quotes

# b. interger
# This are non-decimal values in Python for example 1000,2000
# For example you can have 1000 shillings where 1000 is a number

num=1000
# The value 1000 has a data type of number

# c. Float
# This is a decimal value in Python for example 1000.124

num=1000.124
# The value 1000.124 has a data type of float since it has decimal points

# d. set
'''These are used to store unique values in 
python for example a set of boda boda names like 
boxer,senke'''

boda_boda_names={'boxer','senke','yamaha'}
# This is a set of boda boda names

# Sets do not allow duplicates
duplicates={1,2,2,3}
print(duplicates)

# e. Tuple 
'''This is used to store fixed data in python 
for example a tuple of all boda boda stages in kampala'''

boda_boda_stages=("Nansana","Wandegeya","Kikuubo")
# Tuples cannot be changed and their index starts at 0

# f. Dictionary
'''These are used to store data related to one subject 
or character for example if we want to store your
name and the boda boda stage you work from'''
# They store name in form of key and value

Dict={"name":"Oscar","boda_boda_stage":"Nansana"}
# In this case name is  the key and oscar is the value

# g. List
# This is used to store multiple values in python
''' For example if we wanted to store all names of
 boda boda men at Nansana stage , instead of creating 
 a variable for each name, we can store all names in 
 one list called names
 '''
names=['Juma','Ozzy','Kasawuli','Kifeesi']
# Lists can be changed and they start at index 0
# 
