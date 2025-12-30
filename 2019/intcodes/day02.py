
class IntCode:
    def __init__(self, data):
        self.program = data
        self.pc = 0

    def run(self):
        instr = self.program[self.pc]

        should_stop = False

        if instr == 1:
            self.add()
        elif instr == 2:
            self.mult()
        elif instr == 99:
            should_stop = True

        if should_stop:
            return

        self.pc += 4
        self.run()

    def add(self):
        val1 = self.program[self.program[self.pc + 1]]
        val2 = self.program[self.program[self.pc + 2]]
        self.program[self.program[self.pc + 3]] = val1 + val2

    def mult(self):
        val1 = self.program[self.program[self.pc + 1]]
        val2 = self.program[self.program[self.pc + 2]]
        self.program[self.program[self.pc + 3]] = val1 * val2
