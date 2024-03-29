# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    first=0
    word_lower=word.lower()
    keys=SCRABBLE_LETTER_VALUES.keys()
    values=SCRABBLE_LETTER_VALUES.values()
    if word=="":
        first=0
        second=0
    else:
        for i in word_lower:
            for j in keys:
                if i==j:
                    first+=SCRABBLE_LETTER_VALUES[i]
        z=7*len(word)-3*(n-len(word))
        if z>1:
            second=z
        else:
            second=1
    return (first*second)
      # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))-1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n-1):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand['*']=1
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    b={}
    word_lower=word.lower()
    b=get_frequency_dict(word_lower)
    
    a={}
    for i in hand.keys():
        for j in b.keys():
            if i==j:
                a[i]=hand.get(i,0)-b.get(j,0)
                if a[i]<0:
                    a[i]=0
                    break
                else:
                    break
        else:
            a[i]=hand.get(i,0)
    return a

      # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    d=0
    f=0
    b={}
    v=0
    z=0
    a=[]
    value=0
    word_lower=word.lower()
    b=get_frequency_dict(word_lower)
    p=word_lower.split()
    list_word=list(word_lower)
    list_vowels=list(VOWELS)
    
    for l in range(len(list_word)):
        if list_word[l]=='*':
            for m in range (len(list_vowels)):
                list_word[l]=list_vowels[m]
                c=''.join(list_word)
                a.append(c)
            
            for x in a:    
                for k in word_list:
                    if x==k:
                        d+=1      #WE CAN ALSO STORE POSSIBLE MATCHES FROM WORD LIST
                        break
            else:
                
                break    
    else:
    
        for i in word_list:
            if i==word_lower:
                d+=1
                break
    
    for k in b.keys():
        for l in hand.keys():
            if k==l and b[k]<=hand[l]:
                f=1
                break
        else:
            f=0
            break
        
            
        
    
#               
    if(f==1 and d>0):
        value=1
    
   
    return value
    
      # TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    b=0
    for i in hand.keys():
        if hand[i]>0:
            b+=1
    
    return(b)  # TO DO... Remove this line when you implement this function

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#   for loop
    #word_list=load_words()
    total_score=0
#    total1=0
#    total2=0
    new_hand=hand
    #hand=deal_hand(hand)
    
    while(calculate_handlen(new_hand)>1):
        display_hand(new_hand)
        word=input("Enter word, or !! to indicate that you are finished : ")
        if word=="!!":
            print("Total score :",total_score)
            print("-------------------------------------")
            break
#            for i in range(1):
#                ch=input("Would you like to replay the hand?(yes/no): ")
#                if ch=="yes":
#                    total1=total_score
#                    play_hand(hand, word_list)    
#                    total2=total_score
#                else:
#                    break
            
        else:
            if is_valid_word(word, new_hand, word_list)==1:
            
                total_score+=get_word_score(word,calculate_handlen(new_hand))
                print(word, "earned",get_word_score(word,calculate_handlen(new_hand)),"points . Total:",total_score,"points")
                new_hand=update_hand(new_hand, word)
            else:
                print("That is not a valid word. Please choose another word")
                new_hand=update_hand(new_hand, word)
    else:
        print("Ran out of letters. Total score:",total_score,"points")  
        print("-------------------------------------")
#    for i in range(1):
#        total1=total_score
#        ch=input("Would you like to replay the hand?(yes/no): ")
#            
#        if ch=="yes":
#                
#            play_hand(hand, word_list)    
#            total2=total_score
#            break
           
    return total_score
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    c=[]
    b=VOWELS+CONSONANTS
    for i in hand.keys():
        for j in b:
            if i==j:
                c.append(i)
                break
    d=list(b)
    for i in c:
        d.remove(i)
#    d.remove(letter)
    for i in hand.keys():
        if i==letter:
            value=hand[i]
            break
    a=random.choice(d)
    hand[a]=value
    del(hand[letter])
            
    
                
    return hand        
      # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
#    print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

word_list=load_words()
#word_list=["abc","ice","part","cows","jar","fix"]

#hand={'a':1,'c':1,'p':1,'i':1,'*':1,'t':1,'r':1}
total_list=[]
grand_total=0
hand=deal_hand(7)
num=int(input("Enter total number of hands: "))
for i in range(num):
    hand=deal_hand(7)
    print("current hand : ")
    display_hand(hand)
    
    choice=input("Would you like to substitute a letter? (yes/no): ")
    if choice=="yes":
        letter=input("Which letter would you like to replace: ")
    
        print("current hand : ", substitute_hand(hand, letter))
        total_list.append(play_hand(hand, word_list))
        for j in range(1):
        
            ch=input("Would you like to replay the hand?(yes/no): ")
            
            if ch=="yes":
                total_list.append(play_hand(hand, word_list))
                minimum=min(total_list[j],total_list[j+1])
                total_list.remove(minimum)
                
#                total_list.append(play_hand(hand, word_list))    
                
                break
            
        
    else:
        total_list.append(play_hand(hand, word_list))
        for j in range(1):
        
            ch=input("Would you like to replay the hand?(yes/no): ")
            
            if ch=="yes":
                total_list.append(play_hand(hand, word_list))
                minimum=min(total_list[j],total_list[j+1])
                total_list.remove(minimum)
#                total_list.append(play_hand(hand, word_list))    
                
                break
           
for i in total_list:
    grand_total+=i
print("Total score over all hands: ",grand_total)



