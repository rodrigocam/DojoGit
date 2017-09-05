import tokenize
import ox

def make_line_getter(code):
    lines = code.splitlines()

    def getter():
        if lines:
            # pop(0) retira e retorna o primeiro elemento da lista
            line = lines.pop(0)

            # Agora convertemos para bytestring
            return line.encode('utf-8')

        # Se não houverem mais linhas, retorna uma bytestring vazia
        else:
            return b''

    return getter

TYPE_CODE_TO_NAME = {}
TYPE_NAME_TO_CODE = {}

def to_ox_token(tok):
    type_no = tok.type
    value = tok.string
    lineno = tok.start[0]
    lexpos = tok.start[1]
    type_str = TYPE_CODE_TO_NAME[type_no]
    return ox.Token(type_str, value, lineno, lexpos)

namespace = vars(tokenize)  # converte o módulo para um dicionário

for name, value in namespace.items():
    # consideramos que as constantes de tipo possuem nomes em letras
    # maiúsculas e valores numéricos
    if name.isupper() and isinstance(value, int):
        TYPE_CODE_TO_NAME[value] = name
        TYPE_NAME_TO_CODE[name] = value

def python_tokenize(source):
    getter = make_line_getter(source)
    tokens = tokenize.tokenize(getter)
    ox_tokens = [to_ox_token(tok) for tok in tokens]
    return ox_tokens

def generate_code(tokens):
    code = []
    for tok in tokens:
        if tok.value == 'exibir':
            code.append('print')
        elif tok.value == 'se':
            code.append('if ')
        elif tok.type == 'ENCODING' or tok.type == 'ENDMARKER':
            pass
        else:
            code.append(tok.value)
    return code

s = input()
m_list = python_tokenize(s)
code = generate_code(m_list)
pycode = ''.join(code)
eval(pycode) 
