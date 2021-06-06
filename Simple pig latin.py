#Simple Pig Latin
"""Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""

def pig_it(text):

    text_words = text.split()
    pig_words = []
    for word in text_words:
        if word.isalpha():
            temp = word[1:] + word[0] + "ay"
            pig_words.append(temp)
        else:
            pig_words.append(word)
    return " ".join(pig_words)

print(pig_it("This is my string"))
print(pig_it('Hello world !'))
