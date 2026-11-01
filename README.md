# Звіт до роботи

**Тема:** Загальне тестування та unit-тестування (Python, unittest)

**Мета роботи:** навчитись перевіряти дані за допомогою `assert` та `raise ValueError`, писати unit-тести з `unittest.TestCase`, використовувати `subTest` і `unittest.mock.patch`, оформлювати проєкт із `pyproject.toml` та `Makefile`.

**Виконав:** Бейгул Володимир, група КН-42

## Виконання роботи

### Структура проєкту

```text
01_general_and_unittest/
├── app.py                 клас Figure (get_figure_type, get_figure_length, get_angles)
├── test.py                тести Figure
├── validation.py          власна перевірка введеного числа
├── input_utils.py         функція з input()
├── text_utils.py          count_symbols, count_vowels, divide
├── test_validation.py
├── test_input_utils.py    тести з patch
├── test_text_utils.py
├── demo.py                демонстрація перевірки числа
├── conftest.py            маркер unit для pytest
├── pyproject.toml
├── Makefile
└── pictures/
```

### Команди запуску

```bash
python demo.py
python test.py
python -m unittest -v
make unittest
```

Для pytest і покриття (після `poetry install`): `make test`, `make unit`, `make coverage`, `make html`, `make clean`.

### Завдання 1. Перевірка даних

Розглянув два способи перевірки: `assert` зупиняє програму з повідомленням, `raise ValueError` повідомляє про неправильний аргумент.

⭐ Створив власну перевірку введеного числа: функція [`check_positive_number`](validation.py) перетворює значення на число та викликає `ValueError`, якщо це не число або воно не більше нуля.

```python
def check_positive_number(value):
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError("Введено не число")
    if number <= 0:
        raise ValueError("Число має бути більшим за нуль")
    return number
```

Результат `python demo.py` для правильного та неправильного введення:

```text
assert: Число має бути більшим за нуль!
'5': OK, 5.0
'3.5': OK, 3.5
'-3': ValueError, Число має бути більшим за нуль
'0': ValueError, Число має бути більшим за нуль
'abc': ValueError, Введено не число
'': ValueError, Введено не число
```

Правильне введення (`5`, `3.5`) повертає число. Для `-3` і `0` отримано `ValueError` «Число має бути більшим за нуль», для `abc` і порожнього рядка `ValueError` «Введено не число».

![Результат demo.py](pictures/01_demo.png)

### Завдання 2. Тестування функцій

Створив у [`text_utils.py`](text_utils.py) функції `count_symbols`, `divide` та ⭐ `count_vowels` (голосні латиниці та української: `аеєиіїоуюя`, без урахування регістру).

```python
VOWELS = set("аеєиіїоуюяaeiou")


def count_symbols(text: str) -> int:
    return len(text)


def count_vowels(text: str) -> int:
    return sum(1 for symbol in text.lower() if symbol in VOWELS)


def divide(a, b):
    return a / b
```

Тести в [`test_text_utils.py`](test_text_utils.py):

- `count_symbols("abc") == 3` та `count_symbols("") == 0`;
- `divide(1, 0)` викликає `ZeroDivisionError`;
- ⭐ `count_vowels`: латиниця (`hello` → 2), великі літери (`AEI` → 3), без голосних (`rhythm` → 0);
- 🔥 порожній рядок → 0, рядок із цифрами `12345` → 0, українські літери `Україна` → 4 та `єїюя` → 4.

### Завдання 3. Перший приклад (клас Figure)

Створив кілька об'єктів `Figure` і перевірив `get_figure_type` та `get_figure_length`. Вихідні тести прикладу (`test.py`):

