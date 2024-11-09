import unittest
from runner import Runner
from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        name_1 = Runner('X')
        for _ in range(10):
            name_1.walk()
        self.assertEqual(name_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        name_1 = Runner('X')
        for _ in range(10):
            name_1.run()
        self.assertEqual(name_1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        name_1 = Runner('X')
        name_2 = Runner('Y')
        for _ in range(10):
            name_1.run()
            name_2.walk()
        self.assertNotEqual(name_1.distance, name_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.result = []

    def setUp(self):
        self.name_1 = Runner('Усэйн', 10)
        self.name_2 = Runner('Андрей', 9)
        self.name_3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_first_tournament(self):
        self.all_results = Tournament(90, self.name_1, self.name_3).start()
        self.result.append(self.all_results)
        self.assertTrue(self.all_results.get(len(self.all_results)) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_second_tournament(self):
        self.all_results = Tournament(90, self.name_2, self.name_3).start()
        self.result.append(self.all_results)
        self.assertTrue(self.all_results.get(len(self.all_results)) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_third_tournament(self):
        self.all_results = Tournament(90, self.name_1, self.name_2, self.name_3).start()
        self.result.append(self.all_results)
        self.assertTrue(self.all_results.get(len(self.all_results)) == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for i in range(len(cls.result)):
            dict_new = {}
            for j in range(len(cls.result[i])):
                dict_new[j+1] = str(cls.result[i].get(j+1))
            print(dict_new)


if __name__ == '__main__':
    unittest.main()
