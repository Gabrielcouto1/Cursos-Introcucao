
def newgame():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter the asnwer(A, B, C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses,guesses)

    again = play_again()
    if again == 1:
        print("\n"*30)
        newgame()
    else:
        print("Thanks for playing!")

def check_answer(answer, option):
    if answer == option:
        print("\nCORRECT!")
        return 1
    else:
        print("\nWRONG")
        return 0

def display_score(correct_guesses, guesses):
    print("----------------\nRESULTS\n----------------")

    print("Answers:",end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses:",end=" ")
    for i in guesses:
        print(i, end=" ")
    score = int((correct_guesses/len(questions))*100 )
    print("\nYour score is: "+ str(score)+"%")

def play_again():
    again = str(input("Do you want to play again? Yes/No: ")).lower()
    if again == "yes":
        return 1
    else:
        return 0

questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

newgame()