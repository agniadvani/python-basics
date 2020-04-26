def main():
    a = input("Enter a phrase: ")
    a = a.lower()
    a = remove_spaces(a)
    a = remove_punc(a)
    b = a[::-1]
    if a == b:
        print("Your sentence/word is a palindrome.")
    else:
        print("Your sentence/word is not a palindrome.")



def remove_spaces (phrase):
    for i in phrase:
        if i == ' ':
            phrase = phrase.replace(" ","")
    return phrase

def remove_punc (phrase):
    for i in phrase:
        if i == ",":
            phrase = phrase.replace(",","")
        elif:
             i == ".":
             phrase = phrase.replace(".","")
        elif:
             i == "?":
             phrase = phrase.replace("?","")
    else:
        phrase = phrase
        
    return phrase
        
main()






