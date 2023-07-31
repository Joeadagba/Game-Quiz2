def christian_religious_studies_quiz():
    print('Welcome to My Quiz')

    playing = input('Do you want to play? ')

    if playing.lower() != 'yes':
        quit()

    print("Okay! Let's Play!")
    score = 0

    answer = input('Who is considered the central figure of Christianity? ')
    if answer.lower() == 'jesus christ':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('What is the holy book of Christianity called? ')
    if answer.lower() == 'the bible':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('How many books are in the New Testament of the Bible? ')
    if answer.lower() == '27 books':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('What event is commemorated on Good Friday? ')
    if answer.lower() == 'the crucifixion of jesus christ':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('In which city was Jesus born? ')
    if answer.lower() == 'bethlehem':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('What is the significance of Easter in Christianity? ')
    if answer.lower() == 'the resurrection':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('What is the first book of the Old Testament in the Bible? ')
    if answer.lower() == 'genesis':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('Who was the first man, according to the Bible? ')
    if answer.lower() == 'adam':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('How many disciples did Jesus have? ')
    if answer.lower() == '12':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('What is the significance of the Last Supper in Christianity? ')
    if answer.lower() == 'final meal with disciples before his crucifixion':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('What do Christians traditionally celebrate on December 25th? ')
    if answer.lower() == 'christmas':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('Which Christian denomination is known for its belief in adult baptism? ')
    if answer.lower() == 'baptists':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('What is the term for the Christian rite of initiation involving water, symbolizing cleansing and rebirth? ')
    if answer.lower() == 'baptism':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('In Christianity, what is the Holy Trinity? ')
    if answer.lower() == 'the father, the son, and the holy spirit':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('Which Christian holiday marks the end of the liturgical year and is associated with reflecting on mortality and the afterlife? ')
    if answer.lower() == "all saints' day":
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('What is the name of the Christian event that commemorates the descent of the Holy Spirit upon the apostles after Jesus ascension? ')
    if answer.lower() == 'pentecost':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('Which Christian denomination is known for its strong emphasis on pacifism and nonviolence? ')
    if answer.lower() == 'quakers':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('What is the Christian sacrament that commemorates the Last Supper and Jesus sacrifice? ')
    if answer.lower() == 'communion':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('What is the term for the forgiveness of sins in Christianity? ')
    if answer.lower() == 'atonement':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    answer = input('Who is believed to have written most of the epistles (letters) in the New Testament? ')
    if answer.lower() == 'paul':
        print('Correct!')
        score += 1
    else:
        print('Wrong')

    print('You got ' + str(score) + ' questions correct!')
    print('You got ' + str((score / 20) * 100) + '%')

christian_religious_studies_quiz()