```python
import unittest

from app import Figure


class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Figure("квадрат", 5)

    def test_figure_type(self):
        self.assertEqual("квадрат", self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.obj.get_figure_length)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_invalid_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

⭐ **Тест довжини та пошук помилки.** У наданій версії `app.py` тест `test_figure_length` вже не закоментований і проходить одразу (`Ran 4 tests ... OK`). Метод `get_figure_length` повертає `self.length`, яке задається в конструкторі, тому помилки в реалізації довжини я не виявив.

⭐ **Метод `get_angles` за підходом «спочатку тест».** Тести для `get_angles` написав до реалізації методу. Припущення: трикутник вважається рівностороннім, бо в `Figure` задається лише одна довжина. Результат `python -m unittest -v` **до** додавання методу:

```text
test_all_figure_types (test.TestFigure.test_all_figure_types) ... ok
test_angles_rectangle (test.TestFigure.test_angles_rectangle) ... ERROR
test_angles_square (test.TestFigure.test_angles_square) ... ERROR
test_angles_triangle (test.TestFigure.test_angles_triangle) ... ERROR
test_figure_length (test.TestFigure.test_figure_length) ... ok
test_figure_type (test.TestFigure.test_figure_type) ... ok
test_invalid_figure (test.TestFigure.test_invalid_figure) ... ok
test_invalid_length (test.TestFigure.test_invalid_length) ... ok
test_lengths_subtest (test.TestFigure.test_lengths_subtest) ... ok
test_negative_length (test.TestFigure.test_negative_length) ... ok
test_unknown_figure_type (test.TestFigure.test_unknown_figure_type) ... ok
test_zero_length (test.TestFigure.test_zero_length) ... ok
test_negative_input (test_input_utils.TestAskNumber.test_negative_input) ... ok
test_text_input (test_input_utils.TestAskNumber.test_text_input) ... ok
test_valid_input (test_input_utils.TestAskNumber.test_valid_input) ... ok
test_count_symbols (test_text_utils.TestCountSymbols.test_count_symbols) ... ok
test_digits (test_text_utils.TestCountVowels.test_digits) ... ok
test_digits_with_vowels (test_text_utils.TestCountVowels.test_digits_with_vowels) ... ok
test_empty_string (test_text_utils.TestCountVowels.test_empty_string) ... ok
test_latin (test_text_utils.TestCountVowels.test_latin) ... ok
test_no_vowels (test_text_utils.TestCountVowels.test_no_vowels) ... ok
test_ukrainian (test_text_utils.TestCountVowels.test_ukrainian) ... ok
test_ukrainian_special_letters (test_text_utils.TestCountVowels.test_ukrainian_special_letters) ... ok
test_uppercase (test_text_utils.TestCountVowels.test_uppercase) ... ok
test_divide (test_text_utils.TestDivide.test_divide) ... ok
test_divide_by_zero (test_text_utils.TestDivide.test_divide_by_zero) ... ok
test_empty (test_validation.TestCheckPositiveNumber.test_empty) ... ok
test_negative (test_validation.TestCheckPositiveNumber.test_negative) ... ok
test_not_a_number (test_validation.TestCheckPositiveNumber.test_not_a_number) ... ok
test_valid_float (test_validation.TestCheckPositiveNumber.test_valid_float) ... ok
test_valid_integer (test_validation.TestCheckPositiveNumber.test_valid_integer) ... ok
test_zero (test_validation.TestCheckPositiveNumber.test_zero) ... ok

======================================================================
ERROR: test_angles_rectangle (test.TestFigure.test_angles_rectangle)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/claude/work/01_general_and_unittest/test.py", line 52, in test_angles_rectangle
    self.assertEqual([90, 90, 90, 90], Figure("прямокутник", 5).get_angles())
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Figure' object has no attribute 'get_angles'

======================================================================
ERROR: test_angles_square (test.TestFigure.test_angles_square)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/claude/work/01_general_and_unittest/test.py", line 49, in test_angles_square
    self.assertEqual([90, 90, 90, 90], Figure("квадрат", 5).get_angles())
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Figure' object has no attribute 'get_angles'

======================================================================
ERROR: test_angles_triangle (test.TestFigure.test_angles_triangle)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/claude/work/01_general_and_unittest/test.py", line 55, in test_angles_triangle
    angles = Figure("трикутник", 5).get_angles()
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Figure' object has no attribute 'get_angles'

----------------------------------------------------------------------
Ran 32 tests in 0.005s

FAILED (errors=3)
```

Три тести кутів завершились помилкою `AttributeError: 'Figure' object has no attribute 'get_angles'`, решта 29 проходять.

Після цього додав метод:

```python
    def get_angles(self) -> list:
        if self.type == "трикутник":
            return [60, 60, 60]
        return [90, 90, 90, 90]
