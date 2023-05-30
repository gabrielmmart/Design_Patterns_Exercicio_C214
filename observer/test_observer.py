import unittest
import observer

class TesteStrategy(unittest.TestCase):

    def setUp(self):
        self.dados = [5, 2, 7, 1, 9]

    def test_InstanciaObserver(self):
        ob = observer.Observer()
        erro = 'objeto nao e instancia da classe'
        self.assertIsInstance(ob, observer.Observer, erro)

    def test_ContadorDePalavras(self):
        resultado = observer.contador_de_palavras('existem tres palavras')
        self.assertEqual(resultado, 3)

    def test_Contador_De_Palavras_Pares(self):
        resultado2 = observer.contador_de_palavras_pares('existem tres palavras')
        self.assertEqual(resultado2, 2)

    def test_Contador_De_Palavras_Maiusculas(self):
        resultado2 = observer.contador_palavras_maisculo('existem Tres palavras')
        self.assertEqual(resultado2, 1)


if __name__ == '__main__':
    unittest.main()