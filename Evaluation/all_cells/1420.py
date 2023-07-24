#convert a logical index (D) into a subscript index (F). D is a boolean mask, where 3rd, 4th and 6th values of D are True.
F=np.where(D)
print(D)
print(F)