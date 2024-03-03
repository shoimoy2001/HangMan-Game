import random

def get_random_word_from_wordlist():
    with open("hangman_wordlist.txt", 'r') as file:
        wordlist = file.read().split("\n")
    return random.choice(wordlist)

def initialize_hidden_word(word):
    hidden_word = ['_'] * len(word)
    return hidden_word

def update_hidden_word(word, hidden_word, char):
    for i, c in enumerate(word):
        if c == char:
            hidden_word[i] = char
    return hidden_word

def draw_hangman(chances):
    stages = [
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / 
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |      
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |     
        -
        """,
        """
        --------
        |      |
        |      O
        |      |
        |      |
        |     
        -
        """,
        """
        --------
        |      |
        |      O
        |      
        |      
        |     
        -
        """,
        """
        --------
        |      |
        |      
        |      
        |      
        |     
        -
        """
    ]
    print(stages[chances])

def start_hangman_game():
    player_name = input("Enter Your Name: ")

    random_word = get_random_word_from_wordlist().lower()
    hidden_word = initialize_hidden_word(random_word)
    guessed_letters = []
    chances = 6

    while True:
        if chances == 0:
            print(f"Sorry! {player_name}, You have Lost the Game! the word was: {random_word}")
            print("Better luck next time")
            break
        
        print("\n=== Guess the word ===")
        print(' '.join(hidden_word))
        print(f"(word has {len(random_word)} letters)")
        print(f"Chances left: {chances}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet only")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try another one.")
            continue
        
        guessed_letters.append(guess)

        if guess in random_word:
            hidden_word = update_hidden_word(random_word, hidden_word, guess)
            if '_' not in hidden_word:
                print(f"\nCongratulations, {player_name}! You have Won the Game! The word was: {random_word}")
                break
        else:
            chances -= 1
            draw_hangman(chances)

print("==== Welcome to the Hangman Game ====")

while True:
    choice = input("Do you want to play Hangman? (yes/no): ")

    if choice.lower() == 'yes':
        start_hangman_game()
    elif choice.lower() == 'no':
        print("Quitting the Game...")
        break
    else:
        print("Please enter 'yes' or 'no'.")

