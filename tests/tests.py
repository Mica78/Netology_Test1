import unittest
from main import get_unique_names, get_top_3, get_course_array, courses, mentors, durations


class MyTestCase(unittest.TestCase):

    def test_courses(self):
        self.assertIsInstance(courses, list)
        for value in courses:
            self.assertIsInstance(value, str)

    def test_mentors(self):
        self.assertIsInstance(mentors, list)
        for values in mentors:
            self.assertIsInstance(values, list)
            for value in values:
                self.assertIsInstance(value, str)
                self.assertEqual(len(value.split()), 2)

    def test_durations(self):
        self.assertIsInstance(durations, list)
        for duration in durations:
            self.assertIsInstance(duration, int)

    def test_get_uniq_name(self):
        self.assertEqual(get_unique_names(), "Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, "
                                             "Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, "
                                             "Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, "
                                             "Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, "
                                             "Эдгар, Юрий")

    def test_get_top3(self):
        self.assertEqual(get_top_3(), "Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)")

    def test_get_course_array(self):
        self.assertEqual(get_course_array(),
                         (
                             'Порядок курсов по длительности: [2, 0, 1, 3]',
                             'Порядок курсов по количеству преподавателей: [0, 3, 2, 1]'
                         )
                         )


if __name__ == '__main__':
    unittest.main()
