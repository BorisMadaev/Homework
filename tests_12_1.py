import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        тест метода walk
        :return:
        """
        name_1 = Runner('X')
        for _ in range(10):
            Runner.walk(name_1)
        self.assertEqual(name_1.distance, 50)

    def test_run(self):
        """
        тест метода run
        :return:
        """
        name_1 = Runner('X')
        for _ in range(10):
            Runner.run(name_1)
        self.assertEqual(name_1.distance, 100)

    def test_challenge(self):
        """
        тест различия методов walk и run
        :return:
        """
        name_1 = Runner('X')
        name_2 = Runner('Y')
        for _ in range(10):
            Runner.run(name_1)
            Runner.walk(name_2)
        self.assertNotEqual(name_1.distance, name_2.distance)


if __name__ == '__main__':
    unittest.main()
