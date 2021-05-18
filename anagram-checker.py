#TODO add a description of how to use/how it works

from collections import Counter as count

def word_shredder (word):

    letterbag = count(word)
    s = sorted(letterbag.elements())
    return s

def is_anagram(word_shredde1,word_shredde2,ignore):

    letters1 = word_shredder(word_shredde1)
    letters2 = word_shredder(word_shredde2)

    if ignore:
        while " " in letters1:
            letters1.remove(" ")
        while " " in letters2:
            letters2.remove(" ")

    print(letters1)
    print(letters2)

    return letters1 == letters2

print("please enter two words to test if they are anagrams")
ignore_in = input("ignore spaces? y/n ")
if ignore_in == "y":
    ignore = True
if ignore_in == "n":
    ignore = False

print("ignoring spaces?",ignore)

output = is_anagram(input("word 1: "),input("word 2: "),ignore)
print("are these words anagrams? ",output)
