from collections import Counter

# constants & parameters
MAX_TRIES = 6

HANGMAN_PHOTOS = {}
HANGMAN_PHOTOS[1] = 'x-------x'
HANGMAN_PHOTOS[2] = '\n    x-------x\n    |\n    |\n    |\n    |\n    |\n\t'
HANGMAN_PHOTOS[3] = '\n    x-------x\n    |       |\n    |       0\n    |\n    |\n    |\n\t'
HANGMAN_PHOTOS[4] = '\n    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |\n\t'
HANGMAN_PHOTOS[5] = '\n    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |\n    |\n\t'
HANGMAN_PHOTOS[6] = '\n    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      /\n    |\n\t'
HANGMAN_PHOTOS[7] = '\n    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      / \\\n    |\n\t'

HANGMAN_ASCII_ART = """Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""




# Helper functions
def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    good_length = len(letter_guessed) == 1
    is_a_letter = letter_guessed.isalpha()

    if ((not good_length) and (not is_a_letter)):
        return False
    elif (not good_length):
        return False
    elif (not is_a_letter):
        return False
    elif (letter_guessed in old_letters_guessed):
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    
    if (check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed += letter_guessed.lower()
        print(old_letters_guessed)
        return True
    print("X")
    print(' -> '.join(sorted(old_letters_guessed)))
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    result = ""
    secret_word = secret_word.lower()
    
    for char in secret_word:
        if (char in old_letters_guessed):
            result += char
        else:
            result += "_"
            
    return ' '.join(result)


def check_win(secret_word, old_letters_guessed):
    return ' '.join(secret_word.lower()) == show_hidden_word(secret_word, old_letters_guessed)


def choose_word(file_path, index):
    opened_file = open(file_path, "r")
    words = opened_file.read().split(" ")
    index = index % len(words)
    chosen_word = words[index - 1]
    
    words_dict = Counter(words)
    words = [key for key in words_dict]
    opened_file.close()
    
    return ((len(words), chosen_word))



def main():
    # Printing the opening 
    print(HANGMAN_ASCII_ART, "\n", MAX_TRIES)

    # Finding the new word
    file_path = input("Enter words text file: ")
    index = int(input("Enter word index: "))
    secret_word_tuple = choose_word(file_path, index)
    secret_word = secret_word_tuple[1]

    # Creating parameters
    num_of_tries = 1
    old_letters_guessed = list()

    # Print first stage
    print(HANGMAN_PHOTOS[1])

    while (num_of_tries < MAX_TRIES):
        show_hidden_word(secret_word, old_letters_guessed)
        letter = input("Enter a guess: ")
        
        if (not check_valid_input(letter, old_letters_guessed)):
            print("X")
            print("This guess is invalid.")
            print("X")
            print(' -> '.join(sorted(old_letters_guessed)))
            continue

        if (letter in old_letters_guessed):
            num_of_tries += 1
            print("/):")
            print_hangman(num_of_tries)
            if (num_of_tries == MAX_TRIES):
                print("LOSE")

        else:
            try_update_letter_guessed(letter, old_letters_guessed)
            print(show_hidden_word(secret_word, old_letters_guessed))
            if (check_win(secret_word, old_letters_guessed)):
                print("WIN")
                break



if __name__ == "__main__":
    main()