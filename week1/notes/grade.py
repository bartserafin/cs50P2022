score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
else: # below 60
    print("F")

# tidy up
if 90 >= score <= 100:
    print("A")
elif 80 >= score < 90:
    print("B")
elif 70 >= score < 80:
    print("C")
elif 60 >= score < 70:
    print("D")
else: # below 60
    print("F")