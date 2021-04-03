import json

data = json.load(open("files/data.json"))

def find_word(word):
    if word in data.keys():
        return data[word]
    else:
        return "Did not find word."


print("Welcome to word finder.")

while True:
    word = input("Enter word: ")
    print(find_word(word))

