from getch import getche

source = '''
H: ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
E: ---.
L: +++++++.
.
O: +++.
+++++++++++++++++++++++++++++++++++++++++++++++.
-----------------------------------------------
W: ++++++++.
O: --------.
R: +++.
L: ------.
D: --------.
'''
def comp_bf(source):
    data = [0]
    ptr = 0
    code_ptr = 0
    breakpoints = []

    while code_ptr < len(source):
        cmd = source[code_ptr]

        if cmd == '+':
            data[ptr] = (data[ptr] + 1) % 256
        elif cmd == '-':
            data[ptr] = (data[ptr] - 1) % 256
        elif cmd == '>':
            ptr += 1
            if ptr == len(data):
                data.append(0)
        elif cmd == '<':
            ptr -= 1
        elif cmd == '.':
            print(chr(data[ptr]), end='')
        elif cmd == ',':
            data[ptr] = ord(getche())
        elif cmd == '[':
            if data[ptr] == 0:
                #avança até o ]
                open_brackets = 1
                while open_brackets != 0:
                    code_ptr += 1
                    if source[code_ptr] == '[':
                        open_brackets += 1
                    elif source[code_ptr] == ']':
                        open_brackets -= 1
            else:
                breakpoints.append(code_ptr)
        elif cmd == ']':
            # voltar para a posição do colhete correspondente
            code_ptr = breakpoints.pop() - 1

        code_ptr += 1

comp_bf(source)
