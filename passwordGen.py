import random 
import string

password = string.ascii_letters + string.punctuation + string.digits

def passwordGenerator():
    
        choice = input("do you want to generate password? ").lower()


        if choice == "yes":
            try :
                n=int(input("no of digits in password : "))
                new_password = random.choices(password,k=n)
                print("new password = ",new_password)
            except ValueError:
                  print("invalid input, please input numbers")


        elif   choice == "no":
                print("thank u ")
        else:
            print("invalid input ")  
        


passwordGenerator()

