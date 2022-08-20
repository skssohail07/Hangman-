
from words_list import words
import random

def get_words():
    word = random.choice(words).upper()
    return word


def hangman(chances):
    dispaly_stages =["""
                        --------
                        |      |
                        |      O
                        |     \|/
                        |      |
                        |     / \\
                    """, 
                    """
                        --------
                        |      |
                        |      O
                        |     \|/
                        |      |
                        |     / 
                    
                    """,
                    """
                        --------
                        |      |
                        |      O
                        |     \|/
                        |      |
                        |     
                    
                    """,
                    """
                        --------
                        |      |
                        |      O
                        |     \|
                        |      |
                        |     
                    
                    """,
                    """
                        --------
                        |      |
                        |      O
                        |      |
                        |      |
                        |     
                    
                    """,
                    """
                        --------
                        |      |
                        |      O
                        |      
                        |      
                        |     
                    
                    """,
                    """
                        --------
                        |      |
                        |      
                        |      
                        |      
                        |     
                    
                    """
                    ]
    return dispaly_stages[chances]
    

def game(word):
    success=False
    letters_guessed=[]
    words_guessed=[]
    complete_word="-"*len(word)
    chances=6

    print("\n\nHANGMAN")
    print(hangman(chances))
    print("Guess the word: ",complete_word)
    print("\n")
    while chances>0 and not success:
        guess=input("guess a letter or the word:").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in letters_guessed:
                print("you have already guessed the letter ",guess)
            elif guess not in word:
                print(guess,"doesn't exist in the word")
                chances-=1
                letters_guessed.append(guess)
            else:
                print("bingo! You guessed correct!")
                complete_word_list=list(complete_word)
                indices=[i for i,letter in enumerate(word) if letter==guess]
                for i in indices:
                    complete_word_list[i]=guess
                complete_word="".join(complete_word_list)
                if "-" not in complete_word:
                    success=True

        elif len(guess)==len(word) and guess.isalpha():
            if guess in words_guessed:
                print("you have already guessed the word",guess)
            elif guess !=word:
                print(guess,"is incorrect")
                chances-=1
                words_guessed.append(guess)
            else:
                success=True
                complete_word=word

        else:
            print("not valid!")

        print(hangman(chances))
        print(complete_word)
        print("\n")
    if success:
            print("well done! you have guessed the word ")
    else:
            print("sorry better luck next time!")

def start():
    p=True
    word=get_words()
    game(word)
    while p==True:
        play=input("do yo want to continue playing?(y/n):")
        if play=="y":
            word=get_words()
            game(word)
        else:
            p=False

start()





 
