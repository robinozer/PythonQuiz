# Write your code to expect a terminal of 80 characters wide and 24 rows high

introduction = input("What is your name?\n")

# Validate answer is filled in, and:

print(f'Hello {introduction}, welcome to this Python Quiz. Each question has four answer options. You get one point for each correct answer.\nPress enter to start the quiz. Good luck {introduction}!')

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

SCORE = 0

for question, options in QUESTIONS.items():
    correct_option = options[0]
    for option in options:
        print(f" - {option}")

    user_answer = input(f"{question} ")
    if user_answer == correct_option:
        print(f"{user_answer} is correct. You're a genius!")
        SCORE += 1
    else:
        print(f"{user_answer} is incorrect.\nThe correct answer is {correct_option}.")
