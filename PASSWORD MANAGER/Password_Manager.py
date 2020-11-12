######################
# Password Manager #
######################

import secrets
import os

def CStart():
    chars = 'qwertyuiopasdfghjklzxcvbnm~`1234567890-=!@#$%^&*()_+[]{};:|\<>,./?'

    action = input("/")
    print("")
    print("")
    print("  Action  ·" + action)
    print("")
    print("")

    if action == "PassGen":

        length = input("How Long Do You Want Your Passwords To Be?")
        length = int(length)

        username = input("What Username Do You Want Your Password To Be Linked To?")

        for p in range(1):
            password = ''
            for characters in range(length):
                password += secrets.choice(chars)
        print(username + "  ·  [  " +  password  + "  ]")
        f = open('Password List.txt','a')
        password_list = f.write('\n' + username + "  ·  [  " +  password  + "  ]")
        f.close()
        CStart()

    elif action == "Help":
        f = open('Help.txt','r')
        message = f.read()
        print(message)
        f.close()
        CStart()

    else:
        f = open('Help.txt','r')
        message = f.read()
        print(message)
        f.close()
        CStart()
CStart()