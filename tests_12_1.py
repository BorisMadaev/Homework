import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        тест метода walk
        :return:
        """
        self.name_ = runner.Runner('X')
        for _ in range(10):
            runner.Runner.walk(self.name_)
        self.assertEqual(self.name_.distance, 50)

    def test_run(self):
        """
        тест метода run
        :return:
        """
        self.name_ = runner.Runner('X')
        for _ in range(10):
            runner.Runner.run(self.name_)
        self.assertEqual(self.name_.distance, 100)

    def test_challenge(self):
        """
        тест различия методов walk и run
        :return:
        """
        self.name_1 = runner.Runner('X')
        self.name_2 = runner.Runner('Y')
        for _ in range(10):
            runner.Runner.run(self.name_1)
            runner.Runner.walk(self.name_2)
        self.assertNotEqual(self.name_1.distance, self.name_2.distance)


if __name__ == '__main__':
    unittest.main()
