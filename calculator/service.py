class Service:
    def __init__(self, payload):
        self._num1 = payload.num1
        self._num2 = payload.num2

    def add(self):
        return self._num1 + self._num2

    def minus(self):
        return self._num1 - self._num2

    def multi(self):
        return self._num1 * self._num2

    def divide(self):
        return self._num1 / self._num2