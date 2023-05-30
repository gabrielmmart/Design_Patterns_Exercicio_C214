class SortStrategy:
    def sort(self, dados):
        pass


class BubbleSort(SortStrategy):
    def sort(self, dados):
        dados_ordenados = list(dados)
        n = len(dados_ordenados)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if dados_ordenados[j] > dados_ordenados[j + 1]:
                    dados_ordenados[j], dados_ordenados[j + 1] = dados_ordenados[j + 1], dados_ordenados[j]
        return dados_ordenados


class QuickSort(SortStrategy):
    def sort(self, dados):
        dados_ordenados = list(dados)
        self._quick_sort(dados_ordenados, 0, len(dados_ordenados) - 1)
        return dados_ordenados

    def _quick_sort(self, dados, low, high):
        if low < high:
            pivot = self._partition(dados, low, high)
            self._quick_sort(dados, low, pivot - 1)
            self._quick_sort(dados, pivot + 1, high)

    def _partition(self, dados, low, high):
        pivot = dados[high]
        i = low - 1
        for j in range(low, high):
            if dados[j] < pivot:
                i += 1
                dados[i], dados[j] = dados[j], dados[i]
        dados[i + 1], dados[high] = dados[high], dados[i + 1]
        return i + 1


class InsertionSort(SortStrategy):
    def sort(self, dados):
        dados_ordenados = list(dados)
        n = len(dados_ordenados)
        for i in range(1, n):
            key = dados_ordenados[i]
            j = i - 1
            while j >= 0 and dados_ordenados[j] > key:
                dados_ordenados[j + 1] = dados_ordenados[j]
                j -= 1
            dados_ordenados[j + 1] = key
        return dados_ordenados
    
    
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, dados):
        return self.strategy.sort(dados)


dados = [5, 2, 7, 1, 9]

bubble_sort_strategy = BubbleSort()
quick_sort_strategy = QuickSort()
insertion_sort_strategy = InsertionSort()

sorter = Sorter(bubble_sort_strategy)
dados_ordenados = sorter.sort(dados)
print("Bubble sort:", dados_ordenados)

sorter = Sorter(quick_sort_strategy)
dados_ordenados = sorter.sort(dados)
print("Quick sort:", dados_ordenados)

sorter = Sorter(insertion_sort_strategy)
dados_ordenados = sorter.sort(dados)
print("Insertion sort:", dados_ordenados)