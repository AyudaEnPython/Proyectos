"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import choice
from typing import List
# pip install prototools
from prototools import get_data, str_input, text_align, green, yellow


def is_valid(guess: str, guesses: str, size: int = 5) -> bool:
    return len(guess) == size and guess in guesses


def evaluate(guess: str, word: str, size: int = 5) -> str:
    return "".join([
        green(guess[i]) if guess[i] == word[i] else
        yellow(guess[i]) if guess[i] in word else
        guess[i] for i in range(size)
    ])


def show_words(words: List[str]) -> None:
    for word in words:
        print(word)


def main() -> None:
    attempts, max_attempts, words = 1, 6, []
    GUESSES = get_data("data/guesses.txt")
    SECRET_WORD = choice(get_data("data/answers.txt"))
    while attempts <= max_attempts:
        user_guess = str_input("Enter your guess > ")
        if not is_valid(user_guess, GUESSES):
            text_align(
                "Invalid guess. Please enter an English word with 5 letters."
            )
            show_words(words)
            continue
        if user_guess == SECRET_WORD:
            text_align(
                f"Congratulations! You guessed the word {SECRET_WORD}!"
            )
            break
        words.append(evaluate(user_guess, SECRET_WORD))
        show_words(words)
        attempts += 1
    else:
        text_align(f"Game over! The secret word was: {SECRET_WORD}")


if __name__ == "__main__":
    main()
