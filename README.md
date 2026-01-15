🎮 Hangman Game
<div align="center">

![Hangman Python](https://img.shields.io/badge/Hangman-Python-blue)
![Version](https://img.shields.io/badge/Version-1.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Python](https://img.shields.io/badge/Python-3.8+-blue)

*A classic word guessing game with modern twists!*
</div>
✨ Features

    🎯 5 Exciting Categories: Car Brands, Shops, Cell Phone Brands, Actors, and Singers

    🎨 Beautiful ASCII Art: Visually appealing hangman graphics

    💀 Progressive Stages: Watch Jimmy the hangman figure evolve with each wrong guess

    🏆 Win/Lose Conditions: Save Jimmy or face the consequences!

    🎮 User-Friendly Interface: Simple and intuitive gameplay

📁 Project Structure
text

hangman/
├── main.py              # Main game file
├── hangman_stages.py    # ASCII art for hangman stages
├── README.md           # This file
└── requirements.txt    # Python dependencies

🚀 Quick Start
Prerequisites

    Python 3.8 or higher

Installation

    Clone the repository

bash

git clone https://github.com/yourusername/hangman-game.git
cd hangman-game

    Run the game

bash

python main.py

Or if using Python 3 explicitly:
bash

python3 main.py

🎮 How to Play

    Start the game - You'll see a splash screen with the Hangman logo

    Choose a category - Select from 5 different word categories

    Guess letters - Try to guess the hidden word one letter at a time

    Save Jimmy - You have 6 wrong guesses before Jimmy meets his fate!

    Win or lose - Guess the word to save Jimmy, or run out of guesses to lose

📊 Game Categories
Category	Examples
🚗 Car Brands	Toyota, Mercedes, Tesla
🛍️ Shops	Walmart, Amazon, Nike
📱 Cell Phones	Apple, Samsung, Google
🎬 Actors	Tom Hanks, Brad Pitt, Scarlett Johansson
🎤 Singers	Taylor Swift, Beyoncé, Drake

🛠️ Technical Details
Key Functions

    mask_word(word): Converts letters to underscores while preserving spaces

    reveal_letters(word, masked_word, guess): Reveals correctly guessed letters

    show_item(item): Helper function for displaying ASCII art

Game Logic

    6 Stages: From empty gallows to complete hangman figure

    Word Selection: Random word selection from chosen category

    Input Validation: Case-insensitive letter guessing

    Progress Tracking: Visual feedback for correct/incorrect guesses

📈 Game Stages

The game features 7 visual stages (0-6):

    Stage 0: Empty gallows

    Stage 1: Head appears

    Stage 2: Body appears

    Stage 3: Left arm appears

    Stage 4: Right arm appears

    Stage 5: Left leg appears

    Stage 6: Complete figure - Game Over!

🚀 Future Enhancements

    Difficulty levels (Easy, Medium, Hard)

    Score tracking system

    Multiplayer mode

    Sound effects

    GUI version

    More word categories

    Save/Load game functionality

🤝 Contributing

Contributions are welcome! Here's how you can help:

    Fork the repository

    Create a feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some AmazingFeature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request

📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
👨‍💻 Author

Tyron Aricum

    GitHub: @tyron-aricum

    Project: Hangman Game

🙏 Acknowledgments

    Thanks to all ASCII artists whose work inspired the hangman graphics

    The Python community for excellent documentation and resources

    Everyone who enjoys playing this classic game!

<div align="center">

Made with ❤️ and Python

⭐ Star this repo if you found it useful! ⭐
</div>
