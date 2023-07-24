r = 2
list_degrees = [tuple(k1 if j==i1 else 0 for j in range(r)) 
                for k1 in range(1, 3+1) for i1 in range(0,r)]
#list_degrees += [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]
sym_diff = symmetric_derivatives(list_degrees)
#sym_diff = merge(merge(symmetric_derivatives(list_degrees), 
#                       steenrod_operators(r, 1)), steenrod_operators(r, 2))
character(Range(W2, sym_diff))