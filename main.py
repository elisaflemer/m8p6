import numpy as np
from perceptron import Perceptron

def train_and():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1]) 
    perceptron = Perceptron()
    perceptron.train(X, y)
    print(f"in (0, 0), out: {perceptron.predict([0, 0])}")
    print(f"in (0, 1), out: {perceptron.predict([0, 1])}")
    print(f"in (1, 0), out: {perceptron.predict([1, 0])}")
    print(f"in (1, 1), out: {perceptron.predict([1, 1])}")

def train_or():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 1]) 
    perceptron = Perceptron()
    perceptron.train(X, y)
    print(f"in (0, 0), out: {perceptron.predict([0, 0])}")
    print(f"in (0, 1), out: {perceptron.predict([0, 1])}")
    print(f"in (1, 0), out: {perceptron.predict([1, 0])}")
    print(f"in (1, 1), out: {perceptron.predict([1, 1])}")

def train_nand():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([1, 1, 1, 0]) 
    perceptron = Perceptron()
    perceptron.train(X, y)
    print(f"in (0, 0), out: {perceptron.predict([0, 0])}")
    print(f"in (0, 1), out: {perceptron.predict([0, 1])}")
    print(f"in (1, 0), out: {perceptron.predict([1, 0])}")
    print(f"in (1, 1), out: {perceptron.predict([1, 1])}")

def train_xor():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0]) 
    perceptron = Perceptron()
    perceptron.train(X, y)
    print(f"in (0, 0), out: {perceptron.predict([0, 0])}")
    print(f"in (0, 1), out: {perceptron.predict([0, 1])}")
    print(f"in (1, 0), out: {perceptron.predict([1, 0])}")
    print(f"in (1, 1), out: {perceptron.predict([1, 1])}")

# Exemplo de uso
if __name__ == "__main__":
    print("AND")
    train_and()
    print("OR")
    train_or()
    print("NAND")
    train_nand()
    print("XOR")
    train_xor()