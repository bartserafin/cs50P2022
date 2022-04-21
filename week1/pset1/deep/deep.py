answer = input(" ").strip().lower()

answers = ["42", "forty two", "forty-two"]
if answer in answers:
    print("Yes")
else:
    print("No")