# Задание «Рекордсмены: находим самый продолжительный и самый короткий курс по программированию» из блока "Коллекции данных: словари."

def create_course_list(courses, mentors, durations):
    courses_list = []
    for title, mentor_list, duration in zip(courses, mentors, durations):
        course_dict = {"title": title, "mentors": mentor_list, "duration": duration}
        courses_list.append(course_dict)
    return courses_list


def find_min_max_durations(courses_list):
    min_duration = min(course["duration"] for course in courses_list)
    max_duration = max(course["duration"] for course in courses_list)
    return min_duration, max_duration


def find_courses_by_duration(courses_list, duration):
    matching_courses = [course["title"] for course in courses_list if course["duration"] == duration]
    return matching_courses


def main():
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
               "Frontend-разработчик с нуля"]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков", "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]

    courses_list = create_course_list(courses, mentors, durations)

    min_duration, max_duration = find_min_max_durations(courses_list)

    courses_min = find_courses_by_duration(courses_list, min_duration)
    courses_max = find_courses_by_duration(courses_list, max_duration)

    print(f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_duration} месяца(ев)')
    print(f'Самый длинный курс(ы): {", ".join(courses_max)} - {max_duration} месяца(ев)')


if __name__ == "__main__":
    main()
