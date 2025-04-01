#The entry point to our program and any code that doesn't fit elsewhere

from stats import get_num_words, get_num_characters, sort_on
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit[1]
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_num_characters(text)
    sorted_chars = sort_on(char_counts)
    print (f"Found {num_words} total words")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}") 
    print (f"{char_counts}")
    

def get_book_text(path):
    with open(path) as f:
        words = f.read()
        return words 
        
main()