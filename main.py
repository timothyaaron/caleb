import random
import os
import json 


ALPHABET = "abcdefghijklmnopqrstuvwxyz1234567890 -_=+[{]}|;:'\"/?.>,<!@#$%^&*()`~\\"
OPTIONS = {

    "yes": ["yes", "y", ""],
    "login": ["1", 1, "login", "log in"],
    "sign_up": ["2", 2, "sign_up", "sign up", "create an account"],
    "encipher_message_input": ["1", 1, "one", "encode", "encode a message"],
    "decipher_message_input": ["2", 2, "two", "decode", "decode a massage"],
    "log_out": ["3", 3, "three", "log out"],
    "exit_program_input": ["4", 4, "four", "exit"]

}
FILE_LOCATION = r"C:\Users\cloni\Documents\VS Code\Ciphernet Users"
SYS_RAND = random.SystemRandom()

user_data = {}
home_screen_input = ""


def should_sign_up():
    while True:
        print("To log onto Ciphernet, please enter 1")
        print("If you do not have a account, please enter 2")
        user_input = input().lower()

        if user_input in OPTIONS["login"]:
            return False

        elif user_input in OPTIONS["sign_up"]:
            return True

        else:
            print("Invalid input")


def sign_up():
    while True:
        print("Please enter a username...")
        new_username = input()
        path = f"{FILE_LOCATION}{os.sep}{new_username}{os.sep}{new_username}'s_data"

        if os.path.isfile(f"{path}{os.sep}{new_username}'s_data.txt"):
            print("Username is already taken")

    
        else:
            print(f"Are you sure you want your username to be {new_username}? (Yes or No)")
            confirm_usernameb = input()
            if confirm_usernameb in OPTIONS["yes"]:
                print(f"Your username is {new_username}")
                break

    

    while True:
          print("Please enter a password...")
          new_password = input()
          print(f"Your pasword is {new_password}")
          print(f"Are you sure you want you password to be {new_password}? (Yes or No)")
          check_password = input().lower()
          if check_password in OPTIONS["yes"]:
            user_data[new_username] = new_password
            user_data_double_quotes = json.dumps(user_data)            
            
            try:
                os.makedirs(path)
            except OSError as error:
              print(error)
            
            with open(f"{path}{os.sep}{new_username}'s_data.txt", "w+") as file:
              json.dump(user_data_double_quotes, file)
            
            print("Please log in to your new account.")
            break


def log_in():
    while True:
        print("Enter username...")
        username = input()
        print("Enter Password...")
        password = input()
        global path
        path = f"{FILE_LOCATION}{os.sep}{username}{os.sep}{username}'s_data"

        if os.path.isfile(f"{path}{os.sep}{username}'s_data.txt") is False:
            print("Please enter a valid username and password...")
        else:
            with open(f"{path}{os.sep}{username}'s_data.txt") as f: 
                data = f.read()
            user_data_from_file = json.loads(data)
            user_data_from_file = json.loads(user_data_from_file)
            try:
                if username in user_data_from_file.keys():
                    if password in user_data_from_file[username]:
                        return username
                print("Please enter a valid username and password")
            except:
                print("Please enter a valid username and password.")


def home_screen():      

    while True:
        print("If you would like to encode a message enter 1.")
        print("If you would like to decode a message enter 2.")
        print("if you would like to log out enter 3.")
        print("If you would like to exit enter 4.")
        
        home_screen_input = input().lower()
        return home_screen_input
    

