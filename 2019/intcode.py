class Intcode():
    def __init__(self, program, day, inputs=[]):
        self.program = program
        self.pc = 0
        self.halted = False
        self.inputs = inputs
        self.outputs = []
        self.day = day
        self.relative_base = 0
        self.memory = {}
        self.instr_dict = {
                1: {'data': [0, 1], 'idx': 2},
                2: {'data': [0, 1], 'idx': 2},
                3: {'data': None, 'idx': 0},
                4: {'data': [0], 'idx': None},
                5: {'data': [0, 1], 'idx': None},
                6: {'data': [0, 1], 'idx': None},
                7: {'data': [0, 1], 'idx': 2},
                8: {'data': [0, 1], 'idx': 2},
                9: {'data': [0], 'idx': None}
            }

    def add_input(self, val):
        self.inputs.append(val)

    def get_data(self, idx, mode):
        wanted_pos = self.get_idx(idx, mode)
        if wanted_pos <= len(self.program) - 1:
            return self.program[wanted_pos]
        else:
            return self.memory[wanted_pos]

    def get_idx(self, idx, mode):
        if mode == 0:
            return self.program[idx] if idx <= len(self.program) - 1 else self.memory[idx]
        elif mode == 1:
            return idx
        elif mode == 2:
            return self.relative_base + self.program[idx] if idx <= len(self.program) - 1 else self.memory[idx]

    def set_pc(self, pc):
        self.pc = pc

    def set_relative_base(self, value):
        self.relative_base += value

    def assign_value(self, idx, value):
        if idx <= len(self.program) - 1:
            self.program[idx] = value
        else:
            self.memory[idx] = value

    def run_program(self):
        while not self.halted:
            str_instr = '{:05d}'.format(self.program[self.pc])
            instr, parameter_modes = int(str_instr[-2:]), str_instr[:3]

            if instr == 99:
                self.halted = True
                if self.day == 2:
                    return self.program[0]
                elif self.day == 5 or self.day == 9:
                    return self.outputs
                return False

            # Number of data parameter
            num_data = self.instr_dict[instr]['data']
            # If writing to index
            idx = self.instr_dict[instr]['idx']

            modes = list(map(int, list(parameter_modes)))[::-1]

            vals, cur_idx = [], 0
            cur_idx = 0
            if num_data is not None:
                for data_idx in num_data:
                    vals.append(self.get_data(self.pc + data_idx + 1, modes[data_idx]))
            if idx is not None:
                cur_idx = self.get_idx(self.pc + 1 + idx, modes[idx])

            if instr == 1:
                self.assign_value(cur_idx, vals[0] + vals[1])
                self.set_pc(self.pc + 4)
            elif instr == 2:
                self.assign_value(cur_idx, vals[0] * vals[1])
                self.set_pc(self.pc + 4)
            elif instr == 3:
                input_val = self.inputs.pop(0)
                self.assign_value(cur_idx, input_val)
                self.set_pc(self.pc + 2)
            elif instr == 4:
                self.outputs.append(vals[0])
                self.set_pc(self.pc + 2)
                if self.day == 7:
                    return self.outputs[-1]
            elif instr == 5:
                self.set_pc(vals[1] if vals[0] != 0 else self.pc + 3)
            elif instr == 6:
                self.set_pc(vals[1] if vals[0] == 0 else self.pc + 3)
            elif instr == 7:
                self.assign_value(cur_idx, 1 if vals[0] < vals[1] else 0)
                self.set_pc(self.pc + 4)
            elif instr == 8:
                self.assign_value(cur_idx, 1 if vals[0] == vals[1] else 0)
                self.set_pc(self.pc + 4)
            elif instr == 9:
                self.set_relative_base(vals[0])
                self.set_pc(self.pc + 2)
            else:
                assert False, 'Bad instr: {} {}'.format(instr, self.pc)
