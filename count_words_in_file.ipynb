from collections import Counter
import string

def count_words_in_file(file_path):
    """
    Reads a text file and counts the occurrences of each word in the file.
    :param file_path: Path to the text file
    :return: Dictionary with words as keys and their respective counts as values
    """
    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            text = file.read()

        # Remove punctuation and convert text to lowercase
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator).lower()

        # Split the text into words
        words = cleaned_text.split()

        # Count occurrences of each word
        word_counts = Counter(words)

        # Sort the results alphabetically
        sorted_word_counts = dict(sorted(word_counts.items()))

        return sorted_word_counts

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

if __name__ == "__main__":
    # Prompt the user for the file path
    print("Welcome to the File Manipulation Program!")
    file_path = input("Enter the path to the text file: ")

    # Process the file and display results
    word_counts = count_words_in_file(file_path)
    if word_counts:
        print("\nWord occurrences in the file (sorted alphabetically):")
        for word, count in word_counts.items():
            print(f"{word}: {count}")
