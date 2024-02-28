"""
Caleb's Ciphernet
End-to-end message encryption.
"""
import json
import os
import random


ALPHABET = "abcdefghijklmnopqrstuvwxyz1234567890 -_=+[{]}|;:'\"/?.>,<!@#$%^&*()`~\\"
SYS_RAND = random.SystemRandom()
USER_DATA = {}
HOME = 0
PASS_ = 0
NEW_ACCOUNT = 0
CHECK_YES = ["yes", "y"]


# sign in/up
def login_or_create():
    while True:
        print("To log onto Ciphernet, please enter 1 to login.")
        print("If you do not have a account, please enter 2 to create an account.")
        user_input = input().lower()

        options = [
            ("1", "login", "log in"),
            ("2", "signin", "sign in", "create an account"),
        ]

        for i, valid_inputs in enumerate(options):
            if user_input in valid_inputs:
                return i

        print(f"'{user_input}' not a valid option.\n")


user_input = login_or_create()

while HOME == 0:
    PASS_ = 0

    if start in signin:
        print("Please enter a username...")
        new_username = input().lower()
        while PASS_ == 0:
            if os.path.isfile(new_username + ".txt"):
                print("Username is already taken, Please enter a different username...")
                new_username = input().lower()

            else:
                print(
                    "Are you sure you want your username to be "
                    + new_username
                    + "? (Yes or No)"
                )
                check_username = input().lower()
                if check_username in CHECK_YES or check_username == "":
                    print("Your username is " + new_username)
                    PASS_ = 1
                else:
                    print("Please enter a username...")
                    new_username = input()
                    PASS_ = 0
        PASS_ = 0

        while PASS_ == 0:
            print("Please enter a password...")
            new_password = input()
            print("Your pasword is " + new_password)
            print(
                "Are you sure you want you password to be "
                + new_password
                + "? (Yes or No)"
            )
            check_password = input().lower()
            if check_password in CHECK_YES or check_password == "":
                PASS_ = 1
                USER_DATA[new_username] = new_password
                USER_DATA_double_quotes = json.dumps(USER_DATA)

                with open(new_username + ".txt", "w+", encoding="utf8") as file:
                    json.dump(USER_DATA_double_quotes, file)

                print("Please log in to your new account.")
                start = 1
            else:
                PASS_ = 0

    NEW_ACCOUNT = 1

    if start in login:
        if NEW_ACCOUNT == 0:
            print("Please enter your Username and Password.")
        else:
            PASS_ = 0
            while PASS_ == 0:
                print("Enter Username...")
                username = input()

                print("Enter Password...")
                Password = input()

                if os.path.isfile(username + ".txt") is False:
                    print("Please enter a valid username and password...")
                else:
                    with open(username + ".txt", "r", encoding="utf8") as f:
                        data = f.read()
                    USER_DATA_from_file = json.loads(data)
                    USER_DATA_from_file = json.loads(USER_DATA_from_file)

                    if username in USER_DATA_from_file.keys():
                        if Password == USER_DATA_from_file[username]:
                            PASS_ = 1
                            HOME = 1

                    if PASS_ == 0:
                        print("Please enter a valid username and password.")

PASS_ = 0

