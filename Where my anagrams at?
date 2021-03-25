#Where my anagrams at?

"""Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none. For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []"""

words_1 = 'abba'

list_1 = ['aabb', 'abcd', 'bbaa', 'dada']

# attempt 1

def anagrams(word, words):

    word_copy = sorted(word)
    matches = []

    for wrd in words:
        if sorted(wrd) == word_copy:
            matches.append(wrd)

    return matches

print(anagrams(words_1, list_1))

# refactored attempt

def anagrams(word, words):
    word_copy = sorted(word)
    return [i for i in words if  sorted(i) == word_copy]

print(anagrams(words_1, list_1))
