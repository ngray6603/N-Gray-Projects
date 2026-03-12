#import random to game
import random
#create the definition for the guess
def main ():
    welcome = ['Lets play hangman! Guess the random word I have chosen for you. Pick one letter at a time']
    for line in welcome:
        print(line, sep='\n')
#establishing the game
    #creating the loop for guesses
    play_again = true
    while play_again:
        # create words for game
        word_list = ["python", "redwings", "orange", "popcorn"]
        # choosen a word to play from the list
        chosen_word = random.choice(word_list).lower()
        #making the player choose
        player_guess = None
        #the letters the player chooses
        Player_choosen_letter = []
        word_gues = []
        for letter in chosen_word:
        #creats a blanked out word
            word_gues.apend("-")
        #joins the words that were guessed
        joined_word = None


    #design the hangman
    HANGMANPICS = ("""
        +---+
        I   I
            I
            I
            I
            I
     =============
     """,
     """
        +---+
        I   I
        0   I
            I
            I
            I
     =============
     """,
     """
        +---+
         I   I
         0   I
         !   I
             I
             I
      =============
     """,
     """
         +---+
         I   I
         0   I
        /    I
             I
             I
      =============
      """,
      """
       +---+
       I   I
       0   I
      /!\  I
           I
           I
    =============
    """,
     """
        +---+
        I   I
        0   I
       /!\  I
       /    I
            I
     =============
     """,
     """
         +---+
         I   I
         0   I
        /!\  I
        / \  I
             I
      =============
      """)

    print(HANGMANPICS[0])
    ATTEMPTS = LEN(HANGMANPICS) - 1

    while (attempts != 0 and "-" in word_gues):
       print(("\nYou have {} more chances").format(attempts))
       joined_word = "".join(word_gues)
       print(joined_word)

       try:
           player_chosen_letter = str(input("\nPlease choose letter in alphabet" + "\n> ")).lower()
        #ensuring a valid response
       except:
           print("That guess didnt work, please use letters from A-Z only.")
           continue
    guessed_choices_append(player_chosen_letter)
    for idx, letter in enumerator(chosen_word)):
        if player_chosen_letter == chosen_word[letter]:
            #puts the players choice in the word
            word_guessed[idk] = player_chosen_letter
        if player_chosen_letter not in chosen-word:
            attempts -= 1
            print(HANGMANICS[ (len(HANGMANPICS) -1) -1 attempts])
        #when the player guess the word
        if "-" not in word_guessed:
            print(("\You are right, {} was correct").format(chosen_word))
        #too many choices, player loses
        else:
            print(("\nToo Bad! The word is {}.") format(chosen_word))
        #create loop to play again
        print("\n Want to play hangman again?")

        respose = input(">' ").lower()
        if response not in ("yes", "y"):
            play_again = False

if__name__ == "__main__":
main()




