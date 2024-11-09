import unittest
import tests_12_3


testsuite_new = unittest.TestSuite()
testsuite_new.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testsuite_new.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
object_new = unittest.TextTestRunner(verbosity=2)
object_new.run(testsuite_new)
