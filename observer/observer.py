def contador_de_palavras(frase):
    frase = frase.strip()
    palavras = frase.split()
    return len(palavras)

def contador_de_palavras_pares(frase):
    frase = frase.strip()
    palavras = frase.split()

    palavras_pares = 0
    for palavra in palavras:
        if len(palavra) % 2 == 0:
            palavras_pares += 1

    return palavras_pares

def contador_palavras_maisculo(frase):
    frase = frase.strip()
    palavras = frase.split()

    palavras_maiscula = 0
    for palavra in palavras:
        if palavra[0].isupper():
            palavras_maiscula += 1

    return palavras_maiscula

class Observavel:
    def __init__(self):
        self.observers = []

    def registrar_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notifica_observer(self, data):
        for observer in self.observers:
            observer.update(data)


class Observer:
    def update(self, data):
        pass


# Concrete observer implementation
class ConcreteObserver(Observer):
    def update(self, data):
        print("Frase mandada:", data)
        print("A frase contem "+str(contador_de_palavras(data))+" palavras, das quais "+str(contador_de_palavras_pares(data))
        +" sao pares e "+str(contador_palavras_maisculo(data))+" sao maiusculas.\n")


# Usage example
observavel = Observavel()

observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

observavel.registrar_observer(observer1)
observavel.registrar_observer(observer2)

observavel.notifica_observer("oi galera tudo bem com vcs")

observavel.remove_observer(observer2)

observavel.notifica_observer("Observer2 foi removido.")
