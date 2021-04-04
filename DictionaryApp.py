import json
from difflib import get_close_matches
from difflib import SequenceMatcher

stuff = {"hi": 1, "bye": 2}

dictfile = "files/data.json"
fp = open(dictfile)
data = dict(json.load(fp)) #add dict() to force intellisense for now

##Sorts the results with the highest ratio at the front of the list
def sort_results(word, results):
    print("Inside sort")
    ranked_results = {}
    for result in results:
        ranked_results[result] = SequenceMatcher(None, word, result).ratio()
    
    sorted_results = sorted(ranked_results, key = lambda x: x[1], reverse = True)
    return sorted_results
    

def find_word(word):

    if word in data.keys():
        return data[word]
    elif word.capitalize() in data.keys():
        return data[word.capitalize()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        results = get_close_matches(word, data.keys())
        #Sort results based on match ratio
        results = sort_results(word, results)
        for result in results:
            yesno = input("Did you mean %s? Type 'y' for yes, 'n' for no: " % result)
            yesno = yesno.lower()
            if yesno == "y":
                return data[result]
            elif yesno == "n":
                continue
            else:
                return "Did not understand. Try another word."
        ##The user did not match a word leave
        return "Did not find your word."
        

print("Welcome to word finder 0.6")

while True:
    word = input("Enter word (.exit to exit): ").lower()
    if word == ".exit":
        break
    print(find_word(word))

print("Thank you for using this dictionary. Exiting...")

