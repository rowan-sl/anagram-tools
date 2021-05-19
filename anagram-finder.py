#TODO add a description of how to use/how it works
from collections import Counter as count
import time

with open('./Resources/words.txt', 'r') as f:
    dictionary = f.read()

dictionary = [x.lower() for x in dictionary.split('\n')]

#dictionary = ["evil","log","dog","live","lvei"]

def word_shredder (word):
    letterbag = count(word)
    s = sorted(letterbag.elements())
    return s

def is_anagram(word_shredde1,word_shredde2):
    letters1 = word_shredder(word_shredde1)
    letters2 = word_shredder(word_shredde2)

    while " " in letters1:
        letters1.remove(" ")
    while " " in letters2:
        letters2.remove(" ")

    # print(letters1)
    # print(letters2)

    return letters1 == letters2

print("please enter a word: ")
word2check = input()

anagrams = []

start = time.time()

for word in dictionary:
    if word2check == word:
        continue
    if is_anagram(word2check,word):
        anagrams.append(word)
        print("anagram found")

end = time.time()
#TODO add a thingy to remove the original word from the output

print(len(anagrams),"anagrams have been found for the word: ",word2check,"out of a total of",len(dictionary), "words in only",round(end - start, 2),"seconds!")
print(anagrams)
