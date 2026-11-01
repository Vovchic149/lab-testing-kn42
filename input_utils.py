from validation import check_positive_number


def ask_number(prompt="Введіть число: "):
    return check_positive_number(input(prompt))
