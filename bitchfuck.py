import os
import sys

PERMITTED_KEYWS = {'BITCH', 'NIGGA', 'FUCK', 'STUFF', 'MOTHERFUCKER', 'YO', 'RIDE', 'SHIT'}

TURING_LIMIT = 300


class Machine():
    def __init__(self):
        self.ptr = 0
        self.machine = []
        for i in range(TURING_LIMIT):
            self.machine.append(0)

    def flush(self):
        for i in range(TURING_LIMIT):
            self.machine[i] = 0

    def interpret(self, ops, interactive=False):
        i = 0
        while i < len(ops):
            if ops[i] == 'YO':
                self.ptr += 1
                i += 1
            elif ops[i] == 'NIGGA':
                self.ptr -= 1
                i += 1
            elif ops[i] == 'BITCH':
                self.machine[self.ptr] += 1
                i += 1
            elif ops[i] == 'FUCK':
                self.machine[self.ptr] -= 1
                i += 1
            elif ops[i] == 'RIDE':
                # not supported yet
                pass
                i += 1
            elif ops[i] == 'STUFF':
                end_op = i + 1
                open_internal = 1
                while open_internal != 0:
                    if ops[end_op] == 'STUFF':
                        open_internal += 1
                    if ops[end_op] == 'MOTHERFUCKER':
                        open_internal -= 1
                    end_op += 1
                while self.machine[self.ptr]:
                    self.interpret(ops[i + 1:end_op - 1])
                i = end_op
            elif ops[i] == 'SHIT':
                sys.stdout.write(chr(self.machine[self.ptr]))
                if interactive:
                    sys.stdout.write('\n')
                i += 1


def process(data):
    ops = [d.strip('\n') for d in data]
    for op in ops:
        if op not in PERMITTED_KEYWS:
            print(op)
            raise ValueError(f'Parsing error nigga bitch. yo commands are shit fuck nigga man')
    return ops


if __name__ == '__main__':
    if len(sys.argv) > 2:
        raise ValueError('too much args')
    elif len(sys.argv) == 1:
        machine = Machine()
        print('>>> Welcome to BITCHFUCK 0.0.1 nigga')
        while True:
            data = input('>>>')
            data = process(data.split(' '))
            machine.interpret(data, interactive=True)
    else:
        if not sys.argv[1].endswith('.btf'):
            raise ValueError('not proper file bitch nigga yo')
        else:
            fh = os.getcwd() + '/' + sys.argv[1]
            with open(fh, 'r') as f:
                data = f.readlines()
            data = process(data)
            machine = Machine()
            machine.interpret(data)
