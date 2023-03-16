questions = ("How many planet are there in the Solar System?",
             "What is the name of the 3rd Planet of the Solar System?",
             "What is sun mainly made from?", 
             "How many moons does Mars have?")
# We can add multiple questions here. ^
options = (("A.7", "B. 8", "C. 9", "D. 10"),
           ("A. Mars", "B. Venus", "C. Earth", "D. Jupiter "),
           ("A. Gas", "B. Hydrogen", "C. Nitrogen", "D. None of the above"),
           ("A. 50", "B. 13", "C. 25", "D. 2"))
# We can add multiple options here. ^

answers = ("B", "C", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter the answer(A/B/C/D): ")
    guesses.append(guess)
    if guess == answers:
        score +=1
        print("CORRECT ANSWER! :)")

    else:
        print("INCORRECT ANSWER! :(")
        print(f"{answers[question_num]} is the CORRECT ANSWER!")
