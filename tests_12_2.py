import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    all_results = {}
    @classmethod
    def setUpClass(cls):
        cls.result = []

    def setUp(self):
        self.name_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.name_2 = runner_and_tournament.Runner('Андрей', 9)
        self.name_3 = runner_and_tournament.Runner('Ник', 3)

    def test_tournament_1(self):
        self.all_results = runner_and_tournament.Tournament(90, self.name_1, self.name_3).start()
        self.result.append(self.all_results)
        self.assertTrue(self.all_results.get(len(self.all_results)) == 'Ник')

    def test_tournament_2(self):
        self.all_results = runner_and_tournament.Tournament(90, self.name_2, self.name_3).start()
        self.result.append(self.all_results)
        self.assertTrue(self.all_results.get(len(self.all_results)) == 'Ник')

    def test_tournament_3(self):
        self.all_results = runner_and_tournament.Tournament(90, self.name_1, self.name_2, self.name_3).start()
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
