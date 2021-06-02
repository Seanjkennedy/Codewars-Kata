#If you can read this...

"""Task
You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).
Input:
If, you can read?
Output:
India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?
Note:
The set of used punctuation is .!?.
Punctuation should be kept in your return string, but spaces should not.
Xray should not have a dash within.
Every word and punctuation mark should be seperated by a space ' '.
There should be no trailing whitespace"""

def to_nato(words):
    nato_phone_alpha = {
    'a' : "Alfa",
    'b' : "Bravo",
    'c' : "Charlie",
    'd' : "Delta",
    'e' : "Echo",
    'f' : "Foxtrot",
    'g' : "Golf",
    'h' : "Hotel",
    'i' : "India",
    'j' : "Juliett",
    'k' : "Kilo",
    'l' : "Lima",
    'm' : "Mike",
    'n' : "November",
    'o' : "Oscar",
    'p' : "Papa",
    'q' : "Quebec",
    'r' : "Romeo",
    's' : "Sierra",
    't' : "Tango",
    'u' : "Uniform",
    'v' : "Victor",
    'w' : "Whiskey",
    'x' : "Xray",
    'y' : "Yankee",
    'z' : "Zulu",
    '.' : ".",
    '!' : "!",
    '?' : "?"
    }
    answer = ""
    phrase_split = words.lower().split()
    for word in phrase_split:
        for letter in word:
            answer += nato_phone_alpha[letter] + " "
    return answer.rstrip()



print(to_nato('If you can read'), "\nIndia Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta")
print(to_nato('Did not see that coming'), "\nDelta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf")
print(to_nato('.d?d!'),'\n. Delta ? Delta !')
