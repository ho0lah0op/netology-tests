# Задание «Это вы мне? Подсчитываем тёзок на каждом курсе» из блока "Коллекции данных: словари."

def create_course_list(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    return courses_list


def find_same_names(course):
    unique_names = sorted(list(set([mentor.split()[0] for mentor in course["mentors"]])))
    same_name_list = []
    for name in unique_names:
        count = 0
        for mentor in course["mentors"]:
            if name in mentor:
                count += 1
        if count > 1:
            same_name_list.append(name)
    return same_name_list


def print_same_name_courses(courses_list):
    for course in courses_list:
        same_name_list = find_same_names(course)
        if same_name_list:
            tezki = ", ".join(sorted([mentor for mentor in course["mentors"] if mentor.split()[0] in same_name_list]))
            return f"На курсе {course['title']} есть тёзки: {tezki}"


def main():
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "АлександР Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]
    courses_list = create_course_list(courses, mentors, durations)
    print_same_name_courses(courses_list)


if __name__ == "__main__":
    main()

