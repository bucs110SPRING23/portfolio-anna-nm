def caesar_cipher(text, shift = 5):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new position of the character after the shift
            new_pos = (ord(char) - start + shift) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
        result += char
    return result
txt = open("encrypted.txt", 'w')
encrypted_text = caesar_cipher(text = "The quick brown fox jumps over the lazy dog")
txt.write(encrypted_text)
txt.close()
