# Answer #1: 7071
# Answer #2: 8001

from queue import Queue
import threading

cmds = [cmd.strip().split(' ', 1) for cmd in open('input/18')]

# Qs for the two programs
qs = [Queue(), Queue()]
class Computer(object):
    def __init__(self, qs, id, part1):
        self.part1 = part1
        self.pc = 0
        self.regs = {}
        self.last_sound = -1
        self.qs = qs
        self.id = id
        self.snd_cntr = 0

        # Init all regs
        for op, args in cmds:
            reg = args.split(' ')[0]
            if not reg.isdigit():
                self.regs[reg] = 0

        if not part1:
            self.regs['p'] = id

    def set(self, reg, val):
        self.regs[reg] = self.regs[val] if val in self.regs else int(val)
        self.pc += 1
    
    def add(self, reg, val):
        self.regs[reg] += self.regs[val] if val in self.regs else int(val)
        self.pc += 1

    def mul(self, reg, val):
        self.regs[reg] *= self.regs[val] if val in self.regs else int(val)
        self.pc += 1

    def mod(self, reg, val):
        self.regs[reg] %= self.regs[val] if val in self.regs else int(val)
        self.pc += 1
        
    def snd(self, reg):
        if self.part1:
            self.last_sound = self.regs[reg]
        else:
            self.qs[(self.id + 1)%2].put(int(self.regs.get(reg, reg)))
            self.snd_cntr += 1
            if self.id == 1:
                print('Answer #2: {}'.format(self.snd_cntr), end='\r')
        self.pc += 1

    def rcv(self, reg):
        if self.part1:
            return True if self.regs[reg] != 0 else None
        else:
            self.regs[reg] = self.qs[self.id].get()
        self.pc += 1
        
    def jgz(self, reg, val):
        if reg in self.regs:
            if self.regs[reg] > 0:
                if val in self.regs:
                    self.pc += self.regs[val] - 1
                else:    
                    self.pc += int(val) - 1
        else:
            if int(reg) > 0:
                if val in self.regs:
                    self.pc += self.regs[val] - 1
                else:    
                    self.pc += int(val) - 1
        self.pc += 1

def part1():       
    com = Computer(qs, 0, True)
    while com.pc < len(cmds):
        op, arg = cmds[com.pc]
        if getattr(com, op)(*arg.split()) is not None:
            break
    return com.last_sound

def run_computer(qs, id):
    com = Computer(qs, id, False)
    while com.pc < len(cmds):
        op, arg = cmds[com.pc]
        getattr(com, op)(*arg.split())      

def part2():
    com1 = threading.Thread(target=run_computer, args=(qs, 0))
    com1.start()
    run_computer(qs, 1)

print('Answer #1: {}'.format(part1()))
part2()