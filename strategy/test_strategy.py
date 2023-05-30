import unittest
import strategy

class TesteStrategy(unittest.TestCase):

    def setUp(self):
        self.dados = [5, 2, 7, 1, 9]

    def test_InstanciaBubbleSort(self):
        bubble_sort_strategy = strategy.BubbleSort()
        erro = 'objeto nao e instancia da classe'
        self.assertIsInstance(bubble_sort_strategy, strategy.BubbleSort, erro)

    def test_InstanciaInsertionSort(self):
        insertion_sort_strategy = strategy.InsertionSort()
        erro = 'objeto e instancia da classe'
        self.assertNotIsInstance(insertion_sort_strategy, strategy.BubbleSort, erro)

    def test_QuickSortOrdenando(self):
        quick_sort_strategy = strategy.QuickSort()
        sorter = strategy.Sorter(quick_sort_strategy)
        dados_ordenados = sorter.sort(self.dados)
        self.assertEqual(dados_ordenados, [1, 2, 5, 7, 9])

    def test_BubbleSortOrdenando(self):
        bubble_sort_strategy = strategy.BubbleSort()
        sorter = strategy.Sorter(bubble_sort_strategy)
        dados_ordenados = sorter.sort(self.dados)
        self.assertEqual(dados_ordenados, [1, 2, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()