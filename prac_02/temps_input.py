"""
Program to generate a text file with temperatures.
"""
import random

FILENAME = "temps_input"
LOWEST_TEMPERATURE = -200
HIGHEST_TEMPERATURE = 200
NUMBER_OF_TEMPERATURES = 15


def main():
    create_empty_text_file(FILENAME)
    for _ in range(NUMBER_OF_TEMPERATURES):
        random_temperature = random.uniform(LOWEST_TEMPERATURE, HIGHEST_TEMPERATURE)
        random_temperature = f"{random_temperature}\n"
        append_to_text_file(FILENAME, random_temperature)
        print(random_temperature)
    print(f"{NUMBER_OF_TEMPERATURES} random temperatures have been printed to {FILENAME}.txt")


def create_empty_text_file(filename: str):
    """Create an empty file filename.txt"""
    with open(filename + ".txt", "w", encoding="utf-8") as f:
        f.write("")


def append_to_text_file(filename: str, message: str):
    """Append a string to filename.txt."""
    with open(filename + ".txt", "a", encoding="utf-8") as f:
        f.write(message)


main()
