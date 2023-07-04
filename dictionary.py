import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(wordToSearch):
    wordToSearch=wordToSearch.lower()
    if wordToSearch in data:
        return data[wordToSearch]
    elif wordToSearch.title() in data:
        return data[wordToSearch.title()]
    elif wordToSearch.upper() in data:
        return data[wordToSearch.upper()]
    elif len(get_close_matches(wordToSearch, data.keys()))>0:
        print("Is this the word you are looking for: %s" %get_close_matches(wordToSearch,data.keys())[0])
        decide = input("Press y for YES or n for NO -> ")
        if decide == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n":
            return "No definition found in the dictionary for the given word."
        else:
            return "The input is wrong. Please use y or n."
    else:
        return "No definition found in the dictionary for the given word."



word = input("Please enter the word to search for: ")
output = translate(word)
# print(type(output))

counter = 1
if type(output) == list:
    for item in output:
        print("Definition "+str(counter)+": "+item)
        counter+=1
else:
    print("Definition: "+str(output))

