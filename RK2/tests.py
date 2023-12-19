import unittest
from RK1 import RK1


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.tr1 = {'Books and Humans': [('Пикник на обочине', 950), ('Три товарища', 1100)], 'Book World': [('Зеленая миля', 1200)]}

        self.tr2 = [('Book World', 1200), ('Books and Humans', 1100), ('The reading owl', 1050), ('Read and enjoy', 850)]

        self.tr3 = ('\n'
             'Book World\n''\tПикник на обочине 950\n''\tТри товарища 1100\n''\tДесять негритят 850\n'
             'Books and Humans\n'
             '\tПикник на обочине 950\n'
             '\tТри товарища 1100\n'
             '\tЗеленая миля 1200\n'
             'Read and enjoy\n'
             '\tТри товарища 1100\n'
             '\tТурецкий гамбит 1050\n'
             'The reading owl\n'
             '\tЗеленая миля 1200\n'
             '\tДесять негритят 850')
        self.rk = RK1()

    def test_first(self):
        self.assertEqual(self.rk.first(), self.tr1)

    def test_second(self):
        self.assertEqual(self.rk.second(), self.tr2)

    def test_third(self):
        self.assertEqual(self.rk.third(), self.tr3)


if __name__ == "__main__":
    unittest.main()
