import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 10
QUESTIONS = {
    "What magical event would you most want to experience": [
        "The Triwizard Tournament",
        "Quidditch World Cup",
        "The Yule Ball",
        "None",
    ],
    "Which animal would you choose as your Hogwarts pet? ": [
        "Cat",
        "Owl",
        "Toad",
        "Rat",
    ],
    "Which quidditch position would you most likely play? ": [
        "Seeker",
        "Chaser",
        "Keeper",
        "In the stands cheering them on",
    ],
    "Which of your skills are you most proud of? ": [
        "Ability to make friends ",
        "Ability to keep secrets",
        "Ability to absorb new information",
        "Ability to get what you want",
    ],
    "You're in a duel with a skilled opponent. They fire an unknown spell at you and you shout...": [
        "Expelliarmus",
        "Crucio",
        "Stupefy",
        "Petrificus Totalus",
    ],
    "What class would you like the most? ": [
        "Defense against the dark arts",
        "Potions",
        "Charms",
        "Herbology",
    ],
    "You would be hurt if a person called you... ": [
        "Weak"
        "Mean"
        "Ignorant"
        "Stupid"
    ],
    "Choose a Deathly Hallow": [
        "Resurrection Stone",
        "Elder Wand",
        "Cloak of Invisibility",
    ],
    "What path do you want to follow after leaving Hogwarts?": [
        "Join the ministry",
        "Travel the world for a bit",
        "Settle down and start a family",
        "Continue to work hard and achieve success and riches",
    ],
    "And finally: We know that the Sorting Hat takes into account your preferences. So which Hogwarts house do you "
    "feel you identify with most closely?": [
        "Gryffindor",
        "Ravenclaw",
        "Hufflepuff",
        "Slytherin",
    ]
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]



