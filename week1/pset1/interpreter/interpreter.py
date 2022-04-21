equation = input("Equation: ").strip().split(" ")

x = float(equation[0])
z = float(equation[-1])

if equation[1] == "+":
    print(f"{x + z}")
if equation[1] == "-":
    print(f"{x - z}")
if equation[1] == "*":
    print(f"{x * z:.1f}")
if equation[1] == "/":
    print(f"{x / z:.1f}")