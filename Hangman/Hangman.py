import random
import time

words = ["Fans", "Alright", "Bye", "Hello", "Friend", "Microphone", "Computer", "Television", "Help", "Desk", "Toilet", "Tissue", "Webcam", "Funny", "Jokster", "Joking", "Coding", "Laptop", "Desktop", "Graphics", "Central", "Centre", "Window", "Camera", "Keyboard", "Mouse", "Spider", "Filter", "Racing", "Wheel", "Favourite", "Ring", "Bulb", "Light", "Screen", "Alexa", "Amazon", "Plate", "Spoon", "Forks", "Table", "Wardrobe", "Cupboard", "Cutting", "Handle", "Knob", "Board", "Teaspoon", "Tablespoon", "Issue", "Annoying", "Police", "Pursuit", "Vehicles", "Potato"]
hangmanl = []
gletters = []
ugletters = []
indexs = []

word = ""
inp = ""

data = 0
bes = 0
suc = 1
tgu = 0
att = 0
timee = 0
endte = 0

def start():
    global hangmanl
    global ugletters
    global timee
    global gletters
    global words
    global word
    global suc
    global inp
    global tgu
    global att

    suc = 1
    att = 0
    tgu = 0

    gletters = []
    ugletters = []
    hangmanl = []
    
    inp = ""

    timee = time.time()
    word = words[random.randint(0, len(words) - 1)]
    print("The word I have chosen has " + str(len(word)) + " characters long.")

    for i in range(len(word)):
        hangmanl.append("_")

start()

def findletters():
    global tgu
    global suc
    global word
    global inp
    global endte
    global timee
    global indexs
    global hangmanl

    indexs = []

    for i in range(len(word)):
        if inp.lower() in word.lower()[i]:
            indexs.append(i)
    for i in range(len(indexs)):
        gletters.append(inp.lower())
        hangmanl[indexs[i]] = inp
        print(str(hangmanl))
        suc += 1

def game():
    global gletters
    global ugletters
    global gstring
    global data
    global count2
    global word
    global inp
    global tgu
    global att
    global bes

    global suc
    inp = input("")

    if inp.lower() in word.lower() and len(inp) == 1 and att < 9:
        if inp.lower() in gletters:
            print("Please guess a letter you haven't guessed already.")
            game()
        else:
            if suc >= len(word):
                endte = time.time()
                print("Congratulations! The word was " + str(word) + "! You completed the game in " + str(round(endte - timee, 3)) + " seconds!")
                bes = round(endte - timee, 3)

                with open("Data.txt", "r+") as f:
                    data = f.read()
                    f.seek(0)
                    if float(data) < int(bes):
                        bes = float(data)
                    else:
                        bes = round(endte - timee, 3)
                        f.write(str(round(endte - timee, 3)))

                print("Your current fastest time is " + str(bes) + "!")
                start()
                game()
            else:
                findletters()
                game()
    elif len(inp) != 1:
        print("Please guess only one character long guesses.")
        game()
    elif att >= 10:
        print("The man has now been hanged! You have ran out of tries! The word was " + word + "!")
        start()
        game()
    else:
        if inp.lower() in ugletters:
          print("Please guess a letter you haven't guessed already.")
          game()
        else:
          att += 1
          print("Try again! " + str(inp) + " is not in the word. You have " + str(11 - att) + " attempts remaining.")
          ugletters.append(str(inp))
          game()
game()