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

    score += ask_question("ما هي عاصمة مصر؟", "القاهرة")
    score += ask_question("كم عدد أيام الأسبوع؟", "7")
    score += ask_question("بايثون لغة برمجة؟ (نعم/لا)", "نعم")

    print()
    print("\nالنتيجة النهائية:", score, "/ 3")

    if score == 3:
        print("جامد")
    elif score == 2:
        print("كويس")
    else:
        print("حاول تاني")


main()