from random import randint 

#define letter pool
LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}
#create a copy of LETTER_POOL that can be modified as letters are selected
# available_letters = {
#     'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 
#     'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 
#     'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
# }

def draw_letters():

    #make letter pool of all potential letters
    full_letter_list = []
    for letter, frequency in LETTER_POOL.items():
        full_letter_list += [letter] * frequency

    #generate 10 random letters using random index of full letter list 
    hand = []
    for i in range(10):
        if not full_letter_list: #check if list is empty
            break
        index = randint(0, len(full_letter_list) -1)
        hand.append(full_letter_list.pop(index)) #remove chosen letter to adhere to frequency count
    return hand      


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:] #make copy to modify and not alter original hand
    for char in word.upper(): #ensures no mismatched cap cases
        if char in letter_bank_copy:
            letter_bank_copy.remove(char) #remove used letter from hand to ensure no repetitions
        else:
            return False
    return True

# uses_available_letters("some", draw_letters())
def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass 