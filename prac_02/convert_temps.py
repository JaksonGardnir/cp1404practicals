"""
Program to convert temperatures in text file from Fahrenheit to Celsius.
"""
INPUT_FILENAME = "temps_input"
OUTPUT_FILENAME = "temps_output"


def main():
    # Extract each line of input text file into a list.
    temperature_list_fahrenheit = extract_list_from_text(INPUT_FILENAME)

    create_empty_text_file(OUTPUT_FILENAME)

    for i in range(len(temperature_list_fahrenheit)):
        # Convert Fahrenheit to Celsius.
        temperature_celsius = convert_fahrenheit_to_celsius(float(temperature_list_fahrenheit[i]))
        # Write converted temperatures into output text file.
        append_to_text_file(OUTPUT_FILENAME, str(temperature_celsius) + "\n")


def convert_fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def create_empty_text_file(filename: str):
    """Create an empty file filename.txt"""
    with open(filename + ".txt", "w", encoding="utf-8") as f:
        f.write("")


def append_to_text_file(filename: str, message: str):
    """Append a string to filename.txt."""
    with open(filename + ".txt", "a", encoding="utf-8") as f:
        f.write(message)


def extract_list_from_text(filename: str) -> list[str]:
    """Extract each line of a text file into a list."""
    with open(filename + ".txt", "r", encoding="utf-8") as f:
        list_from_text = f.readlines()
    return list_from_text


main()
