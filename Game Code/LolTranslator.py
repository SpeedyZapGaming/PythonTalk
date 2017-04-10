""" This is the lol-translator by: SpeedyZapGaming """

# Variable
lollish = "ololly"

# Intro
print ("Hello and welcome to the lol-translator!")
print ("This translator was made for fun by SpeedyZapGaming.")
print ("If you are gonna re-upload this then please give credits to SpeedyZapGaming.")
print ("This translator does NOT accept numbers.")

# Asks for word
Word = input("What is the word you want us to translate?: ")

# Result
if len (Word) > 0 and Word.isalpha():
    TheWord = Word.lower()
    FirstLetter = TheWord[0]
    if FirstLetter == "a" or FirstLetter == "e" or FirstLetter == "i" or FirstLetter == "o" or FirstLetter == "u":
        NewWord = Word.lower() + lollish
        print ("The result is,", NewWord)
        print ("Thank you for using the lol translator. See you soon!")
    else:
        NewWord = TheWord[1:] + FirstLetter + lollish
        print("The result is,", NewWord)
        print ("Thank you for using the lol translator. See you soon!")
else:
    print ("You have typed in nothing.")
    print ("OR... You typed in numbers.")
    print ("Please restart the translator.")

""" Thank you for using the lol-translator by: SpeedyZapGaming """


