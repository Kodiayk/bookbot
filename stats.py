# A file that contains functions for analyzing the text

def get_num_words(words):
    count = words.split()
    return len(count)

# take the text from the book as a string and return
# the number of times each character (including symbols and spaces)
# appear in the string

def get_num_characters(text):
    text = text.lower()
    char_counts = {}
    
    for char in text:
         if char in char_counts:
             char_counts[char] += 1
         else: 
             char_counts[char] = 1
    return char_counts

def sort_on(char_counts):
    sorted_chars = []
    
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_chars.append({
                "char": char,
                "count": count
            })
    
    sorted_chars.sort(key=lambda d: d["count"], reverse=True)
    return sorted_chars