print('Welcome to My Quiz')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay! Let's Play! ")
score = 0

answer = input('Who is considered the central figure of Christianity? ')
if answer.lower() == 'Jesus Christ':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('What is the holy book of Christianity called? ')
if answer.lower() == 'The Bible':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('How many books are in the New Testament of the Bible? ')
if answer.lower() == '27 books':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('What event is commemorated on Good Friday? ')
if answer.lower() == 'The crucifixion of Jesus Christ':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('In which city was Jesus born? ')
if answer.lower() == 'Bethlehem':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('What is the significance of Easter in Christianity? ')
if answer.lower() == 'the resurrection of Jesus Christ from the dead.':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('What is the first book of the Old Testament in the Bible? ')
if answer.lower() == 'Genesis':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('Who was the first man, according to the Bible? ')
if answer.lower() == 'Adam':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input(' How many disciples did Jesus have? ')
if answer.lower() == '12 disciples':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('What is the significance of the Last Supper in Christianity? ')
if answer.lower() == 'The Last Supper is when Jesus shared a final meal with his disciples before his crucifixion.':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('What do Christians traditionally celebrate on December 25th? ')
if answer.lower() == 'Christmas':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('Which Christian denomination is known for its belief in adult baptism? ')
if answer.lower() == 'Baptists':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('What is the term for the Christian rite of initiation involving water, symbolizing cleansing and rebirth? ')
if answer.lower() == 'Baptism':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('In Christianity, what is the Holy Trinity? ')
if answer.lower() == 'The Father, the Son, and the Holy Spirit':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('Which Christian holiday marks the end of the liturgical year and is associated with reflecting on mortality and the afterlife? ')
if answer.lower() == "All Saints' Day":
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('What is the name of the Christian event that commemorates the descent of the Holy Spirit upon the apostles after Jesus ascension? ')
if answer.lower() == 'Pentecost':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('Which Christian denomination is known for its strong emphasis on pacifism and nonviolence? ')
if answer.lower() == 'Quakers':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('What is the Christian sacrament that commemorates the Last Supper and Jesus sacrifice? ')
if answer.lower() == 'Communion':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('What is the term for the forgiveness of sins in Christianity? ')
if answer.lower() == 'Atonement':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    answer = input('Who is believed to have written most of the epistles (letters) in the New Testament? ')
if answer.lower() == 'Paul':
    print('Correct! ')
    score += 1
else:
    print('wrong')

    

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score / 20) * 100) + '%')
