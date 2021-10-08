import json

data = json.load(open("D:\\Python Tutorial\\learning-python\\CODE\\Application 1\\data.json"))

def translate(word):
    if word in data:
        meaning = data[word]
        return meaning;
    else:
        return "Word not found"

userWord = input("Enter a word: ")

print(translate(userWord))
