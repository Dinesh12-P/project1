

#importing module
import json
import os

todo_list = []
# taking file name as input from user
fil = input('enter the name of file where you want to store data: ')
f = open(fil, 'a')

# taking the key and value input from user
dictionary = {}
while True:
        key = input("Enter the key : ")
        if key.lower() == 'quit':
             break
        value = input(f"Enter the value for {key}: ")
        dictionary[key] = value
        print (key ,':' ,value )
        break

json_object = json.dumps(dictionary, indent=4)
 

with open(fil , "a") as file:
    file.write(json_object)

    with open(fil ,"r") as file:
          c = file.read()
          print(c)
          with open(fil , "a") as file:
            new = {}
            # taking new key and value
while True:
        key = input("\n Enter the new key to add in dict : ")
        if key.lower() == 'quit':
             break
        value = input(f"Enter the value for new {key}: ")
        new[key] = value
        print (key ,':' ,value )
        break
json_object = json.dumps(new, indent=4)
with open(fil , "a") as file:
    file.write(json_object)
    f = open(fil, 'w')
    d = input('enter the name of file you want to delete ' )
    #deleting the json file
try:
    os.remove(d)
except FileNotFoundError:
   print("file not found")
except PermissionError:
 print("unable to delete")
 f.close()
             


