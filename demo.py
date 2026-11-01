from validation import check_positive_number

number = -1
try:
    assert number > 0, "Число має бути більшим за нуль!"
except AssertionError as error:
    print(f"assert: {error}")

for value in ["5", "3.5", "-3", "0", "abc", ""]:
    try:
        result = check_positive_number(value)
        print(f"{value!r}: OK, {result}")
    except ValueError as error:
        print(f"{value!r}: ValueError, {error}")
