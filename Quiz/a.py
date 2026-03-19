def ask_question(question, correct_answer):
    answer = input(question + " ")
    
    if answer.lower() == correct_answer.lower():
        print("True")
        return 1
    else:
        print("False")
        return 0


def main():
    score = 0

    score += ask_question("Captial of Egypt(Cairo - Sinai - Portsaid): ", "Cairo")
    score += ask_question("how many days on a week(6 - 7 - 8): ", "7")
    score += ask_question("Python is Programing language(Y or N): ", "Y")

    print()
    print("\nFinal Result is", score, "/ 3")

    if score == 3:
        print("Gamed")
    elif score == 2:
        print("Kwaees bs need to do more")
    else:
        print("Try Again")


main()