def encipher(username):
        encipher_path = f"{path}{os.sep}{username}'s_enciphering_data.txt"
        if os.path.isfile(encipher_path) == False:
            open(encipher_path, "w").close()
            
        #user_cipher_data_from_file = json.loads(data)
        #user_cipher_data_from_file = json.loads(user_cipher_data_from_file)
                



        if os.path.getsize(encipher_path) > 0:
            with open(encipher_path, "r") as f: 
                data = f.read()
            user_cipher_data_from_file = json.loads(data)
            user_cipher_data_from_file = json.loads(user_cipher_data_from_file)
        else:
            user_cipher_data_from_file = {}

        
        while True:
            print("Please enter the name of the person you would like to encode for...")
            recipient = input().lower()
            if recipient in user_cipher_data_from_file.keys():
                seed_ = user_cipher_data_from_file[recipient]
                print(f"{recipient}'s ID code is {seed_}")
                break

            else:
                print(recipient + " is not in your saved data. Would you like to create a new key for " + recipient +"? (Yes or No)")
                User_input = input().lower()
                if User_input in OPTIONS["yes"]:
                    seed_ = SYS_RAND.randint(0,1000000000)
                    user_cipher_data_from_file[recipient] = seed_
                    print(f"{recipient}'s ID code is {seed_}")

                    user_cipher_data_from_file_json_format = json.dumps(user_cipher_data_from_file)
                    with open(encipher_path, "w") as file: 
                        json.dump(user_cipher_data_from_file_json_format, file)
                    break



        random.seed(seed_)


        i = 1
        book = ""
        a = 100000

        while a > 0:

            book += ALPHABET[random.randint(0,len(ALPHABET)-1)]
            a -= 1


        open_code = {}
        # makes a list in open code for each letter.
        for letter in ALPHABET:
            open_code[letter] = []
        # Numbers eack letter in the book, then takes the letters and add the corresponding number and adds it to open code.
        for i, letter in enumerate(book.lower()):
            if letter in ALPHABET:
                open_code[letter] += [i]

        print("Enter message to code...")
        secret = input()
        encode =  ""
        # Codes the input
        # For each leter in the message it finds the letter in the open code and then randomly picks one of the number associated with it.
        for letter in secret.lower():
            if letter in ALPHABET:
                encode += str(SYS_RAND.choice(open_code[letter])) + " "
            else:
                encode += letter

        print("Your ciphered message is...")
        print (encode)
        with open(path + "_enciphered_message.txt", "w+") as file:
            file.write(encode)


def decipher(username):
        decipher_path = f"{path}{os.sep}{username}'s_deciphering_data.txt"
        if os.path.isfile(decipher_path) == False:
            Cipher_file = open(decipher_path, "w")
            Cipher_file.close()

        if os.path.getsize(decipher_path) > 0:
            with open(decipher_path, "r") as f: 
                user_cipher_data_from_file = json.loads(json.loads(f.read()))

        else:
            user_cipher_data_from_file = {}


        while True:
            print("Please enter the name of the person you would like to decode a message from...")
            recipient = input().lower()
            if recipient in user_cipher_data_from_file.keys():
                seed_ = user_cipher_data_from_file[recipient]
                break
                
            else:
                print(recipient + " is not in your saved data. Would you like to create a new key for " + recipient +"? (Yes or No)")
                Check = input().lower()

                if Check in OPTIONS["yes"] or Check == "":
                    print("Please enter " + recipient + "'s ID code.")

                    while True:
                        seed_ = input()
                        res = seed_.isdigit()
                    
                        if res == True:
                            seed_ = int(seed_)
                            break
                        else:
                            print("Please enter a valid ID for " + recipient)
                    user_cipher_data_from_file[recipient] = seed_

                    user_cipher_data_from_file_json_format = json.dumps(user_cipher_data_from_file)
                    with open(decipher_path, "w") as file: 
                        json.dump(user_cipher_data_from_file_json_format, file)
                    break


        random.seed(int(seed_))



        i = 1
        book = ""
        a = 100000

        while a > 0:

            book += ALPHABET[random.randint(0,len(ALPHABET)-1)]
            a -= 1

        open_code = {}
        # makes a list in open code for each letter.
        for letter in ALPHABET:
            open_code[letter] = []
        # Numbers eack letter in the book, then takes the letters and add the corresponding number and adds it to open code.
        for i, letter in enumerate(book.lower()):
            if letter in ALPHABET:
                open_code[letter] += [i]

        print("Enter cipher...")
        code = input()
        decoded = ""
        # Decodes entered numbers.
        # It takes the numbers seprates them from each other then finds the number in book and adds it to decoded if it can not find a number it prints it as is.
        for x in code.split(" "):
            try:
                decoded += book[int(x)].lower()
            except:
                decoded += " " if x == "" else x
        print(decoded)
        with open(f"{FILE_LOCATION}{os.sep}{username}{os.sep}{username}_deciphered_message.txt", "w+") as file:
            file.write(decoded)


def run_program():
    if should_sign_up():
        sign_up()
    
    username = log_in()

    while True:
        
        home_screen_input = home_screen()

        if home_screen_input in OPTIONS["encipher_message_input"]:
            encipher(username)

        elif home_screen_input in OPTIONS["decipher_message_input"]:
            decipher(username)

        elif home_screen_input in OPTIONS["log_out"]:
            if should_sign_up():
                sign_up()
            username = log_in()

        if home_screen_input in OPTIONS["exit_program_input"]:
            print("Exiting Program")
            break

        else:
            print("Invalid input")


run_program()
