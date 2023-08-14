generator = {v.multidegree() : [v]}
list_op = merge(merge(partial_derivatives(v.parent()), steenrod_operators(1, 1)), steenrod_operators(1, 2))