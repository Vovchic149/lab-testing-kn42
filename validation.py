def check_positive_number(value):
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError("Введено не число")
    if number <= 0:
        raise ValueError("Число має бути більшим за нуль")
    return number
