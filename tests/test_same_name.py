# Задание 1
import pytest
from same_name import create_course_list, find_same_names


# Тест для create_course_list
def test_create_course_list():
    courses = ["Курс1", "Курс2"]
    mentors = [["Ментор1", "Ментор2"], ["Ментор3", "Ментор4"]]
    durations = [10, 20]
    expected = [
        {"title": "Курс1", "mentors": ["Ментор1", "Ментор2"], "duration": 10},
        {"title": "Курс2", "mentors": ["Ментор3", "Ментор4"], "duration": 20}
    ]
    assert create_course_list(courses, mentors, durations) == expected


# Тест для find_same_names
def test_find_same_names():
    course = {"title": "Курс", "mentors": ["Ментор1", "Ментор1", "Ментор2", "Ментор3"], "duration": 10}
    expected = ["Ментор1"]
    assert find_same_names(course) == expected


if __name__ == "__main__":
    pytest.main()
