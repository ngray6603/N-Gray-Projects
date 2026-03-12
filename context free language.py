def is_an_bn(s):
    # Rule 2: The empty string case (n=0)
    if s == "":
        return True

    # Rule 1: Must start with 'a' and end with 'b'
    if len(s) >= 2 and s[0] == 'a' and s[-1] == 'b':
        # Recursively check the middle (the 'S' in aSb)
        return is_an_bn(s[1:-1])

    # If it doesn't match the rules, it's not in the language
    return False


# Testing the logic
test_strings = ["aaabbb", "ab", "", "aabbb", "ba"]
for word in test_strings:
    print(f"'{word}': {is_an_bn(word)}")
