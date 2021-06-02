#Word to binary

"""Write a function that takes a string and returns an array containing binary numbers equivalent to the ASCII 
codes of the characters of the string. The binary strings should be eight digits long."""

def word_to_bin(word):
    binary = []
    for char in word:
        temp = bin(ord(char))
        binary.append(temp.replace("b",""))

    return binary

print(word_to_bin("man"))
