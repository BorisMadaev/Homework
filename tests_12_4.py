import unittest
from rt_with_exceptions import Runner
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            name_1 = Runner('X', -5)
            logging.info(f'"test_walk" выполнен успешно')
            for _ in range(10):
                name_1.walk()
            self.assertEqual(name_1.distance, 50)
        except ValueError:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        try:
            name_1 = Runner(35)
            for _ in range(10):
                name_1.run()
            self.assertEqual(name_1.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError:
            logging.error(f'Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        name_1 = Runner('X')
        name_2 = Runner('Y')
        for _ in range(10):
            name_1.run()
            name_2.walk()
        self.assertNotEqual(name_1.distance, name_2.distance)


logging.basicConfig(level=logging.INFO,
                    filemode='w',
                    filename="runner_tests.log",
                    encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
if __name__ == '__main__':
    unittest.main()