```

Результат `python -m unittest -v` **після** додавання методу:

```text
test_all_figure_types (test.TestFigure.test_all_figure_types) ... ok
test_angles_rectangle (test.TestFigure.test_angles_rectangle) ... ok
test_angles_square (test.TestFigure.test_angles_square) ... ok
test_angles_triangle (test.TestFigure.test_angles_triangle) ... ok
test_figure_length (test.TestFigure.test_figure_length) ... ok
test_figure_type (test.TestFigure.test_figure_type) ... ok
test_invalid_figure (test.TestFigure.test_invalid_figure) ... ok
test_invalid_length (test.TestFigure.test_invalid_length) ... ok
test_lengths_subtest (test.TestFigure.test_lengths_subtest) ... ok
test_negative_length (test.TestFigure.test_negative_length) ... ok
test_unknown_figure_type (test.TestFigure.test_unknown_figure_type) ... ok
test_zero_length (test.TestFigure.test_zero_length) ... ok
test_negative_input (test_input_utils.TestAskNumber.test_negative_input) ... ok
test_text_input (test_input_utils.TestAskNumber.test_text_input) ... ok
test_valid_input (test_input_utils.TestAskNumber.test_valid_input) ... ok
test_count_symbols (test_text_utils.TestCountSymbols.test_count_symbols) ... ok
test_digits (test_text_utils.TestCountVowels.test_digits) ... ok
test_digits_with_vowels (test_text_utils.TestCountVowels.test_digits_with_vowels) ... ok
test_empty_string (test_text_utils.TestCountVowels.test_empty_string) ... ok
test_latin (test_text_utils.TestCountVowels.test_latin) ... ok
test_no_vowels (test_text_utils.TestCountVowels.test_no_vowels) ... ok
test_ukrainian (test_text_utils.TestCountVowels.test_ukrainian) ... ok
test_ukrainian_special_letters (test_text_utils.TestCountVowels.test_ukrainian_special_letters) ... ok
test_uppercase (test_text_utils.TestCountVowels.test_uppercase) ... ok
test_divide (test_text_utils.TestDivide.test_divide) ... ok
test_divide_by_zero (test_text_utils.TestDivide.test_divide_by_zero) ... ok
test_empty (test_validation.TestCheckPositiveNumber.test_empty) ... ok
test_negative (test_validation.TestCheckPositiveNumber.test_negative) ... ok
test_not_a_number (test_validation.TestCheckPositiveNumber.test_not_a_number) ... ok
test_valid_float (test_validation.TestCheckPositiveNumber.test_valid_float) ... ok
test_valid_integer (test_validation.TestCheckPositiveNumber.test_valid_integer) ... ok
test_zero (test_validation.TestCheckPositiveNumber.test_zero) ... ok

----------------------------------------------------------------------
Ran 32 tests in 0.005s

OK
```

![Тести до виправлення](pictures/02_tests_before.png)

![Тести після виправлення](pictures/03_tests_after.png)

Запуск `python test.py` (лише тести `Figure`):

```text
test_all_figure_types (__main__.TestFigure.test_all_figure_types) ... ok
test_angles_rectangle (__main__.TestFigure.test_angles_rectangle) ... ok
test_angles_square (__main__.TestFigure.test_angles_square) ... ok
test_angles_triangle (__main__.TestFigure.test_angles_triangle) ... ok
test_figure_length (__main__.TestFigure.test_figure_length) ... ok
test_figure_type (__main__.TestFigure.test_figure_type) ... ok
test_invalid_figure (__main__.TestFigure.test_invalid_figure) ... ok
test_invalid_length (__main__.TestFigure.test_invalid_length) ... ok
test_lengths_subtest (__main__.TestFigure.test_lengths_subtest) ... ok
test_negative_length (__main__.TestFigure.test_negative_length) ... ok
test_unknown_figure_type (__main__.TestFigure.test_unknown_figure_type) ... ok
test_zero_length (__main__.TestFigure.test_zero_length) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

🔥 Додав тести для нульової довжини (`test_zero_length`), від'ємної довжини (`test_negative_length`) та невідомого типу фігури (`test_unknown_figure_type`). У всіх очікується `AssertionError`.

