lollish = "ololly"

print ("Hello and welcome to the lol translator!")
print ("REMEMBER: No numbers!")
Word = input("What is the word you want us to translate?: ")
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
    print ("You have typed in nothing or it contained numbers.")
    print ("Thank you for using the lol translator. See you soon!")


