
# Write your code to expect a terminal of 80 characters wide and 24 rows high

QUESTIONS = {
    "Aureolin is a shade of what color?": [
        "Yellow", "Green", "Red", "Orange"
    ],
    "Cerulean is a shade of what color?": [
        "Brown", "Blue", "Grey", "White"
    ],
    "Celadon is a shade of what color?": [
        "White", "Black", "Grey", "Green"
    ],
    "Maroon is a shade of what color?": [
        "Pink", "Blue", "Yellow", "Red"
    ],
    "Umber is a shade of what color?": [
        "Yellow", "Red", "Brown", "Yellow"
    ],
}

for question, options in QUESTIONS.items():
    correct_option = options[0]
    for option in options:
        print(f" - {option}")

    user_answer = input(f"{question}?")
score = 0