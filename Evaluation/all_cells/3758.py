from aipython.searchGeneric import Searcher

s = Searcher(problem=search_simple2)

# Visualization options
s.sleep_time = 0.2 # The time, in seconds, between each step in auto solving
s.line_width = 4.0 # The thickness of edges
s.text_size = 15 # The fontsize of the text
s.detail_level = 1 # 0=no text, 1=truncated text, 2=full text
s.show_edge_costs = True

# Display the widget
display(s)
s.search()