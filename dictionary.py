import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        q = input ("Did you mean %s instead? Enter Y(yes) or N(no):" % get_close_matches(w, data.keys())[0])
        if q == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif q == "N":
            return "The word doesn't exist. Please try again."
        else:
            return "Hmmm, didn't understand that..."
            
    else:
        return "The word doesn't exist. Please check it, and try again!"


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

