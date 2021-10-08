import json
import difflib
from difflib import get_close_matches

data = json.load(open("D:\\Python Tutorial\\learning-python\\CODE\\Application 1\\data.json"))

def translate(word):

    if word in data:
        meaning = data[word]
        if(type(meaning)==list):
            for item in meaning:
                print(item)
        else:
            print(meaning)

    else:
        word = word.lower()

        if word in data:
            meaning = data[word]
            if(type(meaning)==list):
                for item in meaning:
                    print(item)
            else:
                print(meaning)
        else:
            CloseWordList = get_close_matches(word,data.keys())
            if bool(CloseWordList):
                possibleWord = CloseWordList[0]
                confirmation = input("Did you mean " + possibleWord + "? (Write Y for Yes) ")
                if(confirmation == "Y" or confirmation == "y"):
                    if(type(data[possibleWord])==list):
                        for item in data[possibleWord]:
                            print(item)
                    else:
                        print(data[possibleWord])
                else:
                    print("Word does not exist in the dictionary.")
            else:
                print("Word does not exist in the dictionary.")

userWord = input("Enter a word: ")

translate(userWord)
