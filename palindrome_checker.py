def is_palindrome(word):
    """Returns True if the word is a palindrome, False otherwise."""
    return word.lower() == word.lower()[::-1]

if __name__ == "__main__":
    test_word = "radar"
    print(f"Is '{test_word}' a palindrome? {is_palindrome(test_word)}")
