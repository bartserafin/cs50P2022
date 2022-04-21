def twttr(text):
    vowels = ["A", "E", "I", "O", "U"]
    new_text = ""
    for char in text:
        if char.upper() not in vowels:
            new_text += char

    print(f"Output: {new_text}")


str_input = input("Input: ")
twttr(str_input)