from aipython.searchGeneric import AStarSearcher

s_astar = AStarSearcher(problem=search_simple1)

# Visualization options
s_astar.sleep_time = 0.2 # The time, in seconds, between each step in auto solving
s_astar.line_width = 4.0 # The thickness of edges
s_astar.text_size = 15 # The fontsize of the text
s_astar.detail_level = 1 # 0=no text, 1=truncated text, 2=full text
s_astar.show_edge_costs = True
s_astar.show_node_heuristics = True

# Display the widget
display(s_astar)
s_astar.search()