# Assignment 13
# Michael Duong
# Sept. 9, 2021
# Password System

import json
import random
import string

# Lists
lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~', '!', '@', '$', '%', '^', '&', '*', '(', ')']
counter = 3
counter2 = 0
counter4 = 0
counter5 = 0
counter6 = 0

# Statement
while_true_done = True

# Opens file with user list
file = open("j", "r")
x = file.readline()
user_dictionary = json.loads(x)


# Input username
username = input("Username: ")

# Checks if name is in dictionary already
if username in user_dictionary:
    password = input("Welcome back " + username + ". Please enter your password: ")
    password_box = user_dictionary.get(username)
    # if password is right
    if password in password_box:
        print("Welcome to the system " + username)
        # if password is wrong
    else:
        while True:
            # Password try again
            print("Please try again! You have " + str(counter) + " tries remaining")
            counter -= 1
            password_retry = input()
            # If he gets it right again stop the program
            if password_retry in password_box:
                print("Welcome to the system " + username)
                break
            # If there are no more tries
            elif counter == 0:
                print('System will now shutdown')
                break
            
# If the user is not in the system then it will add it            
else:
    while True:
        if while_true_done == False:
                break
        choose = input("Would you like to choose your own password or do you want the system to generate a random password (own/system) ")
        # Choosing own password
        if choose == "own":
            while True:
                password2 = input("password: ")
                    
                # Checking the characters in the password
                for x in password2:
                    if x.isupper() == True:
                        counter2 += 1
                        
                    if x.isnumeric() == True:
                        counter4 += 1
                        
                    if x in string.punctuation:
                        counter5 += 1
                    
                # Checking if there is sufficient things in the password 
                if counter2 == 0:
                    print("Missing 1 capital letter")
                    
                if counter4 == 0:
                    print("Missing 1 number")
                    
                if counter5 == 0:
                    print("Missing 1 symbol")
                
                # Password checker
                if len(password2) <= 8:
                    print("At least 8 characters")
        
                if len(password2) >= 8:
                    if counter2 >= 1:
                        if counter4 >= 1:
                            if counter5 >= 1:
                                print("Welcome to the system " + username)
                                user_dictionary[username] = password2
                                json_dictionary = json.dumps(user_dictionary)
                                file = open("j", "w")
                                file.write(json_dictionary)
                                file.close()
                                while_true_done = False
                                break
                
                    
    
    # Systems generates a password
        elif choose == "system":
            while True:
                question1 = input("number of characters? ")
                question2 = input("number of capitals? ")
                question3 = input("number of numbers? ")
                question4 = input("number of symbols? ")
                together = (question1 + question2 + question3 + question4)
                
                # If the user inputs numbers it is true
                if together.isnumeric() == True:
        
                    number_lowercase = (int(question2) + int(question3) + int(question4))
                    if int(question1) >= number_lowercase:
                        
                        lower_case = (int(question1) - number_lowercase)
                        # Randomly selects characters
                        system_password = random.choices(lower_alphabet, k = int(lower_case))
                        system_password2 = random.choices(alphabet, k = int(question2))
                        system_password3 = random.choices(numbers, k = int(question3))
                        system_password4 = random.choices(symbols, k = int(question4))

                        # joins the characters together
                        joins = ''.join(system_password)
                        joins2 = ''.join(system_password2)
                        joins3 = ''.join(system_password3)
                        joins4 = ''.join(system_password4)              
                        stringer = (joins + joins2 + joins3 + joins4)
                        
                        real_password = random.sample(stringer, k = int(question1))
                        
                        print("Your password is: " + "".join(real_password))
                        
                        # Saves password and username into json file
                        user_dictionary[username] = stringer
                        json_dictionary = json.dumps(user_dictionary)
                        file = open("j", "w")
                        file.write(json_dictionary)
                        file.close()
                        while_true_done = False
                        break
                    else:
                        # If user does not pick enough characters
                        print("Not enough characters, try again!")
                else:
                    if together.isnumeric() == False:
                        # If use does not use numbers
                        print("Use numbers")
            if while_true_done == False:
                break
            
        else:
            # If it is the wrong input
            print("Error!")
            


