from math import exp, cosh
from abc import ABC


class ActivationFunction(ABC):
    def __init__(self):
        self.t = None

    def forward(self, x):
        pass

    def backward(self):
        pass


class ReLU(ActivationFunction):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        self.t = x
        return max(0, x)

    def backward(self):
        return 1 if self.t >= 0 else 0
          

class Sigmoid(ActivationFunction):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        if self.t is None:
            self.t = x
        return 1 / (1 + exp(-x))

    def backward(self):
        return self.forward(self.t) * (1 - self.forward(self.t))


class Tanh(ActivationFunction):
    def __int__(self):
        super().__init__()

    def forward(self, x):
        self.t = x
        return (exp(x) - exp(-x)) / (exp(x) + exp(-x))

    def backward(self):
        return 1 / cosh(self.t) ** 2


a = 10

sigm = Sigmoid()
relu = ReLU()
tanh = Tanh()

print(f'Sigmoid: Forward: {sigm.forward(a)} Backward: {sigm.backward()}')
print(f'ReLU: Forward: {relu.forward(a)} Backward: {relu.backward()}')
print(f'Tanh: Forward: {tanh.forward(a)} Backward: {tanh.backward()}')

