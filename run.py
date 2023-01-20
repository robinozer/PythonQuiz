# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Welcome to this Python Quiz")

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

score = 0

for question, options in QUESTIONS.items():
    correct_option = options[0]
    sorted_options = sorted(options)

    for label, option in enumerate(sorted_options):
        print(f" {label} {option}")

    user_answer_label = int(input(f"{question}"))
    user_answer = sorted_options[user_answer_label]
    if user_answer == correct_option:
        print(f"{user_answer} is correct. You're a genius!")
        score += 1
    else:
        print(f"{user_answer} is incorrect. The correct answer is {correct_option}.")
print(f"\nYour score is {score} out of 5. Well done {introduction}.")
