"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
#I think this will create a list with the following words
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #It created a list called some_words with the above words
#I think this will print the words in the list some_words
for word in some_words:
    print(word) #It printed each word in some_word line by line
#I think this will also print the words in some_words
for x in some_words:
    print(x) #It printed each word in some_word line by line
#I think this will print the exact some_words list
print(some_words) #It printed some_word with exact punctuation marks
#If the length of some_words is greater than 3, print some_words contain more than 3 words
if len(some_words) > 3:
    print('some_words contains more than 3 words') #It printed out some_word contains more than 3 words
#I think this will print the information of this PC
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #It returned the information of system, node, release, version, machine, processor for this PC

usefulFunction()