while PASS_ == 0:
    print("If you would like to encode a message enter 1.")
    print("If you would like to decode a message enter 2.")
    print("If you would like to exit enter 3.")
    HOME = input().lower()
    home_accept_paramiters_for_1 = ["1", 1, "one", "encode", "encode a message"]
    home_accept_paramiters_for_2 = ["2", 2, "two", "decode", "decode a massage"]
    home_accept_paramiters_for_3 = ["3", 3, "three", "exit"]

    if HOME in home_accept_paramiters_for_1:

        if os.path.isfile(username + "_data.txt") is False:
            with open(username + "_data.txt", "w", encoding="utf8"):
                pass  # create/clear file?

        if os.path.getsize(username + "_data.txt") > 0:
            with open(username + "_data.txt", "r", encoding="utf8") as f:
                data = f.read()
            user_cipher_data_from_file = json.loads(data)
            user_cipher_data_from_file = json.loads(user_cipher_data_from_file)
        else:
            user_cipher_data_from_file = {}

        PASS_ = 0
        while PASS_ == 0:
            print("Please enter the name of the person you would like to encode for...")
            recipient = input().lower()
            if recipient in user_cipher_data_from_file.keys():
                seed = user_cipher_data_from_file[recipient]
                print(str(recipient) + "'s ID code is " + str(seed))
                PASS_ = 1

            else:
                print(
                    recipient
                    + "is not in your saved data. Would you like to create a new key for "
                    + recipient
                    + "? (Yes or No)"
                )
                Check = input().lower()
                if Check in CHECK_YES or Check == "":
                    seed = SYS_RAND.randint(0, 1000000000)
                    user_cipher_data_from_file[recipient] = seed
                    print(str(recipient) + "'s ID code is " + str(seed))

                    user_cipher_data_from_file_json_format = json.dumps(
                        user_cipher_data_from_file
                    )
                    with open(username + "_data.txt", "w", encoding="utf8") as file:
                        json.dump(user_cipher_data_from_file_json_format, file)
                    PASS_ = 1
                else:
                    PASS_ = 0

        PASS_ = 0
        random.seed(seed)

        i = 1
        book = ""
        a = 100000

        while a > 0:
            book += ALPHABET[random.randint(0, len(ALPHABET) - 1)]
            a -= 1

        open_code = {}
        # makes a list in open code for each letter.
        for letter in ALPHABET:
            open_code[letter] = []
        # Numbers eack letter in the book, then takes the letters and add the corresponding number
        # and adds it to open code.
        for i, letter in enumerate(book.lower()):
            if letter in ALPHABET:
                open_code[letter] += [i]

        print("Enter message to code...")
        secret = input()
        encode = ""
        # Codes the input
        # For each leter in the message it finds the letter in the open code and then randomly picks
        # one of the number associated with it.
        for letter in secret.lower():
            if letter in ALPHABET:
                encode += str(SYS_RAND.choice(open_code[letter])) + " "
            else:
                encode += letter

        print("Your ciphered message is...")
        print(encode)

    elif HOME in home_accept_paramiters_for_2:
        if os.path.isfile(username + "_decode_data.txt") is False:
            with open(username + "_decode_data.txt", "w", encoding="utf8"):
                pass  # create/clear file?

        if os.path.getsize(username + "_decode_data.txt") > 0:
            with open(username + "_decode_data.txt", "r", encoding="utf8") as f:
                data = f.read()
            user_cipher_data_from_file = json.loads(data)
            user_cipher_data_from_file = json.loads(user_cipher_data_from_file)
        else:
            user_cipher_data_from_file = {}

        PASS_ = 0
        while PASS_ == 0:
            print(
                "Please enter the name of the person you would like to decode a message from..."
            )
            recipient = input().lower()
            if recipient in user_cipher_data_from_file.keys():
                seed = user_cipher_data_from_file[recipient]
                PASS_ = 1

            else:
                print(
                    recipient
                    + " is not in your saved data. Would you like to create a new key for "
                    + recipient
                    + "? (Yes or No)"
                )
                Check = input().lower()
                if Check in CHECK_YES or Check == "":
                    print("Please enter " + recipient + "'s ID code.")
                    PASS_ = 0
                    while PASS_ == 0:
                        seed = input()
                        if seed == "":
                            print("Please entera vaild ID for" + recipient)
                        else:
                            PASS_ = 1
                    user_cipher_data_from_file[recipient] = seed

                    user_cipher_data_from_file_json_format = json.dumps(
                        user_cipher_data_from_file
                    )
                    with open(username + "_decode_data.txt", "w", encoding="utf8") as file:
                        json.dump(user_cipher_data_from_file_json_format, file)
                    PASS_ = 1
                else:
                    PASS_ = 0

        PASS_ = 0
        random.seed(seed)

        i = 1
        book = ""
        a = 100000

        while a > 0:
            book += ALPHABET[random.randint(0, len(ALPHABET) - 1)]
            a -= 1

        open_code = {}
        # makes a list in open code for each letter.
        for letter in ALPHABET:
            open_code[letter] = []


        # Numbers eack letter in the book, then takes the letters and add the corresponding number
        # and adds it to open code.
        for i, letter in enumerate(book.lower()):
            if letter in ALPHABET:
                open_code[letter] += [i]

        print("Enter cipher...")
        code = input()
        decoded = ""
        # Decodes entered numbers.
        # It takes the numbers seprates them from each other then finds the number in book
        # and adds it to decoded if it can not find a number it prints it as is.
        for x in code.split(" "):
            try:
                decoded += book[int(x)].lower()
            except KeyError:
                decoded += " " if x == "" else x
        print(decoded)

    elif HOME in home_accept_paramiters_for_3:
        PASS_ = 1

    else:
        print("Invalid input")
