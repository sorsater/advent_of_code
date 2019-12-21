class Intcode():
    def __init__(self, program, day, inputs=[]):
        self.program = program
        self.pc = 0
        self.halted = False
        self.inputs = inputs
        self.num_params = [0, 2, 2, 0, 1, 2, 2, 2, 2]
        self.outputs = []
        self.day = day

    def get_value(self, idx, mode='0'):
        if mode == '0':
            return self.program[self.program[idx]]
        else:
            return self.program[idx]

    def assign_value(self, idx, value, mode='0'):
        if mode == '0':
            self.program[self.program[idx]] = value
        else:
            self.program[idx] = value

    def add_input(self, val):
        self.inputs.append(val)

    def get_idxs(self, parameter_modes, next_vals):
        return [self.program[val] if parameter_modes[p_idx] == '0' else val for p_idx, val in enumerate(next_vals)]

    def set_pc(self, pc):
        self.pc = pc

    def run_program(self):
        while not self.halted:
            str_instr = '{:05d}'.format(self.program[self.pc])
            instr, parameter_modes = int(str_instr[-2:]), str_instr[:3]

            if instr == 99:
                self.halted = True
                if self.day == 2:
                    return self.program[0]
                elif self.day == 5:
                    return self.outputs
                return False
            values = self.get_idxs(parameter_modes[1:][::-1], self.program[self.pc+1:self.pc+1+self.num_params[instr]])

            if instr == 1:
                a, b = values[0], values[1]
                self.assign_value(self.pc + 3, a + b, '0')
                self.set_pc(self.pc + 4)
            elif instr == 2:
                a, b = values[0], values[1]
                self.assign_value(self.pc + 3, a * b, '0')
                self.set_pc(self.pc + 4)
            elif instr == 3:
                self.assign_value(self.pc + 1, self.inputs[0], '0')
                self.inputs = self.inputs[1:]
                self.set_pc(self.pc + 2)
            elif instr == 4:
                self.outputs.append(values[0])
                self.set_pc(self.pc + 2)
                if self.day == 7:
                    return self.outputs[-1]
            elif instr == 5:
                self.set_pc(values[1] if values[0] != 0 else self.pc + 3)
            elif instr == 6:
                self.set_pc(values[1] if values[0] == 0 else self.pc + 3)
            elif instr == 7:
                val = 1 if values[0] < values[1] else 0
                self.assign_value(self.pc + 3, val, mode='0')    
                self.set_pc(self.pc + 4)
            elif instr == 8:
                val = 1 if values[0] == values[1] else 0
                self.assign_value(self.pc + 3, val, mode='0')
                self.set_pc(self.pc + 4)
            else:
                assert False, 'Bad instr: {} {}'.format(instr, self.pc)
