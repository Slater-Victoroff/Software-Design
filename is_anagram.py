'''This is a simple but lightweight and efficient program
to check if two provided strings are anagrams. The computing
time scales only linearly with the length of the strings
and strings may be of arbitrary length. Returns True if
the two strings are anagrams, False if they are not.'''
	
#Makes a hastable for a given word that equates to a 
#histogram with each letter by iterively running through
#the string. Returns a hashtable.

def make_dictionary(word):
	letters = {}
	for letter in word:
		if letter not in letters:
			letters[letter] = 1
		else:
			letters[letter]+=1
	return letters
	
#checks to see if the hashtables of two words are equal.
#Returns a boolean.

def is_anagram(word1, word2):
	return make_dictionary(word1)==make_dictionary(word2)
	

#Returning to some of the first python I wrote after a long time gave me this improvement

from collections import Counter

is_anagram = lambda word1, word2: Counter(word1) == Counter(word2)

#boom
