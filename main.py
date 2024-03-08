import random
import os
import json


ALPHABET = "abcdefghijklmnopqrstuvwxyz1234567890 -_=+[{]}|;:'\"/?.>,<!@#$%^&*()`~\\"
OPTS = {
    "yes": ["yes", "y", ""],
    "login": ["1", 1, "login", "log in"],
    "sign_up": ["2", 2, "sign_up", "sign up", "create an account"],
}
FILE_LOCATION = r"C:\Users\cloni\Documents\VS Code\Ciphernet Users"

log_in_or_sign_up_var = 0
sys_rand = random.SystemRandom()
current_user = ""
user_data = {}
home = pass_ = New_account = 0
home_accept_paramiters_for_1 = ["1", 1, "one", "encode", "encode a message"]
home_accept_paramiters_for_2 = ["2", 2, "two", "decode", "decode a massage"]
home_accept_paramiters_for_3 = ["3", 3, "three", "exit"]
home_screen_input = ""


def should_signup_first():
    while True:
        print("To log onto Ciphernet, please enter 1")
        print("If you do not have a account, please enter 2")
        user_input = input().lower()

        if user_input in OPTS["login"]:
            return False
        elif user_input in OPTS["sign_up"]:
            return True
        else:
            print("Invalid input")


def sign_up():
    while True:
        print("Please enter a username...")
        new_username = input()
        path = f"{FILE_LOCATION}/{new_username}/{new_username}'s_data"

        if os.path.isfile(path):
            print("username is already taken")
        else:
            print(f"Are you sure you want your username to be {new_username}? (Yes or No)")
            confirm_username = input()
            if confirm_username in OPTS["yes"]:
                print(f"Your username is {new_username}")
                break

    while True:
          print("Please enter a password...")
          new_password = input()
          print(f"Your pasword is {new_password}")

          print(f"Are you sure you want you password to be {new_password}? (Yes or No)")
          confirm_password = input().lower()
          if confirm_password in OPTS["yes"]:
            user_data[new_username] = new_password
            user_data_double_quotes = json.dumps(user_data)

            try:
                os.makedirs(path)
                with open(f"{path}\\{new_username}'s_data.txt", "w+") as file:
                    json.dump(user_data_double_quotes, file)
            except OSError as error:
                print(error)

            print("Please log in to your new account.")
            break


def log_in():
    while True:
        print("Enter username...")
        username = input()

        print("Enter Password...")
        password = input()

        path = f"{FILE_LOCATION}\\{username}\\{username}'s_data"

        if os.path.isfile(f"{path}\\{username}'s_data.txt"):
            with open(f"{path}\\{username}'s_data.txt", "r") as f:
                user_data = json.loads(json.loads(f.read()))

            if password == user_data.get(username):
                    return username

            print("Please enter a valid username and password.")
        else:
            print("Please enter a valid username and password...")


def home_screen():
    pass_ = 0

    while pass_ == 0:
        print("If you would like to encode a message enter 1.")
        print("If you would like to decode a message enter 2.")
        print("If you would like to exit enter 3.")
        global home_screen_input
        home_screen_input = input().lower()
        pass_ = 1


def encipher(username):
        if os.path.isfile(path + "\\" + username + "'s_enciphering_data.txt") == False:

            Cipher_file = open(path + "\\" + username + "'s_enciphering_data.txt", "w")
            Cipher_file.close()

        if os.path.getsize(path + "\\" + username + "'s_enciphering_data.txt") > 0:
            with open(path + "\\" + username + "'s_enciphering_data.txt", "r") as f:
                data = f.read()
            user_cipher_data_from_file = json.loads(data)
            user_cipher_data_from_file = json.loads(user_cipher_data_from_file)
        else:
            user_cipher_data_from_file = {}

        pass_ = 0
        while pass_ == 0:
            print("Please enter the name of the person you would like to encode for...")
            recipient = input().lower()
            if recipient in user_cipher_data_from_file.keys():
                seed_ = user_cipher_data_from_file[recipient]
                print(str(recipient) + "'s ID code is " + str(seed_))
                pass_ = 1

            else:
                print(recipient + " is not in your saved data. Would you like to create a new key for " + recipient +"? (Yes or No)")
                Check = input().lower()
                if Check in CHECK_YES or Check == "":
                    seed_ = sys_rand.randint(0,1000000000)
                    user_cipher_data_from_file[recipient] = seed_
                    print(str(recipient) + "'s ID code is " + str(seed_))

                    user_cipher_data_from_file_json_format = json.dumps(user_cipher_data_from_file)
                    with open(path + "\\" + username + "'s_enciphering_data.txt", "w") as file:
                        json.dump(user_cipher_data_from_file_json_format, file)
                    pass_ = 1
                else:
                    pass_ = 0

        pass_ = 0
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
                encode += str(sys_rand.choice(open_code[letter])) + " "
            else:
                encode += letter

        print("Your ciphered message is...")
        print (encode)
        with open(path + "_enciphered_message.txt", "w+") as file:
              json.dump(encode, file)


def decipher(username):
        if os.path.isfile(path + "\\" + username + "'s_deciphering_data.txt") == False:
            Cipher_file = open(path + "\\" + username + "'s_deciphering_data.txt", "w")
            Cipher_file.close()

        if os.path.getsize(path + "\\" + username + "'s_deciphering_data.txt") > 0:
            with open(path + "\\" + username + "'s_deciphering_data.txt", "r") as f:
                data = f.read()
            user_cipher_data_from_file = json.loads(data)
            user_cipher_data_from_file = json.loads(user_cipher_data_from_file)
        else:
            user_cipher_data_from_file = {}

        pass_ = 0
        while pass_ == 0:
            print("Please enter the name of the person you would like to decode a message from...")
            recipient = input().lower()
            if recipient in user_cipher_data_from_file.keys():
                seed_ = user_cipher_data_from_file[recipient]
                pass_ = 1

            else:
                print(recipient + " is not in your saved data. Would you like to create a new key for " + recipient +"? (Yes or No)")
                Check = input().lower()
                if Check in CHECK_YES or Check == "":
                    print("Please enter " + recipient + "'s ID code.")
                    pass_ = 0
                    while pass_ == 0:
                        seed_ = input()
                        res = seed_.isdigit()

                        if res == True:
                            pass_ = 1
                            seed_ = int(seed_)
                        else:
                            print("Please enter a valid ID for " + recipient)
                    user_cipher_data_from_file[recipient] = seed_

                    user_cipher_data_from_file_json_format = json.dumps(user_cipher_data_from_file)
                    with open(path + "\\" + username + "'s_deciphering_data.txt", "w") as file:
                        json.dump(user_cipher_data_from_file_json_format, file)
                    pass_ = 1
                else:
                    pass_ = 0




        pass_ = 0
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
        with open(FILE_LOCATION + "\\" + username + "\\" + username + "_deciphered_message.txt", "w+") as file:
            json.dump(decoded, file)


def run_program():
    # signin
    if should_signup_first():
        sign_up()

    username = log_in()

    # cipher
    while home_screen_input not in home_accept_paramiters_for_3:
        home_screen()
        if home_screen_input in home_accept_paramiters_for_1:
            encipher(username)

        elif home_screen_input in home_accept_paramiters_for_2:
            decipher(username)

        elif home_screen_input in home_accept_paramiters_for_3:
            print("Exiting Program")

        else:
            print("Invalid input")


if __name__ == "__main__":
    run_program()
