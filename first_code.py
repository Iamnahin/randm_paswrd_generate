#imporitng random modules for choosing random characters for password
import random
#defining a function
def password(length):
    pw=str() #declaring a empty string
    #assigning variables to characters to produce password
    characters="abcdefghijklmnopqrstuvwxyz"+"0123456789"+"!@#$%^&*()"
    for i in range(length): #creating a for loop to run for the length of password
        pw+=random.choice(characters) #randomly going to choose and add them to pw
    return pw
#calling the function
password(10)
