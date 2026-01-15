import random
import hangman_stages

hangman_ascii = r"""
*************************************************       +---+
  /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __           |   |
 / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \          O   |    Developed By Tyron Aricum
/ __  / (_| | | | | (_| | | | | | | (_| | | | |        /|\  |    Version 1.0
\/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|        / \  |
                   |___/                                    |
*************************************************     =========
"""

def show_item(item):
    print(item)

# DISPLAY THE SPLASH SCREEN
show_item(hangman_ascii)

# CAR BRANDS
car_brands = [
    "TOYOTA", "HONDA", "FORD", "BMW", "MERCEDES", "AUDI", "VOLKSWAGEN",
    "NISSAN", "CHEVROLET", "HYUNDAI", "KIA", "TESLA", "SUBARU", "MAZDA",
    "VOLVO", "JEEP", "LEXUS", "PORSCHE", "FERRARI", "LAMBORGHINI"
]

# SHOPS (retail stores/brands)
shops = [
    "WALMART", "TARGET", "AMAZON", "COSTCO", "BESTBUY", "IKEA", "MACYS",
    "NIKE", "ADIDAS", "ZARA", "H&M", "APPLE", "MICROSOFT", "GOOGLE",
    "STARBUCKS", "MCDONALDS", "KFC", "BURGERKING", "WALGREENS", "CVS"
]

# CELL PHONE BRANDS
cell_phone_brands = [
    "APPLE", "SAMSUNG", "GOOGLE", "ONEPLUS", "XIAOMI", "HUAWEI", "OPPO",
    "VIVO", "MOTOROLA", "NOKIA", "SONY", "LG", "HTC", "BLACKBERRY",
    "REALME", "ASUS", "LENOVO", "ZTE", "MICROSOFT", "ALCATEL"
]

# ACTORS
actors = [
    "TOM HANKS", "LEONARDO DICAPRIO", "BRAD PITT", "JOHNNY DEPP", "ROBERT DOWNEY JR",
    "DWAYNE JOHNSON", "CHRIS HEMSWORTH", "SCARLETT JOHANSSON", "JENNIFER LAWRENCE",
    "MERYL STREEP", "DENZEL WASHINGTON", "MORGAN FREEMAN", "SAMUEL L JACKSON",
    "WILL SMITH", "TOM CRUISE", "NICOLE KIDMAN", "JULIA ROBERTS", "GEORGE CLOONEY",
    "MATT DAMON", "CHRISTIAN BALE"
]

# SINGERS
singers = [
    "TAYLOR SWIFT", "BEYONCE", "RIHANNA", "DRAKE", "ED SHEERAN", "ADELE",
    "BRUNO MARS", "JUSTIN BIEBER", "ARIANA GRANDE", "SHAKIRA", "LADY GAGA",
    "KATY PERRY", "POST MALONE", "THE WEEKEND", "BILLIE EILISH", "HARRY STYLES",
    "COLDPLAY", "MAROON5", "PINK", "JUSTIN TIMBERLAKE"
]

# Store all in a dictionary for easy access
categories = {
    0: {"name": "Car Brands", "words": car_brands},
    1: {"name": "Shops", "words": shops},
    2: {"name": "Cell phone brands", "words": cell_phone_brands},
    3: {"name": "actors", "words": actors},
    4: {"name": "singers", "words": singers}
}

selected_category = int(input(r"""
Select a game category?
[0] Car Brands
[1] Shops
[2] Cell Phone Brands
[3] Actors
[4] Singers

Type the number and hit 'enter'
"""))

# Function to mask the word, replacing letters with underscores ('_')
def mask_word(word):
    masked = ""
    for char in word:
        if char == " ":
            masked += " " # Keep spaces
        else:
            masked += "_" # Replace letters with underscore
    return masked

# Function to reveal the word, replacing masked letters with the correct letter
def reveal_letters(word, masked_word, guess):
    """Reveal correctly guessed letters in the masked word."""
    result = ""
    for i in range(len(word)):
        if word[i].upper() == guess.upper():
            result += word[i]  # Reveal the correct letter
        else:
            result += masked_word[i]  # Keep existing character
    return result

random_word = random.choice(categories[selected_category]['words'])
masked_work = mask_word(random_word)
revealed_word = masked_work
current_stage = 0

print(f"selected category: {categories[selected_category]['name']} ")
print(f"""
*************************************
Lets get started...
You have 5 lives, Dont Kill Jimmy!
*************************************
{hangman_stages.HANGMAN_STAGES[current_stage]}
{masked_work}
""")

# Loop - Continue game if user hasn't guessed incorrectly for 6 times
while current_stage < 6:

    letter_guess = input("Guess a letter: ").upper()
    revealed_word = reveal_letters(random_word, revealed_word, letter_guess)


    letter_exists_in_masked_word = (letter_guess in revealed_word)

    if not letter_exists_in_masked_word:
        current_stage += 1

    all_letters_unmasked = ("_" not in revealed_word)

    print(hangman_stages.HANGMAN_STAGES[current_stage])
    print(revealed_word)

    if all_letters_unmasked:
        print(f"CONGRATULATIONS! You guessed the word and SAVED JIMMY!")
        break


if current_stage == 6:
    print(f"You Killed Jimmy! Game Over!")
    print(hangman_stages.HANGMAN_STAGES[current_stage])
    print(f"The word was: {random_word}")
