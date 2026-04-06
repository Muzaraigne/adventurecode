class TuringMachine:
    def __init__(self, name):
        self.name = name
        self.state = 'A'
        self.tape = {}
        self.cursor = 0

    def stateA(self):
        if self.tape.get(self.cursor, 0) == 0:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = 'B'
        else:
            self.tape[self.cursor] = 0
            self.cursor -= 1
            self.state = 'C'

    def stateB(self):
        if self.tape.get(self.cursor, 0) == 0:
            self.tape[self.cursor] = 1
            self.cursor -= 1
            self.state = 'A'
        else:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = 'D'

    def stateC(self):
        if self.tape.get(self.cursor, 0) == 0:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = 'A'
        else:
            self.tape[self.cursor] = 0
            self.cursor -= 1
            self.state = 'E'
    def stateD(self):
        if self.tape.get(self.cursor, 0) == 0:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = 'A'
        else:
            self.tape[self.cursor] = 0
            self.cursor += 1
            self.state = 'B'
    def stateE(self):
        if self.tape.get(self.cursor, 0) == 0:
            self.tape[self.cursor] = 1
            self.cursor -= 1
            self.state = 'F'
        else:
            self.tape[self.cursor] = 1
            self.cursor -= 1
            self.state = 'C'
    def stateF(self):
        if self.tape.get(self.cursor, 0) == 0:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = 'D'
        else:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = 'A'

    def step(self):
        if self.state == 'A':
            self.stateA()
        elif self.state == 'B':
            self.stateB()
        elif self.state == 'C':
            self.stateC()
        elif self.state == 'D':
            self.stateD()
        elif self.state == 'E':
            self.stateE()
        elif self.state == 'F':
            self.stateF()
    def checksum(self):
        return sum(self.tape.values())

class TestMachine(TuringMachine):
    def __init__(self, name):
        super().__init__(name)

    def stateA(self):
        if self.tape.get(self.cursor, 0) == 0:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = 'B'
        else:
            self.tape[self.cursor] = 0
            self.cursor -= 1
            self.state = 'B'

    def stateB(self):
        if self.tape.get(self.cursor, 0) == 0:
            self.tape[self.cursor] = 1
            self.cursor -= 1
            self.state = 'A'
        else:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = 'A'