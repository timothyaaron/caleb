import random
import os
import json


sysrand = random.SystemRandom()
current_user = ""
user_data = {}
home = 0
Pass = 0
New_account = 0
Check_yes = ["yes", "y"]
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890 -_=+[{]}|;:'\"/?.>,<!@#$%^&*()`~\\"

while Pass == 0:
  print("To log onto Ciphernet, please enter 1 to login.")
  print("If you do not have a account, please enter 2 to create an account.")
  Start = input().lower()

  Login = ["1", 1, "login", "log in"]
  Signin = ["2", 2, "signin", "sign in", "create an account"]

  if Start in Login:
    Pass = 1
  elif Start in Signin:
    Pass = 1

  else:
    print("Invalid input")

while home == 0:

  Pass = 0

  if Start in Signin:
      print("Please enter a username...")
      new_username = input().lower()
      while Pass == 0:

        if os.path.isfile(rReplace + "\\" + new_username + ".txt") == True:
            print("Username is already taken, Please enter a different username...")
            new_username = input().lower()

        else:
            print("Are you sure you want your username to be " + new_username + "? (Yes or No)")
            Check_username = input().lower()
            if Check_username in Check_yes or Check_username == "":
                print("Your username is " + new_username)
                Pass = 1
            else:
              print("Please enter a username...")
              new_username = input()
              Pass = 0
      Pass = 0

      while Pass == 0:
          print("Please enter a password...")
          new_password = input()
          print("Your pasword is " + new_password)
          print("Are you sure you want you password to be " + new_password + "? (Yes or No)")
          Check_password = input().lower()
          if Check_password in Check_yes or Check_password == "":
            Pass = 1
            user_data[new_username] = new_password
            user_data_double_quotes = json.dumps(user_data)

            with open(rReplace + "\\" + new_username + ".txt", "w+") as file:
              json.dump(user_data_double_quotes, file)

            print("Please log in to your new account.")
            Start = 1
          else:
            Pass = 0

  New_account = 1

  if Start in Login:
      if New_account == 0:
        print("Please enter your Username and Password.")
      else:
        Pass = 0
        while Pass == 0:
          print("Enter Username...")
          Username = input()
          print("Enter Password...")
          Password = input()
          if os.path.isfile(rReplace + "\\" + Username + ".txt") == False:
             print("Please enter a valid username and password...")
          else:
            with open(rReplace + "\\" + Username + ".txt", "r") as f:
              data = f.read()
            user_data_from_file = json.loads(data)
            user_data_from_file = json.loads(user_data_from_file)

            if Username in user_data_from_file.keys():

              if Password == user_data_from_file[Username]:
                  Pass = 1
                  home = 1



            if Pass == 0:
              print("Please enter a valid username and password.")


#print(sysrand.randint(0,1000000000))

#Seed = input("Please enter a seed...")
#print()

Pass = 0

