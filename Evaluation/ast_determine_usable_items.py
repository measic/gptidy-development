import ast
from item_type import ItemType
from enum import Enum

class ItemType(Enum):
    FUNCTION = 1
    FUNCTION_PARAMETER = 2
    CLASS = 3
    ASSIGN = 4
    FOR_LOOP = 5
    WITH = 6
    IMPORT = 7
    ATTRIBUTE = 8
    CALL = 9

def _append_node(target, node_type, items, parent_node, ignore_underscores):
    # https://docs.python.org/3/library/ast.html
    # base cases are names for variables and function for functions, the rest are recursive
    to_add = []

    # variable cases
    if isinstance(target, ast.Attribute): # e.g. self.img = 1
        # we override the node_type because we don't want attributes
        to_add.append((parent_node, ItemType.ATTRIBUTE, target.attr))
    elif isinstance(target, ast.Name): # e.g. img = 1
        to_add.append((parent_node, node_type, target.id))
    elif isinstance(target, ast.Subscript): # e.g. img[2][5] = 1
        _append_node(target.value, node_type, items, parent_node, ignore_underscores)
    elif isinstance(target, ast.Starred): # e.g. *img = 1
        _append_node(target.value, node_type, items, parent_node, ignore_underscores)
    elif isinstance(target, ast.List) or isinstance(target, ast.Tuple): # e.g. [a, b, c] = [1, 2, 3] or (a, b, c) = (1, 2, 3)
        for item in target.elts:
            _append_node(item, node_type, items, parent_node, ignore_underscores)
    elif isinstance(target, ast.Call): # e.g. globals()[1] = 3
        # we override the node_type because we don't want calls
        to_add.append((parent_node, ItemType.CALL, target.func.id))

    # import case
    elif isinstance(target, ast.FunctionDef) or isinstance(target, ast.AsyncFunctionDef): # e.g. def func(): pass
        to_add.append((parent_node, node_type, target.name))

    elif isinstance(target, ast.Import) or isinstance(target, ast.ImportFrom): # e.g. import numpy
        if hasattr(target, "module") and target.module is not None:
            to_add.append((parent_node, node_type, target.module))
        for alias in target.names:
            _append_node(alias, node_type, items, parent_node, ignore_underscores)

    # alias case (for imports)
    elif isinstance(target, ast.alias): # e.g. import numpy as np
        to_add.append((parent_node, node_type, target.name))
        if hasattr(target, "asname") and target.asname is not None:
            to_add.append((parent_node, node_type, target.asname))

    # arg case
    elif isinstance(target, ast.arg): # e.g. def func(arg): pass
        to_add.append((parent_node, node_type, target.arg))

    # otherwise
    else:
        raise NotImplementedError("Unsupported target type: " + str(type(target)))

    if to_add is not []:
        for item_to_add in to_add:
            # ensure that to_add does not start with underscores (if checking)
            if not (ignore_underscores and item_to_add[2].startswith("_")):
                items.add(item_to_add)

def _get_items_helper(node, items, parent_node, ignore_underscores):
    # function
    if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
        _append_node(node, ItemType.FUNCTION, items, parent_node, ignore_underscores)
    # function parameters
    elif isinstance(node, ast.arguments):
        for arg in node.args:
            _append_node(arg, ItemType.FUNCTION_PARAMETER, items, parent_node, ignore_underscores)
    # class
    elif isinstance(node, ast.ClassDef):
        _append_node(node, ItemType.CLASS, items, parent_node, ignore_underscores)
    # variable
    elif isinstance(node, ast.Assign):
        for target in node.targets:
            _append_node(target, ItemType.ASSIGN, items, parent_node, ignore_underscores)
    # variable
    elif isinstance(node, ast.AugAssign) or isinstance(node, ast.AnnAssign):
        _append_node(node.target, ItemType.ASSIGN, items, parent_node, ignore_underscores)
    # for loop
    elif isinstance(node, ast.For) or isinstance(node, ast.AsyncFor):
        _append_node(node.target, ItemType.FOR_LOOP, items, parent_node, ignore_underscores)
    # with
    elif isinstance(node, ast.With) or isinstance(node, ast.AsyncWith):
        for item in node.items:
            _append_node(item.optional_vars, ItemType.WITH, items, parent_node, ignore_underscores)
    # import
    elif isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
        _append_node(node, ItemType.IMPORT, items, parent_node, ignore_underscores)
        
    for child in ast.iter_child_nodes(node):
        parent_node = parent_node if isinstance(node, ast.For) or isinstance(node, ast.If) else node
        _get_items_helper(child, items, parent_node, ignore_underscores)

def _get_items(node, ignore_underscores):
    items = set()
    _get_items_helper(node, items, None, ignore_underscores)
    return items

"""
This function ensures that items are not repeated across different namespaces
"""
def _filter_items(items, filter_type):
    # count the occurrence of each item
    item_counts = {}
    for item in items:
        name = item[2]
        if name not in item_counts:
            item_counts[name] = 1
        else:
            item_counts[name] += 1
    
    # keep only those that have a count of 1
    item_counts_filtered = []
    for item in item_counts:
        if item_counts[item] == 1:
            item_counts_filtered.append(item)
    
    # determine the type of each filtered item
    item_types = {}
    for item in items:
        name = item[2]
        if name in item_counts_filtered:
            item_types[name] = item[1]

    # filter types
    if filter_type is not None:
        item_types = [k for k, v in item_types.items() if v == filter_type]
    else:
        item_types = list(item_types.keys())
    return item_types

"""
This function determines the items that are usable in the given code
Ensures that items are not repeated across different namespaces or different types
"""
def determine_usable_items(code, filter_type, ignore_underscores):
    tree = ast.parse(code)
    items = _get_items(tree, ignore_underscores)
    return _filter_items(items, filter_type)

"""
This renamer assumes that the code given is either renaming a function or a variable (not both)
Otherwise the behavior is undefined
"""
def change_item_name(code, old_name, new_name):
    # Parse the code into an AST
    tree = ast.parse(code)

    # Modify the AST
    def _process(node):
        if isinstance(node, ast.Name):
            if node.id == old_name:
                node.id = new_name
        elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
            if node.name == old_name:
                node.name = new_name
            
        for child in ast.iter_child_nodes(node):
            _process(child)
    
    _process(tree)

    # Generate the modified code from the modified AST
    modified_code = ast.unparse(tree)
    return modified_code

code = """
from hell import datetime as dt
import d
import c as e

k = 4
"""

print(determine_usable_items(code, ItemType.ASSIGN, ["self"]))