def max_sum(node_list):
    
    for n in node_list:
#         print(n, ':', *list(n.pending))
        while len(n.pending) > 0:            
            f = next(iter(n.pending))
            n.send_ms_msg(f)
            
    for n in reversed(node_list):
        
        while len(n.pending) > 0:
            f = next(iter(n.pending))
            n.send_ms_msg(f)
