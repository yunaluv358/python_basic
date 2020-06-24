from calculator.model import Model
from calculator.service import Service

class Controller:

    def __init__(self):
        pass

    def calc(self, num1, num2, opcode):
        model = Model()
        model.num1 = num1
        model.num2 = num2
        model.opcode = opcode
        service = Service(model)
        if opcode == '+': result = service.add()
        if opcode == '-': result = service.minus()
        if opcode == '*': result = service.multi()
        if opcode == '/': result = service.divide()
        return result

