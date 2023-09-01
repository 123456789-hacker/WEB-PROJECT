import datetime


BIRTH_YEAR = 1991
LIVING_LOCATION = "Szczecin"
LIKING_HALF_LIFE_GAMES = True


def ask_question(question_phrase):
    output = input(question_phrase + "\nAnswer> ")
    return output


def is_answer_true(answer):
    return answer in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'tak']


def age_question():
    answer = ask_question('How old am I?')
    if answer.isdigit():
        years = int(answer)
        now = datetime.datetime.now()
        if (now.year - years) == BIRTH_YEAR:
            return True
        else:
            return False
    return False


def location_question():
    answer = ask_question('Where I live?')
    if answer == LIVING_LOCATION:
        return True
    else:
        return False


def half_life_question():
    answer = ask_question('Do Pawel like Half-Life video games?')
    if is_answer_true(answer) == LIKING_HALF_LIFE_GAMES:
        return True
    else:
        return False


def main():
    answers = []
    answers.append(age_question())
    answers.append(location_question())
    answers.append(half_life_question())
    all_questions = len(answers)
    good_answers = sum(answers)
    percentage = (good_answers/all_questions) * 100
    print("you got " + str(percentage) + "% of good answers!")


main()