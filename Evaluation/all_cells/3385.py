dim = 150
array = np.zeros((dim, dim),dtype=np.uint32)
marray = np.zeros((dim, dim,4),dtype=np.ubyte)
array[20,int(dim/2)] = diva.Annotations.COMMENT | diva.Annotations.BODY_TEXT