while Pass == 0:
  print("If you would like to encode a message enter 1.")
  print("If you would like to decode a message enter 2.")
  print("If you would like to exit enter 3.")
  Home = input().lower()
  Home_accept_paramiters_for_1 = ["1", 1, "one", "encode", "encode a message"]
  Home_accept_paramiters_for_2 = ["2", 2, "two", "decode", "decode a massage"]
  Home_accept_paramiters_for_3 = ["3", 3, "three", "exit"]

  if Home in Home_accept_paramiters_for_1:

    if os.path.isfile(rReplace + "\\" + Username + "_data.txt") == False:
        Cipher_file = open(rReplace + "\\" + Username + "_data.txt", "w")
        Cipher_file.close()

    if os.path.getsize(rReplace + "\\" + Username + "_data.txt") > 0:
        with open(rReplace + "\\" + Username + "_data.txt", "r") as f:
            data = f.read()
        user_cipher_data_from_file = json.loads(data)
        user_cipher_data_from_file = json.loads(user_cipher_data_from_file)
    else:
        user_cipher_data_from_file = {}

    Pass = 0
    while Pass == 0:
      print("Please enter the name of the person you would like to encode for...")
      recipient = input().lower()
      if recipient in user_cipher_data_from_file.keys():
        Seed = user_cipher_data_from_file[recipient]
        print(str(recipient) + "'s ID code is " + str(Seed))
        Pass = 1

      else:
        print(recipient + "is not in your saved data. Would you like to create a new key for " + recipient +"? (Yes or No)")
        Check = input().lower()
        if Check in Check_yes or Check == "":
          Seed = sysrand.randint(0,1000000000)
          user_cipher_data_from_file[recipient] = Seed
          print(str(recipient) + "'s ID code is " + str(Seed))

          user_cipher_data_from_file_json_format = json.dumps(user_cipher_data_from_file)
          with open(rReplace + "\\" + Username + "_data.txt", "w") as file:
            json.dump(user_cipher_data_from_file_json_format, file)
          Pass = 1
        else:
           Pass = 0

    Pass = 0
    random.seed(Seed)


    i = 1
    book = ""
    a = 100000

    while a > 0:

      book += alphabet[random.randint(0,len(alphabet)-1)]
      a -= 1


    open_code = {}
    # makes a list in open code for each letter.
    for letter in alphabet:
      open_code[letter] = []
    # Numbers eack letter in the book, then takes the letters and add the corresponding number and adds it to open code.
    for i, letter in enumerate(book.lower()):
      if letter in alphabet:
        open_code[letter] += [i]

    print("Enter message to code...")
    secret = input()
    Encode =  ""
    # Codes the input
    # For each leter in the message it finds the letter in the open code and then randomly picks one of the number associated with it.
    for letter in secret.lower():
      if letter in alphabet:
        Encode += str(sysrand.choice(open_code[letter])) + " "
      else:
        Encode += letter

    print("Your ciphered message is...")
    print (Encode)

  elif Home in Home_accept_paramiters_for_2:
    if os.path.isfile(rReplace + "\\" + Username + "_decode_data.txt") == False:
      Cipher_file = open(rReplace + "\\" + Username + "_decode_data.txt", "w")
      Cipher_file.close()

    if os.path.getsize(rReplace + "\\" + Username + "_decode_data.txt") > 0:
        with open(rReplace + "\\" + Username + "_decode_data.txt", "r") as f:
            data = f.read()
        user_cipher_data_from_file = json.loads(data)
        user_cipher_data_from_file = json.loads(user_cipher_data_from_file)
    else:
        user_cipher_data_from_file = {}

    Pass = 0
    while Pass == 0:
        print("Please enter the name of the person you would like to decode a message from...")
        recipient = input().lower()
        if recipient in user_cipher_data_from_file.keys():
            Seed = user_cipher_data_from_file[recipient]
            Pass = 1

        else:
            print(recipient + " is not in your saved data. Would you like to create a new key for " + recipient +"? (Yes or No)")
            Check = input().lower()
            if Check in Check_yes or Check == "":
                print("Please enter " + recipient + "'s ID code.")
                Pass = 0
                while Pass == 0:
                  Seed = input()
                  if Seed == "":
                    print("Please entera vaild ID for" + recipient)
                  else:
                     Pass = 1
                user_cipher_data_from_file[recipient] = Seed

                user_cipher_data_from_file_json_format = json.dumps(user_cipher_data_from_file)
                with open(rReplace + "\\" + Username + "_decode_data.txt", "w") as file:
                  json.dump(user_cipher_data_from_file_json_format, file)
                Pass = 1
            else:
                Pass = 0

    Pass = 0
    random.seed(Seed)



    i = 1
    book = ""
    a = 100000

    while a > 0:

      book += alphabet[random.randint(0,len(alphabet)-1)]
      a -= 1

    open_code = {}
    # makes a list in open code for each letter.
    for letter in alphabet:
      open_code[letter] = []
    # Numbers eack letter in the book, then takes the letters and add the corresponding number and adds it to open code.
    for i, letter in enumerate(book.lower()):
      if letter in alphabet:
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

  elif Home in Home_accept_paramiters_for_3:
    Pass = 1

  else:
    print("Invalid input")
