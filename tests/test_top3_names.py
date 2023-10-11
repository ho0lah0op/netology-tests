# Задание 1
import pytest
from top3_names import main


# Smoke Test
def test_main_no_errors():
    mentors = [
        ["Иван Иванов", "Кирилл Кириллов"],
        ["Григорий Григорьев", "Иван Ивашников"]
    ]
    courses = ["Курс 1", "Курс 2"]
    result = main(mentors, courses)
    assert isinstance(result, str)


# Тестирование основного функционала Top3_Names.main()
def test_main_output():
    mentors = [
        ["Иван Иванов", "Кирилл Кириллов"],
        ["Григорий Григорьев", "Иван Ивашников"]
    ]
    courses = ["Курс 1", "Курс 2"]
    result = main(mentors, courses)
    expected = "Иван: 2 раз(а), Григорий: 1 раз(а), Кирилл: 1 раз(а)"
    assert result == expected


if __name__ == "__main__":
    pytest.main()