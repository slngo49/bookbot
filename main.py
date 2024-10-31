def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

    num_words = get_num_words(text) 
    print(f"{num_words} words found in the document")
    
    result = count_character_occurrences(text)
    print(result)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_character_occurrences(text: str) -> dict:
    # Convert text to lowercase
    text = text.lower()
    
    # Initialize a dictionary to hold character counts
    char_count = {}
    
    # Count occurrences of each character
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # Print the analyzed text and results
    print(f"Analyzing text: '{text}'")
    print("Character count results:")
    for char, count in sorted(char_count.items()):
        print(f"The character '{char}' appears {count} time(s)")
    
    return char_count

main()