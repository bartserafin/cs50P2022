def convertToSnake(text):
    """
    Input a camelCase string and returns a snake_case of that string
    """
    snake_case = ""

    for char in text:
        if char.isupper():
            char = "_" + char
        snake_case += char

    snake_case = snake_case.lower()

    print(snake_case)



txt = input("camelCase: ")
convertToSnake(txt)