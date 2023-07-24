new_bicoloring = {}
nodes_one = []
for node, color in bicoloring.items():
    if color == 1:
        nodes_one.append(node)