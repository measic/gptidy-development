from aipython.searchMPP import SearcherMPP

s_mpp = SearcherMPP(problem=search_simple1)

# Visualization options
s_mpp.sleep_time = 0.2 # The time, in seconds, between each step in auto solving
s_mpp.line_width = 4.0 # The thickness of edges
s_mpp.text_size = 15 # The fontsize of the text
s_mpp.detail_level = 1 # 0=no text, 1=truncated text, 2=full text
s_mpp.show_edge_costs = True
s_mpp.show_node_heuristics = True

# Display the widget
display(s_mpp)
s_mpp.search()