import json
import difflib
from difflib import get_close_matches

data = json.load(open("D:\\Python Tutorial\\learning-python\\CODE\\Application 1\\data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        meaning = data[word]
        return meaning;
    else:
        CloseWordList = get_close_matches(word,data.keys())
        if bool(CloseWordList):
            possibleWord = CloseWordList[0]
            return "Did you mean " + possibleWord + "?"
        else:
            return "Wrong Word Input"

userWord = input("Enter a word: ")

print(translate(userWord))
