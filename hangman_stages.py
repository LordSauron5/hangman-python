# Store different hangman stages
HANGMAN_STAGES = [
    # Stage 0: Empty gallows
    r"""
       +---+
       |   |
           |
           |
           |
           |
     =========
     """,

    # Stage 1: Head
    r"""
       +---+
       |   |
       O   |
           |
           |
           |
     =========
     """,

    # Stage 2: Body
    r"""
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
     """,

    # Stage 3: Left Arm
    r"""
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
     """,

    # Stage 4: Right Arm
    r"""
       +---+
       |   |
       O   |
      /|\  |
           |
           |
     =========
     """,

    # Stage 5: Left Leg
    r"""
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
     =========
     """,

    # Stage 6: Right Leg (Complete - Game Over)
    r"""
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
     =========
     """
]