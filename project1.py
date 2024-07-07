# 1. take input form user so that which file user wants to create
#2. insert content inside the file by asking user
#3. user needs to read file
#4. new input add garna paryo
#5. at last file must be deleted by asking user

# laptop wala bhai

# importing os module
import os
# taking the name of file to be created from user
file = input("Enter the name of file that you want to create:")

 # adding data into the file
f = open(file, 'a')
b= input("write what do you want to add: ")
f.write(b)
# opening the txt file by asking the user
# mistake vako xa halka
f = open(file, 'r')
c = input("enter which file you want to to read: ")
c = f.readline()
print('\n'+ c)

# taking user input to modify into the file
f = open(file, 'a')
c = input("write what you want to modify: ")
f.write(c)

#deleting the txt file
f = open(file, 'w')

d = input('enter the name of file you want to delete ' )
try:
    os.remove(d)
except FileNotFoundError:
   print("file not found")
except PermissionError:
 print("unable to delete")

 f.close()
    
