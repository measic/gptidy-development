.searchBranchAndBound import DF_branch_and_bound

s_dfbb = DF_branch_and_bound(problem=search_simple1)

# Visualization options
s_dfbb.sleep_time = 0.2 # The time, in seconds, between each step in auto solving
s_dfbb.line_width = 4.0 # The thickness of edges
s_dfbb.text_size = 15 # The fontsize of the text
s_dfbb.detail_level = 1 # 0=no text, 1=truncated text, 2=full text
s_dfbb.show_edge_costs = True
s_dfbb.show_node_heuristics = True

# Display the widget
display(s_dfbb)
s_dfbb.search()