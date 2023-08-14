#first create a dictionary that we will use to assign colors by community
color_dict = {0: "#0ec4ff", 1: "pink", 2: "yellow"}
g.vs["color"] = [color_dict[community] for community in g.vs["community"]]