Спостереження: перевірки в `Figure` зроблені через `assert`. Якщо запустити Python з прапорцем `-O`, `assert` вимикаються, і `Figure("коло", -5)` створюється без помилки (перевірив: `python -O` повернув довжину `-5`). Для перевірки вхідних даних надійніше `raise ValueError`, але в прикладі лишив `assert`, як вимагає завдання.

### Завдання 4. Життєвий цикл тесту

У `test.py` використано `setUp`, який перед кожним тестом створює `Figure("квадрат", 5)`. Усі методи тестів починаються з `test_`, тести незалежні, бо кожен створює або отримує власний об'єкт.

### Завдання 5. subTest

⭐ Тест `test_all_figure_types` перевіряє всі типи `Figure.FIGURES`, а `test_lengths_subtest` довжини 1, 5, 10:

```python
    def test_all_figure_types(self):
        for figure_type in Figure.FIGURES:
            with self.subTest(figure_type=figure_type):
                figure = Figure(figure_type, 4)
                self.assertEqual(figure_type, figure.get_figure_type)
                self.assertEqual(4, figure.get_figure_length)
```

**Призначення `subTest`:** без нього цикл зупинився б на першому наборі даних, що не пройшов, а інші набори не перевірились би. `subTest` виконує всі набори й у разі помилки показує, який саме (`figure_type='трикутник'`), тому не треба писати окремий тест на кожен тип.

### Завдання 6. mock і patch

⭐ Функція з `input()` у [`input_utils.py`](input_utils.py):

```python
from validation import check_positive_number


def ask_number(prompt="Введіть число: "):
    return check_positive_number(input(prompt))
```

Тести в [`test_input_utils.py`](test_input_utils.py):

```python

    @patch("builtins.input", return_value="5")
    def test_valid_input(self, mock_input):
        self.assertEqual(5.0, ask_number())
        mock_input.assert_called_once_with("Введіть число: ")

    @patch("builtins.input", return_value="-1")
    def test_negative_input(self, mock_input):
        with self.assertRaises(ValueError):
            ask_number()
        mock_input.assert_called_once()

    @patch("builtins.input", return_value="abc")
    def test_text_input(self, mock_input):
        with self.assertRaises(ValueError):
            ask_number()
        mock_input.assert_called_once()
```

**Призначення `mock`:** `@patch("builtins.input", return_value="5")` підміняє `input`, тому тест не чекає введення з клавіатури, виконується автоматично й повторювано. Через `mock_input.assert_called_once_with("Введіть число: ")` також перевіряється, що функція запитала число один раз і з правильним текстом.

### Налаштування проєкту

У [`pyproject.toml`](pyproject.toml) налаштовано Poetry, dev-залежності (`pytest`, `pytest-cov`, `coverage`), `[tool.pytest.ini_options]` (`testpaths`, `python_files`, маркери `unit` і `integration`) та `[tool.coverage.*]`. У [`Makefile`](Makefile) цілі `install`, `test`, `unit`, `integration`, `coverage`, `html`, `clean` (відступи табуляцією) та додаткова ціль `unittest`.

## Висновок

Виконав усі завдання роботи, включно з ⭐ та 🔥: власна перевірка числа, функція підрахунку голосних із тестами (порожній рядок, цифри, українські літери), тести для `Figure` (нульова, від'ємна довжина, невідомий тип), метод `get_angles` із тестами для квадрата, прямокутника й трикутника, тести з `subTest` та `patch`. Усі 32 тести проходять.

Мети роботи досягнуто: навчився перевіряти дані через `assert` і `ValueError`, писати тести на `unittest.TestCase`, перевіряти винятки через `assertRaises`, використовувати `subTest` і `patch`.

Складності: у наданій версії `app.py` помилки в `get_figure_length` не знайшов, тест довжини проходить одразу. Тому приклад тесту, що спочатку не проходить і потім виправляється, показав на `get_angles` (три тести падали з `AttributeError` до реалізації методу).

Feedback: формат здачі через посилання на папку в репозиторії зручний, бо в одному місці лежать код, тести та звіт.

Suggestions: додати в завдання приклад із помилкою, яку справді видно в тестах, і окремо розібрати різницю між `assert` та `ValueError` для перевірки даних.
