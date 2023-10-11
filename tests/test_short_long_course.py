# Задание 1
import pytest
import sys
from io import StringIO
from short_long_course import create_course_list, find_min_max_durations, find_courses_by_duration
from short_long_course import main as slc_main


# Test data
courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

# Тестирование всех функций в изоляции
def test_create_course_list():
    expected = [
        {"title": "Java-разработчик с нуля", "mentors": mentors[0], "duration": durations[0]},
        {"title": "Fullstack-разработчик на Python", "mentors": mentors[1], "duration": durations[1]},
        {"title": "Python-разработчик с нуля", "mentors": mentors[2], "duration": durations[2]},
        {"title": "Frontend-разработчик с нуля", "mentors": mentors[3], "duration": durations[3]}
    ]
    assert create_course_list(courses, mentors, durations) == expected


def test_find_min_max_durations():
    courses_list = create_course_list(courses, mentors, durations)
    assert find_min_max_durations(courses_list) == (12, 20)


def test_find_courses_by_duration():
    courses_list = create_course_list(courses, mentors, durations)
    assert find_courses_by_duration(courses_list, 12) == ["Python-разработчик с нуля"]
    assert find_courses_by_duration(courses_list, 20) == ["Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]


# Тестирование функции main
@pytest.mark.parametrize("expected", [
    "Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)\nСамый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)\n"
])
def test_main(expected):
    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        slc_main()
        output = out.getvalue()
        assert output == expected
    finally:
        sys.stdout = saved_stdout


if __name__ == "__main__":
    pytest.main()
