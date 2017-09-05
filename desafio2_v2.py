from ast import Load
from ast import Subscript
from ast import copy_location
from ast import Index
from ast import Name
from ast import NodeTransformer
from ast import Str
import ast
import inspect


def incr(x):
    __cte = 0
    return x + __cte


"""Crie uma função que leia um objeto python (definição de função ou de classe)
e retorne a árvore sintática correspondente. Seu código deve realizar uma série
de transformações:"""


# cte_to_node: converte constante (int, float ou string)
# em um nó de uma árvore sintática.
def cte_to_node(cte):
    node = ast.Num()
    node.lineno = 0
    node.col_offset = 0
    print(cte)
    print("hueheuheuh")
    node.n = cte
    return node


# tree_to_func: retorna um objeto do tipo função a partir de sua definição como
# árvore sintática.
def tree_to_func(tree):
    func = compile(tree, '<input>', 'exec')
    return func


# func_to_tree: retorna a árvore sintática a partir de um objeto tipo função.
def func_to_tree(func):
    src = inspect.getsource(func)
    tree = ast.parse(src)
    return tree


def transform(func, names):

    tree = func_to_tree(func)

    for node in ast.walk(tree):
            if(isinstance(node, ast.Name)):
                for key, value in names.items():
                    if(node.id == key):
                        print(value)
                        node = DiguiTransformer().visit_Name(node, value)

    return tree


class DiguiTransformer(NodeTransformer):

    def visit_Name(self, node, value):
        return copy_location(Subscript(value=cte_to_node(value),
                                       slice=Index(value=Str(s=node.id)),
                                       ctx=node.ctx), node)


tree = transform(incr, {'__cte': 42})
print(ast.dump(tree))

exec(tree_to_func(tree))
print(incr(3))
