import cryptocode
from password_generator import PasswordGenerator
import maskpass
import os
from subprocess import Popen
import subprocess
import time
import sys


def main():
    class userload():
        def __init__(self,name,password,key,n):
            self.name = name
            self.password = password
            self.key =key

            if n == 1:
                try:
                    f=open(f'db/{self.name}.txt', "r")
                except:
                    p=Popen("lock2.bat", cwd=os.getcwd())
                    time.sleep(1)
                    try:
                        f=open(f'db/{self.name}.txt', "r")
                    except:
                        print("no such user found please register first\n")
                        return
                self.file=[line.strip() for line in f]
                if cryptocode.decrypt(self.file[1],self.key)== self.password:
                    print("You have successfully logged in\n")
                else:
                    print("Wrong password !\n")
                f.close()

            else:
                if(os.path.isdir("db")):
                    if(os.path.isfile(f'db/{self.name}.txt')):
                        print("user already exists login please\n")
                        return
                    else:
                        f=open(f'db/{self.name}.txt', "w")
                else:
                    p=Popen("lock2.bat", cwd=os.getcwd())
                    time.sleep(1)
                    try:
                        f=open(f'db/{self.name}.txt', "w")
                    except:
                        print("da got you")
                        time.sleep(10)
                encryptpassword=cryptocode.encrypt(self.password,self.key)
                f.write(f"{self.name}\n{encryptpassword}\n")
                f.close()
                try:
                    f=open(f'db/{self.name}.txt', "r")
                except:
                    p=Popen("lock2.bat", cwd=os.getcwd())
                    time.sleep(1)
                    f=open(f'db/{self.name}.txt', "r")
                self.file=[line.strip() for line in f]
                print("you have successfully registered\n")
                f.close()

        def add(self):
            self.website=input("enter the website: ")
            self.username=input("enter the username: ")
            self.wpassword=maskpass.askpass(prompt="Password:", mask="#")
            ewpassword=cryptocode.encrypt(self.wpassword,self.key)
            f=open(f'db/{self.name}.txt', "a")
            f.write(f"{self.website}\n{self.username}\n{ewpassword}\n")
            f.close()
            try:
                f=open(f'db/{self.name}.txt', "r")
            except:
                p=Popen("lock2.bat", cwd=os.getcwd())
                time.sleep(1)
                f=open(f'db/{self.name}.txt', "r")
            self.file=[line.strip() for line in f]
            print("password added successfully\n")
            f.close()

        def get(self):
            self.website=input("enter the website: ")
            for i in range(2,len(self.file),3):
                if self.file[i]==self.website:
                    print("your password is: ",cryptocode.decrypt(self.file[i+2],self.key),"\n")
                    break
            else:
                print("no such website found \n")

        def getall(self):
            print("your passwords are: \n")
            print("website username password\n")
            for i in range(2,len(self.file),3):
                print(self.file[i],self.file[i+1],cryptocode.decrypt(self.file[i+2],self.key),"\n")

        def generate(self):
            self.website=input("enter the website: ")
            self.username=input("enter the username: ")
            len=int(input("enter the length of the password(6-16): "))
            if len<6 or len>16:
                print("invalid length\n")
                return
            minu=int(input("enter the minimum no of uppercase letters: "))
            minl=int(input("enter the minimum no of lowercase letters: "))
            minn=int(input("enter the minimum no of numbers: "))
            mins=int(input("enter the minimum no of special characters: "))
            pwo=PasswordGenerator()
            pwo.minlen=len
            pwo.minuchars=minu
            pwo.minlchars=minl
            pwo.minnumbers=minn
            pwo.minschars=mins
            pwo.maxlen=len

            self.wpassword=pwo.generate()
            print("your password is: ",self.wpassword,"\n")

            print("Do you want to add this password to the bank?\n")
            print("1. Yes")
            print("2. No\n")
            choice=int(input("Enter your choice: "))
            if choice==1:
                ewpassword=cryptocode.encrypt(self.wpassword,self.key)
                f=open(f'db/{self.name}.txt', "a")
                f.write(f"{self.website}\n{self.username}\n{ewpassword}\n")
                f.close()
                try:
                    f=open(f'db/{self.name}.txt', "r")
                except:
                    p=Popen("lock2.bat", cwd=os.getcwd())
                    time.sleep(1)
                    f=open(f'db/{self.name}.txt', "r")
                self.file=[line.strip() for line in f]
                print("password added successfully\n")
                f.close()
            else:
                print("password not added\n")

    def register():
        name = input("Enter your name: ")
        password =maskpass.askpass(prompt="Password:", mask="#")
        key=input("give a secret key:")
        print("\nIT will be used as secret key to encrypt and decrypt your passwords, keep it safe\n")
        print(" your password is: ", password)
        print(" your secret key is: ", key)
        print("\n")
        global user
        user=userload(name,password,key,2)

    def login():
        name = input("Enter your name: ")
        password =maskpass.askpass(prompt="Password:", mask="#")
        key=input("give the secret key:")
        global user
        user=userload(name,password,key,1)




    p = Popen("lock2.bat", cwd=os.getcwd())
    time.sleep(3)

    print("Welcome to password manager\n")

    while True:
        print("input the respective no to choose an option\n")
        print("1. Login")
        print("2. Register")
        print("3. Generate a new password")
        print("4. Add a new password to the bank")
        print("5. Get a password from the bank")
        print("6. Get all passwords from the bank")
        print("7. Exit\n")    
        choice = int(input("Enter your choice: "))
        if choice == 1:
            login()
        elif choice == 2:
            register()
        elif choice == 3:
            try:
                user.generate()
            except:
                print("Please login or register first\n")

        elif choice == 4:
            try:
                user.add()
            except:
                print("Please login or register first\n")
        elif choice == 5:
            try:
                user.get()
            except:
                print("Please login or register first\n")
            
        elif choice == 6:
            try:
                user.getall()
            except:
                print("Please login or register first\n")

        elif choice == 7:
            p = Popen("lock2.bat", cwd=os.getcwd())
            exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        p = Popen("lock2.bat", cwd=os.getcwd())
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)



