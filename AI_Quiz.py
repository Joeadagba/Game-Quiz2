def python_comparison_operator_quiz():
    questions = [
        "Who is considered the central figure of Christianity?",
        "What is the holy book of Christianity called?",
        "How many books are in the New Testament of the Bible?",
        "What event is commemorated on Good Friday?",
        "In which city was Jesus born?",
        "What is the significance of Easter in Christianity?",
        "What is the first book of the Old Testament in the Bible?",
        "Who was the first man, according to the Bible?",
        "How many disciples did Jesus have?",
        "What is the significance of the Last Supper in Christianity?",
        "What do Christians traditionally celebrate on December 25th?",
        "Which Christian denomination is known for its belief in adult baptism?",
        "What is the term for the Christian rite of initiation involving water, symbolizing cleansing and rebirth?",
        "In Christianity, what is the Holy Trinity?",
        "Which Christian holiday marks the end of the liturgical year and is associated with reflecting on mortality and the afterlife?",
        "What is the name of the Christian event that commemorates the descent of the Holy Spirit upon the apostles after Jesus' ascension?",
        "Which Christian denomination is known for its strong emphasis on pacifism and nonviolence?",
        "What is the Christian sacrament that commemorates the Last Supper and Jesus' sacrifice?",
        "What is the term for the forgiveness of sins in Christianity?",
        "Who is believed to have written most of the epistles (letters) in the New Testament?"
    ]

    answers = [
        "Jesus Christ",
        "The Bible",
        "27 books",
        "The crucifixion of Jesus Christ",
        "Bethlehem",
        "It celebrates the resurrection of Jesus Christ from the dead",
        "Genesis",
        "Adam",
        "12 disciples",
        "The Last Supper is when Jesus shared a final meal with his disciples before his crucifixion",
        "Christmas, the birth of Jesus Christ",
        "Baptists",
        "Baptism",
        "The Father, the Son (Jesus Christ), and the Holy Spirit",
        "All Saints' Day (November 1st)",
        "Pentecost",
        "Quakers (The Society of Friends)",
        "The Eucharist or Holy Communion",
        "Atonement",
        "The Apostle Paul"
    ]

    score = 0

    print("Welcome to the Christian Religious Studies Quiz!")
    print("Please answer the following questions:")

    for i in range(len(questions)):
        print(f"\nQ{i+1}: {questions[i]}")
        user_answer = input("Your Answer: ")
        if user_answer.strip().lower() == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answers[i]}")

    print("\nQuiz completed!")
    print(f"Your final score is: {score}/{len(questions)}")

python_comparison_operator_quiz()