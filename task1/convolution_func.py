from typing import Callable, Union, List, Dict

import numpy as np


TreeType = Union[int, List, Dict, np.ndarray]


def find_max_depth(tree: TreeType) -> int:
    '''
    Функция принимает на вход древовидную структуру
    и возвращает максимальную глубину ее компонент.
    '''
    if type(tree) is dict:
        if not tree:
            return 1
        else:
            return 1 + max(find_max_depth(v) for v in tree.values())
        
    elif type(tree) is list:
        if not tree:
            return 1
        else:
            return 1 + max(find_max_depth(v) for v in tree)
        
    else:
        return 0


def apply_function(node: TreeType, func: Callable) -> TreeType:
    '''
    Функция принимает на вход компоненту с максимальной глубиной
    и применяет к ней произвольную функцию свертки.
    '''
    if type(node) is list or type(node) is np.ndarray:
        return func(node)
    
    elif type(node) is dict:
        return func(list(node.values()))
    
    else:
        return node


def traverse(node: TreeType, current_depth: int, depth: int, func: Callable) -> TreeType:
    '''
    Функция принимает на вход древовидную структуру, 
    максимальную глубину и произвольную функцию свертки,
    чтобы совершить обход по всей структуре до компонент с максимальной глубиной.
    '''
    if current_depth == depth:
        return apply_function(node, func)
    
    elif type(node) is list:
        return [traverse(child, current_depth + 1, depth, func) for child in node]
    
    elif type(node) is dict:
        return {
            key: traverse(value, current_depth + 1, depth, func)
            for key, value in node.items()
        }
    
    else:
        return node
    

def convolution(tree: TreeType, func: Callable) -> TreeType:
    '''
    Функция принимает на вход древовидную структуру
    и произвольную функцию свертки, чтобы вернуть
    древовидную структуру со "свернутыми" компонентами
    максимальной глубины.
    '''

    if tree:
        max_depth = find_max_depth(tree)
        return traverse(tree, 1, max_depth, func)
    else:
        return tree