import random #use python's random number generator

#loop through all vertices
for vertex in g.vs:
    vertex['community'] = random.randint(0,2) #assign random community from 0 to 2
    vertex['size'] = vertex.indegree()
    
#lets see what node 0 is like as an example:
g.vs[0].attributes()