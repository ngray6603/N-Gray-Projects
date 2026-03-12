#import shuffler
from random import shuffle
#define shuffle
def shuffle_word(Snow_fall):
    Snow_fall = list(Snow_fall)
    shuffle(Snow_fall)
    return '' .join(Snow_fall)
#create a list from text_list that is strings
    Snow_fall = ['Python', 'scramble', 'solution']
#return the original lsit
print("Original list:")
# Print the contects of text_list
print(Snow_fall)
#print message of the unscrabled string
print("\nYour unscrambled letters of the string are:")
#list to apply the shuffle word
result = [shuffle_word(word) for word in 'Snow_fall']
print(result)
